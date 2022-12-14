---
title: Ouverture de différents fichiers de versions Excel Microsoft
type: docs
weight: 20
url: /fr/net/opening-different-microsoft-excel-versions-files/
---
{{% alert color="primary" %}}

Aspose.Cells peut ouvrir une gamme de différents fichiers de versions Excel Microsoft, tels que Microsoft Excel 95/97 - 2003, SpreadsheetML, Opening Microsoft Excel 2007/2010/2013/2016/2019 et Office 365 XLSX ou des fichiers Excel cryptés.

{{% /alert %}}

## **Ouverture de fichiers de différentes versions d'Excel Microsoft**

 Une application doit souvent pouvoir ouvrir des fichiers Excel Microsoft créés dans différentes versions, par exemple, Microsoft Excel 95,97, ou Microsoft Excel 2007/2010/2013/2016/2019 et Office 365 . Vous devrez peut-être charger un fichier dans l'un des nombreux formats, notamment XLS, XLSX, XLSM, XLSB, SpreadsheetML, TabDelimited ou TSV, CSV, ODS, etc. Utilisez le constructeur ou spécifiez le**[Cahier](https://reference.aspose.com/cells/net/aspose.cells/workbook)** classer'**[Format de fichier](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/fileformat)** attribut de type qui spécifie le format à l'aide de l'attribut**[FileFormatType](https://reference.aspose.com/cells/net/aspose.cells/fileformattype)**énumération.

 La**[FileFormatType](https://reference.aspose.com/cells/net/aspose.cells/fileformattype)**énumération contient de nombreux formats de fichiers prédéfinis dont certains sont donnés ci-dessous.

|**Types de formats de fichiers**|**La description**|
|:- |:- |
|CSV|Représente un fichier CSV|
|Excel97To2003|Représente un fichier Excel 97 - 2003|
|Xlsx|Représente un fichier Excel 2007/2010/2013/2016/2019 et Office 365 XLSX|
|Xlsm|Représente un fichier Excel 2007/2010/2013/2016/2019 et Office 365 XLSM|
|XLTX|Représente un fichier XLTX de modèle Excel 2007/2010/2013/2016/2019 et Office 365|
|Xltm|Représente un fichier Excel 2007/2010/2013/2016/2019 et Office 365 prenant en charge les macros XLTM|
|Xlsb|Représente un fichier XLSB binaire Excel 2007/2010/2013/2016/2019 et Office 365|
|TableurML|Représente un fichier SpreadsheetML|
|Tsv|Représente un fichier de valeurs séparées par des tabulations|
|Onglet délimité|Représente un fichier texte délimité par des tabulations|
|cotes|Représente un fichier ODS|
|HTML|Représente un fichier HTML|
|Mhtml|Représente un fichier MHTML|

### **Ouverture des fichiers Microsoft Excel 95/5.0**

Pour ouvrir un fichier Microsoft Excel 95/5.0, utilisez**[Options de chargement] (https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**et définissez l'attribut associé pour le**[Options de chargement] (https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**class pour le fichier modèle à charger. Un exemple de fichier pour tester cette fonctionnalité peut être téléchargé à partir du lien suivant :

[Fichier Excel95](Excel95.xls)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningMicrosoftExcel95Files-1.cs" >}}

### **Ouverture des fichiers Microsoft Excel 97 - 2003**

 Pour ouvrir un fichier Microsoft Excel 97 - 2003, utilisez**[Options de chargement] (https://reference.aspose.com/cells/net/aspose.cells/loadoptions)** et définissez l'attribut associé pour le**[Options de chargement] (https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**class pour le fichier modèle à charger.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningMicrosoftExcel972003Files-1.cs" >}}

### **Ouverture Microsoft Fichiers Excel 2007/2010/2013/2016/2019 et Office 365 XLSX**

 Pour ouvrir un format Microsoft Excel 2007/2010/2013/2016/2019 et Office 365, c'est-à-dire XLSX ou XLSB, spécifiez le chemin du fichier. Vous pouvez aussi utiliser**[Options de chargement] (https://reference.aspose.com/cells/net/aspose.cells/loadoptions)** et définissez les attributs/options associés du**[Options de chargement] (https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**class pour le fichier modèle à charger.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningMicrosoftExcel2007XlsxFiles-1.cs" >}}

### **Ouverture de fichiers Excel cryptés**

 Il est possible de créer des fichiers Excel cryptés en utilisant Microsoft Excel. Pour ouvrir un fichier crypté, utilisez le**[Options de chargement] (https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**et définir ses attributs et options (par exemple, donner un mot de passe) pour le fichier modèle à charger.
Un exemple de fichier pour tester cette fonctionnalité peut être téléchargé à partir du lien suivant :

[Excel crypté](EncryptedExcel.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningEncryptedExcelFiles-1.cs" >}}

Aspose.Cells prend également en charge l'ouverture de fichiers Microsoft Excel 2007, 2010, 2013, 2016, 2019, Office 365 protégés par mot de passe.


