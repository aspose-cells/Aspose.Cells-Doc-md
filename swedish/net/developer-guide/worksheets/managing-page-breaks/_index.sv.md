---
title: Hantera sidbrytningar
type: docs
weight: 30
url: /sv/net/managing-page-breaks/
description: Den här artikeln tillhandahåller exempelkod och förklarar hur man lägger till sidbrytningar, raderar sidbrytningar eller tar bort specifika sidbrytningar i Excel ark programmatiskt med C# API eller .NET bibliotek.
keywords: sidbrytningar c#, excel sidbrytningar c#, rensa sidbrytning c#, ta bort specifik sidbrytning c#
---

{{% alert color="primary" %}}

Enligt definitionen är en sidbrytning en plats i en textflöde där en sida slutar och den nästa börjar. Microsoft Excel låter användare lägga till sidbrytningar i valfri markerad cell i ett kalkylblad.

Placeringen av cellen där sidbrytningen läggs till, sidan avslutas och resten av datan efter sidbrytningen skrivs ut på nästa sida under utskrift. Med andra ord delar sidbrytningar ditt kalkylblad i flera sidor enligt dina specifikationer. Du kan också lägga till sidbrytningar i dina kalkylblad vid runtime med hjälp av Aspose.Cells. Aspose.Cells tillåter utvecklare att lägga till två typer av sidbrytningar:

- Horisontell sidbrytning
- Vertikal sidbrytning

I resten av diskussionen kommer vi att beskriva hur du kan lägga till horisontella eller vertikala sidbrytningar i dina kalkylblad med hjälp av Aspose.Cells.

{{% /alert %}}

## **Sidbrytningar**

Aspose.Cells tillhandahåller en [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)-klass som representerar en Excel-fil. [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)-klassen innehåller en [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)-samling som möjliggör åtkomst till varje kalkylblad i Excel-filen.

Ett kalkylblad representeras av [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)-klassen. [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)-klassen tillhandahåller ett brett utbud av egenskaper och metoder som används för att hantera ett kalkylblad.

Använd [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)-klassens [**HorizontalPageBreaks**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/horizontalpagebreaks) och [**VerticalPageBreaks**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/verticalpagebreaks) egenskaper för att lägga till sidbrytningar.

Egenskaperna [**HorizontalPageBreaks**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/horizontalpagebreaks) och [**VerticalPageBreaks**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/verticalpagebreaks) är samlingar som kan innehålla flera sidbrytningar. Varje samling innehåller flera metoder för att hantera horisontella och vertikala sidbrytningar.

### **Lägga till sidbrytningar**

För att lägga till en sidbrytning i ett kalkylblad, sätt in vertikala och horisontella sidbrytningar vid den angivna cellen genom att anropa metoderna [**HorizontalPageBreakCollection.Add()**](https://reference.aspose.com/cells/net/aspose.cells/horizontalpagebreakcollection/methods/add/index) och [**VerticalPageBreakCollection.Add()**](https://reference.aspose.com/cells/net/aspose.cells/verticalpagebreakcollection/methods/add/index). Varje **Lägg till** -metod tar namnet på cellen där brytet ska läggas till.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-AddingPageBreaks-1.cs" >}}

{{% alert color="primary" %}}

I sidbrytning förhandsgranskning eller utskriftsförhandsgranskning kan du se hur dessa sidbrytningar fungerar.

{{% /alert %}}

### **Rensa alla sidbrytningar**

För att rensa alla sidbrytningar i ett kalkylblad, anropa [**HorizontalPageBreakCollection**](https://reference.aspose.com/cells/net/aspose.cells/horizontalpagebreakcollection) och [**VerticalPageBreakCollection**](https://reference.aspose.com/cells/net/aspose.cells/verticalpagebreakcollection) samlingarnas [**Clear()**](https://docs.microsoft.com/en-us/dotnet/api/system.collections.collectionbase.clear?redirectedfrom=MSDN&view=netframework-4.7.2#System_Collections_CollectionBase_Clear)-metoder.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-ClearAllPageBreaks-1.cs" >}}

### **Ta bort en specifik sidbrytning**

För att ta bort en specifik sidbrytning, anropa metoderna [**HorizontalPageBreakCollection.RemoveAt()**](https://reference.aspose.com/cells/net/aspose.cells/horizontalpagebreakcollection/methods/removeat) och [**VerticalPageBreakCollection.RemoveAt()**](https://reference.aspose.com/cells/net/aspose.cells/verticalpagebreakcollection/methods/removeat). Varje **Ta bort vid** -metod tar index för sidbrytningen som ska tas bort.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-RemoveSpecificPageBreak-1.cs" >}}

## **Viktig information att veta**

När du ställer in {0}-egenskaper (det vill säga {1} och {2}) i siduppsättningsinställningarna påverkas sidbrytningsinställningarna, så om du skriver ut kalkylbladet beaktas inte sidbrytningsinställningarna även om de fortfarande är inställda.
