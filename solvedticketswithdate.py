# import libraries
 
import requests
import json
import sys
 
    # replace {email address} with your Contentful email address and {API token} from Contentful admin section
def main():
    solvedUrl = 'https://contentful.zendesk.com/api/v2/search.json?query=type:ticket group:Support Group status>=solved created>='+ str(sys.argv[1]) + ' created<='+ str(sys.argv[2])
    agents = [14490433387,367604755893,26361445487,368423045353,28586777367,365630360474,1906614437]
    # 368423045353 = Cat
    # 365630360474 = Alma
    # 28586777367 = Fajri
    # 1906614437 = Gabriel
    # 14490433387 = Fernando 
    # 367604755893 = Daria
    # 26361445487 = Sim
    resources = ["https://github.com/contentful/","https://www.contentful.com/developers/","https://www.contentful.com/pricing/","http://contentful.com/faq","https://www.contentful.com/blog/"]
     
    # solvedUrl = 'https://contentful.zendesk.com/api/v2/search.json?query=type:ticket status>=solved created>=2019-01-01 created<=2019-03-31'
    headers = {'Authorization':'Basic Base-64-encoded-email-address-API-token'}
     
    # open the file
    # fo = open("ticket_id.txt","a+")
    solvedTicketsNumber = 0
     
    while solvedUrl:
        fo = open("ticket_id.txt","a+")

        # request for the data
        solvedResponse = requests.get(solvedUrl,headers=headers)
     
        # convert the response into json
        solvedData = solvedResponse.json()
     
        # convert the json formatted response into a string
        solvedData_string =json.dumps(solvedData)
     
        # to be able to traverse the JSON arrays
        solvedData_dump = json.loads(solvedData_string)
     
        limit = len(solvedData_dump['results'])
        solvedTicketsNumber += limit
     
        for index in range(0,limit):
            fo.write(str(solvedData_dump['results'][index]['id']))
            fo.write("\n")
     
        solvedUrl = solvedData_dump['next_page']
        print(solvedUrl)
        print solvedTicketsNumber
     
    else:
        fo.close()


    # tickets.py

    infile = open ("ticket_id.txt","r")
    KBtickets = open ("KB_tickets.txt", "a")
    tickets_solved = 0
    tickets_solved_with_KB = 0
     
    for ticketId in infile:
        try:
            url = 'https://contentful.zendesk.com/api/v2/tickets/'+ticketId+'/comments.json'
            print "Tickets "+ticketId+" is checked..."
            tickets_solved += 1
            KbResponse = requests.get(url,headers=headers)
            KbData = KbResponse.json()
            KbData_string = json.dumps(KbData)
            KbData_dump = json.loads(KbData_string)

            if 'comments' in KbData_dump:
                for index in range (0,len(KbData_dump['comments'])):
                    for resourceIndex in range(0,len(resources)):
                        if (resources[resourceIndex] in KbData_dump['comments'][index]['body']) and (KbData_dump['comments'][index]['author_id'] in agents):
                            print str(KbData_dump['comments'][index]['author_id'])
                            print KbData_dump['comments'][index]['body']
                            KBtickets.write("Ticket ID: "+ticketId+"\n")
                            tickets_solved_with_KB += 1
                            KBtickets.write("Ticket has knowledge docs link submitted by " + str(data_dump['comments'][index]['author_id']) + " related to " + resources[resourceIndex] + "\n")
                        break
            else:
                print("Ticket ID: "+ticketId+" doesn't have comments")
        except Exception:
            print("Ticket ID = "+ticketId+" has exceptions")
            pass

    KBtickets.write("Tickets solved = "+str(tickets_solved))
    KBtickets.write("\n")
    KBtickets.write("Tickets solved with Documentations = "+str(tickets_solved_with_KB))
    KBtickets.close()
    infile.close()

if __name__ == "__main__":
    main()
