---
title: Formatera pivottabell
type: docs
weight: 10
url: /sv/net/formatting-pivot-table/
description: Hur man formaterar pivottabellen med Aspose.Cells for Python via .NET.
keywords: Format pivot table.
---
##  **Pivottabellens utseende**

Hur man skapar en pivottabell förklarar hur man skapar en enkel pivottabell. Den här artikeln beskriver hur du anpassar en pivottabells utseende genom att ställa in olika egenskaper:

- Alternativ för pivottabellformat
- Formatalternativ för pivotfält
- Formatalternativ för datafält

###  **Ställa in alternativ för pivottabellformat**

 De[**Pivottabell**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/)klass styr den övergripande pivottabellen och kan formateras på ett antal sätt.

####  **Ställa in AutoFormat Type**

Microsoft Excel erbjuder ett antal olika förinställda rapportformat. Aspose.Cells for Python via .NET stöder även dessa formateringsalternativ. Så här kommer du åt dem:

1.  Uppsättning[**PivotTable.is_auto_format**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_auto_format/)till *sant**.
1.  Tilldela ett formateringsalternativ från[**PivotTableAutoFormatType**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottableautoformattype/)uppräkning.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SettingAutoFormat-1.py" >}}

####  **Ställa in formatalternativ**

Kodexemplet nedan visar hur man formaterar pivottabellen för att visa totalsummor för rader och kolumner, och hur man ställer in rapportens fältordning. Den visar också hur man ställer in en kundsträng för nollvärden.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SettingFormatOptions-1.py" >}}

####  **Formatera utseende och känsla manuellt**

För att formatera hur pivottabellsrapporten ser ut manuellt, istället för att använda förinställda rapportformat, använd[**PivotTable.format_all(stil)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/format_all/) och[**PivotTable.format(rad, kolumn, stil)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/format/)metoder. Skapa ett stilobjekt för önskad formatering, till exempel:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-FormattingLook-1.py" >}}

###  **Ställa in alternativ för pivotfältsformat**

 De[**Pivotfält**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield/)klass representerar ett fält i en pivottabell och kan formateras på ett antal sätt. Kodexemplet nedan visar hur du:

- Få tillgång till radfält.
- Ställa in delsummor.
- Ställa in autosort.
- Ställa in autoshow.

####  **Ställa in format för rad/kolumn/sidfält**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SettingPageFieldFormat-1.py" >}}

###  **Ställa in format för datafält**

Kodexemplet nedan visar hur man ställer in visningsformat och talformat för datafält.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SettingDataFieldFormat-1.py" >}}

###  **Rensa pivotfält**

 De[**PivotFieldCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfieldcollection/) har en metod som heter[**clear()**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfieldcollection/clear/#)som låter dig rensa pivotfält. Använd den när du vill rensa alla pivotfält i områdena, till exempel sida, kolumn, rad eller data.
Kodexemplet nedan visar hur man rensar alla pivotfält i ett dataområde.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-ClearPivotFields-1.py" >}}
