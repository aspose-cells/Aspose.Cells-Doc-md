---
title: Ouverture de fichiers avec différents formats
type: docs
weight: 30
url: /fr/cpp/opening-files-with-different-formats/

description: L API Aspose.Cells for C++ vous permet d ouvrir/lire différents formats tels que XLSX, HTML, CSV, ODS, TSV, SXC, FODS, etc.
keywords: ouvrir des fichiers xlsx, ouvrir des fichiers html, lire des fichiers fods, lire des fichiers ods, lire des fichiers sxc, ouvrir des fichiers csv, valeurs tabulées, SpreadsheetML, tsv, mhtml
---

{{% alert color="primary" %}}

Avec Aspose.Cells, vous pouvez ouvrir des fichiers avec différents formats. **Aspose.Cells** peut ouvrir une variété de formats de fichier tels que les feuilles de calcul Microsoft Excel (XLS, XLSX, XLSM, XLSB), SpreadsheetML, valeurs séparées par des virgules (CSV), valeurs séparées par des tabulations (TSV), etc.

Si vous avez besoin de connaître tous les formats de fichier pris en charge, veuillez vous référer aux pages suivantes:
[Formats de fichier pris en charge](https://docs.aspose.com/cells/cpp/supported-file-formats/)

{{% /alert %}}

## **Ouvrir des fichiers avec différents formats**

Aspose.Cells permet aux développeurs d'ouvrir des fichiers de feuille de calcul avec différents formats tels que SpreadsheetML, valeurs séparées par des virgules (CSV), valeurs séparées par des tabulations (TSV), fichiers ODS. Pour ouvrir de tels fichiers, les développeurs peuvent utiliser la même méthodologie que celle utilisée pour ouvrir des fichiers de différentes versions de Microsoft Excel.

### **Ouverture de fichiers SpreadsheetML**

Les fichiers SpreadsheetML sont des représentations XML de feuilles de calcul comprenant toutes les informations à leur sujet, telles que la mise en forme, les formules, etc. Depuis Microsoft Excel XP, une option d'exportation XML est ajoutée à Microsoft Excel qui exporte vos feuilles de calcul vers des fichiers SpreadsheetML.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenSpreadsheetMLFile-new.cpp" >}}

### **Ouverture de fichiers HTML**

Aspose.Cells vous permet d'ouvrir un fichier HTML dans un objet Workbook. Le fichier HTML doit être orienté Microsoft Excel, c'est-à-dire que MS-Excel doit pouvoir l'ouvrir.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenHTMLFile-new.cpp" >}}

### **Ouverture des fichiers CSV**

Les fichiers au format Valeurs Séparées par des Virgules (CSV) contiennent des enregistrements où les valeurs sont séparées par des virgules. Les données sont stockées sous forme de tableau où chaque colonne est séparée par le caractère virgule et est encadrée par le caractère double quote. Si une valeur de champ contient un caractère de guillemet double, il est échappé avec une paire de caractères de guillemet double. Vous pouvez également utiliser Microsoft Excel pour exporter des données de feuille de calcul vers un fichier CSV.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenCSVFile-new.cpp" >}}

#### **Ouverture des fichiers CSV et remplacement des caractères invalides**

Dans Excel, lorsque vous ouvrez un fichier CSV contenant des caractères spéciaux, les caractères sont automatiquement remplacés. La même opération est effectuée par l'API Aspose.Cells, comme le montre l'exemple de code ci-dessous.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenCSVFileAndReplaceInvalidCharacters-new.cpp" >}}

Le fichier source d'exemple peut être téléchargé depuis les liens suivants pour tester cette fonctionnalité.

[InvalidCharacters.csv](InvalidCharacters.csv)

### **Ouverture de fichiers texte avec un séparateur personnalisé**

Les fichiers texte sont utilisés pour stocker des données de feuille de calcul sans mise en forme. Le fichier est une sorte de fichier texte brut qui peut avoir des délimiteurs personnalisés.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenTextFilewithCustomSeparator-new.cpp" >}}

Le fichier source d'exemple peut être téléchargé depuis les liens suivants pour tester cette fonctionnalité.

[CustomSeparator.txt](CustomSeparator.txt)

### **Ouverture des fichiers à valeurs séparées par des tabulations**

Un fichier délimité par des tabulations (texte) contient des données de feuille de calcul mais sans aucun formatage. Les données sont disposées en lignes et en colonnes comme dans les tableaux et les feuilles de calcul. Fondamentalement, un fichier délimité par des tabulations est un type spécial de fichier texte brut avec une tabulation entre chaque colonne.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenTabDelimitedFile-new.cpp" >}}

### **Ouverture des fichiers à valeurs séparées par des tabulations (TSV)**

Un fichier à valeurs séparées par des tabulations (TSV) contient des données de feuille de calcul mais sans aucun formatage. C'est la même chose avec un fichier délimité par des tabulations où les données sont disposées en lignes et en colonnes comme dans les tableaux et les feuilles de calcul.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenTSVFile-new.cpp" >}}

### **Ouverture de fichiers SXC**

StarOffice Calc est similaire à Microsoft Excel et prend en charge les formules, les graphiques, les fonctions et les macros. Les feuilles de calcul créées avec ce logiciel sont enregistrées avec l'extension SXC. Le fichier SXC est également utilisé pour les fichiers de feuille de calcul OpenOffice.org Calc. Aspose.Cells peut lire les fichiers SXC comme démontré par l'exemple de code suivant.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenSXCFile-new.cpp" >}}

### **Ouverture de fichiers FODS**

Le fichier FODS est une feuille de calcul enregistrée au format OpenDocument XML sans aucune compression. Aspose.Cells peut lire les fichiers FODS comme démontré par l'exemple de code suivant.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenFODSFile-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
