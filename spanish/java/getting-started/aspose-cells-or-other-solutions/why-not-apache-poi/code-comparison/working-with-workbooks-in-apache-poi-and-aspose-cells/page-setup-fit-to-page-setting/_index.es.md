---
title: Configuración de página  Ajuste a configuración de página
type: docs
weight: 30
url: /es/java/page-setup-fit-to-page-setting/
---

## **Aspose.Cells - Configuración de página - Ajuste a configuración de página**
Para adaptar el contenido de la hoja de cálculo a un número específico de páginas, utilice los métodos setFitToPagesTall y setFitToPagesWide de la clase [PageSetup](/cells/es/java/page-setup-fit-to-page-setting/). Estos métodos también se utilizan para ajustar las hojas de cálculo.

**Java**

{{< highlight java >}}

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
## **Apache POI SS - HSSF & XSSF - Configuración de página - Ajuste a configuración de página**
Apache POI SS utiliza los métodos setFitHeight y setFitWidth para la configuración de ajuste a página.

**Java**

{{< highlight java >}}

 Workbook wb = new XSSFWorkbook();  //or new HSSFWorkbook();

Sheet sheet = wb.createSheet("format sheet");

PrintSetup ps = sheet.getPrintSetup();

sheet.setAutobreaks(true);

ps.setFitHeight((short) 1);

ps.setFitWidth((short) 1);

{{< /highlight >}}
## **Descargar Código en Ejecución**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Descargar Código de Ejemplo**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/workbook/fittoonepage)

{{% alert color="primary" %}} 

Para obtener más detalles, visita [Configuración de opciones de página](http://www.aspose.com/docs/display/cellsjava/Setting+Page+Options).

{{% /alert %}}
