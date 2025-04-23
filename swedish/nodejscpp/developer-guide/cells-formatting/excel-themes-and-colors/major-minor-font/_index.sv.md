---
title: Rubrik och brödtexttema font
linktitle: Rubrik och brödtexttema font
description: Aspose.Cells är ett Node.js bibliotek för att arbeta med kalkylbladsfiler. Det stöder att ställa in tema typsnitt för rubrik och kroppsdel i Excel dokument, vilket gör att användare kan anpassa utseendet och stilen på dokumentet. Denna artikel visar hur man använder Aspose.Cells biblioteket för att arbeta med tema typsnitt för rubrik och kroppsdel i Excel dokument.
keywords: Aspose.Cells, Excel dokument, Rubrik, Kropp, Tematypsnitt, Utseende, Stil, Node.js via C++
type: docs
weight: 120
url: /sv/nodejs-cpp/headings-and-body-theme-font/
---

{{% alert color="primary" %}}

Standardteckensnittet ändras automatiskt när regionsinställningen ändras.

Om standardtypsnittet ändras, ändras också radhöjd och kolumnbredd, och det kan till och med förstöra sidlayouten.

Vad orsakade att standardtypsnittet ändrades?

Om Excel-tematypsnitt är inställt, kommer Excel automatiskt att växla mellan olika typsnitt baserat på den aktuella språkmiljön.

{{% /alert %}}

## **Rubrik- och brödtematypsnitt i Excel**

I Excel, välj Start-fliken, klicka på teckensnittets nedrullningsbara låda, du kommer att se "Tema teckensnitt" med två tema-typsnitt: Calibri Light (Rubriker) och Calibri (Kropp) överst med engelskt regionsinställning.

**![Tema Typsnitt](Tema-Typsnitt.png)**

Om Temateckensnitt är vald, visas teckensnittets namn på ett annat sätt i olika regioner. Om du inte vill att teckensnittet ska ändras automatiskt i olika regioner, välj inte de två Temateckensnitten.

## **Ändra rubrik och kroppens teckensnitt programmässigt**
Med Aspose.Cells for Node.js via C++ kan vi kontrollera om standardteckensnittet är ett tema-teckensnitt eller ställa in tema-typsnitt med [**Font.setSchemeType(FontSchemeType)**](https://reference.aspose.com/cells/nodejs-cpp/font/#setSchemeType-fontschemetype-)-metoden.

Följande exempel visar hur man manipulerar tema-typsnitt.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ThemesAndColors-HeadingsAndBodyThemeFont.js" >}}



## **Dynamiskt hämtar lokalt tema-typsnitt programmässigt**
Ibland är våra servrar och användares maskiner inte i samma region. Hur kan vi få samma typsnitt som användarna vill för filbehandling?

Vi måste ställa in systemets regionala inställningar innan vi laddar filen med [**LoadOptions.setRegion(CountryCode)**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#setRegion-countrycode-)-metoden.

Följande exempelkod visar hur man får lokaltematypsnitt.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ThemesAndColors-GetLocalThemeFont.js" >}}

