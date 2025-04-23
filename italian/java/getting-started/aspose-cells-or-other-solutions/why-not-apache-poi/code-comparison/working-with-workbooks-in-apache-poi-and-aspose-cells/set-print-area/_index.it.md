---
title: Imposta l Area di Stampa
type: docs
weight: 40
url: /it/java/set-print-area/
---

## **Aspose.Cells - Imposta l'Area di Stampa**
Per impostazione predefinita, solo l'area di stampa comprende tutte le aree del foglio di lavoro che contengono dati. Gli sviluppatori possono stabilire un'area di stampa specifica del foglio di lavoro.

Per selezionare un'area di stampa specifica, utilizzare il metodo setPrintArea della classe [PageSetup](/java/pagesetup). Assegna a questa proprietà un intervallo di celle che definisce l'area di stampa.

**Java**

{{< highlight java >}}

 // Instantiating a Workbook object

Workbook workbook = new Workbook();

// Accessing the first worksheet in the Workbook file

WorksheetCollection worksheets = workbook.getWorksheets();

Worksheet sheet = worksheets.get(0);

// Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = sheet.getPageSetup();

// Specifying the cells range (from A1 cell to F20 cell) of the print area

pageSetup.setPrintArea("A1:F20");

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - Imposta Area di Stampa**
Il metodo Workbook.setPrintArea è disponibile per impostare le proprietà di pagina dell'area di stampa.

**Java**

{{< highlight java >}}

 Workbook wb = new HSSFWorkbook();

Sheet sheet = wb.createSheet("Sheet1");

//sets the print area for the first sheet

wb.setPrintArea(0, "$A$1:$C$2");

//Alternatively:

wb.setPrintArea(

        0, //sheet index

        0, //start column

        1, //end column

        0, //start row

        0  //end row

);

{{< /highlight >}}
## **Scarica il codice in esecuzione**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Scarica il codice di esempio**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/workbook/setprintarea)

{{% alert color="primary" %}} 

Per ulteriori dettagli, visita [Impostazione delle opzioni di stampa](/cells/it/java/page-setup-features/#setting-print-options).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
