---
title: Gruppera pivot-fält i pivottabellen
linktitle: Gruppera pivot-fält i pivottabellen
description: Lär dig hur du grupperar rad- och kolumnpivotfält i en pivottabell till datumperioder som månader och kvartal samt numeriska intervall med PivotField.Group och PivotFieldGroupOptions i Aspose.Cells for Python via .NET.
keywords: Aspose.Cells, pivottabell, gruppera pivotfält, PivotField.Group, PivotFieldGroupOptions, datumgruppering, nummergruppering, månader, kvartal, numeriskt intervall, Python via .NET
type: docs
weight: 80
url: /sv/python-net/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Möjliga användningsscenarier**
- Att gruppera pivotfält är användbart när ett rad- eller kolumnfält i en pivottabell innehåller många olika objekt, till exempel ett datumfält med hundratals datum eller ett numeriskt fält med många spridda värden. Grupperingen komprimerar dessa objekt till meningsfulla sektioner: datum till månader, kvartal och år, och tal till intervall som 0–1, 2–3, 4–5. Detta gör en stor pivottabell kompakt och enklare att analysera. Aspose.Cells for Python via .NET tillhandahåller denna funktionalitet via metoden `pivot_field.group()` (automatisk gruppering efter datatyp) och `pivot_field.group(pivot_field_group_options)` (anpassade grupperingsalternativ).
- Datumgruppering rullar upp enskilda datum till större perioder, såsom dagar, månader, kvartal och år, och bygger en tidshierarki (till exempel år, kvartal, månader). Trender över tid blir synliga med en blick, och varje periodnivå blir sitt eget pivotfält i rad- eller kolumnområdet i pivottabellen.
- Gruppering är endast tillgänglig för fält som ligger i rad- eller kolumnområdet i en pivottabell. Ett datafält (värdefält) kan inte grupperas direkt. För att gruppera ett sådant fält måste du först lägga till det i rad- eller kolumnområdet i pivottabellen.

## **Gruppera pivotfält automatiskt**
Den parameterlösa överlagringen `pivot_field.group()` inspekterar fältets datatyp och grupperar det automatiskt. Ett fält som endast innehåller datum (och tomma celler) grupperas per månader. Ett fält som endast innehåller tal (och tomma celler) grupperas i numeriska intervall med ett automatiskt intervall.

```python
import aspose.cells as ac
# Ladda exempelarbetsboken
wb = ac.Workbook("sampleGroupPivotFieldsInPivotTable.xlsx")
# Öppna det andra kalkylbladet och dess pivottabell
pt = wb.worksheets[1].pivot_tables[0]
# Gruppera det första radfältet automatiskt.
# Fältet innehåller datum, så det grupperas efter månader.
field = pt.row_fields[0]
field.group()
# Beräkna pivottabellsdata och spara utdatafilen
pt.calculate_data()
wb.save("outputAutoGroupPivotField.xlsx")
```

## **Gruppera pivotfält med anpassade alternativ**
Klassen `PivotFieldGroupOptions` tillhandahåller anpassad grupperingskonfiguration. För datumfält anger du `start_date`, `end_date` och `group_types`. För numeriska fält anger du `start_number`, `end_number` och `interval`. Egenskapen `new_pivot_field` avgör om grupperingen skapar nya pivotfält bredvid originalet (se avsnittet Notera i slutet av denna artikel).

### **Gruppera ett datumfält efter månader och kvartal**
Följande exempel grupperar datumradfältet i exempelpivottabellen efter månader och kvartal mellan ett start- och slutdatum. Koden läser in [exempelfilen i Excel](sampleGroupPivotFieldsInPivotTable.xlsx), utför grupperingen, beräknar pivottabelldata och sparar det grupperade resultatet. Skärmbilden visar effekten: datumradfältet är nu grupperat efter kvartal och månader.
Observera att ordningen på värdena i `options.group_types` ignoreras. Oavsett i vilken ordning grupptyperna anges visas de grupperade fälten alltid från den största perioden till den minsta: år, kvartal, månader, dagar, timmar, minuter, sekunder. I detta exempel listas månaderna före kvartalen i `options.group_types`, men kvartalen visas som den yttre nivån och månaderna som den inre nivån.

