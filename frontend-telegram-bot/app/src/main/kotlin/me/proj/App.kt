package me.proj

import java.net.http.HttpClient
import kotlin.time.Duration.Companion.seconds
import kotlin.time.toJavaDuration

fun main() = newBot(
    token = System.getenv("TELEGRAM_BOT_TOKEN") ?: error("no telegram token provided"),
    repository = Repository(
        client = HttpClient.newBuilder()
            .version(HttpClient.Version.HTTP_2)
            .connectTimeout(3.seconds.toJavaDuration())
            .build()
    )
).startPolling()
