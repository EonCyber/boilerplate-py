import ApplicationCore from './'

function startApplication({server, router, database}: any) {
    router.init()
    server.start()
    // database.connect('uri','dbname')
}

// start application
startApplication(ApplicationCore)