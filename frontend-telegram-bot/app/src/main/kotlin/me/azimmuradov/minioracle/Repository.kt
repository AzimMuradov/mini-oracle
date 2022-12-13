package me.azimmuradov.minioracle

import io.ktor.client.*
import io.ktor.client.call.*
import io.ktor.client.request.*
import io.ktor.client.statement.*
import me.azimmuradov.minioracle.StringUtils.cmdArgTemplate

class Repository(private val client: HttpClient) {
    suspend fun getAnswers(
        questionType: QuestionType,
        questionContent: String,
    ): Result<List<Answer>> = try {
        client.get(API_ENDPOINT) {
            url {
                parameters.append(name = "question_type", value = questionType.cmdArgTemplate)
                parameters.append(name = "question_content", value = questionContent)
            }
        }.toResult()
    } catch (e: Throwable) {
        Result.failure(e)
    }

    private suspend inline fun <reified T> HttpResponse.toResult(): Result<T> = try {
        Result.success(body())
    } catch (e: Throwable) {
        Result.failure(RuntimeException(body<ErrorAnswers>().error))
    }

    companion object {
        private const val API_ENDPOINT = "https://mini-oracle.up.railway.app/answers"
    }
}
