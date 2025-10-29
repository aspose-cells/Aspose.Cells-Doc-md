---
title: Ouvrir des fichiers de différentes versions de Microsoft Excel
type: docs
weight: 20
url: /fr/python-net/opening-different-microsoft-excel-versions-files/
description: Cet article explique comment ouvrir des fichiers Excel de différentes versions en utilisant l API Aspose.Cells pour Python via .NET.
keywords: Ouvrir différents fichiers Microsoft Excel avec Python, comment ouvrir des fichiers Excel cryptés.
---

{{% alert color="primary" %}}

Aspose.Cells pour Python via .NET peut ouvrir une gamme de fichiers de différentes versions de Microsoft Excel, tels que Microsoft Excel 95/97 - 2003, SpreadsheetML, ouverture de Microsoft Excel 2007/2010/2013/2016/2019 et Office 365 XLSX ou fichiers Excel cryptés.

{{% /alert %}}

## **Comment ouvrir des fichiers de différentes versions de Microsoft Excel**

Une application doit souvent être capable d'ouvrir des fichiers Microsoft Excel créés dans différentes versions, par exemple, Microsoft Excel 95, 97, ou Microsoft Excel 2007/2010/2013/2016/2019 et Office 365. Vous devrez peut-être charger un fichier dans l'un des plusieurs formats, y compris XLS, XLSX, XLSM, XLSB, SpreadsheetML, TabDelimited ou TSV, CSV, ODS, etc. Utilisez le constructeur, ou spécifiez l'attribut de type [**file_format**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/file_format) de la classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) qui spécifie le format en utilisant l'énumération [**FileFormatType**](https://reference.aspose.com/cells/python-net/aspose.cells/fileformattype).

L'énumération [**FileFormatType**](https://reference.aspose.com/cells/python-net/aspose.cells/fileformattype) contient de nombreux formats de fichier prédéfinis dont certains sont donnés ci-dessous.

|**Types de formats de fichier**|**Description**|
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

### **Ouvrir les fichiers Microsoft Excel 95/5.0**

Pour ouvrir un fichier Microsoft Excel 95/5.0, utilisez [**LoadOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions) et définissez l'attribut associé pour la classe [**LoadOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions) du fichier modèle à charger. Un fichier d'exemple pour tester cette fonctionnalité peut être téléchargé à partir du lien suivant:

[Fichier Excel95](Excel95.xls)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningMicrosoftExcel95Files-1.py" >}}

### **Ouvrir les fichiers Microsoft Excel 97-2003**

Pour ouvrir un fichier Microsoft Excel 97 - 2003, utilisez [**LoadOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions) et définissez l'attribut associé pour la classe [**LoadOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions) du fichier modèle à charger.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningMicrosoftExcel972003Files-1.py" >}}

### **Ouvrir les fichiers XLSX de Microsoft Excel 2007/2010/2013/2016/2019 et Office 365**

Pour ouvrir un fichier au format Microsoft Excel 2007/2010/2013/2016/2019 et Office 365, c'est-à-dire XLSX ou XLSB, spécifiez le chemin d'accès au fichier. Vous pouvez également utiliser [**LoadOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions) et définir les attributs/options associées de la classe [**LoadOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions) pour le fichier modèle à charger.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningMicrosoftExcel2007XlsxFiles-1.py" >}}

### **Ouvrir des fichiers Excel chiffrés**

Il est possible de créer des fichiers Excel chiffrés à l'aide de Microsoft Excel. Pour ouvrir un fichier chiffré, utilisez [**LoadOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions) et définissez ses attributs et options (par exemple, donnez un mot de passe) pour le fichier modèle à charger.
Un fichier d'exemple pour tester cette fonctionnalité peut être téléchargé à partir du lien suivant:

[Encrypted Excel](EncryptedExcel.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningEncryptedExcelFiles-1.py" >}}

Aspose.Cells prend également en charge l'ouverture de fichiers Microsoft Excel 2007, 2010, 2013, 2016, 2019, Office 365 protégés par mot de passe.


{{< app/cells/assistant language="python-net" >}}
