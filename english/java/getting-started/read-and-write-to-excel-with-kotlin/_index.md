---
title: Read and Write to Excel With Kotlin
type: docs
weight: 189
url: /java/read-and-write-to-excel-with-kotlin/
description: Learn to read, write, and format Excel files in Kotlin using Aspose.Cells for Java. Includes code examples for formulas and formatting.
keywords: Kotlin Excel, Aspose.Cells Kotlin, Read Excel Kotlin, Write Excel Kotlin, Excel Formulas Kotlin, Excel Cell Formatting, Aspose.Cells Setup.
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Aspose.Cells for Java is a powerful library that enables developers to manipulate Excel files programmatically. While it is designed for Java, it integrates seamlessly with Kotlin, thanks to Kotlin's full interoperability with Java. This document provides a step-by-step guide to reading from and writing to Excel files using Kotlin and Aspose.Cells for Java.

## Prerequisites
- Kotlin and Java Development Kit (JDK) installed.
- A build tool (Maven or Gradle) configured for dependency management.

## Setting Up Aspose.Cells in a Kotlin Project

Add the Aspose.Cells dependency to your project:

### For Maven (`pom.xml`):
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
### For Gradle (`build.gradle.kts`):
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
## Write to Excel

This example demonstrates how to create a new Excel workbook, populate cells with data, and save the file to disk.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Kotlin-WriteToExcel.kt" >}}

## Read from Excel

This example shows how to load an existing Excel file, read cell values, and print the results.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Kotlin-ReadFromExcel.kt" >}}

## Advanced Operations

### Handle Formulas

This example adds a formula (`SUM`) to a cell, recalculates the workbook, and prints the result.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Kotlin-HandleFormulas.kt" >}}

### Format Cells

This example applies styling (bold text, red color, and center alignment) to a cell.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Kotlin-FormatCells.kt" >}}

{{< app/cells/assistant language="java" >}}
