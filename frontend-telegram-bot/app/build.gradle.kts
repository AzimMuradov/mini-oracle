plugins {
    kotlin("jvm") version "1.7.20"
    kotlin("plugin.serialization") version "1.7.20"
    application
}

repositories {
    mavenCentral()
    maven(url = "https://jitpack.io")
}

dependencies {
    // Align versions of all Kotlin components.
    implementation(platform(kotlin("bom")))

    // Use the Kotlin JDK 8 standard library.
    implementation(kotlin("stdlib-jdk8"))


    // Use the KotlinX Coroutines library.
    implementation("org.jetbrains.kotlinx:kotlinx-coroutines-core:1.6.4")

    // Use the Ktor library.
    implementation("io.ktor:ktor-client-core:2.2.1")

    // Use the Ktor CIO engine.
    implementation("io.ktor:ktor-client-cio:2.2.1")

    // Use the Ktor plugins for serialization.
    implementation("io.ktor:ktor-client-content-negotiation:2.2.1")
    implementation("io.ktor:ktor-serialization-kotlinx-json:2.2.1")

    // Use the Telegram bot API.
    implementation("io.github.kotlin-telegram-bot.kotlin-telegram-bot:telegram:6.0.7")


    // Tests

    // Use the Kotlin test library.
    testImplementation(kotlin("test"))

    // Use the JUnit 5.
    testImplementation("org.junit.jupiter:junit-jupiter:5.9.1")
}

application {
    // Define the main class for the application.
    mainClass.set("me.proj.AppKt")
}

tasks {
    test {
        useJUnitPlatform()
    }
}

// jar {
//     manifest {
//         attributes 'Main-Class': 'com.github.kotlintelegrambot.MainKt'
//     }
//
//     from { configurations.runtimeClasspath.collect { it.isDirectory() ? it : zipTree(it) } }
//
//     duplicatesStrategy = DuplicatesStrategy.INCLUDE
// }
