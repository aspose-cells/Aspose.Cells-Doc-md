---
title: Visa och dölj rutnät och radkolumnhuvuden
type: docs
weight: 30
url: /sv/python-net/show-and-hide-gridlines-and-row-column-headers/
description: Denna artikel ger exempel på kod för att använda Aspose.Cells för Python via .NET API för att programmatiskt dölja eller visa rutnätlinjer, rad och kolumnhuvuden i ett Excel arbetsblad.
keywords: Python Excel biblioteket, Python Visa och dölj rutnätlinjer, Hur man visar och döljer rad och kolumnhuvuden i Python, Hur man visar och döljer rutnätlinjer samt rad och kolumnhuvuden i Python.
---

{{% alert color="primary" %}}

Aspose.Cells för Python via .NET stödjer att dölja och visa rutnätlinjer i arbetsbladet, vilka som är synliga som standard. Det ger också kontroll över synligheten av rad- och kolumnhuvuden i arbetsbladet.

{{% /alert %}}

## **Visa och dölj rutnät**

Alla Excel-kalkylblad har rutnät som standard. De hjälper till att avgränsa celler så att det är lätt att ange data i specifika celler. Rutnät gör det möjligt för oss att se ett kalkylblad som en samling av celler, där varje cell är lätt identifierbar.

### **Kontrollera synligheten av rutnäten**

Aspose.Cells för Python via .NET tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/), som representerar en Microsoft Excel-fil. [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/)-klassen innehåller en [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/)-samling som gör det möjligt för utvecklare att få tillgång till varje arbetsblad i Excel-filen. Ett arbetsblad representeras av [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/)-klassen. [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/)-klassen ger ett brett utbud av egenskaper och metoder för att hantera ett arbetsblad. För att kontrollera synligheten av rutnätlinjer, använd [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/) [**is_gridlines_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_gridlines_visible/)-egenskapen. [**is_gridlines_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_gridlines_visible/) är en Boolean-egenskap, vilket betyder att den endast kan lagra ett **true** eller **false** värde.

#### **Gör rutnätslinjer synliga**

Gör rutnätet synligt genom att ange [**is_gridlines_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_gridlines_visible/)egenskapen för klassen [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) till **true**.

#### **Gömmer rutnätslinjer**

Dölj rutnätet genom att ange [**is_gridlines_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_gridlines_visible/)egenskapen för klassen [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) till **false**.

Ett komplett exempel ges nedan som visar användningen av [**is_gridlines_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_gridlines_visible/)egenskapen genom att öppna en Excelfil (book1.xls), dölja rutnätet på det första kalkylarket och spara den modifierade filen som output.xls.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Views-Display-DisplayHideGridlines-1.py" >}}

## **Visa och dölj radkolumnhuvuden**

Alla arbetsblad i en Excel-fil består av celler som är ordnade i rader och kolumner. Alla rader och kolumner har unika värden som används för att identifiera dem och för att identifiera enskilda celler. Till exempel är radnumren – 1, 2, 3, 4, etc. – och kolumner är alfabetiskt ordnade – A, B, C, D, etc. Rad- och kolumnvärdena visas i rubrikerna. Med Aspose.Cells för Python via .NET kan utvecklare kontrollera synligheten av dessa rad- och kolumnrubriker.

### **Kontrollera synligheten av arbetsbladen**

Aspose.Cells för Python via .NET ger en klass, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/), som representerar en Microsoft Excel-fil. [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/)-klassen innehåller en [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/)-samling som gör det möjligt för utvecklare att få tillgång till varje arbetsblad i Excel-filen. Ett arbetsblad representeras av [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/)-klassen. [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/)-klassen ger en [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/)-samling som representerar alla celler i arbetsbladet. [**is_row_column_headers_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_row_column_headers_visible/)-samlingen erbjuder flera metoder för att hantera rader eller kolumner i ett arbetsblad. Några av dessa diskuteras nedan.

#### **Göra rad-/kolumnrubriker synliga**

Gör rad- och kolumnrubriker synliga genom att ställa in klass [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) egenskap [**is_row_column_headers_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_row_column_headers_visible/) till **true**.

#### **Gömma rad-/kolumnrubriker**

Dölj rad- och kolumnrubriker genom att ställa in klass [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) egenskap [**is_row_column_headers_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_row_column_headers_visible/) till **false**.

En komplett exempel nedan visar hur man använder [**is_row_column_headers_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_row_column_headers_visible/) egenskap genom att öppna en excel-fil (book1.xls), dölja rad- och kolumnrubrikerna på den första kalkylbladet och spara den modifierade filen som output.xls.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Views-Display-DisplayHideRowColumnHeaders-1.py" >}}

{{% alert color="primary" %}}

Det går även att använda [**unhide_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_rows) och [**unhide_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_columns) metoder av klassen [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) för att göra flera rader och kolumner synliga.

{{% /alert %}}
{{< app/cells/assistant language="python-net" >}}
