import expressWinston from 'express-winston'
import { transports, format } from 'winston'


const myFormat = format.printf((obj) => {
    // console.log(obj)
    return `${obj.timestamp} [${obj.level}]---[Requester: ${obj.meta.req.headers['user-agent']}]: ${obj.message} - STATUS ${obj.meta.res.statusCode}`
})
const expressLogger = expressWinston.logger({
    level: 'info',
    transports: [
        new transports.Console()
    ],
    format: format.combine(
        format.json(),
        format.prettyPrint(),
        format.timestamp({format: "HH:mm:ss"}),
        format.colorize(),

        myFormat
    )
})
// CONFIGURE RESPONSE, ERROR LOGS
export default expressLogger