---
title: Tracing Precedents and Dependents using Aspose.Cells
type: docs
weight: 60
url: /java/tracing-precedents-and-dependents-using-aspose-cells/
---

## **Aspose.Cells - Tracing Precedents and Dependents**
Complex financial worksheets, especially ones developed in collaboration, can hide the most embarrassing errors. Checking formulas for accuracy and finding the source of an error can be difficult when the formula uses precedent cells and dependent cells.

- **Precedent cells** are cells that are referred to by a formula in another Cell. For example, if cell D10 contains the formula =B5, cell B5 is a precedent to cell D10.
- **Dependent cells** contain formulas that refer to other cells. For example, if cell D10 contains the formula =B5, cell D10 is a dependent of cell B5.

To make the spreadsheet easy to read, you might want to clearly show which cells on a spreadsheet are used in a formula. Similarly, you may want to extract the dependent cells of other cells.

Aspose.Cells allows you to trace cells and find out which are linked.

Tracing Precedents

**Java**

{{< highlight java >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook(dataDir + "workbook.xls");

Cells cells = workbook.getWorksheets().get(0).getCells();

Cell cell = cells.get("A12");

//Tracing precedents of the cell A12.

//The return array contains ranges and cells.

ReferredAreaCollection ret = cell.getPrecedents();

//Printing all the precedent cells' name.

if(ret != null)

{

  for(int m = 0 ; m < ret.getCount(); m++)

  {

    ReferredArea area = ret.get(m);

    StringBuilder stringBuilder = new StringBuilder();

    if (area.isExternalLink())

    {

        stringBuilder.append("[");

        stringBuilder.append(area.getExternalFileName());

        stringBuilder.append("]");

     }

     stringBuilder.append(area.getSheetName());

     stringBuilder.append("!");

     stringBuilder.append(CellsHelper.cellIndexToName(area.getStartRow(), area.getStartColumn()));

     if (area.isArea())

      {

          stringBuilder.append(":");

          stringBuilder.append(CellsHelper.cellIndexToName(area.getEndRow(), area.getEndColumn()));

      }

      System.out.println("Tracing Precedents: " + stringBuilder.toString());

   }

}

{{< /highlight >}}

Tracing Dependents

**Java**

{{< highlight java >}}

 //Get the A1 cell

Cell c = cells.get("A5");

//Get the all the Dependents of A5 cell

Cell[] dependents = c.getDependents(true);

for (int i = 0; i< dependents.length; i++)

{

     System.out.println("Tracing Dependents: " + dependents[i].getWorksheet().getName() +dependents[i].getName() + ":" + dependents[i].getIntValue());

}

{{< /highlight >}}
## **Download Running Code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Download Sample Code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/datahandling/TracingPrecedentsAndDependents.java)

{{% alert color="primary" %}} 

For more details, visit [Tracing Precedents and Dependents](/java/precedents-and-dependents).

{{% /alert %}}
