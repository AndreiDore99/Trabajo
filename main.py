import LoginApp as LoginApp
import src.Conector as conector

conector = conector.Conector()
conector.start()
AppLogin = LoginApp.LoginApp()
AppLogin.mainloop()