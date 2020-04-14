from webdriver_manager import utils
from webdriver_manager.driver import IEDriver, EdgeDriver
from webdriver_manager.manager import DriverManager
import os


class IEDriverManager(DriverManager):
    def __init__(self, version="latest",
                 os_type=utils.os_type(),
                 name="IEDriverServer",
                 url="http://selenium-release.storage.googleapis.com",
                 latest_release_url=None):
        super(IEDriverManager, self).__init__()
        self.driver = IEDriver(version=version,
                               os_type=os_type,
                               name=name,
                               url=url,
                               latest_release_url=latest_release_url)

    def install(self):
        return self.download_driver(self.driver)

class EdgeDriverManager(DriverManager):
    """
    This is meant for the new edge (chromium based)
    """
    def __init__(self, version="latest",
                 os_type=utils.os_type(),
                 path=None,
                 name="edgedriver",
                 url="https://msedgedriver.azureedge.net/",
                 latest_release_url="https://msedgedriver.azureedge.net/LATEST_STABLE",
                 ):
        super(EdgeDriverManager, self).__init__(path)

        self.driver = EdgeDriver(name=name,
                                   version=version,
                                   os_type=os_type,
                                   url=url,
                                   latest_release_url=latest_release_url,
                                   )

    def install(self):
        driver_path = self.download_driver(self.driver)

        os.chmod(driver_path, 0o755)
        return driver_path
        # return self.download_driver(self.driver)


