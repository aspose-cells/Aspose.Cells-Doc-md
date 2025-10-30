---
title: Dölja och visa rader och kolumner
type: docs
weight: 60
url: /sv/python-net/hiding-and-showing-rows-and-columns/
description: Den här artikeln visar hur man döljer och visar rader och kolumner med hjälp av Aspose.Cells för Python via .NET API.
keywords: Python Excel bibliotek, Aspose.Cells Python Dölj och visa rader, Python Dölj och visa kolumner, Python Dölj rader och kolumner, Python Visa rader och kolumner.
---

{{% alert color="primary" %}}

Ibland är det meningsfullt att dölja vissa rader eller kolumner i ett kalkylblad och visa dem senare. Microsoft Excel tillhandahåller den här funktionen och det gör även Aspose.Cells för Python via .NET.

{{% /alert %}}

## **Kontrollera synligheten av rader och kolumner**

Aspose.Cells för Python via .NET tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), som representerar en Microsoft Excel-fil. Klassen [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) innehåller en [**WorksheetCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection) som låter utvecklare komma åt varje kalkylblad i Excel-filen. Ett kalkylblad representeras av klassen [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). Klassen [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) tillhandahåller en [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) som representerar alla celler i kalkylbladet. Samlingen [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) tillhandahåller flera metoder för att hantera rader eller kolumner i ett kalkylblad. Några av dessa diskuteras nedan.

## **Hur man döljer rader och kolumner**

Utvecklare kan dölja en rad eller kolumn genom att anropa  [**hide_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/hide_row/) och  [**hide_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/hide_column/) metoderna i respektive samling. Båda metoderna tar rad- och kolumnindex som parameter för att gömma den specifika raden eller kolumnen.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Hiding-HidingRowsAndColumns-1.py" >}}

{{% alert color="primary" %}}

Det är också möjligt att dölja en rad eller kolumn genom att ställa in radhöjden eller kolumnbredden till 0 respektive.

{{% /alert %}}

## **Hur man visar rader och kolumner**

Utvecklare kan visa vilken som helst dold rad eller kolumn genom att anropa  [**unhide_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_row/) och [**unhide_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_column/) orden samling respektive metoder. Båda metoderna tar två parametrar:

- **Rad- eller kolumnindex** - index för en rad eller kolumn som används för att visa den specifika raden eller kolumnen.
- **Radhöjd eller kolumnbredd** - radhöjden eller kolumnbredden tilldelad till raden eller kolumnen efter att ha visats.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Hiding-UnhidingRowsAndColumns-1.py" >}}

{{% alert color="primary" %}}

När du gör en dold kolumn synlig, om du behöver återställa den till tidigare tilldelad bredd eller till dess originalbredd, vänligen avdölj kolumnen med negativ bredd. Till exempel: arbetsblad.Cells.UnhideColumn(5, -1)

{{% /alert %}}

## **Hur man döljer flera rader och kolumner**

Utvecklare kan dölja flera rader eller kolumner samtidigt genom att anropa  [**hide_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/hide_rows/) och [**hide_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/hide_columns/) orden i respektive samling. Båda metoderna tar startindex för rad eller kolumn och antalet rader eller kolumner som ska döljas som parametrar.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Hiding-HidingMultipleRowsAndColumns-1.py" >}}

{{% alert color="primary" %}}

Det är också möjligt att använda  {1} klassens  {2} och {3} metoder för att göra flera rader och kolumner synliga.

{{% /alert %}}
{{< app/cells/assistant language="python-net" >}}
