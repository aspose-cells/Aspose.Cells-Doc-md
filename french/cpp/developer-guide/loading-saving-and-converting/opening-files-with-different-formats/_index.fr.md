---
title: Ouverture de fichiers avec différents formats
type: docs
weight: 30
url: /fr/cpp/opening-files-with-different-formats/
description: Aspose.Cells for .NET API vous permet d'ouvrir/lire différents formats comme XLSX, HTML, CSV, ODS, TSV, SXC, FODS, etc.
keywords: open xlsx files, open html files, read fods files, read ods files, read sxc files, open csv files, Tab Delimited, SpreadsheetML, tsv, mhtml
---
{{% alert color="primary" %}}

 En utilisant le Aspose.Cells, vous pouvez ouvrir des fichiers avec différents formats.**Aspose.Cells** peut ouvrir une gamme de formats de fichiers tels que des feuilles de calcul Excel Microsoft (XLS, XLSX, XLSM, XLSB), SpreadsheetML, des fichiers à valeurs séparées par des virgules (CSV), des fichiers délimités par des tabulations ou des valeurs séparées par des tabulations (TSV), etc.

Si vous avez besoin de connaître tous les formats de fichiers pris en charge, veuillez vous référer aux pages suivantes :
[Formats de fichiers pris en charge](https://docs.aspose.com/cells/cpp/supported-file-formats/)

{{% /alert %}}

##  **Ouverture de fichiers avec différents formats**

Aspose.Cells permet aux développeurs d'ouvrir des feuilles de calcul avec différents formats tels que SpreadsheetML, valeurs séparées par des virgules (CSV), valeurs délimitées par des tabulations ou séparées par des tabulations (TSV), ODS. Pour ouvrir de tels fichiers, les développeurs peuvent utiliser la même méthodologie que celle qu'ils utilisent pour ouvrir des fichiers de différentes versions d'Excel Microsoft.

###  **Ouverture des fichiers SpreadsheetML**

Les fichiers SpreadsheetML sont des représentations XML de feuilles de calcul comprenant toutes les informations les concernant, telles que le formatage, les formules, etc. Depuis Microsoft Excel XP, une option d'exportation XML est ajoutée à Microsoft Excel qui exporte vos feuilles de calcul vers des fichiers SpreadsheetML.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenSpreadsheetMLFile-new.cpp" >}}

###  **Ouverture des fichiers HTML**

Aspose.Cells vous permet d'ouvrir le fichier HTML dans l'objet Workbook. Le fichier HTML doit être orienté vers Excel Microsoft, c'est-à-dire que MS-Excel devrait pouvoir l'ouvrir.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenHTMLFile-new.cpp" >}}

###  **Ouverture des fichiers CSV**

Les fichiers de valeurs séparées par des virgules (CSV) contiennent des enregistrements dans lesquels les valeurs sont séparées par des virgules. Les données sont stockées sous forme de tableau où chaque colonne est séparée par le caractère virgule et citée par le caractère guillemet double. Si une valeur de champ contient un guillemet double, elle est échappée avec une paire de guillemets doubles. Vous pouvez également utiliser Excel Microsoft pour exporter les données d’une feuille de calcul vers CSV.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenCSVFile-new.cpp" >}}

####  **Ouverture des fichiers CSV et remplacement des caractères invalides**

Dans Excel, lorsque le fichier CSV contenant des caractères spéciaux est ouvert, les caractères sont automatiquement remplacés. La même chose est faite par Aspose.Cells API, comme le montre l'exemple de code ci-dessous.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenCSVFileAndReplaceInvalidCharacters-new.cpp" >}}

Un exemple de fichier source peut être téléchargé à partir des liens suivants pour tester cette fonctionnalité.

[InvalidCharacters.csv](InvalidCharacters.csv)

###  **Ouverture de fichiers texte avec un séparateur personnalisé**

Les fichiers texte sont utilisés pour conserver les données d'une feuille de calcul sans formatage. Le fichier est une sorte de fichier texte brut qui peut avoir des délimiteurs personnalisés.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenTextFilewithCustomSeparator-new.cpp" >}}

Un exemple de fichier source peut être téléchargé à partir des liens suivants pour tester cette fonctionnalité.

[CustomSeparator.txt](CustomSeparator.txt)

###  **Ouverture de fichiers délimités par des tabulations**

Le fichier délimité par des tabulations (texte) contient des données de feuille de calcul mais sans aucun formatage. Les données sont organisées en lignes et en colonnes, comme dans les tableaux et les feuilles de calcul. Fondamentalement, un fichier délimité par des tabulations est un type spécial de fichier texte brut avec une tabulation entre chaque colonne.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenTabDelimitedFile-new.cpp" >}}

###  **Ouverture de fichiers de valeurs séparées par des tabulations (TSV)**

Le fichier de valeurs séparées par des tabulations (TSV) contient des données de feuille de calcul mais sans aucun formatage. C'est la même chose avec le fichier délimité par des tabulations où les données sont organisées en lignes et en colonnes comme dans les tableaux et les feuilles de calcul.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenTSVFile-new.cpp" >}}

###  **Ouverture des fichiers SXC**

StarOffice Calc est similaire à Microsoft Excel et prend en charge les formules, les graphiques, les fonctions et les macros. Les feuilles de calcul créées avec ce logiciel sont enregistrées avec l'extension SXC. Le fichier SXC est également utilisé pour les fichiers de feuille de calcul OpenOffice.org Calc. Aspose.Cells peut lire les fichiers SXC, comme le démontre l'exemple de code suivant.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenSXCFile-new.cpp" >}}

###  **Ouverture des fichiers FODS**

Le fichier FODS est une feuille de calcul enregistrée au format OpenDocument XML sans aucune compression. Aspose.Cells peut lire les fichiers FODS, comme le démontre l'exemple de code suivant.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenFODSFile-new.cpp" >}}
