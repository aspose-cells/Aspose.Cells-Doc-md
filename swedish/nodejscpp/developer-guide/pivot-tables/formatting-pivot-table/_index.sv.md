---
title: Formatera Pivot tabell
type: docs
weight: 10
url: /sv/nodejs-cpp/formatting-pivot-table/
description: Hur man formaterar pivottabell med Aspose.Cells for Node.js via C++.
keywords: Formatera pivot tabell.
---

## **Pivottabellens utseende**

Hur man skapar en pivottabell förklarar hur man skapar en enkel pivottabell. Den här artikeln beskriver hur man anpassar en pivottabells utseende genom att ställa in olika egenskaper:

- Pivottabellformatalternativ
- Alternativ för pivottabellfältformat
- Alternativ för datafältformat

### **Hur man ställer in pivottabellsformatalternativ**

Klassen [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/) kontrollerar den övergripande pivottabellen och kan formateras på olika sätt.

#### **Hur man ställer in automatiskt format typ**

Microsoft Excel erbjuder ett antal förinställda rapportformat. Aspose.Cells for Node.js via C++ stöder även dessa formateringsalternativ. För att komma åt dem:

1. Ställ in [**PivotTable.setIsAutoFormat(value)**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#setIsAutoFormat-boolean-) till **true**.
1. Tilldela ett formateringsalternativ från uppräkningen [**PivotTableAutoFormatType**](https://reference.aspose.com/cells/nodejs-cpp/pivottableautoformattype/).

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-SettingAutoFormat-1.js" >}}

#### **Hur man ställer in formateringsalternativ**

Kodprovet nedan visar hur man formaterar pivottabellen för att visa totaler för rader och kolumner, och hur man ställer in rapportens fältsortering. Det visar också hur man ställer in en anpassad sträng för nollvärden.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-SettingFormatOptions-1.js" >}}

#### **Manuell formatering av utseende**

För att manuellt formatera hur pivottabelrapporten ser ut, istället för att använda förinställda rapportformat, använd [**PivotTable.formatAll(style)**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#formatAll-style-)- och [**PivotTable.format(row, column, style)**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#format-number-number-style-)-metoderna. Skapa en stilobjekt för önskad formatering, till exempel:

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-FormattingLook-1.js" >}}

### **Hur man ställer in pivottabellsfältformatalternativ**

Klassen [**PivotField**](https://reference.aspose.com/cells/nodejs-cpp/pivotfield/) representerar ett fält i en pivottabell och kan formateras på olika sätt. Kodprovet nedan visar hur man:

- Tillgång till radfält.
- Inställning av delsummer.
- Inställning av autosortering.
- Inställning av autoshow.

#### **Hur man ställer in rad/kolumn/sida fältformat**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-SettingPageFieldFormat-1.js" >}}

### **Hur man ställer in datafältformat**

Kodprovet nedan visar hur man ställer in visningsformat och nummerformat för datafält.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-SettingDataFieldFormat-1.js" >}}

### **Hur man rensar pivottabellsfält**

Klassen [**PivotFieldCollection**](https://reference.aspose.com/cells/nodejs-cpp/pivotfieldcollection/) har en metod som heter [**clear()**](https://reference.aspose.com/cells/nodejs-cpp/pivotfieldcollection/#clear--) som låter dig rensa pivottabellsfält. Använd den när du vill rensa alla pivottabellfält i områdena, till exempel sida, kolumn, rad eller data.
Kodprovet nedan visar hur man rensar alla pivottabellfält i ett dataområde.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-ClearPivotFields-1.js" >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
