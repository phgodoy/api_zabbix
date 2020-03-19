import zabbix_api as z
#instancia das variaveis 
zapi =  None
resultq = None
#dados omitidos para envio ao github, informar dados reais para que o programa possa funcionar
url = 'http://localhost/zabbix'
login = 'login'
password = 'password'

#instancia da classe zabbix_api
zap = z.apiZabbix(zapi, resultq,url ,login , password )

#chamada de funcoes
zap.getInstancia(url,login, password )
zap.getHost()
zap.csvCreated()