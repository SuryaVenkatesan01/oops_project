import pytest
import Kohls_automation
def test_login():
    expected = 'Shop by Category'
    assert Kohls_automation.login() == expected
if __name__ == '__main__':
    pytest.main()
