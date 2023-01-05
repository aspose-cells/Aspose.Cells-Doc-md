---
title: Infoga pivottabell
linktitle: Pivottabeller
type: docs
weight: 160
url: /sv/net/create-pivot-table/
description: Skapa och formatera pivottabeller för Excel-kalkylbladsfiler.
---
## **Skapa pivottabell**

Det är möjligt att använda Aspose.Cells för att lägga till pivottabeller till kalkylblad programmatiskt.

### **Pivottabellobjektmodell**

Aspose.Cells tillhandahåller en speciell uppsättning klasser i[**Aspose.Cells.Pivot**](https://reference.aspose.com/cells/net/aspose.cells.pivot) namnutrymme som används för att skapa och kontrollera pivottabeller. Dessa klasser används för att skapa och ställa in[**Pivottabell**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable)objekt, byggstenarna i en pivottabell. Objekten är:

- [**Pivotfält**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield) representerar ett fält i en[**Pivottabell**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable).
- [**PivotFieldCollection**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfieldcollection) representerar en samling av alla[**Pivotfält**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield) föremål i[**Pivottabell**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable).
- [**Pivottabell**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable)representerar en pivottabell på ett kalkylblad.
- [**PivotTableCollection**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection) representerar en samling av alla[**Pivottabell**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable)objekt på ett kalkylblad.

### **Skapa en enkel pivottabell med Aspose.Cells**

1. Lägg till data i ett kalkylblad med hjälp av[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) föremål[**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) metod.
 Dessa data kommer att användas som pivottabellens datakälla.
1.  Lägg till en pivottabell till kalkylbladet genom att anropa[**Pivottabeller**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection) samlingens[**Lägg till**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/add/index)metod, som är inkapslad i Worksheet-objektet.
1.  Få tillgång till det nya[**Pivottabell**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) objekt från[**Pivottabeller**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection)samling genom att skicka pivottabellindexet.
1.  Använd någon av de[**Pivottabell**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable)objekt (förklarat ovan) för att hantera pivottabellen.

Efter exekvering av exempelkoden läggs en pivottabell till i kalkylbladet.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-CreatePivotTable-1.cs" >}}

{{% alert color="primary" %}}

När du tilldelar ett cellområde som datakälla måste området gå från övre vänster till nedre höger. Till exempel är "A1:C3" giltigt men "C3:A1" är det inte.

{{% /alert %}}

## **Förhandsämnen**
- [Konsolideringsfunktion](/cells/sv/net/consolidation-function/)
- [Anpassad sortering i pivottabell](/cells/sv/net/custom-sorting-in-pivot-table/)
- [Anpassa globaliseringsinställningar för pivottabell](/cells/sv/net/customize-globalization-settings-for-pivot-table/)
- [Inaktivera pivottabellsband](/cells/sv/net/disable-pivot-table-ribbons/)
- [Hitta och uppdatera pivottabellerna för kapslade eller barn i överordnade pivottabeller](/cells/sv/net/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/)
- [Formatera pivottabell](/cells/sv/net/formatting-pivot-table/)
- [Hämta extern anslutningsdatakälla för pivottabell](/cells/sv/net/get-external-connection-data-source-of-pivot-table/)
- [Få pivottabellens uppdateringsdatum och uppdatera av vem information](/cells/sv/net/get-pivot-table-refresh-date-and-refresh-by-who-information/)
- [Gruppera pivotfält i pivottabellen](/cells/sv/net/group-pivot-fields-in-the-pivot-table/)
- [Parsar pivotcachade poster medan Excel-fil laddas](/cells/sv/net/parsing-pivot-cached-records-while-loading-excel-file/)
- [Pivottabell och källdata](/cells/sv/net/pivot-table-and-source-data/)
- [Pivottabell Dölj och sortera data](/cells/sv/net/pivot-table-hide-and-sort-data/)
- [Uppdatera och beräkna pivottabellen med beräknade objekt](/cells/sv/net/refresh-and-calculate-pivot-table-having-calculated-items/)
- [Spara pivottabellen i filen ODS](/cells/sv/net/save-pivot-table-in-ods-file/)
- [Visa alternativ för rapportfiltersidor](/cells/sv/net/show-report-filter-pages-option/)
- [Arbeta med datavisningsformat för DataField i pivottabell](/cells/sv/net/working-with-data-display-formats-of-datafield-in-pivot-table/)
