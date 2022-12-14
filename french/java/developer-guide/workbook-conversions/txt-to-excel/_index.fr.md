---
title: Convertir CSV, TSV et TXT en Excel
type: docs
weight: 50
url: /fr/java/convert-csv-tsv-and-txt-to-excel/
---
## **Ouverture de fichiers CSV**

Les fichiers de valeurs séparées par des virgules (CSV) contiennent des enregistrements dont les valeurs sont délimitées ou séparées par des virgules. Dans les fichiers CSV, les données sont stockées dans un format tabulaire dont les champs sont séparés par une virgule et entre guillemets. Si la valeur d'un champ contient un guillemet double, elle est échappée avec une paire de guillemets doubles. Vous pouvez également utiliser Microsoft Excel pour exporter vos données de feuille de calcul vers un fichier CSV.

Pour ouvrir les fichiers CSV, utilisez le**[LoadOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)** classe et sélectionnez la**[CSV](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#CSV)** valeur, prédéfinie dans le**[ChargerFormat](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)**énumération.

## **Exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningCSVFiles-OpeningCSVFiles.java" >}}

### **Ouverture des fichiers CSV et remplacement des caractères invalides**

Dans Excel, lorsque le fichier CSV contenant des caractères spéciaux est ouvert, les caractères sont automatiquement remplacés. La même chose est faite par Aspose.Cells API qui est démontré dans l'exemple de code ci-dessous.

#### **Exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningCSVFilesAndReplacingInvalidCharacters-1.java" >}}

## **Ouverture de fichiers CSV à l'aide de l'analyseur préféré**

Il n'est pas toujours nécessaire d'utiliser les paramètres d'analyseur par défaut pour ouvrir les fichiers CSV. Parfois, l'importation d'un fichier CSV ne crée pas la sortie attendue, car le format de date n'est pas comme prévu ou les champs vides sont traités différemment. Dans ce but**[TxtLoadOptions.PreferredParsers](https://reference.aspose.com/cells/java/com.aspose.cells/txtloadoptions#PreferredParsers)**est disponible pour fournir son propre analyseur préféré pour analyser différents types de données selon les besoins. L'exemple de code suivant illustre l'utilisation de l'analyseur préféré.

Des exemples de fichiers source et de sortie peuvent être téléchargés à partir des liens suivants pour tester cette fonctionnalité.

[exemplePreferredParser.csv](samplePreferredParser.csv)

[outputsamplePreferredParser.xlsx](outputsamplePreferredParser.xlsx)

## **Exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningCSVFilesWithPreferredParser-1.java" >}}

### **Ouverture de fichiers TSV (délimités par des tabulations)**

Les fichiers délimités par des tabulations contiennent des données de feuille de calcul mais sans aucune mise en forme. Les données sont organisées en lignes et en colonnes telles que des tableaux et des feuilles de calcul. En bref, un fichier délimité par des tabulations est un type spécial de fichier texte brut avec une tabulation entre chaque colonne du texte.

Pour ouvrir des fichiers délimités par des tabulations, les développeurs doivent utiliser le**[LoadOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)** classe et sélectionnez la**[TSV](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#TSV)** valeur, prédéfinie dans le**[ChargerFormat](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)**énumération.

## **Exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningTabDelimitedFiles-OpeningTabDelimitedFiles.java" >}}

## **Sujets avancés**
- [Charger ou importer un fichier CSV avec des formules](/cells/fr/java/load-or-import-csv-file-with-formulas/)
- [Coupez les premières lignes et colonnes vides lors de l'exportation de feuilles de calcul au format CSV](/cells/fr/java/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)

