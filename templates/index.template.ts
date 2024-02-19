import express from 'express'
import cors from 'cors'
import bodyParser from 'body-parser'
import ServerCore from './Core/Server/ServerCore'
import RouterCore from './Core/Router/RouterCore'
import mongoose from 'mongoose'
import DatabaseCore from './Core/Database/DatabaseCore'
import expressLogger from "./Shared/Util/Logger/LoggerUtil";
const port = process.env.PORT || '3001'
const app = express()
const dbInterface = mongoose
const middlewares: any = {
    cors: cors,
    bodyParser: bodyParser,
    logger: expressLogger
}

const server = new ServerCore(app, port)
const router = new RouterCore(app, express.Router(), middlewares)
const database = new DatabaseCore(dbInterface)

const ApplicationCore = Object.freeze({
    server, router, database
})

export default ApplicationCore