---
title: Conversion
type: docs
weight: 30
url: /fr/net/conversion/
---

Fonctionnalité unique d'Aspose.Cells qui offre une flexibilité dans les conversions de version sans affecter le travail.
SaveFormat est une énumération qui permet de convertir un document dans les extensions indiquées ci-dessous dans le tableau.

|**Nom du membre** |**Valeur** |**Description** |
| :- | :- | :- |
|CSV |1 |Représente un fichier CSV. |
|Xlsx |6 |Représente un fichier xlsx. |
|Xlsm |7 |Représente un fichier xlsm qui autorise les macros. |
|Xltx |8 |Représente un fichier xltx. |
|Xltm |9 |Représente un fichier xltm qui autorise les macros. |
|TabDelimited |11 |Représente un fichier texte délimité par des tabulations. |
|Html |12 |Représente un fichier HTML. |
|MHtml |17 |Représente un fichier MHTML. |
|ODS |14 |Représente un fichier ods. |
|Excel97To2003 |5 |Représente un fichier xls Excel97-2003. |
|SpreadsheetML |15 |Représente un fichier xml Excel 2003. |
|Xlsb |16 |Représente un fichier xlsb. |
|Auto |0 |Lors de l'enregistrement du fichier sur le disque, le format de fichier correspond à l'extension du nom de fichier. <br>Lors de l'enregistrement du fichier dans le flux, le format de fichier est xlsx. |
|Unknown |255 |Représente un format non reconnu, impossible à enregistrer. |
|Pdf |13 | Représente un fichier Pdf. |
|XPS |20 | Représente un fichier XPS. |
|TIFF |21 | Représente un fichier TIFF. |
|SVG |22 | Représente un fichier SVG. |
|Dif |30 | Format d'échange de données. |
Ci-dessous un extrait de code montrant la conversion de xls en xlsx, vous pouvez aussi le faire dans l'autre sens.

{{< highlight csharp >}}

 Workbook workbook = new Workbook("Sample.xls");

workbook.Save("Converted.xlsx", SaveFormat.Xlsx);

{{< /highlight >}}
## **Télécharger le code source d'exemple**
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Conversion%20between%20Excel%20Formats%20%28Aspose.Cells%29.zip)
{{< app/cells/assistant language="csharp" >}}
