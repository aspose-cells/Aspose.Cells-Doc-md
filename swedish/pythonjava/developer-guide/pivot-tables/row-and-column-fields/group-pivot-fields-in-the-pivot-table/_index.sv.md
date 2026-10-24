---
title: Gruppera pivotfält i pivottabellen
linktitle: Gruppera pivotfält i pivottabellen
description: Lär dig hur du grupperar rad- och kolumnpivotfält i en pivottabell till datumperioder som månader och kvartal samt numeriska intervall med hjälp av PivotField.group och PivotFieldGroupOptions i Aspose.Cells for Python via Java.
keywords: Aspose.Cells, pivottabell, gruppera pivotfält, PivotField.group, PivotFieldGroupOptions, datumgruppering, nummergruppering, månader, kvartal, numeriskt intervall, Python
type: docs
weight: 80
url: /sv/python-java/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Möjliga användningsscenarier**
- Att gruppera pivotfält är användbart när ett rad- eller kolumnfält i en pivottabell innehåller många olika värden, till exempel ett datumfält med hundratals datum eller ett numeriskt fält med många spridda värden. Gruppering slår samman dessa värden till meningsfulla sektioner: datum till månader, kvartal och år, och nummer till intervall som 0-1, 2-3, 4-5. Detta gör en stor pivottabell kompakt och enklare att analysera. Aspose.Cells tillhandahåller denna funktionalitet genom metoden `PivotField.group()` (automatisk gruppering efter datatyp) och `PivotField.group(PivotFieldGroupOptions)` (anpassade grupperingsalternativ).
- Datumgruppering rullar upp de enskilda datumen till större perioder, såsom dagar, månader, kvartal och år, och bygger en tidshierarki (till exempel År, Kvartal, Månader). Trender över tid blir synliga med ett ögonkast, och varje periodnivå blir sitt eget pivotfält i rad- eller kolumnområdet i pivottabellen.
- Gruppering är endast tillgänglig för fält som är placerade i ROW- eller COLUMN-området i en pivottabell. Ett datafält (värdefält) kan inte grupperas direkt. För att gruppera ett sådant fält måste du först lägga till det i rad- eller kolumnområdet i pivottabellen.

## **Gruppera pivotfält automatiskt**
Den parameterlösa överlagringen `PivotField.group()` inspekterar fältets datatyp och grupperar det automatiskt. Ett fält som endast innehåller datum (och tomma celler) grupperas efter månader. Ett fält som endast innehåller nummer (och tomma celler) grupperas i numeriska intervall med hjälp av ett automatiskt intervall.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
# Ladda exempelarbetsboken
wb = Workbook("sampleGroupPivotFieldsInPivotTable.xlsx")
# Öppna det andra kalkylbladet och dess pivottabell
pt = wb.getWorksheets().get(1).getPivotTables().get(0)
# Gruppera det första radfältet automatiskt.
# Fältet innehåller datum, så det grupperas efter månader.
field = pt.getRowFields().get(0)
field.group()
# Beräkna pivottabellens data och spara utdatafilen
pt.calculateData()
wb.save("outputAutoGroupPivotField.xlsx")
jpype.shutdownJVM()
```

## **Gruppera pivotfält med anpassade alternativ**
Klassen `PivotFieldGroupOptions` tillhandahåller anpassad grupperingskonfiguration. För datumfält, ange `StartDate`, `EndDate` och `GroupTypes`. För numeriska fält, ange `StartNumber`, `EndNumber` och `Interval`. Egenskapen `NewPivotField` styr om gruppering skapar nya pivotfält bredvid originalfältet (se avsnittet Notis i slutet av denna artikel).

### **Gruppera ett datumfält efter månader och kvartal**
Följande exempel grupperar datumradfältet i exempel-pivottabellen efter månader och kvartal mellan ett start- och slutdatum. Koden läser in [exempelfilen i Excel](sampleGroupPivotFieldsInPivotTable.xlsx), utför grupperingen, beräknar pivottabellsdata och sparar det grupperade resultatet. Skärmbilden visar effekten: datumradfältet är nu grupperat efter kvartal och månader.
Observera att ordningen på värdena i `options.GroupTypes` ignoreras. Oavsett i vilken ordning grupptyperna listas visas de grupperade fälten alltid från den största perioden till den minsta: år, kvartal, månader, dagar, timmar, minuter, sekunder. I detta exempel listas månaderna före kvartalen i `options.GroupTypes`, men kvartalen visas som den yttre nivån och månaderna som den inre nivån.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, PivotFieldGroupOptions, PivotGroupByType, DateTime
# Ladda exempelarbetsboken
wb = Workbook("sampleGroupPivotFieldsInPivotTable.xlsx")
# Få åtkomst till det andra kalkylbladet och dess pivottabell
pt = wb.getWorksheets().get(1).getPivotTables().get(0)
# Gruppera det första radfältet (ett datumfält) efter månader och kvartal
options = PivotFieldGroupOptions()
options.setStartDate(DateTime(2008, 1, 1))
options.setEndDate(DateTime(2008, 9, 5))
options.setGroupTypes([PivotGroupByType.MONTHS, PivotGroupByType.QUARTERS])
pt.getRowFields().get(0).group(options)
# Beräkna pivottabellsdata och spara utdatafilen
pt.calculateData()
wb.save("outputGroupPivotFieldsInPivotTable.xlsx")
jpype.shutdownJVM()
```

