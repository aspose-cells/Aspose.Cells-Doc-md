---
title: Rubriker och teckensnitt för kroppstema
description: Aspose.Cells är ett .NET-bibliotek för att arbeta med kalkylarksfiler. Den stöder inställning av teckensnitt för rubriker och kroppstema i Excel-dokument, vilket gör det möjligt för användare att anpassa utseendet och stilen på dokumentet. Den här artikeln kommer att introducera hur du använder Aspose.Cells-biblioteket för att arbeta med teckensnitt för rubriker och texttema i Excel-dokument.
keywords: Aspose.Cells, Excel Document, Heading, Body, Theme Font, Appearance, Style
type: docs
weight: 120
url: /sv/net/headings-and-body-theme-font/
---
{{% alert color="primary" %}}

 Standardteckensnittet ändras automatiskt när återinställningen ändras.

Om standardteckensnittet ändras ändras också radhöjden och kolumnbredden, och det kan till och med förstöra sidlayouten.

Vad fick standardteckensnittet att ändras?

Om Excel-tematypsnitt är inställt kommer Excel automatiskt att växla mellan olika typsnitt baserat på den aktuella språkmiljön.


{{% /alert %}}

##  **Rubriker Och Kroppstema Teckensnitt I Excel**

I Excel, välj Hem-fliken, klicka på rullgardinsmenyn för teckensnitt, du kommer att se "Temateckensnitt" med två temateckensnitt: Calibri Light (Rubriker) och Calibri (Body) överst med engelsk regioninställning.

**![Theme Fonts](Theme-Fonts.png)**

Om Temateckensnitt väljs kommer teckensnittsnamnet att visas olika i olika regioner.
Om du inte vill att teckensnittet ska ändras automatiskt i olika regioner, välj inte de två temateckensnitten .


##  **Ändra rubriker och kroppsteckensnitt programmässigt**
 Med Aspose.Cells för .Net kan vi kontrollera om standardteckensnittet är tematypsnitt eller ställa in tematypsnitt med[**Font.SchemeType**](https://reference.aspose.com/cells/net/aspose.cells/font/schemetype/) fast egendom.

Följande exempelkod visar hur man manipulerar temateckensnitt.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Headings-and-body-font.cs" >}}


##  **Får dynamiskt lokalt temateckensnitt programmässigt**
Ibland är våra servrar och användarnas maskiner inte i samma region. Hur kan vi få samma typsnitt som användarna vill ha för filbehandling?

 Vi måste ställa in systemets regionala inställningar innan vi laddar filen med[**LoadOptions.Region**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/region/) fast egendom

Följande exempelkod visar hur man får lokalt tematypsnitt.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Local-Theme-Font.cs" >}}