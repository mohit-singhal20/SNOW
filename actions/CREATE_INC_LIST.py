'''
    .SYNOPSIS
        This is a python script to Creating List of Incidents from Given Payload.
        
    .DESCRIPTION
        This Script is for creating List of Incidents from Given Payload.

    .Input 
        1. payload                  :   Incidents Payload.
    
    .OUTPUT
        1. number_list              :   Incident Number List.      
        2. sys_list                 :   Incident Sys_id list.
        3. count                    :   Total Number of Incidents.

'''

##### IMPORTING ALL REQUIRED MODULES #####
from st2common.runners.base_action import Action
import json
from datetime import datetime                               # Importing datetime module for getting current date and time


class MyEchoAction(Action):
    result = dict()

    def run(self,payload):
        data=payload
        try:
            self.Write_Log("info","Script Execution Started")
            N_LIST=[]
            S_LIST=[]
            self.Write_Log("info","Total Number of Incidents: " + str(len(data)))
            for INC in data:
                S_LIST.append(INC.get('sys_id'))
                N_LIST.append(INC.get('number'))
            
            self.result['count'] = len(N_LIST)
            self.result['number_list'] = N_LIST
            self.result['sys_list'] = S_LIST
            
            self.Write_Log("info","Script Execution Completed")
            
            return (True, json.loads(json.dumps(self.result)))
        except Exception as err:
            Msg=str(err)
            self.Write_Log('error',"Error in Script - " + Msg)
            self.result['count'] = "NA"
            self.result['number_list'] = "NA"
            self.result['sys_list'] = "NA"
            return (False, json.loads(json.dumps(self.result)))

    def Write_Log(self, log_type,log_message):
        # User defined function to Write Log messages
        try:
            logMessage_dateTime_format = "%d-%m-%Y %H:%M:%S:%f"
            dateTime = datetime.now().strftime(logMessage_dateTime_format)
            if(log_type == "info"):
                self.logger.info(dateTime + " - " + log_message)
            elif(log_type == "error"):
                self.logger.error(dateTime + " - " + log_message)
            elif(log_type == "warning"):
                self.logger.warning(dateTime + " - " + log_message)
        except Exception as err:
            Msg=str(err)
