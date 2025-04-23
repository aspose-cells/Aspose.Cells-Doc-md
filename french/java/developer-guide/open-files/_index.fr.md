---
title: Ouverture de fichiers avec différents formats
linktitle: Ouvrir des fichiers
type: docs
weight: 10
url: /fr/java/opening-files-with-different-formats/
---

{{% alert color="primary" %}}

Utilisation par les développeurs d'Aspose.Cells pour ouvrir des fichiers à différentes fins. Par exemple, ouvrir un fichier pour récupérer des données à partir de celui-ci, ou utiliser un fichier de feuille de calcul prédéfinie pour accélérer votre processus de développement. Aspose.Cells permet aux développeurs d'ouvrir différents types de fichiers source. Ces fichiers source peuvent être des rapports Microsoft Excel, SpreadsheetML, des fichiers de valeurs séparées par des virgules (CSV), des fichiers de valeurs séparées par des onglets ou des valeurs séparées par des onglets (TSV). Cet article traite de l'ouverture de ces différents fichiers source à l'aide d'Aspose.Cells.

Si vous avez besoin de connaître tous les formats de fichier pris en charge, veuillez vous référer aux pages suivantes:
[Formats de fichiers pris en charge](https://docs.aspose.com/cells/java/supported-file-formats/)

{{% /alert %}}

## **Moyens simples d'ouvrir des fichiers Excel**

### **Ouverture par chemin**

Pour ouvrir un fichier Microsoft Excel en utilisant le chemin du fichier, transmettez le chemin du fichier en tant que paramètre lors de la création de l'instance de la classe [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook). Le code d'exemple suivant démontre l'ouverture d'un fichier Excel en utilisant le chemin du fichier.

#### **Exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningFilesThroughPath-OpeningFilesThroughPath.java" >}}

### **Ouverture via un flux**

Parfois, le fichier Excel que vous voulez ouvrir est stocké en tant que flux. Dans ce cas, tout comme pour ouvrir un fichier en utilisant le chemin du fichier, transmettez le flux en tant que paramètre lors de l'instanciation de la classe [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook). Le code d'exemple suivant démontre l'ouverture d'un fichier Excel en utilisant un flux.

#### **Exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningFilesThroughStream-OpeningFilesThroughStream.java" >}}

### **Ouverture de fichiers de différentes versions de Microsoft Excel**

L'utilisateur peut utiliser la classe [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) pour spécifier le format du fichier Excel en utilisant l'énumération [**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat).

L'énumération [**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat) contient de nombreux formats de fichier prédéfinis dont certains sont donnés ci-dessous.

|**Types de format**|**Description**|
| :- | :- |
|Csv|Représente un fichier CSV|
|Excel97To2003|Représente un fichier Excel 97 - 2003|
|Xlsx|Représente un fichier XLSX Excel 2007/2010/2013/2016/2019 et Office 365|
|Xlsm|Représente un fichier XLSM Excel 2007/2010/2013/2016/2019 et Office 365|
|Xltx|Représente un modèle de fichier XLTX Excel 2007/2010/2013/2016/2019 et Office 365
|Xltm|Représente un fichier activé par macro XLTM Excel 2007/2010/2013/2016/2019 et Office 365|
|Xlsb|Représente un fichier binaire XLSB Excel 2007/2010/2013/2016/2019 et Office 365|
|SpreadsheetML|Représente un fichier SpreadsheetML|
|Tsv|Représente un fichier de valeurs séparées par des tabulations|
|TabDelimited|Représente un fichier de texte à onglets|
|Ods|Représente un fichier ODS|
|Html|Représente un fichier HTML|
|Mhtml|Représente un fichier MHTML|

### **Ouverture de fichiers Microsoft Excel 95/5.0**

Pour ouvrir des fichiers Microsoft Excel 95, instanciez la classe [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) avec le chemin ou le flux du fichier modèle. Le fichier d'exemple pour tester le code peut être téléchargé depuis le lien suivant :

[Excel95_5.0.xls](Excel95_5.0.xls)

#### **Exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningExcel95_5_0XLSFiles-1.java" >}}

### **Ouverture des fichiers XLS de Microsoft Excel 97 ou des versions ultérieures**

Pour ouvrir des fichiers XLS de Microsoft Excel XLS 97 ou des versions ultérieures, instanciez la classe [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) avec le chemin ou le flux du fichier modèle. Ou utilisez la méthode [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) et sélectionnez la valeur [**EXCEL_97_TO_2003**](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#EXCEL-97-TO-2003) dans l'énumération [**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat).

#### **Exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningMicrosoftExcel972003Files-OpeningMicrosoftExcel972003Files.java" >}}

### **Ouverture des fichiers XLSX de Microsoft Excel 2007 ou des versions ultérieures**

Pour ouvrir des fichiers XLSX de Microsoft Excel 2007 ou des versions ultérieures, instanciez la classe [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) avec le chemin ou le flux du fichier modèle. Ou utilisez la classe [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) et sélectionnez la valeur [**XLSX**](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#XLSX) dans l'énumération [**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat).

#### **Exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningMicrosoftExcel2007XlsxFiles-OpeningMicrosoftExcel2007XlsxFiles.java" >}}

### **Ouvrir des fichiers avec différents formats**

Aspose.Cells permet aux développeurs d'ouvrir des fichiers de feuille de calcul avec différents formats tels que SpreadsheetML, CSV, fichiers à délimitation tabulaire. Pour ouvrir de tels fichiers, les développeurs peuvent utiliser la même méthodologie que celle utilisée pour l'ouverture de fichiers de différentes versions de Microsoft Excel.

### **Ouverture de fichiers SpreadsheetML**

Les fichiers SpreadsheetML sont les représentations XML de vos feuilles de calcul, incluant toutes les informations sur la feuille de calcul telles que le formatage, les formules, etc. Depuis Microsoft Excel XP, une option d'exportation XML est ajoutée à Microsoft Excel qui exporte vos feuilles de calcul vers des fichiers SpreadsheetML.

Pour ouvrir des fichiers SpreadsheetML, utilisez la classe [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) et sélectionnez la valeur [**SPREADSHEET_ML**](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#SPREADSHEET-ML) dans l'énumération [**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat).

#### **Exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningSpreadsheetMLFiles-OpeningSpreadsheetMLFiles.java" >}}

### **Ouverture des fichiers CSV**

Les fichiers de valeurs séparées par des virgules (CSV) contiennent des enregistrements dont les valeurs sont délimitées ou séparées par des virgules. Dans les fichiers CSV, les données sont stockées dans un format tabulaire qui a des champs séparés par le caractère virgule et mis entre guillemets par le caractère double quote. Si la valeur d'un champ contient un double guillemet, elle est échappée avec une paire de double guillemets. Vous pouvez également utiliser Microsoft Excel pour exporter les données de votre feuille de calcul vers un fichier CSV.

Pour ouvrir des fichiers CSV, utilisez la classe [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) et sélectionnez la valeur [**CSV**](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#CSV), prédéfinie dans l'énumération [**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat).

#### **Exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningCSVFiles-OpeningCSVFiles.java" >}}

### **Ouverture des fichiers CSV et remplacement des caractères invalides**

Dans Excel, lorsqu'un fichier CSV avec des caractères spéciaux est ouvert, les caractères sont automatiquement remplacés. Il en va de même pour l'API Aspose.Cells qui est démontrée dans l'exemple de code ci-dessous.

#### **Exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningCSVFilesAndReplacingInvalidCharacters-1.java" >}}

### **Ouverture des fichiers CSV en utilisant un analyseur préféré**

Ce n'est pas toujours nécessaire d'utiliser les paramètres de l'analyseur par défaut pour ouvrir les fichiers CSV. Parfois, l'importation d'un fichier CSV ne crée pas la sortie attendue, comme le format de date n'est pas tel qu'attendu ou les champs vides sont gérés différemment. Dans ce but, [**TxtLoadOptions.PreferredParsers**](https://reference.aspose.com/cells/java/com.aspose.cells/txtloadoptions#PreferredParsers) est disponible pour fournir son propre analyseur préféré pour analyser différents types de données selon les besoins. Le code d'exemple suivant illustre l'utilisation de l'analyseur préféré.  

Le fichier source d'échantillon et les fichiers de sortie peuvent être téléchargés aux liens suivants pour tester cette fonctionnalité.

[samplePreferredParser.csv](samplePreferredParser.csv)

[outputsamplePreferredParser.xlsx](outputsamplePreferredParser.xlsx)

#### **Exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningCSVFilesWithPreferredParser-1.java" >}}

### **Ouverture des fichiers TSV (Séparé par des tabulations)**

Les fichiers tabulés contiennent des données de feuilles de calcul mais sans mise en forme. Les données sont disposées en lignes et colonnes comme des tableaux et des feuilles de calcul. Bref, un fichier tabulé est un type spécial de fichier texte simple avec une tabulation entre chaque colonne dans le texte.

Pour ouvrir des fichiers tabulés, les développeurs doivent utiliser la classe [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) et sélectionner la valeur [**TSV**](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#TSV), prédéfinie dans l'énumération [**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat).

#### **Exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningTabDelimitedFiles-OpeningTabDelimitedFiles.java" >}}

### **Ouverture de fichiers Excel chiffrés**

Nous savons qu'il est possible de créer des fichiers Excel chiffrés à l'aide de Microsoft Excel. Pour ouvrir de tels fichiers chiffrés, les développeurs doivent appeler une méthode LoadOptions surchargée spéciale et sélectionner la valeur DEFAULT prédéfinie dans l'énumération FileFormatType. Cette méthode prendrait également le mot de passe pour le fichier chiffré comme indiqué ci-dessous dans l'exemple.

#### **Exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningEncryptedExcelFiles-OpeningEncryptedExcelFiles.java" >}}

Aspose.Cells prend également en charge l'ouverture de fichiers MS Excel 2013 protégés par mot de passe.

{{% alert color="primary" %}}

Il est fort probable que le constructeur de classe Workbook puisse générer une System.OutOfMemoryException lors du chargement de grandes feuilles de calcul. Cette exception suggère que la mémoire disponible est insuffisante pour charger complètement la feuille de calcul en mémoire, par conséquent, la feuille de calcul doit être chargée en activant les [Préférences de mémoire](/cells/fr/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/).

{{% /alert %}}

### **Ouverture de fichiers SXC**

StarOffice Calc est similaire à Microsoft Excel et prend en charge les formules, les graphiques, les fonctions et les macros. Les feuilles de calcul créées avec ce logiciel sont enregistrées avec l'extension SXC. Le fichier SXC est également utilisé pour les fichiers de feuille de calcul OpenOffice.org Calc. Aspose.Cells peut lire les fichiers SXC comme démontré par l'exemple de code suivant.

#### **Exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Files-Handling-OpeningSXCFiles-1.java" >}}

### **Ouverture de fichiers FODS**

Le fichier FODS est une feuille de calcul enregistrée au format OpenDocument XML sans compression. Aspose.Cells peut lire les fichiers FODS comme le montre l'exemple de code suivant.

#### **Exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Files-Handling-OpeningFODSFiles-1.java" >}}

## **Sujets avancés**
- [Filtrer les noms définis lors du chargement du classeur](/cells/fr/java/filter-defined-names-while-loading-workbook/)
- [Filtrer les objets lors du chargement du classeur ou de la feuille de calcul](/cells/fr/java/filter-objects-while-loading-workbook-or-worksheet/)
- [Obtenir des avertissements lors du chargement d'un fichier Excel](/cells/fr/java/get-warnings-while-loading-excel-file/)
- [Conserver les séparateurs pour les lignes vides lors de l'exportation de feuilles de calcul au format CSV](/cells/fr/java/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)
- [Charger le classeur avec une taille de papier d'imprimante spécifiée](/cells/fr/java/load-workbook-with-specified-printer-paper-size/)
- [Ouvrir des fichiers de différentes versions de Microsoft Excel](/cells/fr/java/opening-different-microsoft-excel-versions-files/)
- [Optimiser l'utilisation de la mémoire lors du travail avec de gros fichiers contenant de grands ensembles de données](/cells/fr/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)
- [Lire des feuilles de calcul numériques développées par Apple Inc. à l'aide d'Aspose.Cells](/cells/fr/java/read-numbers-spreadsheet-developed-by-apple-inc-using-aspose-cells/)
- [Lecture d'un fichier CSV avec des encodages multiples](/cells/fr/java/reading-csv-file-with-multiple-encodings/)
- [Arrêter la conversion ou le chargement à l'aide de InterruptMonitor lorsqu'il prend trop de temps](/cells/fr/java/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/)
- [Utiliser l'API LightCells](/cells/fr/java/using-lightcells-api/)
{{< app/cells/assistant language="java" >}}