```python
import aspose.cells as ac
from datetime import datetime
from aspose.cells.pivot import PivotGroupByType
from aspose.cells.pivot import PivotFieldGroupOptions
# Ladda exempelarbetsboken
wb = ac.Workbook("sampleGroupPivotFieldsInPivotTable.xlsx")
# Öppna det andra kalkylbladet och dess pivottabell
pt = wb.worksheets[1].pivot_tables[0]
# Gruppera det första radfältet (ett datumfält) efter månader och kvartal
options = PivotFieldGroupOptions()
options.start_date = datetime(2008, 1, 1)
options.end_date = datetime(2008, 9, 5)
options.group_types = [PivotGroupByType.MONTHS, PivotGroupByType.QUARTERS]
pt.row_fields[0].group(options)
# Beräkna pivottabellsdata och spara utdatafilen
pt.calculate_data()
wb.save("outputGroupPivotFieldsInPivotTable.xlsx")
```

![Pivottabell grupperad efter månader och kvartal](group-pivot-fields-in-the-pivot-table_1.png)

### **Gruppera ett numeriskt fält i intervall**
`FieldTwo` i exempelpivottabellen är från början ett datafält (värdefält). Eftersom endast rad- eller kolumnfält kan grupperas anropar koden först `pivot_table.add_field_to_area(PivotFieldType.ROW, "FieldTwo")` för att flytta `FieldTwo` till radområdet, uppdaterar pivoten och grupperar sedan det numeriska fältet i intervallen 0–1, 2–3 och 4–5 med `start_number=0`, `end_number=5` och `interval=2`.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
from aspose.cells.pivot import PivotFieldGroupOptions
# Ladda exempelarbetsboken
wb = ac.Workbook("sampleGroupPivotFieldsInPivotTable.xlsx")
# Kom åt det andra kalkylbladet och dess pivottabell
pt = wb.worksheets[1].pivot_tables[0]
# FieldTwo är ett datafält: flytta det först till radområdet,
# eftersom endast rad-/kolumnfält kan grupperas
pt.add_field_to_area(PivotFieldType.ROW, "FieldTwo")
pt.calculate_data()
# Gruppera det numeriska fältet i intervallen 0-1, 2-3, 4-5
options = PivotFieldGroupOptions()
options.start_number = 0.0
options.end_number = 5.0
options.interval = 2.0
pt.row_fields[1].group(options)
# Beräkna pivottabellens data och spara utdatafilen
pt.calculate_data()
wb.save("outputNumberGroupPivotField.xlsx")
```

## **Notera**

{{% alert color="primary" %}}
- Metodöverlagringarna `pivot_field.group_by()` är föråldrade och har tagits bort från API-ytan. `pivot_field.group()` och `pivot_field.group(pivot_field_group_options)` är ersättningarna.
- I Microsoft Excel ERSÄTTER gruppering av ett numeriskt fält det ursprungliga pivotfältet med de grupperade intervallen, medan gruppering av ett datumfält skapar NYA pivotfält (ett per gruppnivå, till exempel Kvartal och Månader) bredvid det ursprungliga fältet. Från och med Aspose.Cells 26.10 följer metoderna `pivot_field.group()` samma beteende som Excel. Egenskapen `PivotFieldGroupOptions.new_pivot_field` finns för kompatibilitet med äldre versioner: den är som standard false för numerisk gruppering och true för datum-tid-gruppering; sätt den till false om du vill att datumgruppering ska ersätta det ursprungliga pivotfältet istället för att skapa nya pivotfält.
- Egenskapen `PivotFieldGroupOptions.interval` har endast effekt vid numerisk gruppering och vid datumgruppering efter dagar (till exempel gruppering av datum i 7-dagarsperioder); den ignoreras när datum grupperas efter månader, kvartal eller år.
{{% /alert %}}

## **Relaterade artiklar**
- [Lägg till rad- och kolumnfält i pivottabell](/cells/sv/python-net/pivot-table-add-row-and-column-fields/)
- [Filtrera pivottabeller efter etikett eller värde](/cells/sv/python-net/filter-by-label-or-value-of-pivot-table/)
- [Lägg till sidfält i pivottabell](/cells/sv/python-net/add-page-field-in-pivot-table/)
- [Tillämpa stil på pivottabell](/cells/sv/python-net/apply-style-to-pivot-table/)
- [Uppdatera pivottabell](/cells/sv/python-net/refresh-pivot-table/)

{{< app/cells/assistant language="python-net" >}}