---
title: Inställning av marginaler
type: docs
weight: 20
url: /sv/python-net/setting-margins/
description: I denna artikel lär du dig hur man ställer in marginalerna för ett Excel kalkylblad med hjälp av exempel på kod. Du lär dig också hur man programmässigt ställer in marginalerna för sidans centrum, rubrik och sidfot för sidinställningar med Aspose.Cells för Python via .NET API.
keywords: Python Excel bibliotek, Python ställ in excel kalkylbladsmarginal till centrum, ställ in kalkylblads rubrik och sidfotsmarginal med Python.
---

{{% alert color="primary" %}}

Aspose.Cells för Python via .NET stöder fullt ut Microsoft Excels sidinställningsalternativ. Utvecklare kan behöva konfigurera sidinställningsinställningar för kalkylblad för att kontrollera utskriftsprocessen. Denna ämne diskuterar hur man använder Aspose.Cells för Python via .NET för att konfigurera sidmarginaler.

{{% /alert %}}

## **Hur man ställer in marginaler**

Aspose.Cells för Python via .NET tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), som representerar en Excel-fil. Klassen [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) innehåller [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets)-samlingen som ger åtkomst till varje kalkylblad i Excel-filen. Ett kalkylblad representeras av klassen [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet).

[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)-klassen tillhandahåller egenskapen [**page_setup**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/page_setup/) som används för att ställa in sidlayoutalternativen för ett arbetsblad. [**page_setup**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/page_setup)-attributet är ett objekt av [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup)-klassen som möjliggör för utvecklare att ställa in olika sidlayoutalternativ för ett utskrivet arbetsblad. [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup)-klassen tillhandahåller olika egenskaper och metoder som används för att ställa in sidlayoutalternativ.

## **Hur man ställer in sidmarginaler**

Ställ in sidmarginaler (vänster, höger, över, under) med medlemmar i [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup)-klassen. Några av metoderna är listade nedan som används för att specificera sidmarginaler:

- [**left_margin**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/left_margin/)
- [**right_margin**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/right_margin/)
- [**top_margin**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/top_margin/)
- [**bottom_margin**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/bottom_margin/)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-SetMargins-1.py" >}}

## **Hur man centrerar på sidan**

Det är möjligt att centrera någonting på en sida horisontellt och vertikalt. För detta finns det några användbara medlemmar i [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup)-klassen, [**center_horizontally**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/center_horizontally/) och [**center_vertically**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/center_vertically/).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-SetMargins-CenterOnPage.py" >}}

## **Hur man ställer in rubrik- och sidfotsmarginaler**

Ställ in sidhuvud- och sidfotmarginaler med medlemmar i [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup)-klassen som [**header_margin**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/header_margin) och [**footer_margin**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/footer_margin).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-SetMargins-HeaderAndFooterMargins.py" >}}
