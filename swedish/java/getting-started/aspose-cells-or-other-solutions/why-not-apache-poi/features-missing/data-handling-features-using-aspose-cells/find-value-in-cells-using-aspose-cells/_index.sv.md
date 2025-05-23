---
title: Hitta värde i celler med Aspose.Cells
type: docs
weight: 10
url: /sv/java/find-value-in-cells-using-aspose-cells/
---

## **Aspose.Cells - Hitta värde i celler**
I Microsoft Excel kan användare söka efter celler som innehåller specifik data. Till exempel, att klicka på **Redigera** och sedan **Sök** öppnar sökdialogen. Användarna anger ett värde och klickar på **OK** för att söka efter det. Excel markerar matchande fält.

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
## **Ladda ned körbar kod**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Ladda ned provkoden**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/search/AsposeFindCellsWithString.java)

{{% alert color="primary" %}} 

För mer detaljer, besök [Hitta eller Sök Data](/cells/sv/java/hitta-eller-sok-data).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
