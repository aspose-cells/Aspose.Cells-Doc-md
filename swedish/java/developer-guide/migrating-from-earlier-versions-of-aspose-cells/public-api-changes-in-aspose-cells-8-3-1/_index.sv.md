---
title: Offentliga API-ändringar i Aspose.Cells 8.3.1
type: docs
weight: 120
url: /sv/java/public-api-changes-in-aspose-cells-8-3-1/
---
{{% alert color="primary" %}} 

Det här dokumentet beskriver ändringarna av Aspose.Cells API från version 8.3.0 till 8.3.1 som kan vara av intresse för modul-/applikationsutvecklare.

{{% /alert %}} 
## **Lade till API:er**
### **Egenskapen DataLabels.ShowCellRange tillagd**
Getter/setter för egenskapen ShowCellRange har lagts till i DataLabels-klassen för att efterlikna Excels funktionalitet för att formatera diagrammets dataetiketter under körning. Observera att Excel tillhandahåller den här funktionen genom följande steg.

1. Välj Dataetiketter i serien och högerklicka för att öppna popup-menyn.
1.  Klicka på**Formatera dataetiketter...** och det kommer att synas**Etikettalternativ**.
1.  Markera eller avmarkera kryssrutan**Etikett innehåller - Värde från Cells**.

 Exempelkoden nedan ger åtkomst till dataetiketterna i diagramserien och ställer sedan in DataLabels.setShowCellRange()-metoden till true för att efterlikna Excels funktion för**Etikett innehåller - Värde från Cells**.

**Java**

{{< highlight "csharp" >}}

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

 Vänligen kontrollera artikeln[Visar Cell intervall som dataetiketter](/cells/sv/java/showing-cell-range-as-the-data-labels/) för mer information.

{{% /alert %}} 

### **Metoder Cell.getTable & ListObject.putCellValue Added**
Metoderna Cell.getTable & ListObject.putCellValue har lagts till med Aspose.Cells för Java 8.3.1 för att underlätta för användarna att komma åt ListObject från en cell och lägga till värden inuti den med hjälp av rad- och kolumnförskjutningar. Följande exempelkod läser in källkalkylarket och lägger till värden i tabellen.

**Java**

{{< highlight "csharp" >}}

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

 Vänligen kontrollera artikeln[Få åtkomst till tabell från Cell och lägga till värden i den med hjälp av rad- och kolumnförskjutningar](/cells/sv/java/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/) för mer information.

{{% /alert %}} 

### **Metoder OdsSaveOptions.isStrictSchema11 & OdsSaveOptions.setStrictSchema11 har lagts till**
Metoderna isStrictSchema11 & setStrictSchema11 har lagts till i klassen OdsSaveOptions för att göra det möjligt för utvecklarna att spara kalkylarket i format som överensstämmer med ODF v1.2-specifikationen. Standardvärdet för egenskapen setStrictSchema11 är falskt, vilket betyder att från version 8.3.1 av Aspose.Cells API:er kommer ODS-filerna att sparas som ODF-format version 1.2 som standard.

Nedan medföljande kodavsnitt sparar ODS-filen i ODF 1.2-format.

**Java**

{{< highlight "csharp" >}}

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

 Vänligen kontrollera artikeln[Spara ODS-fil i ODF 1.1 och 1.2 Specifikationer](/cells/sv/java/save-ods-file-in-odf-1-1-and-1-2-specifications/) för mer information.

{{% /alert %}} 

### **Metod SparklineCollection.add Tillagd**
 Aspose.Cells API:er har avslöjat metoden SparklineCollection.add(String dataRange, int row, int column) för att ange dataintervall och plats för Sparkline Group. Observera att Excel tillhandahåller samma funktion genom följande steg.

1. Välj cellen som innehåller din Sparkline.
1.  Välj**Redigera data från Sparkline** avsnitt inuti**Design** flik
1.  Välja**Redigera gruppplats och data**.
1. Specificera**Dataområde** & **Plats**.

 Följande exempelkod läser in källkalkylarket, kommer åt den första sparklinegruppen och lägger till nya dataintervall och platser för sparklinegruppen.

**Java**

{{< highlight "csharp" >}}

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

 Vänligen kontrollera artikeln[Kopiera Sparkline genom att ange dataintervall och plats för Sparkline Group](/cells/sv/java/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/) för mer information.

{{% /alert %}}
