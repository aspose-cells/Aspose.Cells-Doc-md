---
title: Ajout d'hyperliens aux données de lien dans Aspose.Cells
type: docs
weight: 10
url: /fr/net/adding-hyperlinks-to-link-data-in-aspose-cells/
---
{{% alert color="primary" %}}

Un lien hypertexte permet de créer un lien entre deux entités. Tout le monde connaît l'utilisation des hyperliens, en particulier sur les sites Web.

En utilisant Aspose.Cells, les développeurs peuvent créer différents types d'hyperliens dans les fichiers Excel Microsoft. Cette rubrique explique quels types d'hyperliens sont pris en charge par Aspose.Cells et comment ils peuvent être utilisés dans nos fichiers Excel.

{{% /alert %}}

## **Ajout d'hyperliens**

Trois types d'hyperliens peuvent être ajoutés à une cellule à l'aide du Aspose.Cells :

- [Ajouter un lien à une URL](#adding-link-to-a-url).
- [Ajouter un lien vers une autre cellule dans le même fichier](#adding-a-link-to-a-cell-in-the-same-file).
- [Ajouter un lien vers un fichier externe](#adding-a-link-to-an-external-file).

 Aspose.Cells permet aux développeurs d'ajouter des liens hypertexte vers des fichiers Excel en utilisant le API ou[feuilles de calcul de concepteur](/cells/fr/net/what-is-a-designer-spreadsheet/)(feuilles de calcul où les hyperliens sont créés manuellement et Aspose.Cells est utilisé pour les importer dans d'autres feuilles de calcul).

 Aspose.Cells fournit une classe,[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook) qui représente un fichier Excel Microsoft. La[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook) classe contient un[**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) qui permet d'accéder à chaque feuille de calcul dans le fichier Excel. Une feuille de calcul est représentée par le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classer. La[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) La classe fournit différentes méthodes pour ajouter différents liens hypertexte aux fichiers Excel.

### **Ajouter un lien à une URL**

 La[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe contient un[**Hyperliens**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/hyperlinks) le recueil. Chaque élément de la collection Hyperlinks représente un lien hypertexte. Ajoutez des liens hypertexte aux URL en appelant la méthode Add de la collection Hyperlinks. La méthode Add prend les paramètres suivants :

- Cell nom, le nom de la cellule à laquelle le lien hypertexte sera ajouté.
- Nombre de lignes, le nombre de lignes dans cette plage de liens hypertexte.
- Nombre de colonnes, le nombre de colonnes dans cette plage de liens hypertexte
- URL, l'adresse URL.

**C#**

{{< highlight "csharp" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Workbook object

int i = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by passing its sheet index

Worksheet worksheet = workbook.Worksheets[i];

//Adding a hyperlink to a URL at "A1" cell

worksheet.Hyperlinks.Add("A1", 1, 1, "http://www.aspose.com");

//Saving the Excel file

workbook.Save("C:\\book1.xls");

{{< /highlight >}}

### **Ajout d'un lien vers un Cell dans le même fichier**

Il est possible d'ajouter des liens hypertexte aux cellules d'un même fichier Excel en appelant la méthode Add de la collection Hyperlink. La méthode Add fonctionne pour les liens hypertexte internes et externes. Une version de la méthode surchargée prend les paramètres suivants :

- Cell nom, le nom de la cellule à laquelle le lien hypertexte sera ajouté.
- Nombre de lignes, le nombre de lignes dans cette plage de liens hypertexte.
- Nombre de colonnes, le nombre de colonnes dans cette plage de liens hypertexte.
- URL, l'adresse de la cellule cible.

**C#**

{{< highlight "csharp" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Obtaining the reference of the first (default) worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Adding an internal hyperlink to the "B9" cell of the other worksheet "Sheet2" in

//the same Excel file

worksheet.Hyperlinks.Add("B3", 1, 1, "Sheet2!B9");

//Saving the Excel file

workbook.Save("C:\\book1.xls");

{{< /highlight >}}

### **Ajouter un lien vers un fichier externe**

Il est possible d'ajouter des liens hypertexte vers des fichiers Excel externes en appelant la méthode Add de la collection Hyperlinks. La méthode Add prend les paramètres suivants :

- Cell nom, le nom de la cellule à laquelle le lien hypertexte sera ajouté.
- Nombre de lignes, le nombre de lignes dans cette plage de liens hypertexte.
- Nombre de colonnes, le nombre de colonnes dans cette plage de liens hypertexte.
- URL, l'adresse de la cible, fichier Excel externe.

**C#**

{{< highlight "csharp" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Excel object

int i = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by passing its sheet index

Worksheet worksheet = workbook.Worksheets[i];

//Adding an internal hyperlink to the "B9" cell of the other worksheet "Sheet2" in

//the same Excel file

worksheet.Hyperlinks.Add("A5", 1, 1, "C:\\book1.xls");

//Saving the Excel file

workbook.Save("C:\\book2.xls");

{{< /highlight >}}

## **Télécharger le code d'exécution**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Adding%20Hyperlinks%20to%20Link%20Data)

## **Télécharger l'exemple de code**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
