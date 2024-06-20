---
title: Visa och dölj rutnät och radkolumnhuvuden
type: docs
weight: 30
url: /sv/net/show-and-hide-gridlines-and-row-column-headers/
description: Den här artikeln tillhandahåller exempelkod för att använda C# API eller .NET Library för att programmatiskt dölja eller visa rutnät, rad och kolumnhuvuden i ett Excel kalkylblad.
---

{{% alert color="primary" %}}

Aspose.Cells stödjer döljning och visning av kalkylbladets rutnät som är synliga som standard. Den ger också kontroll över synligheten av radkolumnhuvuden på kalkylbladet.

{{% /alert %}}

## **Visa och dölj rutnät**

Alla Excel-kalkylblad har rutnät som standard. De hjälper till att avgränsa celler så att det är lätt att ange data i specifika celler. Rutnät gör det möjligt för oss att se ett kalkylblad som en samling av celler, där varje cell är lätt identifierbar.

### **Kontrollera synligheten av rutnäten**

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), som representerar en Microsoft Excel-fil. [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)klassen innehåller en [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)samling som tillåter utvecklare att komma åt varje kalkylblad i Excel-filen. Ett kalkylbla representeras av [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)klassen. [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)klassen ger ett brett utbud av egenskaper och metoder för att hantera ett kalkylblad. För att kontrollera synligheten av rutnätet, använd [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)klassens [**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible)egenskap. [**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible)är en boolean-egenskap, vilket betyder att den endast kan lagra ett **true** eller **false**-värde.

#### **Gör rutnätslinjer synliga**

Gör rutnätet synligt genom att ange [**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible)egenskapen för klassen [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) till **true**.

#### **Gömmer rutnätslinjer**

Dölj rutnätet genom att ange [**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible)egenskapen för klassen [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) till **false**.

Ett komplett exempel ges nedan som visar användningen av [**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible)egenskapen genom att öppna en Excelfil (book1.xls), dölja rutnätet på det första kalkylarket och spara den modifierade filen som output.xls.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-DisplayHideGridlines-1.cs" >}}

## **Visa och dölj radkolumnhuvuden**

Alla kalkylblad i en Excel-fil består av celler som är ordnade i rader och kolumner. Alla rader och kolumner har unika värden som används för att identifiera dem och individuella celler. Till exempel har rader nummer - 1, 2, 3, 4, osv.- och kolumner är ordnade alfabetiskt - A, B, C, D, osv. Rad- och kolumnvärdena visas i huvudena. Med Aspose.Cells kan utvecklare kontrollera synligheten av dessa rad- och kolumnhuvuden.

### **Kontrollera synligheten av arbetsbladen**

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), som representerar en Microsoft Excel-fil. [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)klassen innehåller en [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)samling som tillåter utvecklare att komma åt varje kalkylblad i Excel-filen. Ett kalkylbla representeras av [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)klassen. [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)klassen ger ett brett utbud av egenskaper och metoder för att hantera ett kalkylblad. För att kontrollera synligheten av rad- och kolumnhuvuden, använd [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)klassens [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible)egenskap. [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible)är en boolean-egenskap, vilket betyder att den endast kan lagra ett **true** eller **false** värde.

#### **Göra rad-/kolumnrubriker synliga**

Gör rad- och kolumnrubriker synliga genom att ställa in klass [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) egenskap [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) till **true**.

#### **Gömma rad-/kolumnrubriker**

Dölj rad- och kolumnrubriker genom att ställa in klass [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) egenskap [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) till **false**.

En komplett exempel nedan visar hur man använder [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) egenskap genom att öppna en excel-fil (book1.xls), dölja rad- och kolumnrubrikerna på den första kalkylbladet och spara den modifierade filen som output.xls.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-DisplayHideRowColumnHeaders-1.cs" >}}

{{% alert color="primary" %}}

Det går även att använda [**UnhideRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhiderows) och [**UnhideColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhidecolumns) metoder av klassen [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) för att göra flera rader och kolumner synliga.

{{% /alert %}}
