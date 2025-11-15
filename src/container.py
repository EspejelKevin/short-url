from dependency_injector import containers, providers

from contextlib import contextmanager
from typing import Optional

from infrastructure import MySQL, MySQLRepository
from application import (DBService, GetURL, CreateShorter)
from domain import Settings


class RepositoriesContainer(containers.DeclarativeContainer):
    settings = providers.Dependency(Settings)
    mysql = providers.Singleton(MySQL, host=settings.provided.MYSQL_HOST, user=settings.provided.MYSQL_USER,
                                password=settings.provided.MYSQL_PASSWORD, db=settings.provided.MYSQL_DB)
    mysql_repository = providers.Singleton(MySQLRepository, db_factory=mysql.provider)


class ServicesContainer(containers.DeclarativeContainer):
    repositories: RepositoriesContainer = providers.DependenciesContainer()
    db_service = providers.Factory(DBService, repository=repositories.mysql_repository)


class UseCasesContainer(containers.DeclarativeContainer):
    services: ServicesContainer = providers.DependenciesContainer()
    settings = providers.Dependency(Settings)
    get_url = providers.Factory(GetURL, db_service=services.db_service)
    create_shorter = providers.Factory(CreateShorter, db_service=services.db_service)


class AppContainer(containers.DeclarativeContainer):
    settings = providers.ThreadSafeSingleton(Settings)
    repositories = providers.Container(
        RepositoriesContainer, settings=settings)
    services = providers.Container(
        ServicesContainer, repositories=repositories)
    use_cases = providers.Container(
        UseCasesContainer, services=services)


class SingletonContainer:
    container: Optional[AppContainer] = None

    @classmethod
    @contextmanager
    def scope(cls):
        try:
            cls.container.services.init_resources()
            yield cls.container
        finally:
            cls.container.services.shutdown_resources()

    @classmethod
    def init(cls) -> None:
        if cls.container is None:
            cls.container = AppContainer()