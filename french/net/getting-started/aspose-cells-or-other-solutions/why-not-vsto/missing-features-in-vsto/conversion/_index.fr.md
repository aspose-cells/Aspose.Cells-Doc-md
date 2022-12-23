---
title: Conversion
type: docs
weight: 30
url: /fr/net/conversion/
---
Aspose.Cells fonctionnalité unique qui offre une flexibilité dans les conversions de version sans affecter le travail.
SaveFormat est une énumération qui peut convertir un document dans les extensions indiquées ci-dessous dans le tableau.

|**Nom de membre** |**Évaluer** |**Description** |
|:- |:- |:- |
|CSV |1 | Représente un fichier CSV.|
| Xlsx|6 | Représente un fichier xlsx.|
| Xlsm|7 | Représente un fichier xlsm qui active les macros.|
| XLTX|8 | Représente un fichier xltx.|
| Xltm|9 | Représente un fichier xltm qui active les macros.|
|TabDelimited |11 | Représente un fichier texte délimité par des tabulations.|
| HTML|12 | Représente un fichier html.|
| MHtml|17 | Représente un fichier mhtml.|
|ODS |14 | Représente un fichier ods.|
| Excel97To2003|5 | Représente un fichier xls Excel97-2003.|
|SpreadsheetML |15 | Représente un fichier xml Excel 2003.|
| Xlsb|16 | Représente un fichier xlsb.|
| Auto|0 | Si vous enregistrez le fichier sur le disque, le format de format de fichier s'accorde à l'extension du nom de fichier.<br>Si vous enregistrez le fichier dans le flux, le format de fichier est xlsx.|
| Inconnue|255 | Représente un format non reconnu, ne peut pas être enregistré.|
| PDF|13 | Représente un fichier Pdf.|
|XPS |20 | Représente un fichier XPS.|
|TIFF |21 | Représente un fichier TIFF.|
|SVG |22 | Représente un fichier SVG.|
| Diff|30 | Format d'échange de données.|
Vous trouverez ci-dessous un extrait de code qui montre la conversion de xls en xlsx, vous pouvez également le faire vice versa

{{< highlight "csharp" >}}

 Workbook workbook = new Workbook("Sample.xls");

workbook.Save("Converted.xlsx", SaveFormat.Xlsx);

{{< /highlight >}}
## **Télécharger l'exemple de code**
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Conversion%20between%20Excel%20Formats%20%28Aspose.Cells%29.zip)
