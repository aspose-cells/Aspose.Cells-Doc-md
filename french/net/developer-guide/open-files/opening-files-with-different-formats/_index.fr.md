---
title: Ouverture de fichiers avec différents formats
type: docs
weight: 30
url: /fr/net/opening-files-with-different-formats/
description: Aspose.Cells for .NET API vous permet d'ouvrir/lire différents formats comme XLSX, HTML, CSV, ODS, TSV, SXC, FODS, etc.
keywords: open xlsx files, open html files, read fods files, read ods files, read sxc files, open csv files, Tab Delimited, SpreadsheetML, tsv, mhtml
---
{{% alert color="primary" %}}

 En utilisant Aspose.Cells, vous pouvez ouvrir des fichiers avec différents formats.**Aspose.Cells** peut ouvrir une gamme de formats de fichiers tels que des feuilles de calcul Excel Microsoft (XLS, XLSX, XLSM, XLSB), SpreadsheetML, des fichiers de valeurs séparées par des virgules (CSV), des fichiers de valeurs séparées par des tabulations ou des valeurs séparées par des tabulations (TSV), etc.

Si vous avez besoin de connaître tous les formats de fichiers pris en charge, veuillez vous référer aux pages suivantes :
[Formats de fichiers pris en charge](https://docs.aspose.com/cells/net/supported-file-formats/)

{{% /alert %}}

## **Ouverture de fichiers avec différents formats**

Aspose.Cells permet aux développeurs d'ouvrir des fichiers de feuille de calcul avec différents formats tels que SpreadsheetML, valeurs séparées par des virgules (CSV), valeurs délimitées par des tabulations ou séparées par des tabulations (TSV), fichiers ODS. Pour ouvrir de tels fichiers, les développeurs peuvent utiliser la même méthodologie que celle utilisée pour ouvrir des fichiers de différentes versions d'Excel Microsoft.

### **Ouverture de fichiers SpreadsheetML**

Les fichiers SpreadsheetML sont des représentations XML des feuilles de calcul, y compris toutes les informations les concernant, telles que le formatage, les formules, etc. Depuis Microsoft Excel XP, une option d'exportation XML est ajoutée à Microsoft Excel qui exporte vos feuilles de calcul vers des fichiers SpreadsheetML.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningSpreadsheetMLFiles-1.cs" >}}

### **Ouverture de fichiers HTML**

Aspose.Cells vous permet d'ouvrir le fichier HTML dans l'objet Workbook. Le fichier HTML doit être orienté Excel Microsoft, c'est-à-dire que MS-Excel doit pouvoir l'ouvrir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningHTMLFile-1.cs" >}}

### **Ouverture de fichiers CSV**

Les fichiers de valeurs séparées par des virgules (CSV) contiennent des enregistrements dans lesquels les valeurs sont séparées par des virgules. Les données sont stockées sous forme de tableau où chaque colonne est séparée par le caractère virgule et entre guillemets doubles. Si une valeur de champ contient un guillemet double, elle est échappée avec une paire de guillemets doubles. Vous pouvez également utiliser Microsoft Excel pour exporter des données de feuille de calcul vers CSV.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningCSVFiles-1.cs" >}}

#### **Ouverture des fichiers CSV et remplacement des caractères invalides**

Dans Excel, lorsque le fichier CSV contenant des caractères spéciaux est ouvert, les caractères sont automatiquement remplacés. La même chose est faite par Aspose.Cells API qui est démontré dans l'exemple de code ci-dessous.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningCSVFilesAndReplacingInvalidCharacters-1.cs" >}}

#### **Utilisation de l'analyseur préféré**

Il n'est pas toujours nécessaire d'utiliser les paramètres d'analyseur par défaut pour ouvrir les fichiers CSV. Parfois, l'importation d'un fichier CSV ne crée pas la sortie attendue, car le format de date n'est pas comme prévu ou les champs vides sont traités différemment. Dans ce but**TxtLoadOptions.PreferredParsers**est disponible pour fournir son propre analyseur préféré pour analyser différents types de données selon les besoins. L'exemple de code suivant illustre l'utilisation de l'analyseur préféré.

Des exemples de fichiers source et de sortie peuvent être téléchargés à partir des liens suivants pour tester cette fonctionnalité.

[exemplePreferredParser.csv](samplePreferredParser.csv)

[outputsamplePreferredParser.xlsx](outputsamplePreferredParser.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningCSVFilesWithPreferredParser-1.cs" >}}

### **Ouverture de fichiers texte avec un séparateur personnalisé**

Les fichiers texte sont utilisés pour contenir des données de feuille de calcul sans formatage. Le fichier est une sorte de fichier texte brut qui peut avoir des délimiteurs personnalisés.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningTextFilewithCustomSeparator-1.cs" >}}

### **Ouverture de fichiers délimités par des tabulations**

Le fichier délimité par des tabulations (texte) contient des données de feuille de calcul mais sans aucune mise en forme. Les données sont organisées en lignes et en colonnes comme dans les tableaux et les feuilles de calcul. Fondamentalement, un fichier délimité par des tabulations est un type spécial de fichier texte brut avec une tabulation entre chaque colonne.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningTabDelimitedFiles-1.cs" >}}

### **Ouverture de fichiers de valeurs séparées par des tabulations (TSV)**

Le fichier de valeurs séparées par des tabulations (TSV) contient des données de feuille de calcul mais sans aucune mise en forme. Il en va de même avec le fichier délimité par des tabulations où les données sont disposées en lignes et en colonnes comme dans les tableaux et les feuilles de calcul.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningTSVFiles-1.cs" >}}

### **Ouverture des fichiers SXC**

StarOffice Calc est similaire à Microsoft Excel et prend en charge les formules, les graphiques, les fonctions et les macros. Les feuilles de calcul créées avec ce logiciel sont enregistrées avec l'extension SXC. Le fichier SXC est également utilisé pour les fichiers de feuille de calcul OpenOffice.org Calc. Aspose.Cells peut lire les fichiers SXC comme illustré par l'exemple de code suivant.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningSXCFiles-1.cs" >}}

### **Ouverture des fichiers FODS**

Le fichier FODS est une feuille de calcul enregistrée dans OpenDocument XML sans aucune compression. Aspose.Cells peut lire les fichiers FODS comme le montre l'exemple de code suivant.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningFODSFiles-1.cs" >}}

