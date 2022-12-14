package me.azimmuradov.minioracle

object StringUtils {
    fun formatAnswer(qType: QuestionType, title: String, answer: String) =
        """✅   _${qType.questionPrefix} ${title.escapeForTg()}?_ \-\- *${answer.escapeForTg()}*"""

    fun formatError(text: String) = """
        |❌   $text
        |Please try again\.\.\.
    """.trimMargin()

    // See https://core.telegram.org/bots/api#markdownv2-style
    fun String.escapeForTg() = replace("""[\\_*\[\]()~`>#+\-=|{}.!]""".toRegex()) { """\${it.value}""" }

    val QuestionType.questionPrefix
        get() = when (this) {
            QuestionType.SOMEBODY -> "Who is"
            QuestionType.SOMETHING -> "What is"
        }

    val QuestionType.cmdName
        get() = when (this) {
            QuestionType.SOMEBODY -> "who"
            QuestionType.SOMETHING -> "what"
        }

    val QuestionType.cmdArgTemplate
        get() = when (this) {
            QuestionType.SOMEBODY -> "somebody"
            QuestionType.SOMETHING -> "something"
        }
}
