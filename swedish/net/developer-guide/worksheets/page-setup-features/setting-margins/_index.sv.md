---
title: Ställa in marginaler
type: docs
weight: 20
url: /sv/net/setting-margins/
description: I den här artikeln kommer du att lära dig hur du ställer in marginalerna för ett Excel-kalkylblad med hjälp av exempelkod. Du kommer också att lära dig hur du programmässigt ställer in marginalerna för sidcentret, sidhuvudet och sidfotsmarginalerna för sidinställningar med hjälp av C# API eller .NET bibliotek.
keywords: set excel worksheet margin to center c#, set worksheet header and footer margin c#
---
{{% alert color="primary" %}}

Aspose.Cells stöder fullt ut Microsoft Excels sidinställningar. Utvecklare kan behöva konfigurera sidinställningar för kalkylblad för att styra utskriftsprocessen. Det här ämnet diskuterar hur man använder Aspose.Cells för att konfigurera sidmarginaler.

{{% /alert %}}

##  **Ställa in marginaler**

 Aspose.Cells tillhandahåller en klass,[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , som representerar en Excel-fil. De[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook) klass innehåller[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) samling som ger åtkomst till varje kalkylblad i Excel-filen. Ett arbetsblad representeras av[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)klass.

 De[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klass ger[**Utskriftsformat**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup) egenskap som används för att ställa in sidinställningar för ett kalkylblad. De[**Utskriftsformat**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup) attribut är ett objekt för[**Utskriftsformat**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup) klass som gör det möjligt för utvecklare att ställa in olika sidlayoutalternativ för ett utskrivet kalkylblad. De[**Utskriftsformat**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup)klass tillhandahåller olika egenskaper och metoder som används för att ställa in sidinställningar.

###  **Sidmarginaler**

 Ställ in sidmarginaler (vänster, höger, topp, botten) med[**Utskriftsformat**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup)klassmedlemmar. Nedan listas några av metoderna som används för att ange sidmarginaler:

- [**Vänster marginal**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/leftmargin)
- [**Högermarginal**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/rightmargin)
- [**TopMargin**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/topmargin)
- [**Bottenmarginal**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/bottommargin)

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetMargins-1.cs" >}}

###  **Centrera på sidan**

 Det är möjligt att centrera något på en sida horisontellt och vertikalt. För detta finns det några användbara medlemmar av[**Utskriftsformat**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup) klass,[**Center Horisontellt**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/centerhorizontally) och[**Centrera Vertikalt**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/centervertically).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetMargins-CenterOnPage.cs" >}}

###  **Marginaler för sidhuvud och sidfot**

 Ställ in sidhuvuds- och sidfotsmarginaler med[**Utskriftsformat**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup) klassmedlemmar som t.ex[**HeaderMargin**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/headermargin) och[**FooterMargin**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/footermargin).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetMargins-HeaderAndFooterMargins.cs" >}}
