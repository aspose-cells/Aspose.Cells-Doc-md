---
title: Imposta pagina - Adatta alla pagina
type: docs
weight: 30
url: /it/java/page-setup-fit-to-page-setting/
---
## **Aspose.Cells - Imposta pagina - Adatta alla pagina**
Per adattare il contenuto del foglio di lavoro a un numero specifico di pagine, utilizzare il file[Impostazione della pagina](/cells/it/java/page-setup-fit-to-page-setting/)class' setFitToPagesTall e setFitToPagesWide. Questi metodi vengono utilizzati anche per ridimensionare i fogli di lavoro.

**Java**

{{< highlight "java" >}}

 // Instantiating a Workbook object

Workbook workbook = new Workbook();

// Accessing the first worksheet in the Excel file

WorksheetCollection worksheets = workbook.getWorksheets();

int sheetIndex = worksheets.add();

Worksheet sheet = worksheets.get(sheetIndex);

PageSetup pageSetup = sheet.getPageSetup();

// Setting the number of pages to which the length of the worksheet will

// be spanned

pageSetup.setFitToPagesTall(1);

// Setting the number of pages to which the width of the worksheet will be spanned

pageSetup.setFitToPagesWide(1);

{{< /highlight >}}
## **Apache POI SS - HSSF e XSSF - Imposta pagina - Adatta alla pagina**
Apache POI SS utilizza i metodi setFitHeight e setFitWidth per adattare le impostazioni alla pagina.

**Java**

{{< highlight "java" >}}

 Workbook wb = new XSSFWorkbook();  //or new HSSFWorkbook();

Sheet sheet = wb.createSheet("format sheet");

PrintSetup ps = sheet.getPrintSetup();

sheet.setAutobreaks(true);

ps.setFitHeight((short) 1);

ps.setFitWidth((short) 1);

{{< /highlight >}}
## **Scarica il codice in esecuzione**
- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Scarica il codice di esempio**
- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/workbook/fittoonepage)

{{% alert color="primary" %}} 

 Per maggiori dettagli, visita[Impostazione delle opzioni della pagina](http://www.aspose.com/docs/display/cellsjava/Setting+Page+Options).

{{% /alert %}}
