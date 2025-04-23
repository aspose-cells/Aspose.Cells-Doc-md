---
title: Ajout de liens hypertexte pour lier les données dans Aspose.Cells
type: docs
weight: 10
url: /fr/net/adding-hyperlinks-to-link-data-in-aspose-cells/
---

{{% alert color="primary" %}}

Un lien hypertexte est utilisé pour créer un lien entre deux entités. Tout le monde est familier avec l'utilisation des liens hypertexte, en particulier sur les sites Internet.

En utilisant Aspose.Cells, les développeurs peuvent créer différents types de liens hypertexte dans les fichiers Microsoft Excel. Ce sujet explique quels types de liens hypertexte sont pris en charge par Aspose.Cells et comment ils peuvent être utilisés dans nos fichiers Excel.

{{% /alert %}}

## **Ajout de liens hypertexte**

Trois types de liens hypertexte peuvent être ajoutés à une cellule à l'aide d'Aspose.Cells :

- [Ajout de lien vers une URL](#adding-link-to-a-url).
- [Ajout d'un lien vers une autre cellule dans le même fichier](#adding-a-link-to-a-cell-in-the-same-file).
- [Ajout d'un lien vers un fichier externe](#adding-a-link-to-an-external-file).

Aspose.Cells permet aux développeurs d'ajouter des hyperliens aux fichiers Excel soit en utilisant l'API, soit en [feuilles de calcul de concepteur](/cells/fr/net/what-is-a-designer-spreadsheet/) (feuilles de calcul où les hyperliens sont créés manuellement et Aspose.Cells est utilisé pour les importer dans d'autres feuilles de calcul).

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contient une [**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) qui permet d'accéder à chaque feuille de calcul dans le fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) offre différentes méthodes pour ajouter différents hyperliens aux fichiers Excel.

### **Ajout de lien vers une URL**

La classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) contient une collection [**Hyperlinks**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/hyperlinks). Chaque élément dans la collection Hyperliens représente un hyperlien. Ajoutez des hyperliens vers des URL en appelant la méthode Add de la collection Hyperliens. La méthode Add prend les paramètres suivants :

- Nom de la cellule, le nom de la cellule à laquelle le lien hypertexte sera ajouté.
- Nombre de lignes, le nombre de lignes dans cette plage de liens hypertexte.
- Nombre de colonnes, le nombre de colonnes dans cette plage d'hyperliens
- URL, l'adresse URL.

**C#**

{{< highlight csharp >}}

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

### **Ajouter un lien vers une cellule dans le même fichier**

Il est possible d'ajouter des hyperliens aux cellules dans le même fichier Excel en appelant la méthode Add de la collection Hyperlink. La méthode Add fonctionne à la fois pour les hyperliens internes et externes. Une version de la méthode surchargée prend les paramètres suivants :

- Nom de la cellule, le nom de la cellule à laquelle le lien hypertexte sera ajouté.
- Nombre de lignes, le nombre de lignes dans cette plage de liens hypertexte.
- Nombre de colonnes, le nombre de colonnes dans cette plage de liens hypertexte.
- URL, l'adresse de la cellule cible.

**C#**

{{< highlight csharp >}}

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

Il est possible d'ajouter des hyperliens vers des fichiers Excel externes en appelant la méthode Add de la collection Hyperlinks. La méthode Add prend les paramètres suivants:

- Nom de la cellule, le nom de la cellule à laquelle le lien hypertexte sera ajouté.
- Nombre de lignes, le nombre de lignes dans cette plage de liens hypertexte.
- Nombre de colonnes, le nombre de colonnes dans cette plage de liens hypertexte.
- URL, l'adresse de la cible, fichier Excel externe.

**C#**

{{< highlight csharp >}}

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

## **Télécharger le code en cours d'exécution**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Adding%20Hyperlinks%20to%20Link%20Data)

## **Télécharger le code source d'exemple**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
{{< app/cells/assistant language="csharp" >}}
