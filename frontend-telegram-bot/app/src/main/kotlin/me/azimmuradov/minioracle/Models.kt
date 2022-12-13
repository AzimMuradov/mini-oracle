package me.azimmuradov.minioracle

import kotlinx.serialization.Serializable

@Serializable
data class Answer(val title: String, val answer: String)

@Serializable
data class ErrorAnswers(val error: String)
