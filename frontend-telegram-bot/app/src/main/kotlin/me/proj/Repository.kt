package me.proj

import kotlinx.serialization.decodeFromString
import kotlinx.serialization.json.Json
import java.net.URI
import java.net.http.HttpClient
import java.net.http.HttpRequest
import java.net.http.HttpResponse

class Repository(private val client: HttpClient) {
    fun getAnswers(
        questionType: QuestionType,
        questionContent: String,
    ): Result<List<Answer>> = try {
        client.send(generateRequest(questionType, questionContent), HttpResponse.BodyHandlers.ofString())
            .toResult { Json.decodeFromString<ErrorAnswers>(it).error }
            .map { responseBody -> Json.decodeFromString(responseBody) }
    } catch (e: Throwable) {
        Result.failure(e)
    }

    private fun generateRequest(questionType: QuestionType, questionContent: String) =
        HttpRequest.newBuilder().apply {
            val query = listOf("question_type=$questionType", "question_content=$questionContent")
                .joinToString(separator = "&")
            uri(URI.create("$API_ENDPOINT?$query"))
            GET()
        }.build()

    private inline fun <T> HttpResponse<T>.toResult(convertErrorBody: (String) -> String?): Result<T> = try {
        if (statusCode() in 200 until 300) {
            Result.success(body())
        } else {
            Result.failure(Exception(convertErrorBody(body().toString())))
        }
    } catch (e: Throwable) {
        Result.failure(e)
    }

    companion object {
        private const val API_ENDPOINT = "https://mini-oracle.up.railway.app/answers"
    }
}
