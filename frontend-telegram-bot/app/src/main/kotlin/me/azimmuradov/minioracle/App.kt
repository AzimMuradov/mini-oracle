package me.azimmuradov.minioracle

import io.ktor.client.*
import io.ktor.client.engine.cio.*
import io.ktor.client.plugins.contentnegotiation.*
import io.ktor.serialization.kotlinx.json.*

fun main() = newBot(
    token = System.getenv("TELEGRAM_BOT_TOKEN") ?: error("no telegram token provided"),
    repository = Repository(
        client = HttpClient(CIO) {
            install(ContentNegotiation) {
                json()
            }
            engine {
                threadsCount = 2
                pipelining = true
            }
        }
    )
).startPolling()
