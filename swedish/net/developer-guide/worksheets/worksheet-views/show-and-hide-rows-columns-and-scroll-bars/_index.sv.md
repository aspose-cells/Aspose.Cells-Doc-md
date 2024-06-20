---
title: Visa och Dölja rader, Kolumner och Rullningslistor
type: docs
weight: 20
url: /sv/net/show-and-hide-rows-columns-and-scroll-bars/
description: Den här artikeln visar hur man programmatiskt visar och döljer Excel kalkylbladets rader och kolumner med hjälp av C# språket och .NET API eller Bibliotek. Synligheten av rullningslistor kan justeras och flera rader och kolumner kan döljas.
---

{{% alert color="primary" %}}

Aspose.Cells tillhandahåller sätt att kontrollera synligheten av rader, kolumner och rullningslistor på ett kalkylblad.

{{% /alert %}}

## **Visa och göm rader och kolumner**

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), som representerar en Microsoft Excel-fil. Klassen [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) innehåller en [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) samling som tillåter utvecklare att få åtkomst till varje kalkylblad i Excel-filen. Ett kalkylblad representeras av klassen [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). Klassen [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) tillhandahåller en [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) samling som representerar alla celler i kalkylbladet. Klassen [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) tillhandahåller flera metoder för att hantera rader eller kolumner i ett kalkylblad. Några av dessa diskuteras nedan.

### **Visa Rader och Kolumner**

Utvecklare kan visa vilken som helst dold rad eller kolumn genom att anropa  [**UnhideRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhiderow) och [**UnhideColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhidecolumn) orden samling respektive metoder. Båda metoderna tar två parametrar:

- **Rad- eller kolumnindex** - index för en rad eller kolumn som används för att visa den specifika raden eller kolumnen.
- **Radhöjd eller kolumnbredd** - radhöjden eller kolumnbredden tilldelad till raden eller kolumnen efter att ha visats.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-UnhidingRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

När du gör en dold kolumn synlig, om du behöver återställa den till tidigare tilldelad bredd eller till dess originalbredd, vänligen avdölj kolumnen med negativ bredd. Till exempel: arbetsblad.Cells.UnhideColumn(5, -1)

{{% /alert %}}

### **Dölj Rader och Kolumner**

Utvecklare kan dölja en rad eller kolumn genom att anropa  [**HideRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hiderow) och  [**HideColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hidecolumn) metoderna i respektive samling. Båda metoderna tar rad- och kolumnindex som parameter för att gömma den specifika raden eller kolumnen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-HidingRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

Det är också möjligt att dölja en rad eller kolumn genom att ställa in radhöjden eller kolumnbredden till 0 respektive.

{{% /alert %}}

### **Dölj Flera Rader och Kolumner**

Utvecklare kan dölja flera rader eller kolumner samtidigt genom att anropa  [**HideRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hiderows) och [**HideColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hidecolumns) orden i respektive samling. Båda metoderna tar startindex för rad eller kolumn och antalet rader eller kolumner som ska döljas som parametrar.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-HidingMultipleRowsAndColumns-1.cs" >}}

## **Visa och dölj bildrullningsfält**

Rullningslistor används för att navigera bland innehållet i en fil. Vanligtvis finns det två typer av rullningslistor:

- Vertikala bildrullningsfält
- Horisontella bildrullningsfält

Microsoft Excel tillhandahåller också horisontella och vertikala bildrullningsfält så att användare kan bläddra genom arbetsbladets innehåll. Med Aspose.Cells kan utvecklare kontrollera synligheten av båda typer av bildrullningsfält i Excelfiler.

### **Kontrollera Synligheten för Rullningslistor**

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) som representerar en Excel-fil. Klassen [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) tillhandahåller ett brett utbud av egenskaper och metoder för att hantera en Excel-fil. För att kontrollera synligheten för rullningslistor, använd klassen [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) egenskaperna [**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) och [**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible). [**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) och [**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) är booleska egenskaper, vilket innebär att dessa egenskaper bara kan lagra **true** eller **false** värden.

#### **Gör bildrullningsfält synliga**

Gör rullningslistor synliga genom att ställa in klassens [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) egenskap [**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) eller [**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) till **true**.

#### **Dölja bildrullningsfält**

Dölj rullningslistor genom att ställa in klassens [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) egenskap [**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) eller [**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) till **false**.

**Exempelkod**

Nedan finns en komplett kod som öppnar en Excel-fil, book1.xls, gömmer båda rullningsfälten och sparar sedan den modifierade filen som output.xls.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-DisplayHideScrollBars-1.cs" >}}
