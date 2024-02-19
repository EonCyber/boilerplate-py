import { Mongoose } from "mongoose"

export default class DatabaseCore {
    
    constructor(private dbInterface: Mongoose) {
    }

    async connect(dbUri: string, dbName: string) {
        try {
            await this.dbInterface.connect(dbUri, { dbName: dbName})
            console.log('[+] Database Connection up')
        } catch(e: any) {
            throw new Error(e)
        }
        
    }
}