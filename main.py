import login as login
import src.Conector as conector

conector = conector.Conector()
conector.start()
login = login.LoginApp()
AppLogin = login.LoginApp()
AppLogin.mainloop()