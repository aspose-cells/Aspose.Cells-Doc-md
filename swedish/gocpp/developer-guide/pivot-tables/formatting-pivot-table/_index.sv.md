---
title: Formatera pivottabell med Golang via C++
linktitle: Formatera Pivot tabell
type: docs
weight: 10
url: /sv/go-cpp/formatting-pivot-table/
description: Lär dig hur man anpassar utseendet på pivot tabeller med Aspose.Cells for C++.
---

## **Pivottabellens utseende**

Hur man skapar en pivottabell förklarar hur man skapar en enkel pivottabell. Den här artikeln beskriver hur man anpassar en pivottabells utseende genom att ställa in olika egenskaper:

- Pivottabellformatalternativ
- Alternativ för pivottabellfältformat
- Alternativ för datafältformat

### **Inställning av pivottabellformatalternativ**

Klassen [**PivotTable**](https://reference.aspose.com/cells/go-cpp/pivottable/) kontrollerar den övergripande pivottabellen och kan formateras på olika sätt.

#### **Inställning av autoformat typ**

Microsoft Excel erbjuder ett antal förinställda rapportformat. Aspose.Cells stöder också dessa formateringsalternativ. För att komma åt dem:

1. Ställ in [**PivotTable.IsAutoFormat**](https://reference.aspose.com/cells/go-cpp/pivottable/isautoformat/) till **true**.
1. Tilldela ett formateringsalternativ från uppräkningen [**PivotTableAutoFormatType**](https://reference.aspose.com/cells/go-cpp/pivottableautoformattype/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FormattingPivotTable.go" >}}
#### **Inställning av formatalternativ**

Följande kodexempel visar hur man formaterar pivot-tabellen för att visa grand totals för rader och kolumner, och hur man ställer in rapportens fältordning. Det visar också hur man ställer in en anpassad sträng för null-värden.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FormattingPivotTable-1.go" >}}
#### **Manuell formatering av utseende**

För att formatera hur pivot-tabellrapporten ser ut manuellt, istället för att använda förinställda rapportformat, använd [**PivotTable.Format()**](https://reference.aspose.com/cells/go-cpp/pivottable/format_pivotarea_style/)-och [**PivotTable.FormatAll()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/formatall/)-metoderna. Skapa ett stildokument för önskad formatering, till exempel:

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FormattingPivotTable-2.go" >}}
### **Inställning av pivottabellfältformatalternativ**

Klassen [**PivotField**](https://reference.aspose.com/cells/go-cpp/pivotfield/) representerar ett fält i en pivottabell och kan formateras på olika sätt. Kodprovet nedan visar hur man:

- Tillgång till radfält.
- Inställning av delsummer.
- Inställning av autosortering.
- Inställning av autoshow.

#### **Inställning av format för rad/kolumn/sidofältsformat**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FormattingPivotTable-3.go" >}}
### **Anger format för datafält**

Kodprovet nedan visar hur man ställer in visningsformat och nummerformat för datafält.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FormattingPivotTable-4.go" >}}
### **Rensa pivottabellsfält**

Klassen [**PivotFieldCollection**](https://reference.aspose.com/cells/go-cpp/pivotfieldcollection/) har en metod som heter [**Clear()**](https://reference.aspose.com/cells/go-cpp/pivotfieldcollection/clear/) som låter dig rensa pivottabellsfält. Använd den när du vill rensa alla pivottabellfält i områdena, till exempel sida, kolumn, rad eller data.
Kodprovet nedan visar hur man rensar alla pivottabellfält i ett dataområde.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FormattingPivotTable-5.go" >}}
