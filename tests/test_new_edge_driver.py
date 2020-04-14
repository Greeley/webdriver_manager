"""
Name: Test edge driver
Author: Dakota Carter (dakota.carter@perficient.com)
Description: Wrote these tests to try and test edgedriver downloading of the new edge driver and pairing with selenium
currently on Mac OS the webdriver downloads but cannot launch edge.
"""
import os
from webdriver_manager.microsoft import EdgeDriverManager
import pytest
from selenium import webdriver
# from selenium.webdriver.common.service import Service



def test_edge_manager_with_specific_version():
    bin = EdgeDriverManager("76.0.172.0").install()
    assert os.path.exists(bin)


def test_driver_can_be_saved_to_custom_path():
    custom_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "custom")

    path = EdgeDriverManager(version="76.0.172.0", path=custom_path).install()
    assert os.path.exists(path)
    assert custom_path in path


@pytest.mark.parametrize('path', [".", None])
def test_edge_manager_with_latest_version(path):
    bin = EdgeDriverManager(path=path).install()
    assert os.path.exists(bin)


def test_edge_manager_with_wrong_version():
    with pytest.raises(ValueError) as ex:
        EdgeDriverManager("0.2").install()
    assert "There is no such driver by url" in ex.value.args[0]


def test_edge_manager_with_selenium():
    driver_path = EdgeDriverManager().install()
    driver = webdriver.Edge(executable_path=driver_path)
    driver.get("http://automation-remarks.com")
    driver.close()


@pytest.mark.parametrize('path', [".", None])
def test_edge_manager_cached_driver_with_selenium(path):
    EdgeDriverManager(path=path).install()
    webdriver.Edge(EdgeDriverManager(path=path).install())


@pytest.mark.parametrize('path', [".", None])
def test_edge_manager_with_win64_os(path):
    EdgeDriverManager(os_type="win64", path=path).install()


@pytest.mark.parametrize('os_type', ['win32', 'win64'])
def test_can_get_edge_for_win(os_type):
    path = EdgeDriverManager(os_type=os_type).install()
    assert os.path.exists(path)
