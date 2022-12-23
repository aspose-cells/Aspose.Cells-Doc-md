---
title: Hämta Cell Innehåll
type: docs
weight: 10
url: /sv/java/getting-cell-contents/
---
## **Aspose.Cells - Få Cell Innehåll**
Metoden Cells.get() är tillgänglig för att komma åt celler.

**Java**

{{< highlight "java" >}}

 //Åtkomst till det första kalkylbladet i Excel-filen

Arbetsblad arbetsblad = workbook.getWorksheets().get(0);

Cells celler = kalkylblad.getCells();

//Åtkomst till det maximala visningsintervallet

Range range = workheet.getCells().getMaxDisplayRange();

int tcols = range.getColumnCount();

int trows = range.getRowCount();

System.out.println("Totalt antal rader:" + trows);

System.out.println("Totalt kol:" + tcols);

// Access värde på Cell B4

//=====================================================

System.out.println(cells.get("B4").getValue());

Cell cell = cells.get(3,1); //Access värde på Cell B4

System.out.println(cell.getValue());

//=====================================================

RowCollection rows = cells.getRows();

 för (int i = 0 ; i< rows.getCount() ; i++)

{

	for (int j = 0 ; j < tcols ; j++)

	{

		if (cells.get(i,j).getType() != CellValueType.IS_NULL)

		{

			System.out.println(cells.get(i,j).getName() + " - " + cells.get(i,j).getValue());

		}

	}

}

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - Få Cell Innehåll**
Apache POI tillhandahåller klassen Cell för åtkomst till olika egenskaper hos celler.

**Java**

{{< highlight "java" >}}

 Sheet sheet1 = wb.getSheetAt(0);

for (Row row : sheet1) {

    for (Cell cell : row) {

        CellReference cellRef = new CellReference(row.getRowNum(), cell.getColumnIndex());

        System.out.print(cellRef.formatAsString());

        System.out.print(" - ");

        switch (cell.getCellType()) {

            case Cell.CELL_TYPE_STRING:

                System.out.println(cell.getRichStringCellValue().getString());

                break;

            case Cell.CELL_TYPE_NUMERIC:

                if (DateUtil.isCellDateFormatted(cell)) {

                    System.out.println(cell.getDateCellValue());

                } else {

                    System.out.println(cell.getNumericCellValue());

                }

                break;

            case Cell.CELL_TYPE_BOOLEAN:

                System.out.println(cell.getBooleanCellValue());

                break;

            case Cell.CELL_TYPE_FORMULA:

                System.out.println(cell.getCellFormula());

                break;

            default:

                System.out.println();

        }

    }

}

{{< /highlight >}}
## **Ladda ner Running Code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Ladda ner provkod**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/datahandling/gettingcellcontent)

{{% alert color="primary" %}} 

 För mer information, besök[Datahanteringsfunktioner med Aspose.Cells](/cells/sv/java/data-handling-features-using-aspose-cells/)

{{% /alert %}}
