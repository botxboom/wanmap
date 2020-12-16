from nmaputils import nmap as nm

def fullScan(host):
    servicesRunning = {}
    portList = []
    serviveNameList = []
    serviceStateList = []
    serviceVersionList = []
    productList = []

    scanner = nm.PortScanner()
    result = scanner.scan(host, arguments='-T4 -O -A')
    services = result['scan'][host]['tcp']
    for data in services:
        portList.append(data)
        serviceStateList.append(services[data]['state'])
        serviveNameList.append(services[data]['name'])
        productList.append(services[data]['product'])
        serviceVersionList.append(services[data]['version'])
        servicesRunning['Port'] = portList
        servicesRunning['State'] = serviceStateList
        servicesRunning['Name'] = serviveNameList
        servicesRunning['Version'] = serviceVersionList
        servicesRunning['Product'] = productList
       
    osName = result['scan'][host]['osmatch'][0]['name']
    accuracyFound = result['scan'][host]['osmatch'][0]['accuracy']
    hostname = result['scan'][host]['hostnames'][0]['name']
    return [hostname, servicesRunning, osName, accuracyFound]
    
