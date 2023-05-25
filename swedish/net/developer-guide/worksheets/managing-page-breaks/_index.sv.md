---
title: Hantera sidbrytningar
type: docs
weight: 30
url: /sv/net/managing-page-breaks/
description: Den här artikeln innehåller exempelkod och förklarar hur du lägger till sidbrytningar, rensar sidbrytningar eller tar bort specifika sidbrytningar i Excel-kalkylblad programmatiskt med hjälp av biblioteket C# API eller .NET.
keywords: page breaks c#, excel page breaks c#, clear page break c#, delete specific page break c#
---
{{% alert color="primary" %}}

Enligt definitionen är en sidbrytning en plats i ett textflöde där en sida slutar och nästa börjar. Microsoft Excel låter användare lägga till sidbrytningar i valfri vald cell i ett kalkylblad.

Platsen för cellen där sidbrytningen läggs till, sidan avslutas och resten av data efter sidbrytningen skrivs ut på nästa sida under utskrift. Med enkla ord delar sidbrytningar upp ditt kalkylblad i flera sidor enligt dina specifikationer. Du kan också lägga till sidbrytningar till dina kalkylblad under körning med Aspose.Cells. Aspose.Cells tillåter utvecklare att lägga till två typer av sidbrytningar:

- Horisontell sidbrytning
- Vertikal sidbrytning

I resten av diskussionen kommer vi att beskriva hur du kan lägga till horisontella eller vertikala sidbrytningar i dina kalkylblad med Aspose.Cells.

{{% /alert %}}

##  **Sidbrytningar**

Aspose.Cells tillhandahåller en[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook) klass som representerar en Excel-fil. De[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook) klass innehåller en[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)samling som ger åtkomst till varje kalkylblad i Excel-filen.

 Ett arbetsblad representeras av[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klass. De[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)klass tillhandahåller ett brett utbud av egenskaper och metoder som används för att hantera ett kalkylblad.

För att lägga till sidbrytningar, använd[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klass'[**HorizontalPageBreaks**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/horizontalpagebreaks) och[**VerticalPageBreaks**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/verticalpagebreaks)egenskaper.

 De[**HorizontalPageBreaks**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/horizontalpagebreaks) och[**VerticalPageBreaks**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/verticalpagebreaks)egenskaper är samlingar som kan innehålla flera sidbrytningar. Varje samling innehåller flera metoder för att hantera horisontella och vertikala sidbrytningar.

###  **Lägga till sidbrytningar**

 För att lägga till en sidbrytning i ett kalkylblad, infoga vertikala och horisontella sidbrytningar i den angivna cellen genom att anropa[**HorizontalPageBreakCollection.Add()**](https://reference.aspose.com/cells/net/aspose.cells/horizontalpagebreakcollection/methods/add/index) och[**VerticalPageBreakCollection.Add()**](https://reference.aspose.com/cells/net/aspose.cells/verticalpagebreakcollection/methods/add/index) metoder. Varje**Lägg till** metoden tar namnet på cellen där brytningen ska läggas till.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-AddingPageBreaks-1.cs" >}}

{{% alert color="primary" %}}

I lägena för förhandsgranskning av sidbrytningar eller förhandsgranskning av utskrifter kan du se hur dessa sidbrytningar fungerar.

{{% /alert %}}

###  **Rensa alla sidbrytningar**

 För att rensa alla sidbrytningar i ett kalkylblad, anropa[**HorizontalPageBreakCollection**](https://reference.aspose.com/cells/net/aspose.cells/horizontalpagebreakcollection) och[**VerticalPageBreakCollection**](https://reference.aspose.com/cells/net/aspose.cells/verticalpagebreakcollection) samlingar'[**Clear()**](https://docs.microsoft.com/en-us/dotnet/api/system.collections.collectionbase.clear?redirectedfrom=MSDN&view=netframework-4.7.2#System_Collections_CollectionBase_Clear)metoder.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-ClearAllPageBreaks-1.cs" >}}

###  **Ta bort specifik sidbrytning**

 För att ta bort en specifik sidbrytning, ring till[**HorizontalPageBreakCollection.RemoveAt()**](https://reference.aspose.com/cells/net/aspose.cells/horizontalpagebreakcollection/methods/removeat) och[**VerticalPageBreakCollection.RemoveAt()**](https://reference.aspose.com/cells/net/aspose.cells/verticalpagebreakcollection/methods/removeat) metoder. Varje**Ta bortAt**metoden tar indexet för sidbrytningen på väg att tas bort.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-RemoveSpecificPageBreak-1.cs" >}}

##  **Viktigt att veta**

 När du ställer in**FitToPages** egenskaper (det vill säga[**FitToPagesTall**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopagestall) och[**FitToPagesWide**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopageswide)) i sidinställningarna påverkas sidbrytningsinställningarna, så om du skriver ut kalkylbladet beaktas inte sidbrytningsinställningarna även om de fortfarande är inställda.
