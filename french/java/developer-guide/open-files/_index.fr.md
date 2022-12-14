---
title: Ouverture de fichiers avec différents formats
linktitle: Ouvrir des fichiers
type: docs
weight: 10
url: /fr/java/opening-files-with-different-formats/
---
{{% alert color="primary" %}}

Les développeurs utilisent Aspose.Cells pour ouvrir des fichiers à des fins différentes. Par exemple, ouvrez un fichier pour en extraire des données ou utilisez une feuille de calcul de concepteur prédéfinie pour accélérer votre processus de développement. Aspose.Cells permet aux développeurs d'ouvrir différents types de fichiers source. Ces fichiers sources peuvent être des rapports Excel Microsoft, SpreadsheetML, des fichiers de valeurs séparées par des virgules (CSV), des fichiers de valeurs séparées par des tabulations ou des fichiers TSV. Cet article traite de l'ouverture de ces différents fichiers source à l'aide de Aspose.Cells.

Si vous avez besoin de connaître tous les formats de fichiers pris en charge, veuillez vous référer aux pages suivantes :
[Formats de fichiers pris en charge](https://docs.aspose.com/cells/java/supported-file-formats/)

{{% /alert %}}

## **Des moyens simples d'ouvrir des fichiers Excel**

### **Ouverture par chemin**

Pour ouvrir un fichier Excel Microsoft à l'aide du chemin du fichier, passez le chemin du fichier en tant que paramètre lors de la création de l'instance du**[Classeur](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)**classer. L'exemple de code suivant illustre l'ouverture d'un fichier Excel à l'aide du chemin d'accès au fichier.

#### **Exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningFilesThroughPath-OpeningFilesThroughPath.java" >}}

### **Ouverture via Stream**

Parfois, le fichier Excel que vous souhaitez ouvrir est stocké sous forme de flux. Dans ce cas, similaire à l'ouverture d'un fichier en utilisant le chemin du fichier, passez le flux en tant que paramètre lors de l'instanciation du**[Classeur](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)**classer. L'exemple de code suivant illustre l'ouverture d'un fichier Excel à l'aide de stream.

#### **Exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningFilesThroughStream-OpeningFilesThroughStream.java" >}}

### **Ouverture de fichiers de différentes versions d'Excel Microsoft**

 L'utilisateur peut utiliser le**[LoadOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)** classe pour spécifier le format du fichier Excel à l'aide de la**[ChargerFormat](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)**énumération.

 La**[ChargerFormat](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)**énumération contient de nombreux formats de fichiers prédéfinis dont certains sont donnés ci-dessous.

|**Types de formats**|**La description**|
|:- |:- |
|CSV|Représente un fichier CSV|
|Excel97To2003|Représente un fichier Excel 97 - 2003|
|Xlsx|Représente un fichier Excel 2007/2010/2013/2016/2019 et Office 365 XLSX|
|Xlsm|Représente un fichier Excel 2007/2010/2013/2016/2019 et Office 365 XLSM|
|XLTX|Représente un fichier XLTX de modèle Excel 2007/2010/2013/2016/2019 et Office 365|
|Xltm|Représente un fichier Excel 2007/2010/2013/2016/2019 et Office 365 prenant en charge les macros XLTM|
|Xlsb|Représente un fichier XLSB binaire Excel 2007/2010/2013/2016/2019 et Office 365|
|TableurML|Représente un fichier SpreadsheetML|
|Tsv|Représente un fichier de valeurs séparées par des tabulations|
|Onglet délimité|Représente un fichier texte délimité par des tabulations|
|cotes|Représente un fichier ODS|
|HTML|Représente un fichier HTML|
|Mhtml|Représente un fichier MHTML|

### **Ouverture des fichiers Microsoft Excel 95/5.0**

 Pour ouvrir les fichiers Microsoft Excel 95, instanciez le**[Classeur](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)**instance avec le chemin ou le flux du fichier modèle. Un exemple de fichier pour tester le code peut être téléchargé à partir du lien suivant :

[Excel95_5.0.xls](Excel95_5.0.xls)

#### **Exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningExcel95_5_0XLSFiles-1.java" >}}

### **Ouverture des fichiers XLS Microsoft Excel 97 ou versions ultérieures**

 Pour ouvrir les fichiers XLS de Microsoft Excel XLS 97 ou versions ultérieures, instanciez le**[Classeur](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)** instance avec le chemin ou le flux du fichier modèle. Ou utilisez le**[LoadOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)** méthode et sélectionnez la**[EXCEL_97_TO_2003](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#EXCEL_97_TO_2003)** valeur dans le**[ChargerFormat](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)**énumération.

#### **Exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningMicrosoftExcel972003Files-OpeningMicrosoftExcel972003Files.java" >}}

### **Ouverture des fichiers XLSX Microsoft Excel 2007 ou versions ultérieures**

 Pour ouvrir les fichiers XLSX de Microsoft Excel 2007 ou versions ultérieures, instanciez le**[Classeur](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)**instance avec le chemin ou le flux du fichier modèle. Ou utilisez le**[LoadOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)** classe et sélectionnez la**[XLSX](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#XLSX)** valeur dans le**[ChargerFormat](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)**énumération.

#### **Exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningMicrosoftExcel2007XlsxFiles-OpeningMicrosoftExcel2007XlsxFiles.java" >}}

### **Ouverture de fichiers avec différents formats**

Aspose.Cells permet aux développeurs d'ouvrir des fichiers de feuille de calcul avec différents formats tels que SpreadsheetML, CSV, fichiers délimités par des tabulations. Pour ouvrir de tels fichiers, les développeurs peuvent utiliser la même méthodologie que celle utilisée pour ouvrir des fichiers de différentes versions d'Excel Microsoft.

### **Ouverture de fichiers SpreadsheetML**

Les fichiers SpreadsheetML sont les représentations XML de vos feuilles de calcul, y compris toutes les informations sur la feuille de calcul telles que le formatage, les formules, etc. Depuis Microsoft Excel XP, une option d'exportation XML est ajoutée à Microsoft Excel qui exporte vos feuilles de calcul vers des fichiers SpreadsheetML.

Pour ouvrir les fichiers SpreadsheetML, utilisez le**[LoadOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)** classe et sélectionnez la**[SPREADSHEET_ML](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#SPREADSHEET_ML)** valeur dans le**[ChargerFormat](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)**énumération.

#### **Exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningSpreadsheetMLFiles-OpeningSpreadsheetMLFiles.java" >}}

### **Ouverture de fichiers CSV**

Les fichiers de valeurs séparées par des virgules (CSV) contiennent des enregistrements dont les valeurs sont délimitées ou séparées par des virgules. Dans les fichiers CSV, les données sont stockées dans un format tabulaire dont les champs sont séparés par une virgule et entre guillemets. Si la valeur d'un champ contient un guillemet double, elle est échappée avec une paire de guillemets doubles. Vous pouvez également utiliser Microsoft Excel pour exporter vos données de feuille de calcul vers un fichier CSV.

Pour ouvrir les fichiers CSV, utilisez le**[LoadOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)** classe et sélectionnez la**[CSV](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#CSV)** valeur, prédéfinie dans le**[ChargerFormat](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)**énumération.

#### **Exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningCSVFiles-OpeningCSVFiles.java" >}}

### **Ouverture des fichiers CSV et remplacement des caractères invalides**

Dans Excel, lorsque le fichier CSV contenant des caractères spéciaux est ouvert, les caractères sont automatiquement remplacés. La même chose est faite par Aspose.Cells API qui est démontré dans l'exemple de code ci-dessous.

#### **Exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningCSVFilesAndReplacingInvalidCharacters-1.java" >}}

### **Ouverture de fichiers CSV à l'aide de l'analyseur préféré**

Il n'est pas toujours nécessaire d'utiliser les paramètres d'analyseur par défaut pour ouvrir les fichiers CSV. Parfois, l'importation d'un fichier CSV ne crée pas la sortie attendue, car le format de date n'est pas comme prévu ou les champs vides sont traités différemment. Dans ce but**[TxtLoadOptions.PreferredParsers](https://reference.aspose.com/cells/java/com.aspose.cells/txtloadoptions#PreferredParsers)**est disponible pour fournir son propre analyseur préféré pour analyser différents types de données selon les besoins. L'exemple de code suivant illustre l'utilisation de l'analyseur préféré.

Des exemples de fichiers source et de sortie peuvent être téléchargés à partir des liens suivants pour tester cette fonctionnalité.

[exemplePreferredParser.csv](samplePreferredParser.csv)

[outputsamplePreferredParser.xlsx](outputsamplePreferredParser.xlsx)

#### **Exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningCSVFilesWithPreferredParser-1.java" >}}

### **Ouverture de fichiers TSV (délimités par des tabulations)**

Les fichiers délimités par des tabulations contiennent des données de feuille de calcul mais sans aucune mise en forme. Les données sont organisées en lignes et en colonnes telles que des tableaux et des feuilles de calcul. En bref, un fichier délimité par des tabulations est un type spécial de fichier texte brut avec une tabulation entre chaque colonne du texte.

Pour ouvrir des fichiers délimités par des tabulations, les développeurs doivent utiliser le**[LoadOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)** classe et sélectionnez la**[TSV](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#TSV)** valeur, prédéfinie dans le**[ChargerFormat](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)**énumération.

#### **Exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningTabDelimitedFiles-OpeningTabDelimitedFiles.java" >}}

### **Ouverture de fichiers Excel cryptés**

Nous savons qu'il est possible de créer des fichiers Excel cryptés en utilisant Microsoft Excel. Pour ouvrir de tels fichiers chiffrés, les développeurs doivent appeler une méthode spéciale LoadOptions surchargée et sélectionner la valeur DEFAULT, prédéfinie dans l'énumération FileFormatType. Cette méthode prendrait également le mot de passe du fichier crypté, comme indiqué ci-dessous dans l'exemple.

#### **Exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningEncryptedExcelFiles-OpeningEncryptedExcelFiles.java" >}}

Aspose.Cells prend également en charge l'ouverture de fichiers MS Excel 2013 protégés par mot de passe.

{{% alert color="primary" %}}

Il y a de bonnes chances que le constructeur Workbook lève System.OutOfMemoryException lors du chargement de feuilles de calcul volumineuses. Cette exception suggère que la mémoire disponible est insuffisante pour charger complètement la feuille de calcul dans la mémoire, par conséquent, la feuille de calcul doit être chargée tout en activant le[Préférences de mémoire](/cells/fr/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/).

{{% /alert %}}

### **Ouverture des fichiers SXC**

StarOffice Calc est similaire à Microsoft Excel et prend en charge les formules, les graphiques, les fonctions et les macros. Les feuilles de calcul créées avec ce logiciel sont enregistrées avec l'extension SXC. Le fichier SXC est également utilisé pour les fichiers de feuille de calcul OpenOffice.org Calc. Aspose.Cells peut lire les fichiers SXC comme illustré par l'exemple de code suivant.

#### **Exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Files-Handling-OpeningSXCFiles-1.java" >}}

### **Ouverture des fichiers FODS**

Le fichier FODS est une feuille de calcul enregistrée dans OpenDocument XML sans aucune compression. Aspose.Cells peut lire les fichiers FODS comme le montre l'exemple de code suivant.

#### **Exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Files-Handling-OpeningFODSFiles-1.java" >}}

## **Sujets avancés**
- [Filtrer les noms définis lors du chargement du classeur](/cells/fr/java/filter-defined-names-while-loading-workbook/)
- [Filtrer les objets lors du chargement du classeur ou de la feuille de calcul](/cells/fr/java/filter-objects-while-loading-workbook-or-worksheet/)
- [Obtenir des avertissements lors du chargement du fichier Excel](/cells/fr/java/get-warnings-while-loading-excel-file/)
- [Conserver les séparateurs pour les lignes vides lors de l'exportation des feuilles de calcul au format CSV](/cells/fr/java/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)
- [Charger le classeur avec le format de papier d'imprimante spécifié](/cells/fr/java/load-workbook-with-specified-printer-paper-size/)
- [Ouverture de différents fichiers de versions Excel Microsoft](/cells/fr/java/opening-different-microsoft-excel-versions-files/)
- [Optimisation de l'utilisation de la mémoire lors de l'utilisation de fichiers volumineux contenant de grands ensembles de données](/cells/fr/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)
- [Lire la feuille de calcul des nombres Développé par Apple Inc. en utilisant Aspose.Cells](/cells/fr/java/read-numbers-spreadsheet-developed-by-apple-inc-using-aspose-cells/)
- [Lecture d'un fichier CSV avec plusieurs encodages](/cells/fr/java/reading-csv-file-with-multiple-encodings/)
- [Arrêtez la conversion ou le chargement à l'aide d'InterruptMonitor lorsque cela prend trop de temps](/cells/fr/java/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/)
- [Utilisation de LightCells API](/cells/fr/java/using-lightcells-api/)
