---
title: Ouverture de différents fichiers de versions Excel Microsoft
type: docs
weight: 20
url: /fr/java/opening-different-microsoft-excel-versions-files/
---
{{% alert color="primary" %}}

Aspose.Cells peut ouvrir une gamme de différents fichiers de versions Excel Microsoft, tels que Microsoft Excel 95/97 - 2003, SpreadsheetML, Opening Microsoft Excel 2007/2010/2013/2016/2019 et Office 365 XLSX ou des fichiers Excel cryptés.

{{% /alert %}}

## **Ouverture de fichiers de différentes versions d'Excel Microsoft**

 Une application doit souvent pouvoir ouvrir des fichiers Excel Microsoft créés dans différentes versions, par exemple, Microsoft Excel 95,97, ou Microsoft Excel 2007/2010/2013/2016/2019 et Office 365 . Vous devrez peut-être charger un fichier dans l'un des nombreux formats, notamment XLS, XLSX, XLSM, XLSB, SpreadsheetML, TabDelimited ou TSV, CSV, ODS, etc. Utilisez le constructeur ou utilisez le**[Classeur](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)** classer'**[setFileFormat](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#FileFormat)** méthode pour spécifier le format à l'aide de la**[FileFormatType](https://reference.aspose.com/cells/java/com.aspose.cells/FileFormatType)**énumération.

 La**[FileFormatType](https://reference.aspose.com/cells/java/com.aspose.cells/FileFormatType)**énumération contient de nombreux formats de fichiers prédéfinis dont certains sont donnés ci-dessous.

|**Types de formats de fichiers**|**La description**|
|:- |:- |
|CSV|Représente un fichier CSV|
|EXCELLER_97_À_2003|Représente un fichier Excel 97 - 2003|
|XLSX|Représente un fichier Excel 2007/2010/2013/2016/2019 et Office 365 XLSX|
|XLSM|Représente un fichier Excel 2007/2010/2013/2016/2019 et Office 365 XLSM|
|XLTX|Représente un fichier XLTX de modèle Excel 2007/2010/2013/2016/2019 et Office 365|
|XLTM|Représente un fichier Excel 2007/2010/2013/2016/2019 et Office 365 prenant en charge les macros XLTM|
|XLSB|Représente un fichier XLSB binaire Excel 2007/2010/2013/2016/2019 et Office 365|
|SPREADSHEET_ML|Représente un fichier SpreadsheetML|
|VST|Représente un fichier de valeurs séparées par des tabulations|
|ONGLET DÉLIMITÉ|Représente un fichier texte délimité par des tabulations|
|SAO|Représente un fichier ODS|
|HTML|Représente un fichier HTML|
|M_HTML|Représente un fichier MHTML|

### **Ouverture des fichiers Microsoft Excel 95/5.0**

Pour ouvrir un fichier Microsoft Excel 95/5.0, utilisez**[LoadOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)**et définissez l'attribut associé pour le**ChargerOptions**class pour le fichier modèle à charger. Un exemple de fichier pour tester cette fonctionnalité peut être téléchargé à partir du lien suivant :

[Fichier Excel95](Excel95.xls)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "OpenExcel95Files.java" >}}

### **Ouverture des fichiers Microsoft Excel 97 - 2003**

 Pour ouvrir un fichier Microsoft Excel 97 - 2003, utilisez**[LoadOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)** et définissez l'attribut associé pour le**ChargerOptions**class pour le fichier modèle à charger.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "OpenExcel97-2003Files.java" >}}

### **Ouverture Microsoft Fichiers Excel 2007/2010/2013/2016/2019 et Office 365 XLSX**

 Pour ouvrir un format Microsoft Excel 2007/2010/2013/2016/2019 et Office 365, c'est-à-dire XLSX ou XLSB, spécifiez le chemin du fichier. Vous pouvez aussi utiliser**[LoadOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)** et définissez les attributs/options associés du**ChargerOptions**class pour le fichier modèle à charger.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "OpenExcel2007Files.java" >}}

### **Ouverture de fichiers Excel cryptés**

 Il est possible de créer des fichiers Excel cryptés en utilisant Microsoft Excel. Pour ouvrir un fichier crypté, utilisez le**[LoadOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)** et définir ses attributs et options (par exemple, donner un mot de passe) pour le fichier modèle à charger.
Un exemple de fichier pour tester cette fonctionnalité peut être téléchargé à partir du lien suivant :

[Excel crypté](EncryptedExcel.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "OpenEncryptedExcelFiles.java" >}}

Aspose.Cells prend également en charge l'ouverture de fichiers Microsoft Excel 2007, 2010, 2013, 2016, 2019, Office 365 protégés par mot de passe.
