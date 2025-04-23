---
title: Läs och skriv till Excel med Kotlin
type: docs
weight: 189
url: /sv/java/read-and-write-to-excel-with-kotlin/
description: Lär dig att läsa, skriva och formatera Excel filer i Kotlin med Aspose.Cells for Java. Inkluderar kodexempel för formler och formatering.
keywords: Kotlin Excel, Aspose.Cells Kotlin, Läs Excel Kotlin, Skriv Excel Kotlin, Excel Formler Kotlin, Excel Cellformatering, Aspose.Cells Setup.
---

Aspose.Cells for Java är ett kraftfullt bibliotek som möjliggör för utvecklare att manipulera Excel-filer programmatiskt. Även om det är utformat för Java, integreras det sömlöst med Kotlin tack vare Kotlin's fullständiga interoperabilitet med Java. Detta dokument ger en steg-för-steg-guide för att läsa från och skriva till Excel-filer med Kotlin och Aspose.Cells for Java.

## Förutsättningar
- Kotlin och Java Development Kit (JDK) installerade.
- Ett byggverktyg (Maven eller Gradle) konfigurerat för beroendehantering.

## Sätta upp Aspose.Cells i ett Kotlin-projekt

Lägg till Aspose.Cells-beroendet i ditt projekt:

### För Maven (`pom.xml`):
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
### För Gradle (`build.gradle.kts`):
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
## Skriv till Excel

Detta exempel visar hur man skapar en ny Excel-arbetsbok, fyller celler med data och sparar filen till disk.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Kotlin-WriteToExcel.kt" >}}

## Läs från Excel

Detta exempel visar hur man laddar en befintlig Excel-fil, läser cellvärden och skriver ut resultaten.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Kotlin-ReadFromExcel.kt" >}}

## Avancerade operationer

### Hantera formler

Detta exempel lägger till en formel (`SUM`) i en cell, omberäknar arbetsboken och skriver ut resultatet.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Kotlin-HandleFormulas.kt" >}}

### Formatera celler

Detta exempel tillämpar styling (fet text, röd färg och centrerad inriktning) på en cell.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Kotlin-FormatCells.kt" >}}

{{< app/cells/assistant language="java" >}}
