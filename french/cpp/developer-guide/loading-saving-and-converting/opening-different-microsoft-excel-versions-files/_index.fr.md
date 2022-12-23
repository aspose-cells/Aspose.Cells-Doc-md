---
title: Ouverture de différents fichiers de versions Excel Microsoft
type: docs
weight: 20
url: /fr/cpp/opening-different-microsoft-excel-versions-files/
---
{{% alert color="primary" %}}

Aspose.Cells peut ouvrir une gamme de différents fichiers de versions Excel Microsoft, tels que Microsoft Excel 95/97 - 2003, SpreadsheetML, Opening Microsoft Excel 2007/2010/2013/2016/2019 et Office 365 XLSX ou des fichiers Excel cryptés.

{{% /alert %}}

## **Ouverture de fichiers de différentes versions d'Excel Microsoft**

 Une application doit souvent pouvoir ouvrir des fichiers Excel Microsoft créés dans différentes versions, par exemple, Microsoft Excel 95,97, ou Microsoft Excel 2007/2010/2013/2016/2019 et Office 365 . Vous devrez peut-être charger un fichier dans l'un des nombreux formats, y compris XLS, XLSX, XLSM, XLSB, SpreadsheetML, TabDelimited ou TSV, CSV, ODS et ainsi de suite. Utilisez le constructeur ou spécifiez le**[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)** classe'**[SetFileFormat] (https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#aa74a10e0aa88e3a8386ea328165896dc)**méthode pour spécifier le format à l'aide de la**[FileFormatType](https://reference.aspose.com/cells/cpp/namespace/aspose.cells#a7831f25a251b1cd95079f091aa1faf40)**énumération.
	
 Le**[FileFormatType](https://reference.aspose.com/cells/cpp/namespace/aspose.cells#a7831f25a251b1cd95079f091aa1faf40)**énumération contient de nombreux formats de fichiers prédéfinis dont certains sont donnés ci-dessous.

|**Types de formats de fichiers**|**Description**|
|:- |:- |
|FileFormatType_CSV|Représente un fichier CSV|
|FileFormatType_Excel97To2003|Représente un fichier Excel 97 - 2003|
|FileFormatType_Xlsx|Représente un fichier Excel 2007/2010/2013/2016/2019 et Office 365 XLSX|
|FileFormatType_Xlsm|Représente un fichier Excel 2007/2010/2013/2016/2019 et Office 365 XLSM|
|FileFormatType_Xltx|Représente un fichier de modèle Excel 2007/2010/2013/2016/2019 et Office 365 XLTX|
|FileFormatType_Xltm|Représente un fichier Excel 2007/2010/2013/2016/2019 et Office 365 prenant en charge les macros XLTM|
|FileFormatType_Xlsb|Représente un fichier Excel 2007/2010/2013/2016/2019 et Office 365 binaire XLSB|
|FileFormatType_SpreadsheetML|Représente un fichier SpreadsheetML|
|FileFormatType_Tsv|Représente un fichier de valeurs séparées par des tabulations|
|FileFormatType_TabDelimited|Représente un fichier texte délimité par des tabulations|
|FileFormatType_Ods|Représente un fichier ODS|
|FileFormatType_Html|Représente un fichier HTML|
|FileFormatType_MHtml|Représente un fichier MHTML|

### **Ouverture des fichiers Microsoft Excel 95/5.0**

Pour ouvrir un fichier Microsoft Excel 95/5.0, utilisez**[ILoadOptions](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_load_options)**et définissez l'attribut associé pour le**IChargerOptions**class pour le fichier modèle à charger. Un exemple de fichier pour tester cette fonctionnalité peut être téléchargé à partir du lien suivant :

[Fichier Excel95](Excel95.xls)

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenExcel95Files.cpp" >}}

### **Ouverture des fichiers Microsoft Excel 97 - 2003**

 Pour ouvrir un fichier Microsoft Excel 97 - 2003, utilisez**[ILoadOptions](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_load_options)** et définissez l'attribut associé pour le**IChargerOptions**class pour le fichier modèle à charger.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenExcel97-2003Files.cpp" >}}

### **Ouverture Microsoft Fichiers Excel 2007/2010/2013/2016/2019 et Office 365 XLSX**

Pour ouvrir un format Microsoft Excel 2007/2010/2013/2016/2019 et Office 365, c'est-à-dire XLSX ou XLSB, indiquez le chemin du fichier. Vous pouvez aussi utiliser**[ILoadOptions](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_load_options)** et définissez les attributs/options associés du**IChargerOptions**class pour le fichier modèle à charger.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenExcel2007Files.cpp" >}}

Aspose.Cells prend également en charge l'ouverture de fichiers Microsoft Excel 2007, 2010, 2013, 2016, 2019, Office 365 protégés par mot de passe.


