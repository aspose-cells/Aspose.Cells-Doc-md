---
title: Trouver la valeur dans Cells
type: docs
weight: 20
url: /fr/net/find-value-in-cells/
---
## **Aspose.Cells - Trouver la valeur dans Cells**
Dans Microsoft Excel, les utilisateurs peuvent rechercher des cellules contenant des données spécifiques. Par exemple, en cliquant**Éditer**et alors**Trouver**ouvre la boîte de dialogue Rechercher. Les utilisateurs entrent une valeur et cliquent**D'ACCORD**pour le chercher. Excel met en évidence les champs correspondants.

**C#**

{{< highlight "cs" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook("../../data/test.xlsx");

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Finding the cell containing the specified formula

Cells cells = worksheet.Cells;

//Instantiate FindOptions

FindOptions findOptions = new FindOptions();

//Finding the cell containing a string value that starts with "Or"

findOptions.LookAtType = LookAtType.StartWith;

Cell cell = cells.Find("SH", null, findOptions);

//Printing the name of the cell found after searching worksheet

Console.WriteLine("Name of the cell containing String: " + cell.Name);

{{< /highlight >}}
## **Télécharger le code d'exécution**
 Télécharger**Trouver la valeur dans Cells** forment l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Find.Value.In.Cells.Aspose.Cells.zip)

{{% alert color="primary" %}} 

 Pour plus de détails, visitez[Rechercher ou rechercher des données](/cells/fr/net/find-or-search-data/).

{{% /alert %}}
