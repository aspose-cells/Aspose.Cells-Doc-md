---
title: Ouverture de différents fichiers de versions Excel Microsoft
type: docs
weight: 20
url: /fr/cpp/opening-different-microsoft-excel-versions-files/
---
{{% alert color="primary" %}}

Aspose.Cells peut ouvrir une gamme de différents fichiers de versions Excel Microsoft, tels que Microsoft Excel 95/97 - 2003, SpreadsheetML, Ouverture Microsoft Excel 2007/2010/2013/2016/2019 et Office 365 XLSX ou En Fichiers Excel cryptés.

{{% /alert %}}

##  **Ouverture de fichiers de différentes versions d'Excel Microsoft**

 Une application doit souvent être capable d'ouvrir des fichiers Excel Microsoft créés dans différentes versions, par exemple Microsoft Excel 95,97 ou Microsoft Excel 2007/2010/2013/2016/2019 et Office 365. Vous devrez peut-être charger un fichier dans l'un des formats suivants, notamment XLS, XLSX, XLSM, XLSB, SpreadsheetML, TabDelimited ou TSV, CSV, ODS, etc. Utilisez le constructeur ou spécifiez le**[Cahier d'exercices](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)**classe'**[SetFileFormat](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/setfileformat/)** méthode pour spécifier le format à l'aide de la**[FileFormatType](https://reference.aspose.com/cells/cpp/aspose.cells/fileformattype/)**énumération.
	
 Le**[FileFormatType](https://reference.aspose.com/cells/cpp/aspose.cells/fileformattype/)**L'énumération contient de nombreux formats de fichiers prédéfinis, dont certains sont indiqués ci-dessous.

|**Types de formats de fichiers**|**Description**|
| :- | :- |
|FichierFormatType_CSV|Représente un fichier CSV|
|FileFormatType_Excel97To2003|Représente un fichier Excel 97 - 2003|
|FileFormatType_Xlsx|Représente un fichier Excel 2007/2010/2013/2016/2019 et Office 365 XLSX|
|FileFormatType_Xlsm|Représente un fichier Excel 2007/2010/2013/2016/2019 et Office 365 XLSM|
|FileFormatType_Xltx|Représente un fichier de modèle Excel 2007/2010/2013/2016/2019 et Office 365 XLTX.|
|FileFormatType_Xltm|Représente un fichier XLTM prenant en charge les macros Excel 2007/2010/2013/2016/2019 et Office 365.|
|FileFormatType_Xlsb|Représente un fichier binaire XLSB Excel 2007/2010/2013/2016/2019 et Office 365.|
|FileFormatType_SpreadsheetML|Représente un fichier SpreadsheetML|
|FileFormatType_Tsv|Représente un fichier de valeurs séparées par des tabulations|
|FileFormatType_TabDelimited|Représente un fichier texte délimité par des tabulations|
|FileFormatType_Ods|Représente un fichier ODS|
|FileFormatType_Html|Représente un fichier HTML|
|FileFormatType_MHtml|Représente un fichier MHTML|

###  **Ouverture des fichiers Excel Microsoft 95/5.0**

Pour ouvrir un fichier Excel 95/5.0 Microsoft, utilisez**[LoadOptions](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/)**et définissez l'attribut associé pour le**Options de chargement**classe pour le fichier modèle à charger. Un exemple de fichier pour tester cette fonctionnalité peut être téléchargé à partir du lien suivant :

[Fichier Excel95](Excel95.xls)

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenExcel95Files-new.cpp" >}}

###  **Ouverture des fichiers Excel Microsoft 97 - 2003**

 Pour ouvrir un fichier Excel Microsoft 97 - 2003, utilisez**[LoadOptions](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/)** et définissez l'attribut associé pour le**Options de chargement**classe pour le fichier modèle à charger.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenExcel97-2003Files-new.cpp" >}}

###  **Ouverture des fichiers Excel Microsoft 2007/2010/2013/2016/2019 et Office 365 XLSX**

Pour ouvrir un format Microsoft Excel 2007/2010/2013/2016/2019 et Office 365, c'est-à-dire XLSX ou XLSB, précisez le chemin du fichier. Vous pouvez aussi utiliser**[LoadOptions](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/)** et définissez les attributs/options associés du**Options de chargement**classe pour le fichier modèle à charger.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenExcel2007Files-new.cpp" >}}

Aspose.Cells prend également en charge l'ouverture de fichiers Microsoft Excel 2007, 2010, 2013, 2016, 2019, Office 365 protégés par mot de passe.


