---
title: Hitta eller sök data
type: docs
weight: 50
url: /sv/net/find-or-search-data/
---
{{% alert color="primary" %}}

Microsoft Excel tillåter användare att hitta celler i ett kalkylblad som innehåller specificerade data.

{{% /alert %}}

## **Hitta Cells Innehåller specificerade data**

### **Använder Microsoft Excel**

 Microsoft Excel tillåter användare att hitta celler i ett kalkylblad som innehåller specificerade data. Om du väljer**Redigera** från**Hitta** menyn i Microsoft Excel kommer du att se en dialogruta där du kan ange sökvärdet.

Här letar vi efter värdet "Apelsiner". Aspose.Cells tillåter också utvecklare att hitta celler i kalkylbladet som innehåller specificerade värden.

### **Använder Aspose.Cells**

 Aspose.Cells tillhandahåller en klass,[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , som representerar en Microsoft Excel-fil. De[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook) klass innehåller en[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) samling som ger åtkomst till varje kalkylblad i Excel-filen. Ett arbetsblad representeras av[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klass. De[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klass ger en[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)samling som representerar alla celler i kalkylbladet. De[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)samling tillhandahåller flera metoder för att hitta celler i ett kalkylblad som innehåller användarspecificerad data. Några av dessa metoder diskuteras mer i detalj nedan.

{{% alert color="primary" %}}

Alla sökmetoder returnerar referenserna till cellerna som innehåller den angivna informationen för sökning.

{{% /alert %}}

## **Hitta Cells som innehåller en formel**

 Utvecklare kan hitta en specificerad formel i kalkylbladet genom att anropa[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) samlingens[**Hitta**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index) metod. Vanligtvis är[**Hitta**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index)Metoden accepterar tre parametrar:

- **Objekt:**Objektet att söka efter. Typen ska vara int,double,DateTime,string,bool.
- **Föregående cell:**Föregående cell med samma objekt. Denna parameter kan ställas in på null om du söker från början.
- FindOptions: Alternativ för att hitta det önskade objektet.

I exemplen nedan används kalkylbladsdata för att öva på att hitta metoder:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Find-FindingCellsContainingFormula-1.cs" >}}

## **Hitta data eller formler med FindOptions**

 Det är möjligt att hitta specificerade värden med hjälp av[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) samlingens[**Hitta**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index) metod med olika[**Hitta Alternativ**](https://reference.aspose.com/cells/net/aspose.cells/findoptions) . Vanligtvis är[**Hitta**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index)metoden accepterar följande parametrar:

- **Sökvärde**data eller värde som ska sökas efter.
- **Föregående cell**, den sista cellen som innehöll samma värde. Denna parameter kan ställas in på null när du söker från början.
- **Hitta alternativ**, sökalternativen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Find-FindingDataOrFormulasUsingFindOptions-1.cs" >}}

## **Hitta Cells som innehåller specificerat strängvärde eller nummer**

 Det är möjligt att hitta specificerade strängvärden genom att anropa detsamma[**Hitta**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index) metod som finns i[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) samling med olika[**Hitta Alternativ**](https://reference.aspose.com/cells/net/aspose.cells/findoptions).

 Specificera[**FindOptions.LookInType**](https://reference.aspose.com/cells/net/aspose.cells/findoptions/properties/lookintype) och[**FindOptions.LookAtType**](https://reference.aspose.com/cells/net/aspose.cells/findoptions/properties/lookattype) egenskaper. Följande exempelkod illustrerar hur man använder dessa egenskaper för att hitta celler med olika antal strängar vid**början** eller vid**Centrum** eller vid**slutet** av cellens sträng.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Find-FindingCellsContainingStringValueOrNumber-1.cs" >}}

## **Förhandsämnen**
- [Hitta Cells med specifik stil](/cells/sv/net/find-cells-with-specific-style/)
- [Ta reda på om cellvärdet börjar med ett citattecken](/cells/sv/net/find-if-the-cell-value-starts-with-single-quote-mark/)
- [Sök efter data med originalvärden](/cells/sv/net/search-data-using-original-values/)
