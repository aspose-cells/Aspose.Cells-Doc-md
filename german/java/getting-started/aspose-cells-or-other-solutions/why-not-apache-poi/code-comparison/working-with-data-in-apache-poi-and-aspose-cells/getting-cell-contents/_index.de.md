---
title: Zellinhalte abrufen
type: docs
weight: 10
url: /de/java/getting-cell-contents/
---

## **Aspose.Cells - Abrufen von Zellinhalten**
Die Methode Cells.get() steht zur Verfügung, um auf Zellen zuzugreifen.

**Java**

{{< highlight java >}}

 //Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.getWorksheets().get(0);

Cells cells = worksheet.getCells();

//Access the Maximum Display Range

Range range = worksheet.getCells().getMaxDisplayRange();

int tcols = range.getColumnCount();

int trows = range.getRowCount();

System.out.println("Total Rows:" + trows);

System.out.println("Total Cols:" + tcols);

// Access value of Cell B4

//=====================================================

System.out.println(cells.get("B4").getValue());

Cell cell = cells.get(3,1); //Access value of Cell B4

System.out.println(cell.getValue());

//=====================================================

RowCollection rows = cells.getRows();

for (int i = 0 ; i < rows.getCount() ; i++)

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
## **Apache POI SS - HSSF XSSF - Abrufen von Zellinhalten**
Apache POI bietet die Klasse Cell zum Abrufen verschiedener Eigenschaften von Zellen.

**Java**

{{< highlight java >}}

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
## **Laufenden Code herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Beispielcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/datahandling/gettingcellcontent)

{{% alert color="primary" %}} 

Weitere Details finden Sie unter [Datenverarbeitungsfunktionen mit Aspose.Cells](/cells/de/java/data-handling-features-using-aspose-cells/)

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
