package me.proj

import com.github.kotlintelegrambot.bot
import com.github.kotlintelegrambot.dispatch
import com.github.kotlintelegrambot.dispatcher.Dispatcher
import com.github.kotlintelegrambot.dispatcher.command
import com.github.kotlintelegrambot.dispatcher.handlers.CommandHandlerEnvironment
import com.github.kotlintelegrambot.entities.ChatId
import com.github.kotlintelegrambot.entities.ParseMode
import com.github.kotlintelegrambot.logging.LogLevel
import me.proj.QuestionType.SOMEBODY
import me.proj.QuestionType.SOMETHING
import me.proj.StringUtils.cmdArgTemplate
import me.proj.StringUtils.cmdName
import me.proj.StringUtils.formatAnswer
import me.proj.StringUtils.formatError
import me.proj.StringUtils.questionPrefix

fun newBot(token: String, repository: Repository) = bot {
    this.token = token
    timeout = 30
    logLevel = LogLevel.All()

    dispatch {
        command("start") {
            sendFormattedMessage(
                text = """
                    |Bot started\.\.\.
                    |If you need any help, use the `/help` command\.
                """.trimMargin(),
            )
        }

        commandGetAnswers(SOMEBODY, repository)

        commandGetAnswers(SOMETHING, repository)

        command("help") {
            fun QuestionType.formatted() = """"_$questionPrefix \_?_""""
            fun QuestionType.cmdHelp() =
                """`/$cmdName $cmdArgTemplate` \- ask ${formatted()} type of question"""
            sendFormattedMessage(
                text = """
                    |*Mini\-oracle* can give you answers for two types of questions: ${SOMEBODY.formatted()} and ${SOMETHING.formatted()}\.
                    |
                    |*Commands*
                    |`/help` \- call this message
                    |${SOMEBODY.cmdHelp()}
                    |${SOMETHING.cmdHelp()}
                """.trimMargin()
            )
        }
    }
}


fun CommandHandlerEnvironment.sendFormattedMessage(text: String) {
    bot.sendMessage(
        chatId = ChatId.fromId(message.chat.id),
        text = text,
        parseMode = ParseMode.MARKDOWN_V2
    )
}

fun Dispatcher.commandGetAnswers(qType: QuestionType, repository: Repository) = command(qType.cmdName) {
    if (args.size == 1) {
        repository.getAnswers(
            questionType = qType,
            questionContent = args.first()
        ).fold(
            onSuccess = { answers ->
                if (answers.isNotEmpty()) {
                    for ((title, answer) in answers) {
                        sendFormattedMessage(formatAnswer(qType, title, answer))
                    }
                } else {
                    sendFormattedMessage(text = """👽   No answers found\.\.\.""")
                }
            },
            onFailure = { ex ->
                sendFormattedMessage(formatError(text = ex.message ?: "Unexpected error"))
            }
        )
    } else {
        with(qType) {
            sendFormattedMessage(
                formatError(
                    text = """Wrong number of arguments, expected: `/${cmdName} ${cmdArgTemplate}`"""
                )
            )
        }
    }
}
