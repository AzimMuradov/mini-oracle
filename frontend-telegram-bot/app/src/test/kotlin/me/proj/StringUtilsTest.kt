package me.proj

import me.proj.QuestionType.SOMEBODY
import me.proj.QuestionType.SOMETHING
import me.proj.StringUtils.escapeForTg
import me.proj.StringUtils.formatAnswer
import me.proj.StringUtils.formatError
import org.junit.jupiter.params.ParameterizedTest
import org.junit.jupiter.params.provider.Arguments.arguments
import org.junit.jupiter.params.provider.MethodSource
import kotlin.test.assertEquals

internal class StringUtilsTest {

    @ParameterizedTest
    @MethodSource("formatAnswerTestData")
    fun formatAnswer(qType: QuestionType, title: String, answer: String, formattedAnswerText: String) {
        assertEquals(
            expected = formattedAnswerText,
            actual = formatAnswer(qType, title, answer)
        )
    }

    @ParameterizedTest
    @MethodSource("formatErrorTestData")
    fun formatError(text: String, formattedErrText: String) {
        assertEquals(
            expected = formattedErrText,
            actual = formatError(text)
        )
    }

    @ParameterizedTest
    @MethodSource("escapeForTgTestData")
    fun `escape for tg`(text: String, escapedText: String) {
        assertEquals(
            expected = escapedText,
            actual = text.escapeForTg()
        )
    }


    companion object {
        @JvmStatic
        fun formatAnswerTestData() = listOf(
            listOf(
                SOMEBODY, "", "",
                """✅   _Who is ?_ \-\- **"""
            ),
            listOf(
                SOMEBODY, "Alice", "programmer",
                """✅   _Who is Alice?_ \-\- *programmer*"""
            ),
            listOf(
                SOMETHING, "#!", "shebang",
                """✅   _What is \#\!?_ \-\- *shebang*"""
            ),
            listOf(
                SOMETHING, "Life", """¯\_(ツ)_/¯""",
                """✅   _What is Life?_ \-\- *¯\\\_\(ツ\)\_/¯*"""
            ),
        ).map { (a, b, c, d) -> arguments(a, b, c, d) }

        @JvmStatic
        fun formatErrorTestData() = listOf(
            "" to """
                     |❌   
                     |Please try again\.\.\.
                     """.trimMargin(),
            "err" to """
                     |❌   err
                     |Please try again\.\.\.
                     """.trimMargin(),
            "err!" to """
                     |❌   err\!
                     |Please try again\.\.\.
                     """.trimMargin(),
        ).map { (a, b) -> arguments(a, b) }

        @JvmStatic
        fun escapeForTgTestData() = listOf(
            """""" to """""",
            """\""" to """\\""",
            """\\""" to """\\\\""",
            """.""" to """\.""",
            """\.""" to """\\\.""",
            """-""" to """\-""",
            """*""" to """\*""",
            """*\**""" to """\*\\\*\*""",
            """*bold _italic bold_*""" to """\*bold \_italic bold\_\*""",
            """\_*[]()~`>#+-=|{}.!""" to """\\\_\*\[\]\(\)\~\`\>\#\+\-\=\|\{\}\.\!""",
        ).map { (a, b) -> arguments(a, b) }
    }
}
