---
title: Visa och Dölja rader, Kolumner och Rullningslistor
type: docs
weight: 20
url: /sv/python-net/show-and-hide-rows-columns-and-scroll-bars/
description: Denna artikel demonstrerar hur man programmässigt visar och döljer rader och kolumner i Excel ark med hjälp av Aspose.Cells för Python via .NET API. Synligheten för scrollningslinjer kan justeras, och flera rader och kolumner kan döljas.
keywords: Python Excel bibliotek, Python visa rader och kolumner, Python dölj rader och kolumner, Python visa vertikal scroll list, Python visa horisontell scroll list, Python dölja vertikal scroll list, Python dölja horisontell scroll list, Python Visa och Dölj Rader, Kolumner och Scroll Listor.
---

{{% alert color="primary" %}}

Aspose.Cells för Python via .NET ger sätt att kontrollera synligheten för Rader, Kolumner och Scroll-Listor i ett kalkylblad.

{{% /alert %}}

## **Visa och göm rader och kolumner**

Aspose.Cells för Python via .NET tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), som representerar en Microsoft Excel-fil. Klassen [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) innehåller en [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) samling som låter utvecklare få åtkomst till varje kalkylblad i Excel-filen. Ett kalkylblad representeras av klassen [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). Klassen [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) ger en [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) samling som representerar alla celler i kalkylbladet. Samlingen [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) ger flera metoder för att hantera rader eller kolumner i ett kalkylblad. Några av dessa diskuteras nedan.

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

Microsoft Excel tillhandahåller också horisontella och vertikala skrollbars så att användare kan scrolla genom arbetsbladets innehåll. Med Aspose.Cells för Python via .NET kan utvecklare kontrollera synligheten för båda typerna av skrollbars i Excel-filer.

### **Kontrollera Synligheten för Rullningslistor**

Aspose.Cells för Python via .NET ger en klass, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), som representerar en Excel-fil. [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)-klassen ger ett brett spektrum av egenskaper och metoder för att hantera en Excel-fil. För att kontrollera synligheten av skrollbars, använd [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)-klassens [**WorkbookSettings.is_v_scroll_bar_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/is_v_scroll_bar_visible) och [**WorkbookSettings.is_h_scroll_bar_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/is_h_scroll_bar_visible)-egenskaper. [**WorkbookSettings.is_v_scroll_bar_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/is_v_scroll_bar_visible) och [**WorkbookSettings.is_h_scroll_bar_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/is_h_scroll_bar_visible) är Boolean-egenskaper, vilket innebär att dessa egenskaper endast kan lagra **true** eller **false** värden.

#### **Gör bildrullningsfält synliga**

Gör rullningslistor synliga genom att ställa in klassens [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) egenskap [**WorkbookSettings.is_v_scroll_bar_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/is_v_scroll_bar_visible) eller [**WorkbookSettings.is_h_scroll_bar_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/is_h_scroll_bar_visible) till **true**.

#### **Dölja bildrullningsfält**

Dölj rullningslistor genom att ställa in klassens [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) egenskap [**WorkbookSettings.is_v_scroll_bar_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/is_v_scroll_bar_visible) eller [**WorkbookSettings.is_h_scroll_bar_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/is_h_scroll_bar_visible) till **false**.

**Exempelkod**

Nedan finns en komplett kod som öppnar en Excel-fil, book1.xls, gömmer båda rullningsfälten och sparar sedan den modifierade filen som output.xls.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Views-Worksheets-Display-DisplayHideScrollBars-1.py" >}}
