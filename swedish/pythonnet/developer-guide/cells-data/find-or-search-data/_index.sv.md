---
title: Hitta eller söka data
type: docs
weight: 50
url: /sv/python-net/find-or-search-data/
description: Lär dig hur du hittar eller söker celler i ett kalkylblad som innehåller specificerad data genom Aspose.Cells för Python via .NET API.
keywords: Python Excel bibliotek, Sök efter data med Python, Sök efter celler som innehåller en formel med Python, Sök efter celler som innehåller en formel med Python, Hitta data eller formler med hjälp av FindOptions i Python, Sök efter data eller formler med hjälp av FindOptions i Python, Hitta eller sök efter celler som innehåller specificerat strängvärde eller nummer med Python, Hitta eller sök efter celler som innehåller specificerad data
---

{{% alert color="primary" %}}

Microsoft Excel tillåter användare att hitta celler i ett kalkylblad som innehåller specificerade data.

{{% /alert %}}

## **Att hitta celler som innehåller specificerad data**

### **Använda Microsoft Excel**

Microsoft Excel tillåter användare att hitta celler i ett kalkylark som innehåller specificerade data. Om du väljer **Redigera** från **Sök**-menyn i Microsoft Excel kommer du att se en dialog där du kan specificera sökvärdet.

Här letar vi efter värdet "Apelsiner". Aspose.Cells tillåter också utvecklare att hitta celler i kalkylarket som innehåller specificerade värden.

### **Använda Aspose.Cells**

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), som representerar en Microsoft Excel-fil. [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)-klassen innehåller en [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets)-samling som ger åtkomst till varje kalkylblad i Excel-filen. Ett kalkylblad representeras av [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)-klassen. [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)-klassen tillhandahåller en [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells)-samling som representerar alla celler i kalkylarket. [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells)-samlingen tillhandahåller flera metoder för att hitta celler i ett kalkylark som innehåller användarspecificerad data. Några av dessa metoder diskuteras nedan mer i detalj.

{{% alert color="primary" %}}

Alla Find-metoder returnerar referenser till celler som innehåller den specificerade datan att söka.

{{% /alert %}}

## **Att hitta celler som innehåller en formel**

Utvecklare kan hitta en specificerad formel i kalkylarket genom att anropa [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells)-samlingens [**find**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/find/#any-aspose.cells.Cell-aspose.cells.FindOptions)-metod. Vanligtvis accepterar [**find**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/find/#any-aspose.cells.Cell-aspose.cells.FindOptions)-metoden tre parametrar:

- **vad:** Objektet att söka efter. Typen ska vara int,double, DateTime, string, bool.
- **föregående_cell:** Föregående cell med samma objekt. Denna parameter kan vara inställd på null om sökning från början.
- **find_options:** Alternativ för att hitta det nödvändiga objektet.

Nedan används exempel på kalkylarksdata för att öva på hittametoder.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FindingCellsContainingFormula-1.py" >}}

## **Hitta data eller formler med FindOptions**

Det är möjligt att hitta angivna värden med hjälp av [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) kollektionens [**find**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/find/#any-aspose.cells.Cell-aspose.cells.FindOptions) metod med olika [**FindOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/findoptions). Vanligtvis accepterar [**find**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/find/#any-aspose.cells.Cell-aspose.cells.FindOptions) metoden följande parametrar:

- **vad:**, datan eller värdet som ska sökas efter.
- **föregående_cell**, den senaste cellen som innehöll samma värde. Denna parameter kan vara inställd på null när du söker från början.
- **find_options**, hitta alternativ.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FindingDataOrFormulasUsingFindOptions-1.py" >}}

## **Hitta celler som innehåller specifierade strängvärden eller nummer**

Det är möjligt att hitta angivna strängvärden genom att anropa samma [**find**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/find/#any-aspose.cells.Cell-aspose.cells.FindOptions) metod som finns i [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) kollektion med olika [**FindOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/findoptions).

Ange [**FindOptions.look_in_type**](https://reference.aspose.com/cells/python-net/aspose.cells/findoptions/look_in_type/) och [**FindOptions.look_at_type**](https://reference.aspose.com/cells/python-net/aspose.cells/findoptions/look_at_type/) egenskaperna. Följande exempelkod illustrerar hur man använder dessa egenskaper för att hitta celler med olika antal strängar i **början** eller i **mitten** eller i **änden** av cellens sträng.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FindingCellsContainingStringValueOrNumber-1.py" >}}

## **Fortsatta ämnen**
- [Hitta celler med specifik stil](/cells/sv/python-net/find-cells-with-specific-style/)
- [Ta reda på om cellvärdet börjar med citattecken](/cells/sv/python-net/find-if-the-cell-value-starts-with-single-quote-mark/)
- [Sök data med originalvärden](/cells/sv/python-net/search-data-using-original-values/)
{{< app/cells/assistant language="python-net" >}}
