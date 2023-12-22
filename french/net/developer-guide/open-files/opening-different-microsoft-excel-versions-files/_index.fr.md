---
title: Ouvrir différents fichiers de versions Excel Microsoft
type: docs
weight: 20
url: /fr/net/opening-different-microsoft-excel-versions-files/
description: Cet article explique comment ouvrir différentes versions d'Excel en utilisant Aspose.Cells for .NET API.
keywords: C# Open Different Microsoft Excel file, How do I open Encrypted Excel Files.
---
{{% alert color="primary" %}}

Aspose.Cells peut ouvrir une gamme de différents fichiers de versions Excel Microsoft, tels que Microsoft Excel 95/97 - 2003, SpreadsheetML, Ouverture Microsoft Excel 2007/2010/2013/2016/2019 et Office 365 XLSX ou En Fichiers Excel cryptés.

{{% /alert %}}

##  **Comment ouvrir des fichiers de différentes versions d'Excel Microsoft**

 Une application doit souvent être capable d'ouvrir des fichiers Excel Microsoft créés dans différentes versions, par exemple Microsoft Excel 95,97 ou Microsoft Excel 2007/2010/2013/2016/2019 et Office 365. Vous devrez peut-être charger un fichier dans l'un des formats suivants, notamment XLS, XLSX, XLSM, XLSB, SpreadsheetML, TabDelimited ou TSV, CSV, ODS, etc. Utilisez le constructeur ou spécifiez le**[Cahier d'exercices](https://reference.aspose.com/cells/net/aspose.cells/workbook)**classe'**[Format de fichier](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/fileformat)** attribut type qui spécifie le format à l'aide de l'attribut**[FileFormatType](https://reference.aspose.com/cells/net/aspose.cells/fileformattype)**énumération.

 Le**[FileFormatType](https://reference.aspose.com/cells/net/aspose.cells/fileformattype)**L'énumération contient de nombreux formats de fichiers prédéfinis, dont certains sont indiqués ci-dessous.

|**Types de formats de fichiers**|**Description**|
| :- | :- |
|CSV|Représente un fichier CSV|
|Excel97À2003|Représente un fichier Excel 97 - 2003|
|XLSX|Représente un fichier Excel 2007/2010/2013/2016/2019 et Office 365 XLSX|
|Xlsm|Représente un fichier Excel 2007/2010/2013/2016/2019 et Office 365 XLSM|
|XLTX|Représente un fichier de modèle Excel 2007/2010/2013/2016/2019 et Office 365 XLTX.|
|XLTM|Représente un fichier XLTM prenant en charge les macros Excel 2007/2010/2013/2016/2019 et Office 365.|
|Xlsb|Représente un fichier binaire XLSB Excel 2007/2010/2013/2016/2019 et Office 365.|
|SpreadsheetML|Représente un fichier SpreadsheetML|
|Tsv|Représente un fichier de valeurs séparées par des tabulations|
|TabDelimited|Représente un fichier texte délimité par des tabulations|
|Cotes|Représente un fichier ODS|
|HTML|Représente un fichier HTML|
|Mhtml|Représente un fichier MHTML|

###  **Ouvrir les fichiers Excel Microsoft 95/5.0**

Pour ouvrir un fichier Excel 95/5.0 Microsoft, utilisez**[LoadOptions](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**et définissez l'attribut associé pour le**[LoadOptions](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**classe pour le fichier modèle à charger. Un exemple de fichier pour tester cette fonctionnalité peut être téléchargé à partir du lien suivant :

[Fichier Excel95](Excel95.xls)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningMicrosoftExcel95Files-1.cs" >}}

###  **Ouvrir les fichiers Microsoft Excel 97 - 2003**

 Pour ouvrir un fichier Excel Microsoft 97 - 2003, utilisez**[LoadOptions](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)** et définissez l'attribut associé pour le**[LoadOptions](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**classe pour le fichier modèle à charger.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningMicrosoftExcel972003Files-1.cs" >}}

###  **Ouvrir les fichiers Excel Microsoft 2007/2010/2013/2016/2019 et Office 365 XLSX**

Pour ouvrir un format Microsoft Excel 2007/2010/2013/2016/2019 et Office 365, c'est-à-dire XLSX ou XLSB, précisez le chemin du fichier. Vous pouvez aussi utiliser**[LoadOptions](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)** et définissez les attributs/options associés du**[LoadOptions](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**classe pour le fichier modèle à charger.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningMicrosoftExcel2007XlsxFiles-1.cs" >}}

###  **Ouvrir des fichiers Excel cryptés**

 Il est possible de créer des fichiers Excel cryptés en utilisant Microsoft Excel. Pour ouvrir un fichier crypté, utilisez le**[LoadOptions](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**et définissez ses attributs et options (par exemple, donnez un mot de passe) pour que le fichier modèle soit chargé.
Un exemple de fichier pour tester cette fonctionnalité peut être téléchargé à partir du lien suivant :

[Excel crypté](EncryptedExcel.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningEncryptedExcelFiles-1.cs" >}}

Aspose.Cells prend également en charge l'ouverture de fichiers Microsoft Excel 2007, 2010, 2013, 2016, 2019, Office 365 protégés par mot de passe.


