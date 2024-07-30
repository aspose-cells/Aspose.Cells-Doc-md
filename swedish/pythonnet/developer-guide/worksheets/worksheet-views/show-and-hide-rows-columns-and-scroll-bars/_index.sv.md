---
title: Visa och Dölja rader, Kolumner och Rullningslistor
type: docs
weight: 20
url: /sv/python-net/show-and-hide-rows-columns-and-scroll-bars/
description: Denna artikel visar hur man programmatiskt visar och döljer Excel arkrad och kolumner med hjälp av Aspose.Cells för Python via .NET API. Synligheten av rullningsfält kan justeras och flera rader och kolumner kan döljas.
keywords: Python Excel Library, Python visa rader och kolumner, Python dölj rader och kolumner, Python visa vertikalt rullningsfält, Python visa horisontellt rullningsfält, Python dölj vertikalt rullningsfält, Python dölj horisontell rullningsfält, Python Visa och Dölj Rader Kolumner och Rullningsfält.
---

{{% alert color="primary" %}}

Aspose.Cells för Python via .NET ger sätt att kontrollera synligheten av Rader, Kolumner och Rullningsfält i ett kalkylblad.

{{% /alert %}}

## **Visa och göm rader och kolumner**

Aspose.Cells för Python via .NET ger en klass, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), som representerar en Microsoft Excel-fil. Klassen [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) innehåller en [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) samling som gör det möjligt att komma åt varje arbetsblad i Excel-filen. Ett arbetsblad representeras av klassen [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). Klassen [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) tillhandahåller en [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) samling som representerar alla celler i arbetsbladet. Klassen [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) tillhandahåller flera metoder för att hantera rader eller kolumner i ett arbetsblad. Några av dessa diskuteras nedan.

### **Visa Rader och Kolumner**

Utvecklare kan visa vilken som helst dold rad eller kolumn genom att anropa  [**unhide_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_row/) och [**unhide_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_column/) orden samling respektive metoder. Båda metoderna tar två parametrar:

- **Rad- eller kolumnindex** - index för en rad eller kolumn som används för att visa den specifika raden eller kolumnen.
- **Radhöjd eller kolumnbredd** - radhöjden eller kolumnbredden tilldelad till raden eller kolumnen efter att ha visats.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Views-RowsColumns-Hiding-UnhidingRowsAndColumns-1.py" >}}

{{% alert color="primary" %}}

När du gör en dold kolumn synlig, om du behöver återställa den till tidigare tilldelad bredd eller till dess originalbredd, vänligen avdölj kolumnen med negativ bredd. Till exempel: arbetsblad.Cells.UnhideColumn(5, -1)

{{% /alert %}}

### **Dölj Rader och Kolumner**

Utvecklare kan dölja en rad eller kolumn genom att anropa  [**hide_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/hide_row/) och  [**hide_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/hide_column/) metoderna i respektive samling. Båda metoderna tar rad- och kolumnindex som parameter för att gömma den specifika raden eller kolumnen.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Views-RowsColumns-Hiding-HidingRowsAndColumns-1.py" >}}

{{% alert color="primary" %}}

Det är också möjligt att dölja en rad eller kolumn genom att ställa in radhöjden eller kolumnbredden till 0 respektive.

{{% /alert %}}

### **Dölj Flera Rader och Kolumner**

Utvecklare kan dölja flera rader eller kolumner samtidigt genom att anropa  [**hide_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/hide_rows/) och [**hide_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/hide_columns) orden i respektive samling. Båda metoderna tar startindex för rad eller kolumn och antalet rader eller kolumner som ska döljas som parametrar.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Views-RowsColumns-Hiding-HidingMultipleRowsAndColumns-1.py" >}}

## **Visa och dölj bildrullningsfält**

Rullningslistor används för att navigera bland innehållet i en fil. Vanligtvis finns det två typer av rullningslistor:

- Vertikala bildrullningsfält
- Horisontella bildrullningsfält

Microsoft Excel tillhandahåller även horisontella och vertikala rullningsfält så att användare kan bläddra genom innehållet i kalkylbladet. Med hjälp av Aspose.Cells för Python via .NET kan utvecklare kontrollera synligheten av båda typerna av rullningsfält i Excel-filer.

### **Kontrollera Synligheten för Rullningslistor**

Aspose.Cells för Python via .NET ger en klass, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) som representerar en Excel-fil. Klassen [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) innehåller ett brett utbud av egenskaper och metoder för att hantera en Excel-fil. För att kontrollera synligheten av rullningsfält, använd klassens [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) egenskaper [**WorkbookSettings.is_v_scroll_bar_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/is_v_scroll_bar_visible) och [**WorkbookSettings.is_h_scroll_bar_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/is_h_scroll_bar_visible). [**WorkbookSettings.is_v_scroll_bar_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/is_v_scroll_bar_visible) och [**WorkbookSettings.is_h_scroll_bar_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/is_h_scroll_bar_visible) är booleska egenskaper, vilket innebär att dessa egenskaper bara kan spara **true** eller **false** värden.

#### **Gör bildrullningsfält synliga**

Gör rullningslistor synliga genom att ställa in klassens [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) egenskap [**WorkbookSettings.is_v_scroll_bar_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/is_v_scroll_bar_visible) eller [**WorkbookSettings.is_h_scroll_bar_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/is_h_scroll_bar_visible) till **true**.

#### **Dölja bildrullningsfält**

Dölj rullningslistor genom att ställa in klassens [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) egenskap [**WorkbookSettings.is_v_scroll_bar_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/is_v_scroll_bar_visible) eller [**WorkbookSettings.is_h_scroll_bar_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/is_h_scroll_bar_visible) till **false**.

**Exempelkod**

Nedan finns en komplett kod som öppnar en Excel-fil, book1.xls, gömmer båda rullningsfälten och sparar sedan den modifierade filen som output.xls.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Views-Worksheets-Display-DisplayHideScrollBars-1.py" >}}
