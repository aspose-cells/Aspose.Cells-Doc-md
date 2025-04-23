---
title: Convertir CSV, TSV et TXT en Excel
type: docs
weight: 50
url: /fr/java/convert-csv-tsv-and-txt-to-excel/
---

## **Ouverture des fichiers CSV**

Les fichiers de valeurs séparées par des virgules (CSV) contiennent des enregistrements dont les valeurs sont délimitées ou séparées par des virgules. Dans les fichiers CSV, les données sont stockées dans un format tabulaire qui a des champs séparés par le caractère virgule et mis entre guillemets par le caractère double quote. Si la valeur d'un champ contient un double guillemet, elle est échappée avec une paire de double guillemets. Vous pouvez également utiliser Microsoft Excel pour exporter les données de votre feuille de calcul vers un fichier CSV.

Pour ouvrir des fichiers CSV, utilisez la classe [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) et sélectionnez la valeur [**CSV**](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#CSV), prédéfinie dans l'énumération [**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat).

## **Exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningCSVFiles-OpeningCSVFiles.java" >}}

### **Ouverture des fichiers CSV et remplacement des caractères invalides**

Dans Excel, lorsqu'un fichier CSV avec des caractères spéciaux est ouvert, les caractères sont automatiquement remplacés. Il en va de même pour l'API Aspose.Cells qui est démontrée dans l'exemple de code ci-dessous.

#### **Exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningCSVFilesAndReplacingInvalidCharacters-1.java" >}}

## **Ouverture des fichiers CSV en utilisant un analyseur préféré**

Ce n'est pas toujours nécessaire d'utiliser les paramètres de l'analyseur par défaut pour ouvrir les fichiers CSV. Parfois, l'importation d'un fichier CSV ne crée pas la sortie attendue, comme le format de date n'est pas tel qu'attendu ou les champs vides sont gérés différemment. Dans ce but, [**TxtLoadOptions.PreferredParsers**](https://reference.aspose.com/cells/java/com.aspose.cells/txtloadoptions#PreferredParsers) est disponible pour fournir son propre analyseur préféré pour analyser différents types de données selon les besoins. Le code d'exemple suivant illustre l'utilisation de l'analyseur préféré.  

Le fichier source d'échantillon et les fichiers de sortie peuvent être téléchargés aux liens suivants pour tester cette fonctionnalité.

[samplePreferredParser.csv](samplePreferredParser.csv)

[outputsamplePreferredParser.xlsx](outputsamplePreferredParser.xlsx)

## **Exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningCSVFilesWithPreferredParser-1.java" >}}

### **Ouverture des fichiers TSV (Séparé par des tabulations)**

Les fichiers tabulés contiennent des données de feuilles de calcul mais sans mise en forme. Les données sont disposées en lignes et colonnes comme des tableaux et des feuilles de calcul. Bref, un fichier tabulé est un type spécial de fichier texte simple avec une tabulation entre chaque colonne dans le texte.

Pour ouvrir des fichiers tabulés, les développeurs doivent utiliser la classe [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) et sélectionner la valeur [**TSV**](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#TSV), prédéfinie dans l'énumération [**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat).

## **Exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningTabDelimitedFiles-OpeningTabDelimitedFiles.java" >}}

## **Sujets avancés**
- [Charger ou importer un fichier CSV avec des formules](/cells/fr/java/load-or-import-csv-file-with-formulas/)
- [Supprimer les lignes et colonnes vides en tête lors de l'exportation de feuilles de calcul au format CSV](/cells/fr/java/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)

{{< app/cells/assistant language="java" >}}
