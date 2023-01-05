---
title: Formatera pivottabell
type: docs
weight: 60
url: /sv/java/formatting-pivot-table/
---
## **Pivottabellens utseende**

[Hur man skapar en pivottabell](/cells/sv/java/create-pivot-table/) visade hur man skapar en enkel pivottabell. Den här artikeln går längre och diskuterar hur man anpassar en pivottabells utseende genom att ställa in egenskaper.

### **Ställa in alternativ för pivottabellformat**

 De[**Pivottabell**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable) class låter dig ställa in olika formateringsalternativ för en pivottabell.

#### **Ställa in AutoFormat och PivotTableStyle Typer**

 Kodexemplet som följer illustrerar hur du ställer in autoformattypen och pivottabellstiltypen med hjälp av[**AutoFormatType**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#AutoFormatType) och[**PivotTableStyleType**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#PivotTableStyleType) egenskaper.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-SetAutoFormatandPivotTableStyleTypes-SetAutoFormatandPivotTableStyleTypes.java" >}}

#### **Ställa in formatalternativ**

Kodexemplet som följer illustrerar hur du ställer in ett antal formateringsalternativ för en pivottabellsrapport, inklusive att lägga till totalsummor för rader och kolumner.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-SettingFormatOptions-SettingFormatOptions.java" >}}

### **Ställa in PivotFields-formatalternativ**

Förutom att styra formateringen av den övergripande pivottabellen tillåter Aspose.Cells for Java finjusterad kontroll av formateringen för radfält, kolumnfält och sidfält.

#### **Ställa in format för rad-, kolumn- och sidfält**

Kodexemplet som följer visar hur man kommer åt radfält, kommer åt en viss rad, ställer in delsummor, tillämpar automatisk sortering och använder alternativet autoShow.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-SetRowColumnPageFieldsFormat-SetRowColumnPageFieldsFormat.java" >}}

### **Ställa in datafältsformat**

Följande kodrader illustrerar hur man formaterar datafält.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-SettingDataFieldFormat-SettingDataFieldFormat.java" >}}

### **Ändra en pivottabells snabbstil**

Kodexemplen som följer visar hur man ändrar den snabbstil som tillämpas på en pivottabell.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-ModifyPivotTableQuickStyle-ModifyPivotTableQuickStyle.java" >}}

### **Rensa pivotfält**

[**PivotFieldCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotFieldCollection) har en metod som heter[**klar()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotfieldcollection#clear()som rensar pivotfält. Använd den för att rensa pivotfält i alla områden, till exempel sida, kolumn, rad eller data.
Kodexemplet nedan visar hur man rensar alla pivotfält i dataområdet.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-ClearPivotFields-ClearPivotFields.java" >}}

## **Konsolideringsfunktion**

### **Tillämpa ConsolidationFunction på datafält i pivottabellen**

 Aspose.Cells kan användas för att tillämpa ConsolidationFunction på datafält (eller värdefält) i pivottabellen. I Microsoft Excel kan du högerklicka på värdefältet och sedan välja**Inställningar för värdefält...** och välj sedan fliken**Sammanfatta värden efter**. Därifrån kan du välja valfri konsolideringsfunktion som Summa, Antal, Genomsnitt, Max, Min, Produkt, Distinkt antal etc.

 Aspose.Cells tillhandahåller[**Konsolideringsfunktion**](https://reference.aspose.com/cells/java/com.aspose.cells/ConsolidationFunction) uppräkning för att stödja följande konsolideringsfunktioner.

- [**ConsolidationFunction.AVERAGE**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#AVERAGE)
- [**ConsolidationFunction.COUNT**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#COUNT)
- [**Consolidation Function.COUNT_NUMS**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#COUNT_NUMS)
- [**ConsolidationFunction.DISTINCT_COUNT**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#DISTINCT_COUNT)
- [**ConsolidationFunction.MAX**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#MAX)
- [**Consolidation Function.MIN**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#MIN)
- [**ConsolidationFunction.PRODUCT**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#PRODUCT)
- [**ConsolidationFunction.STD_DEV**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#STD_DEV)
- [**ConsolidationFunction.STD_DEVP**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#STD_DEVP)
- [**ConsolidationFunction.SUM**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#SUM)
- [**ConsolidationFunction.VAR**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#VAR)
- [**ConsolidationFunction.VARP**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#VARP)

 Följande kod gäller**Medel** konsolideringsfunktion till första datafältet (eller värdefältet) och**DistinctCount** konsolideringsfunktion till andra datafält (eller värdefält).

{{% alert color="primary" %}}

DistinctCount-konsolideringsfunktionen stöds endast av Microsoft Excel 2013.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-ConsolidationFunctions-ConsolidationFunctions.java" >}}
