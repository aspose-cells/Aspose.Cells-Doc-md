---
title: Förändringar i den offentliga API en i Aspose.Cells 8.3.1
type: docs
weight: 120
url: /sv/java/public-api-changes-in-aspose-cells-8-3-1/
---

{{% alert color="primary" %}} 

Detta dokument beskriver förändringarna i Aspose.Cells API från version 8.3.0 till 8.3.1 som kan vara av intresse för modul-/applikationsutvecklare.

{{% /alert %}} 
## **Tillagda API:er**
### **Tillagd DataLabels.ShowCellRange Egenskap**
Getter/setter har lagts till egenskapen ShowCellRange till DataLabels-klassen för att härma Excels funktionalitet för att formatera diagrammets Data-etiketter vid körning. Observera, Excel tillhandahåller denna funktion genom följande steg. 

1. Välj Data Labels för serien och högerklicka för att öppna snabbmenyn.
1. Klicka på **Formatera Data Labels...** och det kommer att visa **Märkets alternativ**.
1. Markera eller avmarkera kryssrutan **Märket innehåller - Värde från celler**.

Den provkod nedan får åtkomst till diagrammets Data-etiketter och ställer sedan in DataLabels.setShowCellRange()-metoden till true för att härma Excels funktion av **Ettikett Innehåller - Värde Från Celler**.

**Java**

{{< highlight csharp >}}

 //Create workbook from the source spreadsheet containing an existing chart

Workbook workbook = new Workbook("sample.xlsx");

//Access the first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access the chart inside the worksheet

Chart chart = worksheet.getCharts().get(0);

//Check the "Label Contains - Value From Cells"

DataLabels dataLabels = chart.getNSeries().get(0).getDataLabels();

dataLabels.setShowCellRange(true);

//Save the workbook

workbook.save("output.xlsx");

{{< /highlight >}}

{{% alert color="primary" %}} 

Vänligen kontrollera artikeln [Visa cellområde som datamärken](/cells/sv/java/visa-cellområde-som-datamärken/) för mer information.

{{% /alert %}} 

### **Tillagda Cell.getTable & ListObject.putCellValue Metoder**
Metoderna Cell.getTable & ListObject.putCellValue har lagts till med Aspose.Cells for Java 8.3.1 för att underlätta för användarna att komma åt ListObject från en cell och lägga till värden i den med hjälp av rad- och kolumnförskjutningar. Följande exempelkod laddar källkalkylarket och lägger till värden i tabellen.

**Java**

{{< highlight csharp >}}

 //Create workbook from source Excel file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access cell D5 which lies inside the table

Cell cell = worksheet.getCells().get("D5");

//Put value inside the cell D5

cell.putValue("D5 Data");

//Access the Table from this cell

ListObject table = cell.getTable();

//Add some value using Row and Column Offset

table.putCellValue(2, 2, "Offset [2,2]");

//Save the workbook

workbook.save("output.xlsx");

{{< /highlight >}}

{{% alert color="primary" %}} 

Vänligen kontrollera artikeln [Åtkomst till tabell från cell och lägga till värden i den med rad- och kolumnförskjutningar](/cells/sv/java/åtkomst-till-tabell-från-cell-och-lägga-till-värden-i-den-med-rad-och-kolumnförskjutningar/) för mer information.

{{% /alert %}} 

### **Tillagda OdsSaveOptions.isStrictSchema11 & OdsSaveOptions.setStrictSchema11 Metoder**
Metoderna isStrictSchema11 & setStrictSchema11 har lagts till i OdsSaveOptions-klassen för att möjliggöra för utvecklare att spara kalkylarket i format som överensstämmer med ODF v1.2-specifikationen. Standardvärdet för egenskapen setStrictSchema11 är falskt, vilket innebär att från version 8.3.1 av Aspose.Cells API:er kommer ODS-filer att sparas som ODF-format version 1.2 som standard.

Nedan följer kodsnutt som sparar ODS-filen i ODF 1.2-format.

**Java**

{{< highlight csharp >}}

 //Create workbook

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Put some value in cell A1

Cell cell = worksheet.getCells().get("A1");

cell.putValue("Welcome to Aspose!");

//Save ODS in ODF 1.2 version which is default

OdsSaveOptions options = new OdsSaveOptions();

workbook.save("ODF1.2.ods", options);

//Save ODS in ODF 1.1 version

options.setStrictSchema11(true);

workbook.save("ODF1.1.ods", options);

{{< /highlight >}}

{{% alert color="primary" %}} 

Vänligen kontrollera artikeln [Spara ODS-fil i ODF 1.1 och 1.2 Specifikationer](/cells/sv/java/spara-ods-fil-i-odf-1-1-och-1-2-specifikationer/) för mer information.

{{% /alert %}} 

### **Tillagd SparklineCollection.add Metod**
Aspose.Cells API:er har exponerat metoden SparklineCollection.add(String dataRange, int row, int column) för att ange dataräckvidd och plats för Sparkline-gruppen. Observera att Excel tillhandahåller samma funktion genom följande steg. 

1. Välj cellen som innehåller din Sparkline.
1. Välj **Redigera data** från avsnittet **Design** inne i fliken **Design**
1. Välj **Redigera gruppläge och data**.
1. Ange **Data Range** & **Location**.

Exempelkoden nedan laddar källkalkylarket, får åtkomst till den första sparkline gruppen och lägger till nya dataområden och platser för sparkline gruppen. 

**Java**

{{< highlight csharp >}}

 //Create workbook from source Excel file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access the first sparkline group

SparklineGroup group = worksheet.getSparklineGroupCollection().get(0);

//Add Data Ranges and Locations inside this sparkline group

group.getSparklineCollection().add("D5:O5", 4, 15);

group.getSparklineCollection().add("D6:O6", 5, 15);

group.getSparklineCollection().add("D7:O7", 6, 15);

group.getSparklineCollection().add("D8:O8", 7, 15);

//Save the workbook

workbook.save("output.xlsx");

{{< /highlight >}}

{{% alert color="primary" %}} 

Vänligen kontrollera artikeln [Kopiera Sparkline genom att ange dataräckvidd och plats för Sparkline-gruppen](/cells/sv/java/kopiera-sparkline-genom-att-ange-dataräckvidd-och-plats-för-sparkline-gruppen/) för mer information.

{{% /alert %}}
