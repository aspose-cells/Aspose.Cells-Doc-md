---
title: Avancerade skyddsinställningar sedan Excel XP
type: docs
weight: 30
url: /sv/net/advanced-protection-settings-since-excel-xp/
---
{{% alert color="primary" %}}

Sedan lanseringen av Excel 2002 eller XP har Microsoft lagt till många avancerade skyddsinställningar.

{{% /alert %}}

## **Introduktion**

Dessa skyddsinställningar begränsar eller tillåter användare att:

- Ta bort rader eller kolumner.
- Redigera innehåll, objekt eller scenarier.
- Formatera celler, rader eller kolumner.
- Infoga rader, kolumner eller hyperlänkar.
- Välj låsta eller olåsta celler.
- Använd pivottabeller och mycket mer.

Aspose.Cells stöder alla avancerade skyddsinställningar som erbjuds av Excel XP eller senare versioner.

### **Avancerade skyddsinställningar med Excel XP och senare versioner**

Så här visar du skyddsinställningarna i Excel XP:

1.  Från**Verktyg** menyn, välj**Skydd** följd av**Skydda ark**. En dialogruta kommer att visas.

För att se skyddsinställningarna som är tillgängliga i Excel 2016

1.  Från**Fil** menyn, välj**Skydda arbetsbok** följd av**Skydda nuvarande ark**.
1.  Välj**Skydda ark** i**Recension** meny.

Om du följer stegen som nämns ovan visas en dialogruta där du kan tillåta eller begränsa kalkylbladsfunktioner eller tillämpa ett lösenord på kalkylbladet.

### **Avancerade skyddsinställningar med Aspose.Cells**

Aspose.Cells stöder alla avancerade skyddsinställningar.

 Aspose.Cells tillhandahåller en klass,[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , som representerar en Microsoft Excel-fil. De[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook) klass innehåller en[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) samling som ger åtkomst till varje kalkylblad i Excel-filen. Ett arbetsblad representeras av[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)klass.

 De[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klass ger[**Skydd**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection) egenskap som används för att tillämpa dessa avancerade skyddsinställningar. De[**Skydd**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection) egendom är i själva verket ett föremål för[**Skydd**](https://reference.aspose.com/cells/net/aspose.cells/protection)klass som kapslar in flera booleska egenskaper för att inaktivera eller aktivera begränsningar.

Nedan finns ett litet exempel på applikation. Den öppnar en Excel-fil och använder de flesta av de avancerade skyddsinställningarna som stöds av Excel XP och senare versioner.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-AdvancedProtectionSettings-1.cs" >}}

{{% alert color="primary" %}}

 Vänligen ring inte[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klass'[**Skydda**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/protect/index) metod när du använder[**Skydd**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection)fast egendom. Spara också filen i Excel97To2003- eller Xlsx-format eftersom de avancerade skyddsinställningarna endast stöds av Excel XP och senare versioner.

{{% /alert %}}

### **Cell Låsningsproblem**

Om du vill hindra användare från att redigera celler måste cellerna låsas innan några skyddsinställningar tillämpas. Annars kan cellerna redigeras även om kalkylbladet är skyddat. I Microsoft Excel XP kan celler låsas genom följande dialogruta:

|**Dialog för att låsa celler i Excel XP**|
|:- |
|![todo:image_alt_text](advanced-protection-settings-since-excel-xp_1.png)|

Det är möjligt att låsa celler med Aspose.Cells API också. Varje cell kan få[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style) formatering som innehåller en boolesk egenskap,[**Är låst**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked) . Ställ in[**Är låst**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked) egendom till**Sann** eller**falsk** för att låsa eller låsa upp cellen.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-LockCell-1.cs" >}}
