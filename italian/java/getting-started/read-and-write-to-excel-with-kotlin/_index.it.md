---
title: Leggi e Scrivi su Excel con Kotlin
type: docs
weight: 189
url: /it/java/read-and-write-to-excel-with-kotlin/
description: Impara a leggere, scrivere e formattare file Excel in Kotlin usando Aspose.Cells for Java. Include esempi di codice per formule e formattazione.
keywords: Kotlin Excel, Aspose.Cells Kotlin, Leggi Excel Kotlin, Scrivi Excel Kotlin, Formule Excel Kotlin, Formattazione Cella Excel, Configurazione Aspose.Cells.
---

Aspose.Cells for Java è una libreria potente che permette agli sviluppatori di manipolare i file Excel programmaticamente. Pur essendo progettata per Java, si integra perfettamente con Kotlin grazie alla completa interoperabilità di Kotlin con Java. Questo documento fornisce una guida passo passo per leggere e scrivere file Excel usando Kotlin e Aspose.Cells for Java.

## Prerequisiti
- Kotlin e Java Development Kit (JDK) installati.
- Uno strumento di build (Maven o Gradle) configurato per la gestione delle dipendenze.

## Configurare Aspose.Cells in un progetto Kotlin

Aggiungi la dipendenza di Aspose.Cells al tuo progetto:

### Per Maven (`pom.xml`):
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
### Per Gradle (`build.gradle.kts`):
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
## Scrivere in Excel

Questo esempio mostra come creare un nuovo workbook Excel, populare le celle con dati e salvare il file sul disco.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Kotlin-WriteToExcel.kt" >}}

## Leggere da Excel

Questo esempio mostra come caricare un file Excel esistente, leggere i valori delle celle e stampare i risultati.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Kotlin-ReadFromExcel.kt" >}}

## Operazioni Avanzate

### Gestire le Formule

Questo esempio aggiunge una formula (`SUM`) a una cella, ricalcola il workbook e stampa il risultato.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Kotlin-HandleFormulas.kt" >}}

### Formattare le Celle

Questo esempio applica uno stile (testo in grassetto, colore rosso e allineamento al centro) a una cella.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Kotlin-FormatCells.kt" >}}

{{< app/cells/assistant language="java" >}}
