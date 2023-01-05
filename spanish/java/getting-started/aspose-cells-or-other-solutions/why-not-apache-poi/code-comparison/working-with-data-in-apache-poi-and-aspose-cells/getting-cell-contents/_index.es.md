---
title: Obtener Cell Contenido
type: docs
weight: 10
url: /es/java/getting-cell-contents/
---
## **Aspose.Cells - Obtener Cell Contenido**
El método Cells.get() está disponible para acceder a las celdas.

**Java**

{{< highlight "java" >}}

 //Accediendo a la primera hoja de trabajo en el archivo de Excel

Hoja de trabajo hoja de trabajo = libro de trabajo.getWorksheets().get(0);

Cells celdas = hoja de trabajo.getCells();

//Acceda al rango máximo de visualización

Rango rango = hoja de trabajo.getCells().getMaxDisplayRange();

int tcols = range.getColumnCount();

int trows = range.getRowCount();

System.out.println("Total de filas:" + trows);

System.out.println("Total de columnas:" + tcols);

// Valor de acceso de Cell B4

//=====================================================

System.out.println(cells.get("B4").getValue());

Cell celda = celdas.get(3,1); //Valor de acceso de Cell B4

System.out.println(cell.getValue());

//=====================================================

RowCollection filas = celdas.getRows();

 para (int i = 0 ; i< rows.getCount() ; i++)

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
## **Apache POI SS - HSSF XSSF - Obtener Cell Contenido**
Apache POI proporciona la clase Cell para acceder a varias propiedades de las celdas.

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
## **Descargar código de ejecución**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Descargar código de muestra**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/datahandling/gettingcellcontent)

{{% alert color="primary" %}} 

 Para más detalles, visite[Funciones de manejo de datos usando Aspose.Cells](/cells/es/java/data-handling-features-using-aspose-cells/)

{{% /alert %}}
