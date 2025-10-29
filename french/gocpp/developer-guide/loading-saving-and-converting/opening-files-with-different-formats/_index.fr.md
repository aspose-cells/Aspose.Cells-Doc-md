---
title: Ouverture de fichiers avec différents formats
type: docs
weight: 30
url: /fr/go-cpp/opening-files-with-different-formats/

description: L API Aspose.Cells for Go via C++ vous permet d ouvrir/lire différents formats comme XLSX, HTML, CSV, ODS, TSV, SXC, FODS, etc.
keywords: ouvrir des fichiers xlsx, ouvrir des fichiers html, lire des fichiers fods, lire des fichiers ods, lire des fichiers sxc, ouvrir des fichiers csv, valeurs tabulées, SpreadsheetML, tsv, mhtml
---

{{% alert color="primary" %}}

Avec Aspose.Cells, vous pouvez ouvrir des fichiers avec différents formats. **Aspose.Cells** peut ouvrir une gamme de formats de fichiers tels que les feuilles de calcul Microsoft Excel (XLS, XLSX, XLSM, XLSB), SpreadsheetML, valeurs séparées par des virgules (CSV), fichiers délimités par tabulation ou tabulaires (TSV), etc.

Si vous avez besoin de connaître tous les formats de fichier pris en charge, veuillez vous référer aux pages suivantes:
[Formats de fichiers pris en charge](https://docs.aspose.com/cells/go-cpp/supported-file-formats/)

{{% /alert %}}

## **Ouvrir des fichiers avec différents formats**

Aspose.Cells permet aux développeurs d'ouvrir des fichiers de feuilles de calcul avec différents formats tels que SpreadsheetML, valeurs séparées par des virgules (CSV), fichiers délimités par tabulation ou TSV, et fichiers ODS. Pour ouvrir de tels fichiers, les développeurs peuvent utiliser la même méthodologie que celle utilisée pour ouvrir des fichiers de différentes versions de Microsoft Excel.

### **Ouverture de fichiers SpreadsheetML**

Les fichiers SpreadsheetML sont des représentations XML de feuilles de calcul incluant toutes les informations à leur sujet, telles que la mise en forme, les formules, etc. Depuis Microsoft Excel XP, une option d'exportation XML a été ajoutée à Microsoft Excel pour exporter vos feuilles de calcul vers des fichiers SpreadsheetML.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenSpreadsheetMLFile.go" >}}

### **Ouverture de fichiers HTML**

Aspose.Cells vous permet d'ouvrir un fichier HTML dans un objet Workbook. Le fichier HTML doit être orienté Microsoft Excel, c'est-à-dire que MS-Excel doit pouvoir l'ouvrir.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenHTMLFile.go" >}}

### **Ouverture des fichiers CSV**

Les fichiers au format Valeurs Séparées par des Virgules (CSV) contiennent des enregistrements où les valeurs sont séparées par des virgules. Les données sont stockées sous forme de tableau où chaque colonne est séparée par le caractère virgule et est encadrée par le caractère double quote. Si une valeur de champ contient un caractère de guillemet double, il est échappé avec une paire de caractères de guillemet double. Vous pouvez également utiliser Microsoft Excel pour exporter des données de feuille de calcul vers un fichier CSV.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenCSVFile.go" >}}

### **Ouverture de fichiers texte avec un séparateur personnalisé**

Les fichiers texte sont utilisés pour stocker des données de feuille de calcul sans mise en forme. Le fichier est une sorte de fichier texte brut qui peut avoir des délimiteurs personnalisés.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenTextFilewithCustomSeparator.go" >}}

Des fichiers sources d'exemple peuvent être téléchargés à partir des liens suivants pour tester cette fonctionnalité.

[CustomSeparator.txt](CustomSeparator.txt)

### **Ouverture des fichiers à valeurs séparées par des tabulations**

Un fichier de texte délimité par tabulation (Text) contient des données de feuille de calcul mais sans mise en forme. Les données sont organisées en lignes et colonnes comme dans les tableaux et feuilles de calcul. Fondamentalement, un fichier délimité par tabulation est un type particulier de fichier texte simple avec une tabulation entre chaque colonne.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenTabDelimitedFile.go" >}}

### **Ouverture des fichiers à valeurs séparées par des tabulations (TSV)**

Un fichier de valeurs séparées par des tabulations (TSV) contient des données de feuille de calcul mais sans mise en forme. C'est la même chose qu'un fichier délimité par tabulation où les données sont organisées en lignes et colonnes comme dans les tableaux et feuilles de calcul.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenTSVFile.go" >}}

### **Ouverture de fichiers SXC**

StarOffice Calc est similaire à Microsoft Excel et supporte les formules, graphiques, fonctions, et macros. Les feuilles de calcul créées avec ce logiciel sont enregistrées avec l'extension SXC. Le fichier SXC est également utilisé pour les fichiers de feuilles de calcul OpenOffice.org Calc. Aspose.Cells peut lire les fichiers SXC, comme illustré par l'exemple de code suivant.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenSXCFile.go" >}}

### **Ouverture de fichiers FODS**

Le fichier FODS est une feuille de calcul enregistrée en XML OpenDocument sans compression. Aspose.Cells peut lire les fichiers FODS, comme démontré par l'exemple de code suivant.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenFODSFile.go" >}}
