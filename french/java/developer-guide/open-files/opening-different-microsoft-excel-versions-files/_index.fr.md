---
title: Ouvrir des fichiers de différentes versions de Microsoft Excel
type: docs
weight: 20
url: /fr/java/opening-different-microsoft-excel-versions-files/
---

{{% alert color="primary" %}}

Aspose.Cells peut ouvrir une gamme de fichiers de différentes versions de Microsoft Excel, tels que Microsoft Excel 95/97 - 2003, SpreadsheetML, ouverture de Microsoft Excel 2007/2010/2013/2016/2019 et Office 365 XLSX ou des fichiers Excel chiffrés.

{{% /alert %}}

## **Ouverture de fichiers de différentes versions de Microsoft Excel**

Une application doit souvent être capable d'ouvrir des fichiers Microsoft Excel créés dans différentes versions, par exemple, Microsoft Excel 95,97, ou Microsoft Excel 2007/2010/2013/2016/2019 et Office 365. Vous pourriez avoir besoin de charger un fichier dans l'un des plusieurs formats, y compris XLS, XLSX, XLSM, XLSB, SpreadsheetML, TabDelimited ou TSV, CSV, ODS, etc. Utilisez le constructeur ou utilisez la méthode [**setFileFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#FileFormat) de la classe [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) pour spécifier le format en utilisant l'énumération [**FileFormatType**](https://reference.aspose.com/cells/java/com.aspose.cells/FileFormatType).

L'énumération [**FileFormatType**](https://reference.aspose.com/cells/java/com.aspose.cells/FileFormatType) contient de nombreux formats de fichier prédéfinis dont certains sont donnés ci-dessous.

|**Types de formats de fichier**|**Description**|
| :- | :- |
|CSV|Représente un fichier CSV|
|EXCEL_97_TO_2003|Représente un fichier Excel 97 - 2003
|XLSX|Représente un fichier XLSX Excel 2007/2010/2013/2016/2019 et Office 365|
|XLSM|Représente un fichier XLSM Excel 2007/2010/2013/2016/2019 et Office 365|
|XLTX|Représente un fichier modèle XLTX Excel 2007/2010/2013/2016/2019 et Office 365|
|XLTM|Représente un fichier XLTM activé par macro Excel 2007/2010/2013/2016/2019 et Office 365|
|XLSB|Représente un fichier XLSB binaire Excel 2007/2010/2013/2016/2019 et Office 365|
|SPREADSHEET_ML|Représente un fichier SpreadsheetML
|TSV|Représente un fichier de valeurs séparées par des tabulations|
|TAB_DELIMITED|Représente un fichier texte tabulé
|ODS|Représente un fichier ODS|
|HTML|Représente un fichier HTML|
|M_HTML|Représente un fichier MHTML

### **Ouverture de fichiers Microsoft Excel 95/5.0**

Pour ouvrir un fichier Microsoft Excel 95/5.0, utilisez [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) et définissez l'attribut associé pour la classe [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) du fichier modèle à charger. Un fichier d'exemple pour tester cette fonctionnalité peut être téléchargé à partir du lien suivant:

[Fichier Excel95](Excel95.xls)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "OpenExcel95Files.java" >}}

### **Ouverture de fichiers Microsoft Excel 97 - 2003**

Pour ouvrir un fichier Microsoft Excel 97 - 2003, utilisez [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) et définissez l'attribut associé pour la classe [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) du fichier modèle à charger.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "OpenExcel97-2003Files.java" >}}

### **Ouverture de fichiers Microsoft Excel 2007/2010/2013/2016/2019 et Office 365 XLSX**

Pour ouvrir un fichier au format Microsoft Excel 2007/2010/2013/2016/2019 et Office 365, c'est-à-dire XLSX ou XLSB, spécifiez le chemin d'accès au fichier. Vous pouvez également utiliser [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) et définir les attributs/options associées de la classe [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) pour le fichier modèle à charger.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "OpenExcel2007Files.java" >}}

### **Ouverture de fichiers Excel chiffrés**

Il est possible de créer des fichiers Excel chiffrés à l'aide de Microsoft Excel. Pour ouvrir un fichier chiffré, utilisez [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) et définissez ses attributs et options (par exemple, donnez un mot de passe) pour le fichier modèle à charger. 
Un fichier d'exemple pour tester cette fonctionnalité peut être téléchargé à partir du lien suivant:

[Encrypted Excel](EncryptedExcel.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "OpenEncryptedExcelFiles.java" >}}

Aspose.Cells prend également en charge l'ouverture de fichiers Microsoft Excel 2007, 2010, 2013, 2016, 2019, Office 365 protégés par mot de passe.
