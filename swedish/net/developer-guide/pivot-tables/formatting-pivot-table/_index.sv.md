---
title: Formatera pivottabell
type: docs
weight: 10
url: /sv/net/formatting-pivot-table/
---
## **Pivottabellens utseende**

Hur man skapar en pivottabell förklarar hur man skapar en enkel pivottabell. Den här artikeln beskriver hur du anpassar en pivottabells utseende genom att ställa in olika egenskaper:

- Alternativ för pivottabellformat
- Formatalternativ för pivotfält
- Formatalternativ för datafält

### **Ställa in alternativ för pivottabellformat**

 De[**Pivottabell**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable)klass styr den övergripande pivottabellen och kan formateras på ett antal sätt.

#### **Ställa in AutoFormat Type**

Microsoft Excel erbjuder ett antal olika förinställda rapportformat. Aspose.Cells stöder även dessa formateringsalternativ. Så här kommer du åt dem:

1.  Uppsättning[**Pivottabell.IsAutoFormat**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isautoformat) till**Sann**.
1.  Tilldela ett formateringsalternativ från[**PivotTableAutoFormatType**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottableautoformattype)uppräkning.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-SettingAutoFormat-1.cs" >}}

#### **Ställa in formatalternativ**

Kodexemplet nedan visar hur man formaterar pivottabellen för att visa totalsummor för rader och kolumner, och hur man ställer in rapportens fältordning. Den visar också hur man ställer in en kundsträng för nollvärden.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-SettingFormatOptions-1.cs" >}}

#### **Formatera utseende och känsla manuellt**

 För att formatera hur pivottabellsrapporten ser ut manuellt, istället för att använda förinställda rapportformat, använd[**PivotTable.Format()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/format) och[**PivotTable.FormatAll()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/formatall)metoder. Skapa ett stilobjekt för önskad formatering, till exempel:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-FormattingLook-1.cs" >}}

### **Ställa in alternativ för pivotfältsformat**

 De[**Pivotfält**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield)klass representerar ett fält i en pivottabell och kan formateras på ett antal sätt. Kodexemplet nedan visar hur du:

- Få tillgång till radfält.
- Ställa in delsummor.
- Ställa in autosort.
- Ställa in autoshow.

#### **Ställa in format för rad/kolumn/sidfält**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-SettingPageFieldFormat-1.cs" >}}

### **Ställa in format för datafält**

Kodexemplet nedan visar hur man ställer in visningsformat och talformat för datafält.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-SettingDataFieldFormat-1.cs" >}}

### **Rensa pivotfält**

 De[**PivotFieldCollection**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfieldcollection) har en metod som heter[**Klar()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfieldcollection/methods/clear)som låter dig rensa pivotfält. Använd den när du vill rensa alla pivotfält i områdena, till exempel sida, kolumn, rad eller data.
Kodexemplet nedan visar hur man rensar alla pivotfält i ett dataområde.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-ClearPivotFields-1.cs" >}}
