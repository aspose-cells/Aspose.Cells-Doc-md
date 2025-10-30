---
title: Hantera sidbrytningar
type: docs
weight: 30
url: /sv/python-net/managing-page-breaks/
description: Denna artikel innehåller exempel på kod och förklarar hur man lägger till sidbrytningar, rensar sidbrytningar eller tar bort specifika sidbrytningar i Excel ark programmässigt med Aspose.Cells för Python via .NET API er.
keywords: Python Excel bibliotek, Python sidbrytningar, Excel sidbrytningar i Python, rensa sidbrytning i Python.
---

{{% alert color="primary" %}}

Enligt definitionen är en sidbrytning en plats i en textflöde där en sida slutar och den nästa börjar. Microsoft Excel låter användare lägga till sidbrytningar i valfri markerad cell i ett kalkylblad.

Platsen för cellen där sidbrytningen läggs till, slutet av sidan och resten av data efter sidbrytningen skrivs ut på nästa sida vid utskrift. Enkelt uttryckt delar sidbrytningar ditt kalkylblad i flera sidor enligt dina inställningar. Du kan också lägga till sidbrytningar i dina kalkylblad vid körning med Aspose.Cells för Python via .NET. Aspose.Cells för Python via .NET tillåter utvecklare att lägga till två typer av sidbrytningar:

- Horisontell sidbrytning
- Vertikal sidbrytning

I resten av diskussionen beskriver vi hur du kan lägga till horisontella eller vertikala sidbrytningar i dina kalkylblad med Aspose.Cells för Python via .NET.

{{% /alert %}}

## **Sidbrytningar**

Aspose.Cells för Python via .NET tillhandahåller en [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)-klass som representerar en Excel-fil. [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)-klassen innehåller en [**Worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets)-samling som ger åtkomst till varje ark i Excel-filen.

Ett kalkylblad representeras av [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)-klassen. [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)-klassen tillhandahåller ett brett utbud av egenskaper och metoder som används för att hantera ett kalkylblad.

Använd [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)-klassens [**horizontal_page_breaks**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/horizontal_page_breaks) och [**vertical_page_breaks**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/vertical_page_breaks) egenskaper för att lägga till sidbrytningar.

Egenskaperna [**horizontal_page_breaks**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/horizontal_page_breaks) och [**vertical_page_breaks**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/vertical_page_breaks) är samlingar som kan innehålla flera sidbrytningar. Varje samling innehåller flera metoder för att hantera horisontella och vertikala sidbrytningar.

## **Hur man lägger till sidbrytningar**

För att lägga till en sidbrytning i ett arbetsblad, infoga vertikala och horisontella sidbrytningar vid den angivna cellen genom att anropa [**HorizontalPageBreakCollection.add()**](https://reference.aspose.com/cells/python-net/aspose.cells/horizontalpagebreakcollection/add/#str)- och [**VerticalPageBreakCollection.add()**](https://reference.aspose.com/cells/python-net/aspose.cells/verticalpagebreakcollection/add/#str)-metoderna. Varje **add**-metod tar namnet på cellen där brytningen ska läggas till.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Value-AddingPageBreaks-1.py" >}}

{{% alert color="primary" %}}

I sidbrytning förhandsgranskning eller utskriftsförhandsgranskning kan du se hur dessa sidbrytningar fungerar.

{{% /alert %}}


## **Viktig information att veta**

När du ställer in {0}-egenskaper (det vill säga {1} och {2}) i siduppsättningsinställningarna påverkas sidbrytningsinställningarna, så om du skriver ut kalkylbladet beaktas inte sidbrytningsinställningarna även om de fortfarande är inställda.
{{< app/cells/assistant language="python-net" >}}
