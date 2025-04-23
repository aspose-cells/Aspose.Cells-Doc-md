---
title: Nascondi e Mostra Celle
type: docs
weight: 30
url: /it/java/hide-and-unhide-cells/
---

## **Aspose.Cells - Nascondi e Mostra Righe e Colonne**
Aspose.Cells fornisce una classe, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook), che rappresenta un file Microsoft Excel. La classe Workbook contiene una WorksheetCollection che consente di accedere a ogni foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato dalla classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). La classe Worksheet fornisce una raccolta Cells che rappresenta tutte le celle nel foglio di lavoro. La raccolta Cells fornisce diversi metodi per gestire righe o colonne in un foglio di lavoro. 

**Java**

{{< highlight java >}}

 Workbook workbook = new Workbook("workbook.xls");

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.getWorksheets().get(0);

Cells cells = worksheet.getCells();

cells.hideRow(2); //Hiding the 3rd row of the worksheet

cells.hideColumn(1); //Hiding the 2nd column of the worksheet

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - Nascondi / Mostra Celle**
Per Nascondere una riga o colonna, Apache POI SS fornisce il metodo Row.setZeroHeight(boolean).

**Java**

{{< highlight java >}}

 InputStream inStream = new FileInputStream("workbook.xls");

Workbook workbook = WorkbookFactory.create(inStream);

Sheet sheet = workbook.createSheet();

Row row = sheet.createRow(0);

row.setZeroHeight(true);

{{< /highlight >}}
## **Scarica il codice in esecuzione**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Scarica il codice di esempio**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/hideunhidecells)

{{% alert color="primary" %}} 

Per ulteriori dettagli, visita [Nascondere e Mostrare Righe e Colonne](/java/hiding-and-showing-rows-and-columns).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
