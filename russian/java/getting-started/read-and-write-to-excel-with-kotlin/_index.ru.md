---
title: Чтение и запись Excel с Kotlin
type: docs
weight: 189
url: /ru/java/read-and-write-to-excel-with-kotlin/
description: Научитесь читать, писать и форматировать файлы Excel на Kotlin с помощью Aspose.Cells for Java. Включены примеры кода для формул и форматирования.
keywords: Координаты Excel для Kotlin, Aspose.Cells для Kotlin, чтение Excel на Kotlin, запись Excel на Kotlin, формулы Excel на Kotlin, форматирование ячеек Excel, настройка Aspose.Cells.
---

Aspose.Cells for Java — мощная библиотека, позволяющая разработчикам программно манипулировать файлами Excel. Несмотря на то, что она предназначена для Java, она легко интегрируется с Kotlin благодаря полной совместимости Kotlin с Java. Этот документ предоставляет пошаговое руководство по чтению и записи файлов Excel с помощью Kotlin и Aspose.Cells for Java.

## Предварительные требования
- Установлены Kotlin и Java Development Kit (JDK).
- Настроен инструмент сборки (Maven или Gradle) для управления зависимостями.

## Настройка Aspose.Cells в проекте Kotlin

Добавьте зависимость Aspose.Cells в ваш проект:

### Для Maven (`pom.xml`):
```xml
<repositories>
    <repository>
        <id>AsposeJavaAPI</id>
        <name>Aspose Java API</name>
        <url>https://releases.aspose.com/java/repo/</url>
    </repository>
</repositories>

<dependencies>
    <!-- Aspose.Cells for Java -->
    <dependency>
        <groupId>com.aspose</groupId>
        <artifactId>aspose-cells</artifactId>
        <version>25.2</version>
    </dependency>

    <!-- Mandatory Bouncy Castle Libraries -->
    <dependency>
        <groupId>org.bouncycastle</groupId>
        <artifactId>bcprov-jdk15on</artifactId>
        <version>1.68</version>
    </dependency>
    <dependency>
        <groupId>org.bouncycastle</groupId>
        <artifactId>bcpkix-jdk15on</artifactId>
        <version>1.68</version>
    </dependency>
</dependencies>
```
### Для Gradle (`build.gradle.kts`):
```kotlin
repositories {
    maven { url = uri("https://releases.aspose.com/java/repo/") }
}

dependencies {
    // Aspose.Cells for Java
    implementation("com.aspose:aspose-cells:25.2")

    // Mandatory Bouncy Castle Libraries
    implementation("org.bouncycastle:bcprov-jdk15on:1.68")
    implementation("org.bouncycastle:bcpkix-jdk15on:1.68")
}
```
## Запись в Excel

Этот пример показывает, как создать новую таблицу Excel, заполнить ячейки данными и сохранить файл на диск.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Kotlin-WriteToExcel.kt" >}}

## Чтение из Excel

Этот пример показывает, как загрузить существующий файл Excel, считать значения ячеек и вывести результаты.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Kotlin-ReadFromExcel.kt" >}}

## Продвинутые операции

### Обработка формул

Этот пример добавляет формулу (`SUM`) в ячейку, пересчитывает книгу и выводит результат.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Kotlin-HandleFormulas.kt" >}}

### Форматирование ячеек

Этот пример применяет стиль (жирный текст, красный цвет и выравнивание по центру) к ячейке.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Kotlin-FormatCells.kt" >}}

{{< app/cells/assistant language="java" >}}
