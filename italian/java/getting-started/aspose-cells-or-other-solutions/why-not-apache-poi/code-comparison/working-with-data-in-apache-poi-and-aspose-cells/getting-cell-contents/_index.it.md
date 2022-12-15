---
title: Ottenere Cell Contenuto
type: docs
weight: 10
url: /it/java/getting-cell-contents/
---
## **Aspose.Cells - Ottenere Cell Contenuto**
Il metodo Cells.get() è disponibile per accedere alle celle.

**Giava**

{{< highlight "java" >}}

 //Accesso al primo foglio di lavoro nel file Excel

Foglio di lavoro foglio di lavoro = workbook.getWorksheets().get(0);

Cells celle = foglio di lavoro.getCells();

//Accedi all'intervallo di visualizzazione massimo

Intervallo intervallo = foglio di lavoro.getCells().getMaxDisplayRange();

int tcols = range.getColumnCount();

int trows = range.getRowCount();

System.out.println("Righe totali:" + trows);

System.out.println("Totale colonne:" + tcols);

// Valore di accesso di Cell B4

//=====================================================

System.out.println(cells.get("B4").getValue());

Cell cella = celle.get(3,1); //Valore di accesso di Cell B4

System.out.println(cell.getValue());

//=====================================================

RowCollection righe = cells.getRows();

 per (int i = 0 ; i< rows.getCount() ; i++)

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
## **Apache POI SS - HSSF XSSF - Ottenere Cell Contenuto**
Apache POI fornisce la classe Cell per accedere a varie proprietà delle celle.

**Giava**

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
## **Scarica il codice in esecuzione**
- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Scarica il codice di esempio**
- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/datahandling/gettingcellcontent)

{{% alert color="primary" %}} 

 Per maggiori dettagli, visita[Funzioni di gestione dei dati utilizzando Aspose.Cells](/cells/it/java/data-handling-features-using-aspose-cells/)

{{% /alert %}}
