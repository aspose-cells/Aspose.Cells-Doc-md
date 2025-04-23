---
title: Skapa Pivot tabel
type: docs
weight: 10
url: /sv/java/create-pivot-table/
---

## **Skapa Pivottabell**

### **Skapa Pivot-tabell med hjälp av Aspose.Cells**

{{% alert color="primary" %}}

Med Aspose.Cells är det möjligt att lägga till pivot-tabeller i kalkylblad. Aspose.Cells har ett antal specialklasser som används specifikt för att skapa och kontrollera pivot-tabeller. Dessa klasser används för att skapa och ställa in egenskaper för en [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable) -objekt, som används som byggstenar för pivot-tabellen.

Pivot-tabell-objekten är:

- [**PivotField**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotField): det representerar ett fält i en pivot-tabell.
- [**PivotFieldCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotFieldCollection): det representerar en samling av alla [**PivotField**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotField) -objekt i pivot-tabellen.
- [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable): det representerar en pivot-tabell.
- [**PivotTableCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTableCollection): det representerar en samling av alla pivot-tabell-objekt på kalkylarket.

{{% /alert %}}

### **Skapar en enkel pivot-tabell**

För att skapa en pivot-tabell med Aspose.Cells, följ följande steg:

1. Lägg till några data i arbetsbladsceller genom att använda [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell) -objektets [**setValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value) -metod. Dessa data kommer att användas som en datakälla för pivot-tabellen.
2. Lägg till en pivot-tabell på arbetsbladet genom att anropa [**add**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#add-com.aspose.cells.PivotTable-int-int-java.lang.String-) -metoden i [**PivotTableCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTableCollection) -klassen, inkapslad i [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) -objektet.
1. Hämta objektet [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable) från [**PivotTableCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTableCollection) genom att passera indexet [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable).
1. Använd något av pivot-tabellobjekten (som förklaras ovan) inkapslat i objektet [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable) för att hantera pivot-tabellen.

{{% alert color="primary" %}}

När du tilldelar en cellintervall som datakälla måste intervallet vara inställt från det översta vänstra till det nedersta högra. Till exempel är "A1:C3" giltigt; "C3:A1" är ogiltigt.

{{% /alert %}}

Exemplet nedan visar hur man skapar en enkel pivot-tabell enligt de grundläggande stegen som anges ovan. När koden utförs läggs en pivot-tabell till i arbetsbladet:

**Skapa en pivottabell baserad på ett motsvarande fält**

![todo:image_alt_text](create-pivot-table_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-CreatePivotTable-CreatePivotTable.java" >}}
{{< app/cells/assistant language="java" >}}
