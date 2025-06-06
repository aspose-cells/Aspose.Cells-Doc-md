---
title: Ouvrir des fichiers de différentes versions de Microsoft Excel
type: docs
weight: 20
url: /fr/go-cpp/opening-different-microsoft-excel-versions-files/
---

{{% alert color="primary" %}}

Aspose.Cells peut ouvrir une gamme de fichiers de différentes versions de Microsoft Excel, tels que Microsoft Excel 95/97 - 2003, SpreadsheetML, ouverture de Microsoft Excel 2007/2010/2013/2016/2019 et Office 365 XLSX ou des fichiers Excel chiffrés.

{{% /alert %}}

## **Ouverture de fichiers de différentes versions de Microsoft Excel**

Une application doit souvent être capable d'ouvrir des fichiers Microsoft Excel créés dans différentes versions, par exemple, Microsoft Excel 95, 97, ou Microsoft Excel 2007/2010/2013/2016/2019 et Office 365. Vous pourriez avoir besoin de charger un fichier dans l'un des plusieurs formats, y compris XLS, XLSX, XLSM, XLSB, SpreadsheetML, TabDelimited ou TSV, CSV, ODS, etc. Utilisez le constructeur ou spécifiez la méthode [**SetFileFormat**](https://reference.aspose.com/cells/go-cpp/workbook/setfileformat/) de la classe [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) pour spécifier le format à l’aide de l’énumération [**FileFormatType**](https://reference.aspose.com/cells/go-cpp/fileformattype/).

L’énumération [**FileFormatType**](https://reference.aspose.com/cells/go-cpp/fileformattype/) contient de nombreux formats de fichiers prédéfinis, dont certains sont listés ci-dessous.

|**Types de formats de fichier**|**Description**|
| :- | :- |
|FileFormatType_CSV|Représente un fichier CSV|
|FileFormatType_Excel97To2003|Représente un fichier Excel 97 - 2003|
|FileFormatType_Xlsx|Représente un fichier Excel 2007/2010/2013/2016/2019 et Office 365 XLSX|
|FileFormatType_Xlsm|Représente un fichier Excel 2007/2010/2013/2016/2019 et Office 365 XLSM|
|FileFormatType_Xltx|Représente un fichier modèle XLTX Excel 2007/2010/2013/2016/2019 et Office 365|
|FileFormatType_Xltm|Représente un fichier XLTM Excel 2007/2010/2013/2016/2019 et Office 365 activé par des macros|
|FileFormatType_Xlsb|Représente un fichier binaire XLSB Excel 2007/2010/2013/2016/2019 et Office 365|
|FileFormatType_SpreadsheetML|Représente un fichier SpreadsheetML|
|FileFormatType_Tsv|Représente un fichier de valeurs séparées par des tabulations (TSV)|
|FileFormatType_TabDelimited|Représente un fichier texte tabulé|
|FileFormatType_Ods|Représente un fichier ODS|
|FileFormatType_Html|Représente un fichier HTML|
|FileFormatType_MHtml|Représente un fichier MHTML|

### **Ouverture de fichiers Microsoft Excel 95/5.0**

Pour ouvrir un fichier Microsoft Excel 95/5.0, utilisez [**LoadOptions**](https://reference.aspose.com/cells/go-cpp/loadoptions/) et définissez l'attribut associé pour la classe [**LoadOptions**](https://reference.aspose.com/cells/go-cpp/loadoptions/) du fichier modèle à charger. Un fichier d'exemple pour tester cette fonctionnalité peut être téléchargé à partir du lien suivant:

[Fichier Excel95](Excel95.xls)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenExcel95Files.go" >}}

### **Ouverture de fichiers Microsoft Excel 97 - 2003**

Pour ouvrir un fichier Microsoft Excel 97 - 2003, utilisez [**LoadOptions**](https://reference.aspose.com/cells/go-cpp/loadoptions/) et définissez l'attribut associé pour la classe [**LoadOptions**](https://reference.aspose.com/cells/go-cpp/loadoptions/) du fichier modèle à charger.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenExcel97-2003Files.go" >}}

### **Ouverture de fichiers Microsoft Excel 2007/2010/2013/2016/2019 et Office 365 XLSX**

Pour ouvrir un fichier au format Microsoft Excel 2007/2010/2013/2016/2019 et Office 365, c'est-à-dire XLSX ou XLSB, spécifiez le chemin d'accès au fichier. Vous pouvez également utiliser [**LoadOptions**](https://reference.aspose.com/cells/go-cpp/loadoptions/) et définir les attributs/options associées de la classe [**LoadOptions**](https://reference.aspose.com/cells/go-cpp/loadoptions/) pour le fichier modèle à charger.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenExcel2007Files.go" >}}

Aspose.Cells prend également en charge l'ouverture de fichiers Microsoft Excel protégés par mot de passe, tels que ceux de Excel 2007, 2010, 2013, 2016, 2019 et Office 365.
