---
title: Inställning av marginaler
type: docs
weight: 20
url: /sv/net/setting-margins/
description: I den här artikeln kommer du att lära dig hur du ställer in marginalerna för ett Excel ark med hjälp av provkod. Du kommer också att lära dig hur du programmatically ställer in marginalerna för sidcentrum, sidhuvud och sidfotmarginaler i Sidlayout med hjälp av C# API eller .NET bibliotek.
keywords: ställ in excels ark med marginal till mitten c#, ställ in sidmarginaler för sidhuvud och sidfot c#
---

{{% alert color="primary" %}}

Aspose.Cells stödjer helt Microsoft Excels siduppställningsalternativ. Utvecklare kan behöva konfigurera siduppställningsinställningarna för kalkylblad för att kontrollera utskriftsprocessen. Det här avsnittet diskuterar hur man använder Aspose.Cells för att konfigurera sidmarginaler.

{{% /alert %}}

## **Ställa in marginaler**

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), som representerar en Excelfil. [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)-klassen innehåller [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)-samlingen som möjliggör åtkomst till varje arbetsblad i Excelfilen. Ett arbetsblad representeras av [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)-klassen.

[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)-klassen tillhandahåller egenskapen [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup) som används för att ställa in sidlayoutalternativen för ett arbetsblad. [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup)-attributet är ett objekt av [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup)-klassen som möjliggör för utvecklare att ställa in olika sidlayoutalternativ för ett utskrivet arbetsblad. [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup)-klassen tillhandahåller olika egenskaper och metoder som används för att ställa in sidlayoutalternativ.

### **Sidmarginaler**

Ställ in sidmarginaler (vänster, höger, över, under) med medlemmar i [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup)-klassen. Några av metoderna är listade nedan som används för att specificera sidmarginaler:

- [**LeftMargin**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/leftmargin)
- [**RightMargin**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/rightmargin)
- [**TopMargin**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/topmargin)
- [**BottomMargin**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/bottommargin)

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetMargins-1.cs" >}}

### **Centrera på sidan**

Det är möjligt att centrera någonting på en sida horisontellt och vertikalt. För detta finns det några användbara medlemmar i [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup)-klassen, [**CenterHorizontally**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/centerhorizontally) och [**CenterVertically**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/centervertically).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetMargins-CenterOnPage.cs" >}}

### **Sid- och fotmarginaler**

Ställ in sidhuvud- och sidfotmarginaler med medlemmar i [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup)-klassen som [**HeaderMargin**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/headermargin) och [**FooterMargin**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/footermargin).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetMargins-HeaderAndFooterMargins.cs" >}}
{{< app/cells/assistant language="csharp" >}}
