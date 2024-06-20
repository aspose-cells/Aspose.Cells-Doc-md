---
title: Formatera Pivot tabell
type: docs
weight: 60
url: /sv/java/formatting-pivot-table/
---

## **Pivottabellens utseende**

[Hur man skapar en pivot-tabell](/cells/sv/java/create-pivot-table/) visade hur man skapar en enkel pivot-tabell. Den här artikeln går vidare och diskuterar hur man anpassar ett pivot-tabells utseende genom att ställa in egenskaper.

### **Inställning av pivottabellformatalternativ**

[**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable) -klassen låter dig ange olika formateringsalternativ för en pivot-tabell.

#### **Inställning av AutoFormat och PivotTableStyle-typer**

Det följande kodexemplet illustrerar hur man ställer in autoformat-typen och pivot-tabellstil-typen med hjälp av [**AutoFormatType**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#AutoFormatType) och [**PivotTableStyleType**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#PivotTableStyleType) egenskaperna.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-SetAutoFormatandPivotTableStyleTypes-SetAutoFormatandPivotTableStyleTypes.java" >}}

#### **Inställning av formatalternativ**

Kodexemplet nedan illustrerar hur man anger ett antal formateringsalternativ för en pivot-tabellrapport, inklusive att lägga till totaler för rader och kolumner.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-SettingFormatOptions-SettingFormatOptions.java" >}}

### **Anger PivotFields formatalternativ**

Förutom att kontrollera formateringen av den övergripande pivot-tabellen, tillåter Aspose.Cells for Java finjusterad kontroll av formateringen för radfält, kolumnfält och sidofält.

#### **Anger format för rad-, kolumn- och sidofält**

Exemplet nedan visar hur man får åtkomst till radfält, får åtkomst till en specifik rad, anger delsummer, tillämpar automatisk sortering och använder autoVisa-alternativet.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-SetRowColumnPageFieldsFormat-SetRowColumnPageFieldsFormat.java" >}}

### **Anger format för datafält**

De följande kodraderna illustrerar hur man formaterar datafält.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-SettingDataFieldFormat-SettingDataFieldFormat.java" >}}

### **Ändra en Pivottabells snabbstil**

Exemplen nedan visar hur man ändrar den snabba stilen som tillämpas på en pivottabell.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-ModifyPivotTableQuickStyle-ModifyPivotTableQuickStyle.java" >}}

### **Rensa pivottabellsfält**

[**PivotFieldCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotFieldCollection) har en metod med namnet [**clear()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotfieldcollection#clear--) som rensar pivotfält. Använd den för att rensa pivotfält i alla områden, till exempel sidor, kolumner, rader eller data.
Kodexemplet nedan visar hur man rensar alla pivotfält i dataområdet.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-ClearPivotFields-ClearPivotFields.java" >}}

## **Konsolideringsfunktion**

### **Tillämpning av ConsolidationFunction på datavärderna i pivottabellen**

Aspose.Cells kan användas för att tillämpa ConsolidationFunction på datavärderna (eller värdefälten) i pivottabellen. I Microsoft Excel kan du högerklicka på värdefältet och sedan välja alternativet **Värdefältsinställningar...** och sedan välja fliken **Summera värden efter**. Där kan du välja valfri ConsolidationFunction som Summa, Antal, Medel, Max, Min, Produkt, Distinkt antal etc.

Aspose.Cells tillhandahåller uppräkning för att stödja följande konsolideringsfunktioner.

- [**ConsolidationFunction.AVERAGE**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#AVERAGE)
- [**ConsolidationFunction.COUNT**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#COUNT)
- [**ConsolidationFunction.COUNT_NUMS**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#COUNT_NUMS)
- [**ConsolidationFunction.DISTINCT_COUNT**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#DISTINCT_COUNT)
- [**ConsolidationFunction.MAX**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#MAX)
- [**ConsolidationFunction.MIN**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#MIN)
- [**ConsolidationFunction.PRODUCT**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#PRODUCT)
- [**ConsolidationFunction.STD_DEV**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#STD_DEV)
- [**ConsolidationFunction.STD_DEVP**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#STD_DEVP)
- [**ConsolidationFunction.SUM**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#SUM)
- [**ConsolidationFunction.VAR**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#VAR)
- [**ConsolidationFunction.VARP**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#VARP)

Den följande koden tillämpar **Medelvärde** konsolideringsfunktionen på det första datavärdet (eller värdefältet) och **Distinkt antal** konsolideringsfunktionen på det andra datavärdet (eller värdefältet).

{{% alert color="primary" %}}

Distinkt antal konsolideringsfunktionen stöds endast av Microsoft Excel 2013.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-ConsolidationFunctions-ConsolidationFunctions.java" >}}
