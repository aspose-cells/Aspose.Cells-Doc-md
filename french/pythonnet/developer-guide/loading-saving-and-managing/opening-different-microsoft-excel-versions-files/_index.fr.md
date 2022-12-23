---
title: Ouverture de différents fichiers de versions Excel Microsoft
type: docs
weight: 20
url: /fr/python-net/opening-different-microsoft-excel-versions-files/
---
{{% alert color="primary" %}}

Aspose.Cells peut ouvrir une gamme de différents fichiers de versions Excel Microsoft, tels que Microsoft Excel 95/97 - 2003, SpreadsheetML, Opening Microsoft Excel 2007/2010/2013/2016/2019 et Office 365 XLSX ou des fichiers Excel cryptés.

{{% /alert %}}

## **Ouverture de fichiers de différentes versions d'Excel Microsoft**

 Une application doit souvent pouvoir ouvrir des fichiers Excel Microsoft créés dans différentes versions, par exemple, Microsoft Excel 95,97, ou Microsoft Excel 2007/2010/2013/2016/2019 et Office 365 . Vous devrez peut-être charger un fichier dans l'un des nombreux formats, y compris XLS, XLSX, XLSM, XLSB, SpreadsheetML, TabDelimited ou TSV, CSV, ODS et ainsi de suite. Utilisez le constructeur ou spécifiez le**Cahier** classe'**format de fichier**attribut de type qui spécifie le format à l'aide de l'attribut**TypeFormatFichier**énumération.

 Le**TypeFormatFichier**énumération contient de nombreux formats de fichiers prédéfinis dont certains sont donnés ci-dessous.

|**Types de formats de fichiers**|**Description**|
|:- |:- |
|CSV|Représente un fichier CSV|
|EXCELLER_97_À_2003|Représente un fichier Excel 97 - 2003|
|XLSX|Représente un fichier Excel 2007/2010/2013/2016/2019 et Office 365 XLSX|
|XLSM|Représente un fichier Excel 2007/2010/2013/2016/2019 et Office 365 XLSM|
|XLTX|Représente un fichier de modèle Excel 2007/2010/2013/2016/2019 et Office 365 XLTX|
|XLTX|Représente un fichier Excel 2007/2010/2013/2016/2019 et Office 365 prenant en charge les macros XLTM|
|XLSB|Représente un fichier Excel 2007/2010/2013/2016/2019 et Office 365 binaire XLSB|
|SPREADSHEET_ML|Représente un fichier SpreadsheetML|
|TSV|Représente un fichier de valeurs séparées par des tabulations|
|ONGLET DÉLIMITÉ|Représente un fichier texte délimité par des tabulations|
|ODS|Représente un fichier ODS|
|HTML|Représente un fichier HTML|
|M_HTML|Représente un fichier MHTML|

### **Ouverture des fichiers Microsoft Excel 95/5.0**

Pour ouvrir un fichier Microsoft Excel 95/5.0, utilisez**ChargerOptions**et définissez l'attribut associé pour le**ChargerOptions**class pour le fichier modèle à charger. Un exemple de fichier pour tester cette fonctionnalité peut être téléchargé à partir du lien suivant :

[Fichier Excel95](Excel95.xls)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenExcel95Files.py" >}}

### **Ouverture des fichiers Microsoft Excel 97 - 2003**

 Pour ouvrir un fichier Microsoft Excel 97 - 2003, utilisez**ChargerOptions** et définissez l'attribut associé pour le**ChargerOptions**class pour le fichier modèle à charger.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenExcel97-2003Files.py" >}}

### **Ouverture Microsoft Fichiers Excel 2007/2010/2013/2016/2019 et Office 365 XLSX**

Pour ouvrir un format Microsoft Excel 2007/2010/2013/2016/2019 et Office 365, c'est-à-dire XLSX ou XLSB, indiquez le chemin du fichier. Vous pouvez aussi utiliser**ChargerOptions** et définissez les attributs/options associés du**ChargerOptions**class pour le fichier modèle à charger.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenExcel2007Files.py" >}}

### **Ouverture de fichiers Excel cryptés**

 Il est possible de créer des fichiers Excel cryptés en utilisant Microsoft Excel. Pour ouvrir un fichier crypté, utilisez le**ChargerOptions**et définir ses attributs et options (par exemple, donner un mot de passe) pour le fichier modèle à charger.
Un exemple de fichier pour tester cette fonctionnalité peut être téléchargé à partir du lien suivant :

[Excel crypté](EncryptedExcel.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenEncryptedExcelFiles.py" >}}

Aspose.Cells prend également en charge l'ouverture de fichiers Microsoft Excel 2007, 2010, 2013, 2016, 2019, Office 365 protégés par mot de passe.


