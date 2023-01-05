---
title: Skapa pivottabell
type: docs
weight: 10
url: /sv/java/create-pivot-table/
---
## **Skapa pivottabell**

### **Skapa pivottabell med Aspose.Cells**

{{% alert color="primary" %}}

 Med Aspose.Cells är det möjligt att lägga till pivottabeller i kalkylblad. Aspose.Cells har ett antal specialklasser som används specifikt för att skapa och styra pivottabeller. Dessa klasser används för att skapa och ställa in egenskaperna för en[**Pivottabell**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable)objekt, som används som byggstenar för pivottabellen.

Pivottabellobjekten är:

- [**Pivotfält**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotField): det representerar ett fält i en pivottabell.
- [**PivotFieldCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotFieldCollection) det representerar en samling av alla[**Pivotfält**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotField)objekt i pivottabellen.
- [**Pivottabell**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable): den representerar en pivottabell.
- [**PivotTableCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTableCollection): det representerar samlingen av alla pivottabellobjekt på kalkylbladet.

{{% /alert %}}

### **Skapa en enkel pivottabell**

För att skapa en pivottabell med Aspose.Cells, följ stegen nedan:

1.  Lägg till några data till kalkylbladsceller genom att använda[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell) föremål[**satt värde**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value)metod. Dessa data kommer att användas som en datakälla för pivottabellen.
1. Lägg till en pivottabell till kalkylbladet genom att anropa[**Lägg till**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#add(com.aspose.cells.PivotTable,%20int,%20int,%20java.lang.String) ) metod för[**PivotTableCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTableCollection) klass, inkapslad i[**Arbetsblad**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)objekt.
1.  Få tillgång till[**Pivottabell**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable) objekt från[**PivotTableCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTableCollection) genom att passera[**Pivottabell**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable)index.
1.  Använd något av pivottabellsobjekten (förklarat ovan) inkapslade i[**Pivottabell**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable)objekt för att hantera pivottabellen.

{{% alert color="primary" %}}

När du tilldelar ett cellintervall som datakälla måste intervallet ställas in från det övre vänstra till det nedre högra hörnet. Till exempel är "A1:C3" giltigt; "C3:A1" är ogiltigt.

{{% /alert %}}

Kodexemplet nedan visar hur man skapar en enkel pivottabell genom att följa de grundläggande stegen ovan. När du kör koden läggs en pivottabell till i kalkylbladet:

**Skapa en pivottabell baserat på ett motsvarande fält**

![todo:image_alt_text](create-pivot-table_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-CreatePivotTable-CreatePivotTable.java" >}}
