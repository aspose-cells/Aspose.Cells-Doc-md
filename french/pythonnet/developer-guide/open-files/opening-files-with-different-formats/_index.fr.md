---
title: Ouverture de fichiers avec différents formats
type: docs
weight: 30
url: /fr/python-net/opening-files-with-different-formats/
description: L API Aspose.Cells pour Python via .NET vous permet d ouvrir/lire différents formats comme XLSX, HTML, CSV, ODS, TSV, SXC, FODS, etc.
keywords: ouvrir des fichiers xlsx, ouvrir des fichiers html, lire des fichiers fods, lire des fichiers ods, lire des fichiers sxc, ouvrir des fichiers csv, valeurs tabulées, SpreadsheetML, tsv, mhtml
---

{{% alert color="primary" %}}

En utilisant Aspose.Cells pour Python via .NET, vous pouvez ouvrir des fichiers avec différents formats. Aspose.Cells pour Python via .NET peut ouvrir une gamme de formats de fichiers tels que les feuilles de calcul Microsoft Excel (XLS, XLSX, XLSM, XLSB), SpreadsheetML, valeurs séparées par des virgules (CSV), fichiers délimités par des tabulations ou valeurs séparées par des tabulations (TSV), etc.

Si vous avez besoin de connaître tous les formats de fichier pris en charge, veuillez vous référer aux pages suivantes:
[Formats de fichier pris en charge](https://docs.aspose.com/cells/python-net/supported-file-formats/)

{{% /alert %}}

## **Ouvrir des fichiers avec différents formats**

Aspose.Cells pour Python via .NET permet aux développeurs d'ouvrir des fichiers de feuilles de calcul avec différents formats tels que SpreadsheetML, valeurs séparées par des virgules (CSV), délimitation par tabulation ou valeurs séparées par des tabulations (TSV), fichiers ODS. Pour ouvrir ces fichiers, les développeurs peuvent utiliser la même méthodologie que pour ouvrir des fichiers de différentes versions de Microsoft Excel.

### **Ouverture de fichiers SpreadsheetML**

Les fichiers SpreadsheetML sont des représentations XML de feuilles de calcul comprenant toutes les informations à leur sujet, telles que la mise en forme, les formules, etc. Depuis Microsoft Excel XP, une option d'exportation XML est ajoutée à Microsoft Excel qui exporte vos feuilles de calcul vers des fichiers SpreadsheetML.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningSpreadsheetMLFiles-1.py" >}}

### **Ouverture de fichiers HTML**

Aspose.Cells pour Python via .NET vous permet d'ouvrir un fichier HTML dans un objet Workbook. Le fichier HTML doit être orienté Microsoft Excel, c’est-à-dire qu’MS-Excel doit pouvoir l’ouvrir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningHTMLFile-1.py" >}}

### **Ouverture des fichiers CSV**

Les fichiers au format Valeurs Séparées par des Virgules (CSV) contiennent des enregistrements où les valeurs sont séparées par des virgules. Les données sont stockées sous forme de tableau où chaque colonne est séparée par le caractère virgule et est encadrée par le caractère double quote. Si une valeur de champ contient un caractère de guillemet double, il est échappé avec une paire de caractères de guillemet double. Vous pouvez également utiliser Microsoft Excel pour exporter des données de feuille de calcul vers un fichier CSV.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningCSVFiles-1.py" >}}

#### **Ouverture des fichiers CSV et remplacement des caractères invalides**

Dans Excel, lorsque vous ouvrez un fichier CSV avec des caractères spéciaux, les caractères sont automatiquement remplacés. La même chose est faite par l’API Aspose.Cells pour Python via .NET, comme illustré dans l’exemple de code ci-dessous.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningCSVFilesAndReplacingInvalidCharacters-1.py" >}}



### **Ouverture des fichiers à valeurs séparées par des tabulations**

Un fichier délimité par des tabulations (texte) contient des données de feuille de calcul mais sans aucun formatage. Les données sont disposées en lignes et en colonnes comme dans les tableaux et les feuilles de calcul. Fondamentalement, un fichier délimité par des tabulations est un type spécial de fichier texte brut avec une tabulation entre chaque colonne.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningTabDelimitedFiles-1.py" >}}

### **Ouverture des fichiers à valeurs séparées par des tabulations (TSV)**

Un fichier à valeurs séparées par des tabulations (TSV) contient des données de feuille de calcul mais sans aucun formatage. C'est la même chose avec un fichier délimité par des tabulations où les données sont disposées en lignes et en colonnes comme dans les tableaux et les feuilles de calcul.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningTSVFiles-1.py" >}}

### **Ouverture de fichiers SXC**

StarOffice Calc est similaire à Microsoft Excel et supporte les formules, graphiques, fonctions et macros. Les feuilles de calcul créées avec ce logiciel sont enregistrées avec l’extension SXC. Le fichier SXC est également utilisé pour les fichiers de feuilles de calcul OpenOffice.org Calc. Aspose.Cells pour Python via .NET peut lire les fichiers SXC comme démontré dans l’exemple de code suivant.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningSXCFiles-1.py" >}}

### **Ouverture de fichiers FODS**

Le fichier FODS est une feuille de calcul enregistrée en XML OpenDocument sans compression. Aspose.Cells pour Python via .NET peut lire les fichiers FODS comme démontré dans l’exemple de code ci-dessous.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningFODSFiles-1.py" >}}
