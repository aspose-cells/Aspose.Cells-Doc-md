---
title: Lire et écrire dans Excel avec Kotlin
type: docs
weight: 189
url: /fr/java/read-and-write-to-excel-with-kotlin/
description: Apprenez à lire, écrire et formater des fichiers Excel en Kotlin avec Aspose.Cells for Java. Inclut des exemples de code pour les formules et le formatage.
keywords: Kotlin Excel, Aspose.Cells Kotlin, Lecture Excel Kotlin, Écriture Excel Kotlin, Formules Excel Kotlin, Formatage des cellules Excel, Configuration Aspose.Cells.
---

Aspose.Cells for Java est une bibliothèque puissante qui permet aux développeurs de manipuler des fichiers Excel par programmation. Bien qu'elle soit conçue pour Java, elle s’intègre parfaitement avec Kotlin, grâce à l’interopérabilité complète de Kotlin avec Java. Ce document fournit un guide étape par étape pour lire et écrire des fichiers Excel avec Kotlin et Aspose.Cells for Java.

## Prérequis
- Kotlin et JDK (Java Development Kit) installés.
- Un outil de construction (Maven ou Gradle) configuré pour la gestion des dépendances.

## Configuration de Aspose.Cells dans un projet Kotlin

Ajoutez la dépendance Aspose.Cells à votre projet :

### Pour Maven (`pom.xml`) :
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
### Pour Gradle (`build.gradle.kts`) :
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
## Écrire dans Excel

Cet exemple montre comment créer un nouveau classeur Excel, remplir les cellules avec des données et enregistrer le fichier sur le disque.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Kotlin-WriteToExcel.kt" >}}

## Lire dans Excel

Cet exemple montre comment charger un fichier Excel existant, lire les valeurs des cellules et afficher les résultats.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Kotlin-ReadFromExcel.kt" >}}

## Opérations avancées

### Gérer les formules

Cet exemple ajoute une formule (`SUM`) à une cellule, recalcule le classeur et affiche le résultat.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Kotlin-HandleFormulas.kt" >}}

### Formater les cellules

Cet exemple applique un style (gras, couleur rouge et alignement centré) à une cellule.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Kotlin-FormatCells.kt" >}}

{{< app/cells/assistant language="java" >}}
