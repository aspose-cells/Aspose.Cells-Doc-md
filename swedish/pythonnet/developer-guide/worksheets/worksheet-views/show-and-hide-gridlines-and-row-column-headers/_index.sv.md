---
title: Visa och dölj rutnät och radkolumnhuvuden
type: docs
weight: 30
url: /sv/python-net/show-and-hide-gridlines-and-row-column-headers/
description: Denna artikel ger provkod för att använda Aspose.Cells för Python via .NET API för att programmatiskt dölja eller visa rutnätslinjer, rad och kolumnrubriker för en Excel ark.
keywords: Python Excel Library, Python Visa och Dölj Rutnätslinjer, Hur man Visa och Döljer Rad och Kolumnrubriker i Python, Hur man Visa och Döljer Rutnätslinjer och Rad och Kolumnrubriker i Python.
---

{{% alert color="primary" %}}

Aspose.Cells för Python via .NET stödjer dölja och visa Rutnätslinjer för kalkylbladet som är synliga som standard. Den ger också kontroll över synligheten av Rad- och Kolumnrubriker för kalkylbladet.

{{% /alert %}}

## **Visa och dölj rutnät**

Alla Excel-kalkylblad har rutnät som standard. De hjälper till att avgränsa celler så att det är lätt att ange data i specifika celler. Rutnät gör det möjligt för oss att se ett kalkylblad som en samling av celler, där varje cell är lätt identifierbar.

### **Kontrollera synligheten av rutnäten**

Aspose.Cells för Python via .NET ger ett klass, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/), som representerar en Microsoft Excel-fil. Klassen [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/) innehåller en [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/) samling som tillåter utvecklare att komma åt varje arbetsblad i Excel-filen. Ett arbetsblad representeras av klassen [**Worksheet**](https://reference.aspose.com/cells/python-et/aspose.cells/worksheet/). Klassen [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/) tillhandahåller ett brett utbud av egenskaper och metoder för att hantera ett arbetsblad. För att kontrollera synligheten av rutnätslinjer, använd klassen [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/) egenskap [**is_gridlines_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_gridlines_visible/). [**is_gridlines_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_gridlines_visible/) är en boolesk egenskap, vilket innebär att den bara kan spara ett **true** eller **false** värde.

#### **Gör rutnätslinjer synliga**

Gör rutnätet synligt genom att ange [**is_gridlines_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_gridlines_visible/)egenskapen för klassen [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) till **true**.

#### **Gömmer rutnätslinjer**

Dölj rutnätet genom att ange [**is_gridlines_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_gridlines_visible/)egenskapen för klassen [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) till **false**.

Ett komplett exempel ges nedan som visar användningen av [**is_gridlines_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_gridlines_visible/)egenskapen genom att öppna en Excelfil (book1.xls), dölja rutnätet på det första kalkylarket och spara den modifierade filen som output.xls.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Views-Display-DisplayHideGridlines-1.py" >}}

## **Visa och dölj radkolumnhuvuden**

Alla arbetsblad i en Excel-fil består av celler som är ordnade i rader och kolumner. Alla rader och kolumner har unika värden som används för att identifiera dem och individuella celler. Till exempel är rader numrerade - 1, 2, 3, 4, osv. - och kolumner är ordnade alfabetiskt - A, B, C, D, osv. Rad- och kolumnvärdena visas i rubrikerna. Med hjälp av Aspose.Cells för Python via .NET kan utvecklare kontrollera synligheten av dessa rad- och kolumnrubriker.

### **Kontrollera synligheten av arbetsbladen**

Aspose.Cells för Python via .NET ger ett klass, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/), som representerar en Microsoft Excel-fil. Klassen [**Workbook**](https://reference.aspose.com/cells/pytho-net/aspose.cells/workbook/) innehåller en [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/) samling som tillåter utvecklare att komma åt varje arbetsblad i Excel-filen. Ett arbetsblad representeras av klassen [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/). Klassen [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/) tillhandahåller ett brett utbud av egenskaper och metoder för att hantera ett arbetsblad. För att kontrollera synligheten av rad- och kolumnrubriker, använd klassen [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/) egenskap [**is_row_column_headers_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_row_column_headers_visible/). [**is_row_column_headers_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_row_column_headers_visible/) är en boolesk egenskap, vilket innebär att den bara kan spara ett **true** eller **false** värde.

#### **Göra rad-/kolumnrubriker synliga**

Gör rad- och kolumnrubriker synliga genom att ställa in klass [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) egenskap [**is_row_column_headers_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_row_column_headers_visible/) till **true**.

#### **Gömma rad-/kolumnrubriker**

Dölj rad- och kolumnrubriker genom att ställa in klass [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) egenskap [**is_row_column_headers_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_row_column_headers_visible/) till **false**.

En komplett exempel nedan visar hur man använder [**is_row_column_headers_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_row_column_headers_visible/) egenskap genom att öppna en excel-fil (book1.xls), dölja rad- och kolumnrubrikerna på den första kalkylbladet och spara den modifierade filen som output.xls.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Views-Display-DisplayHideRowColumnHeaders-1.py" >}}

{{% alert color="primary" %}}

Det går även att använda [**unhide_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_rows) och [**unhide_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_columns) metoder av klassen [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) för att göra flera rader och kolumner synliga.

{{% /alert %}}
