---
title: Trouver une valeur dans les cellules
type: docs
weight: 20
url: /fr/net/find-value-in-cells/
---

## **Aspose.Cells - Trouver des valeurs dans les cellules**
Dans Microsoft Excel, les utilisateurs peuvent rechercher des cellules contenant des données spécifiques. Par exemple, en cliquant sur **Modifier** puis sur **Rechercher**, cela ouvre la boîte de dialogue de recherche. Les utilisateurs saisissent une valeur et cliquent sur **OK** pour la rechercher. Excel met en surbrillance les champs correspondants.

**C#**

{{< highlight cs >}}

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
## **Télécharger le code en cours d'exécution**
Téléchargez **Trouver une valeur dans les cellules** à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Find.Value.In.Cells.Aspose.Cells.zip)

{{% alert color="primary" %}} 

Pour plus de détails, visitez [Rechercher ou trouver des données](/cells/fr/net/find-or-search-data/).

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
