---
title: Gruppering, Avgruppering av rader och kolumner
type: docs
weight: 30
url: /sv/go-cpp/grouping-ungrouping-rows-and-columns/
---

## **Introduktion**

I en Microsoft Excel-fil kan du skapa en översikt över data för att kunna visa och dölja detaljnivåer med en enda musklick.

Klicka på **Översiktssymboler**, 1,2,3, + och - för att snabbt visa endast de rader eller kolumner som ger sammanfattningar eller rubriker för avsnitt i ett blad, eller så kan du använda symbolerna för att se detaljer under en enskild sammanfattning eller rubrik.

## **Hantering av gruppering av rader och kolumner**

Aspose.Cells tillhandahåller en klass, [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) som representerar en Microsoft Excel-fil. [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) klassen innehåller en [Worksheets](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) samling som möjliggör åtkomst till varje arbetsblad i Excel-filen. Ett arbetsblad är representerat av [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) klassen. [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) klassen tillhandahåller en [Cells](https://reference.aspose.com/cells/go-cpp/cells/) samling som representerar alla celler i arbetsbladet.

[Cells](https://reference.aspose.com/cells/go-cpp/cells/) samlingen ger flera metoder för att hantera rader eller kolumner i ett arbetsblad, några av dessa diskuteras nedan i mer detalj.

### **Gruppering av rader och kolumner**

Det är möjligt att gruppera rader eller kolumner genom att anropa metoderna [GroupRows](https://reference.aspose.com/cells/go-cpp/cells/grouprows/) och [GroupColumns](https://reference.aspose.com/cells/go-cpp/cells/groupcolumns/) i [Cells](https://reference.aspose.com/cells/go-cpp/cells/) samlingen. Båda metoderna tar följande parametrar:

- Den första rad- eller kolumnindex, den första raden eller kolumnen i gruppen.
- Den sista rad- eller kolumnindex, den sista raden eller kolumnen i gruppen.
- Är dold, en boolesk parameter som specificerar om rader/kolumner ska döljas efter gruppering eller inte.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GroupingRowsColumns.go" >}}

#### **Gruppinställningar**

Microsoft Excel tillåter att du konfigurerar gruppinställningar för att visa:

- Sammanfattande rader under detaljer.
- Sammanfattande kolumner till höger om detaljer.

## **Avgruppering av rader och kolumner**

För att avgruppera några grupperade rader eller kolumner, anropa [Cells](https://reference.aspose.com/cells/go-cpp/cells/) samlingens [UngroupRows](https://reference.aspose.com/cells/go-cpp/cells/ungrouprows/) och [UngroupColumns](https://reference.aspose.com/cells/go-cpp/cells/ungroupcolumns/) metoder. Båda metoderna tar två parametrar:

- Första rad- eller kolumnindex, första rad/kolumn som ska avgrupperas.
- Sista rad- eller kolumnindex, sista rad/kolumn som ska avgrupperas.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-UnGroupingRowsColumns.go" >}}
