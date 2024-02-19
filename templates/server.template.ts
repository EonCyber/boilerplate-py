import { Application } from 'express'


export default class ServerCore {

    constructor(private app: Application, private serverPort: string){}

    start() {
        try {
            this.app.listen(this.serverPort)
            console.log(`[+] Http Server Up. Port: ${this.serverPort}`)
    
        } catch (e: any) {
            throw new Error(e)
        }
    }
}