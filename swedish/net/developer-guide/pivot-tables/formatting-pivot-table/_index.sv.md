---
title: Formatera Pivot tabell
type: docs
weight: 10
url: /sv/net/formatting-pivot-table/
---

## **Pivottabellens utseende**

Hur man skapar en pivottabell förklarar hur man skapar en enkel pivottabell. Den här artikeln beskriver hur man anpassar en pivottabells utseende genom att ställa in olika egenskaper:

- Pivottabellformatalternativ
- Alternativ för pivottabellfältformat
- Alternativ för datafältformat

### **Inställning av pivottabellformatalternativ**

Klassen [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) kontrollerar den övergripande pivottabellen och kan formateras på olika sätt.

#### **Inställning av autoformat typ**

Microsoft Excel erbjuder ett antal olika förinställda rapportformat. Aspose.Cells stöder också dessa formateringsalternativ. För att komma åt dem:

1. Ställ in [**PivotTable.IsAutoFormat**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isautoformat) till **true**.
1. Tilldela ett formateringsalternativ från uppräkningen [**PivotTableAutoFormatType**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottableautoformattype).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-SettingAutoFormat-1.cs" >}}

#### **Inställning av formatalternativ**

Kodprovet nedan visar hur man formaterar pivottabellen för att visa totaler för rader och kolumner, och hur man ställer in rapportens fältsortering. Det visar också hur man ställer in en anpassad sträng för nollvärden.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-SettingFormatOptions-1.cs" >}}

#### **Manuell formatering av utseende**

För att formatera hur pivottabellsrapporten ser ut manuellt, istället för att använda förinställda rapportformat, använd [**PivotTable.Format()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/format)- och [**PivotTable.FormatAll()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/formatall)-metoderna. Skapa en stilobjekt för den önskade formateringen, till exempel:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-FormattingLook-1.cs" >}}

### **Inställning av pivottabellfältformatalternativ**

Klassen [**PivotField**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield) representerar ett fält i en pivottabell och kan formateras på olika sätt. Kodprovet nedan visar hur man:

- Tillgång till radfält.
- Inställning av delsummer.
- Inställning av autosortering.
- Inställning av autoshow.

#### **Inställning av format för rad/kolumn/sidofältsformat**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-SettingPageFieldFormat-1.cs" >}}

### **Inställning av format för datafält**

Kodprovet nedan visar hur man ställer in visningsformat och nummerformat för datafält.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-SettingDataFieldFormat-1.cs" >}}

### **Rensa pivottabellsfält**

Klassen [**PivotFieldCollection**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfieldcollection) har en metod som heter [**Clear()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfieldcollection/methods/clear) som låter dig rensa pivottabellsfält. Använd den när du vill rensa alla pivottabellfält i områdena, till exempel sida, kolumn, rad eller data.
Kodprovet nedan visar hur man rensar alla pivottabellfält i ett dataområde.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-ClearPivotFields-1.cs" >}}
