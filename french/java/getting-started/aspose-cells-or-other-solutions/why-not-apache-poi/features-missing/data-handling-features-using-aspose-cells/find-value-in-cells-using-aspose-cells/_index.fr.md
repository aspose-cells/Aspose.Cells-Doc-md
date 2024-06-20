---
title: Trouver des valeurs dans les cellules avec Aspose.Cells
type: docs
weight: 10
url: /fr/java/find-value-in-cells-using-aspose-cells/
---

## **Aspose.Cells - Trouver des valeurs dans les cellules**
Dans Microsoft Excel, les utilisateurs peuvent rechercher des cellules contenant des données spécifiques. Par exemple, en cliquant sur **Modifier** puis sur **Rechercher**, cela ouvre la boîte de dialogue de recherche. Les utilisateurs saisissent une valeur et cliquent sur **OK** pour la rechercher. Excel met en surbrillance les champs correspondants.

**Java**

{{< highlight java >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook("workbook.xls");

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.getWorksheets().get(0);

//Finding the cell containing the specified formula

Cells cells = worksheet.getCells();

//Instantiate FindOptions

FindOptions findOptions = new FindOptions();

//Finding the cell containing a string value that starts with "Or"

findOptions.setLookAtType(LookAtType.START_WITH);

Cell cell = cells.find("SH",null,findOptions);

//Printing the name of the cell found after searching worksheet

System.out.println("Name of the cell containing String: " + cell.getName());

{{< /highlight >}}
## **Télécharger le code en cours d'exécution**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Télécharger le code source d'exemple**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/search/AsposeFindCellsWithString.java)

{{% alert color="primary" %}} 

Pour plus de détails, visitez [Rechercher ou trouver des données](/cells/fr/java/find-or-search-data).

{{% /alert %}}
