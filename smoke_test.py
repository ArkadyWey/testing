class LoginSystem:
    def login(self, username, password):
        # Simulate the login process
        if username == "admin" and password == "admin123":
            return True
        else:
            return False

def test_smoke_login_successful():
    login_system = LoginSystem()
    result = login_system.login("admin", "admin123")
    assert result, "Smoke test for successful login failed."

def test_smoke_login_failure():
    login_system = LoginSystem()
    result = login_system.login("user", "invalid_password")
    assert not result, "Smoke test for failed login failed."