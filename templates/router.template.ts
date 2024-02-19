import { Application, Router } from "express";

const routes = {
    base: '/v1/api',
}
export default class RouterCore {
    constructor(private app: Application, private router: Router, private middlewares: any){}


    configMiddleware() {
        this.app.use(this.middlewares.cors({ origin: ['http://localhost:5173', 'http://127.0.0.1:5173', 'http://127.0.0.1:3000'], credentials: true})) // cors Middleware
        this.app.use(this.middlewares.bodyParser.json()) // Body-Parser Json() Middleware

        this.app.use(this.middlewares.logger) // Winston Express Logger Middleware
        console.log('[+] Middlewares Configured')
    }
    
    configRoutes(){ 
        // Configure new route handlers here
        this.app.use(routes.base, this.router)
        console.log('[+] Api Routes Configured')
    }

    init(){
        this.configMiddleware()
        this.configRoutes()
     }
}