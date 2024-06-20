---
title: Hitta eller söka data
type: docs
weight: 50
url: /sv/net/find-or-search-data/
description: Lär dig hur man hittar eller söker celler i ett kalkylark som innehåller specificerade data genom Aspose.Cells for .NET API.
keywords: Hitta data, Sök data, Hitta celler som innehåller en formel, Sök celler som innehåller en formel, Hitta data eller formler med hjälp av FindOptions, Sök data eller formler med hjälp av FindOptions, Hitta eller sök celler som innehåller specificerat strängvärde eller nummer, Hitta eller sök celler som innehåller specificerad data
---

{{% alert color="primary" %}}

Microsoft Excel tillåter användare att hitta celler i ett kalkylblad som innehåller specificerade data.

{{% /alert %}}

## **Att hitta celler som innehåller specificerad data**

### **Använda Microsoft Excel**

Microsoft Excel tillåter användare att hitta celler i ett kalkylark som innehåller specificerade data. Om du väljer **Redigera** från **Sök**-menyn i Microsoft Excel kommer du att se en dialog där du kan specificera sökvärdet.

Här letar vi efter värdet "Apelsiner". Aspose.Cells tillåter också utvecklare att hitta celler i kalkylarket som innehåller specificerade värden.

### **Använda Aspose.Cells**

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), som representerar en Microsoft Excel-fil. [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)-klassen innehåller en [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)-samling som ger åtkomst till varje kalkylblad i Excel-filen. Ett kalkylblad representeras av [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)-klassen. [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)-klassen tillhandahåller en [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)-samling som representerar alla celler i kalkylarket. [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)-samlingen tillhandahåller flera metoder för att hitta celler i ett kalkylark som innehåller användarspecificerad data. Några av dessa metoder diskuteras nedan mer i detalj.

{{% alert color="primary" %}}

Alla Find-metoder returnerar referenser till celler som innehåller den specificerade datan att söka.

{{% /alert %}}

## **Att hitta celler som innehåller en formel**

Utvecklare kan hitta en specificerad formel i kalkylarket genom att anropa [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)-samlingens [**Find**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index)-metod. Vanligtvis accepterar [**Find**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index)-metoden tre parametrar:

- **Objekt:** Data att söka efter. Typen ska vara int, double, DateTime, string, bool.
- **Föregående cell:** Föregående cell med samma objekt. Denna parameter kan vara inställd på null om sökningen görs från början.
- FindOptions: Alternativ för att hitta den erforderliga datan.

Nedan används exempel på kalkylarksdata för att öva på hittametoder.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Find-FindingCellsContainingFormula-1.cs" >}}

## **Hitta data eller formler med FindOptions**

Det är möjligt att hitta angivna värden med hjälp av [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) kollektionens [**Find**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index) metod med olika [**FindOptions**](https://reference.aspose.com/cells/net/aspose.cells/findoptions). Vanligtvis accepterar [**Find**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index) metoden följande parametrar:

- **Sökvärde**, data eller värde som ska sökas efter.
- **Föregående cell**, den sista cellen som innehöll samma värde. Denna parameter kan ställas in till null när du söker från början.
- **Hitta alternativ**, hitta alternativ.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Find-FindingDataOrFormulasUsingFindOptions-1.cs" >}}

## **Hitta celler som innehåller specifierade strängvärden eller nummer**

Det är möjligt att hitta angivna strängvärden genom att anropa samma [**Find**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index) metod som finns i [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) kollektion med olika [**FindOptions**](https://reference.aspose.com/cells/net/aspose.cells/findoptions).

Ange [**FindOptions.LookInType**](https://reference.aspose.com/cells/net/aspose.cells/findoptions/properties/lookintype) och [**FindOptions.LookAtType**](https://reference.aspose.com/cells/net/aspose.cells/findoptions/properties/lookattype) egenskaperna. Följande exempelkod illustrerar hur man använder dessa egenskaper för att hitta celler med olika antal strängar i **början** eller i **mitten** eller i **änden** av cellens sträng.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Find-FindingCellsContainingStringValueOrNumber-1.cs" >}}

## **Fortsatta ämnen**
- [Hitta celler med specifik stil](/cells/sv/net/find-cells-with-specific-style/)
- [Ta reda på om cellvärdet börjar med citattecken](/cells/sv/net/find-if-the-cell-value-starts-with-single-quote-mark/)
- [Sök data med originalvärden](/cells/sv/net/search-data-using-original-values/)
