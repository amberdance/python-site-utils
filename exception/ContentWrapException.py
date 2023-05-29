from exception.SiteUtilsException import SiteUtilsException


class ContentWrapException(SiteUtilsException):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
