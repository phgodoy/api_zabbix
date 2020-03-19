#bibliotecas importadas
from pyzabbix.api import ZabbixAPI
from pyzabbix import ZabbixMetric, ZabbixSender
from datetime import datetime
import csv
import time

class apiZabbix:

    #inicia objetos 
    def __init__(self, zapi, result1, url, user, password ):
        self.zapi = zapi
        self.result1 = result1
        self.url = url
        self.user = user
        self.password = password
        

       
    # cria instancia da class ZabbixAPI    
    def getInstancia(self, url, user, password):
         self.zapi = ZabbixAPI(url=self.url, user= self.user, password=self.password)
    



    # obter os hosts 
    def getHost(self):
    
        for result1 in self.zapi.host.get(output = 'extend'):
            if(result1['status'] == '1'):
                print('hostid:',result1['hostid'])
                print('host:', result1['host'])
                print('available:', result1['available'])
                print('ipmi_authtype:', result1['ipmi_authtype'])
                print('ipmi_privilege:', result1['ipmi_privilege'])
                print('name:', result1['name'])
                print('tls_connect:', result1['tls_connect'])
                print('tls_accept:', result1['tls_accept'])
                print('auto_compress:', result1['auto_compress'])
                print('inventory_mode:', result1['inventory_mode'])
                print('status:',result1['status'])
                print()

   

 
                            
    #coleta dados  do sistema(esta retornando 'vazio')
    def getHistory(self,zapi):
        #cria intervalo de tempo 
        time_till = time.mktime(datetime.now().timetuple())
        time_from = time_till - 60 * 60 * 4  # 4 hours


        history = self.zapi.history.get(itemids=[self.result1['hostid']],
                                time_from=int(time_from),
                                time_till=int(time_till),
                                output='extend',
                                limit='5000',
                                )
        print(history) 


    #cria csv
    def csvCreated(self):
        writer = csv.writer(open("host.csv", "w"))

        #grava informacoes no arquivo criado
        for result1 in self.zapi.host.get(output = 'extend'):
            if(result1['status'] == '1'):
                writer.writerow([
                    'hostid:', result1['hostid'], 
                    'host:', result1['host'],
                    'status:', result1['status'],
                    'available:', result1['available'],
                    'ipmi_authtype:', result1['ipmi_authtype'],
                    'ipmi_privilege:', result1['ipmi_privilege'],
                    'name:', result1['name'],
                    'tls_connect:',result1['tls_connect'],
                    'tls_accept:', result1['tls_accept'],
                    'auto_compress:', result1['auto_compress'],
                    'inventory_mode:', result1['inventory_mode'],
                    'status:', result1['status']
                    ])
        print('csv gerado')            
            