![Pivottabell grupperad efter månader och kvartal](group-pivot-fields-in-the-pivot-table_1.png)

### **Gruppera ett numeriskt fält i intervall**
`FieldTwo` i exempel-pivottabellen är initialt ett datafält (värdefält). Eftersom endast rad- eller kolumnfält kan grupperas anropar koden först `pivotTable.addFieldToArea(PivotFieldType.ROW, "FieldTwo")` för att flytta `FieldTwo` till radområdet, uppdaterar pivoten och grupperar sedan det numeriska fältet i intervallen 0-1, 2-3 och 4-5 med `StartNumber = 0`, `EndNumber = 5` och `Interval = 2`.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, PivotFieldType, PivotFieldGroupOptions
# Ladda exempelarbetsboken
wb = Workbook("sampleGroupPivotFieldsInPivotTable.xlsx")
# Öppna det andra kalkylbladet och dess pivottabell
pt = wb.getWorksheets().get(1).getPivotTables().get(0)
# FieldTwo är ett datafält: flytta det till radområdet först,
# eftersom endast rad-/kolumnfält kan grupperas
pt.addFieldToArea(PivotFieldType.ROW, "FieldTwo")
pt.calculateData()
# Gruppera det numeriska fältet i intervallen 0-1, 2-3, 4-5
options = PivotFieldGroupOptions()
options.setStartNumber(0)
options.setEndNumber(5)
options.setInterval(2)
pt.getRowFields().get(1).group(options)
# Beräkna pivottabellsdata och spara utdatafilen
pt.calculateData()
wb.save("outputNumberGroupPivotField.xlsx")
jpype.shutdownJVM()
```

## **Notis**

{{% alert color="primary" %}}
- Metodöverlagringarna `PivotField.groupBy()` är föråldrade och har tagits bort från API-ytan. `PivotField.group()` och `PivotField.group(PivotFieldGroupOptions)` är ersättningarna.
- I Microsoft Excel ERSÄTTER gruppering av ett numeriskt fält det ursprungliga pivotfältet med de grupperade intervallen, medan gruppering av ett datumfält skapar NYA pivotfält (ett per gruppnivå, till exempel Kvartal och Månader) bredvid originalfältet. Från och med Aspose.Cells 26.10 följer metoderna `PivotField.group()` samma beteende som Excel. Egenskapen `PivotFieldGroupOptions.NewPivotField` finns för kompatibilitet med äldre versioner: den är som standard false för numerisk gruppering och true för datum-/tidsgruppering; sätt den till false om du vill att datumgruppering ska ersätta det ursprungliga pivotfältet istället för att skapa nya pivotfält.
- Egenskapen `PivotFieldGroupOptions.Interval` har endast effekt för numerisk gruppering och för datumgruppering efter dagar (till exempel gruppering av datum i 7-dagarsperioder); den ignoreras när datum grupperas efter månader, kvartal eller år.
{{% /alert %}}

## **Relaterade artiklar**
- [Lägg till rad- och kolumnfält i pivottabell](/cells/sv/python-java/pivot-table-add-row-and-column-fields/)
- [Filtrera pivottabeller efter etikett eller värde](/cells/sv/python-java/filter-by-label-or-value-of-pivot-table/)
- [Lägg till sidfält i pivottabell](/cells/sv/python-java/add-page-field-in-pivot-table/)
- [Tillämpa stil på pivottabell](/cells/sv/python-java/apply-style-to-pivot-table/)
- [Uppdatera pivottabell](/cells/sv/python-java/refresh-pivot-table/)

{{< app/cells/assistant language="python" >}}