---
title: Rubrik och kroppstema typsnitt med Golang via C++
linktitle: Rubrik och brödtexttema font
description: Aspose.Cells är ett C++ bibliotek för att arbeta med kalkylbladsfiler. Det stödjer att ställa in rubrik och kroppstema typsnitt i Excel dokument, vilket gör det möjligt för användare att anpassa utseendet och stilen på dokumentet. Denna artikel introducerar hur man använder Aspose.Cells biblioteket för att arbeta med rubrik och kroppstema typsnitt i Excel dokument.
keywords: Aspose.Cells, Excel dokument, Rubrik, Text, Tema Font, Utseende, Stil
type: docs
weight: 120
url: /sv/go-cpp/headings-and-body-theme-font/
---

{{% alert color="primary" %}}

Standardteckensnittet ändras automatiskt när regionsinställningen ändras.

Om standardtypsnittet ändras, ändras också radhöjd och kolumnbredd, och det kan till och med förstöra sidlayouten.

Vad orsakade att standardtypsnittet ändrades?

Om Excel-tematypsnitt är inställt, kommer Excel automatiskt att växla mellan olika typsnitt baserat på den aktuella språkmiljön.

{{% /alert %}}

## **Rubrik- och brödtematypsnitt i Excel**

I Excel, välj fliken Hem, klicka på teckensnitt rullgardinsmenyn, du ser "Temateckensnitt" med två temateckensnitt: Calibri Light (Rubriker) och Calibri (Kropp) med en engelsk regioninställning överst.

**![Tema Typsnitt](Tema-Typsnitt.png)**

Om Temateckensnitt är valt, visas teckensnittets namn olika i olika regioner.
Om du inte vill att teckensnittet ska ändras automatiskt i olika regioner, välj inte de två Tematecknen.

## **Ändra rubrik och kroppens teckensnitt programmässigt**
Med Aspose.Cells for C++ kan vi kontrollera om standardteckensnittet är ett tema-teckensnitt eller ställa in tema-teckensnittet med egenskapen [**Font.GetSchemeType()**](https://reference.aspose.com/cells/go-cpp/font/getschemetype/).

Följande exempelkod visar hur man manipulerar tematypsnitt.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-MajorMinorFont.go" >}}
## **Dynamiskt hämtar lokalt tema-typsnitt programmässigt**
Ibland är våra servrar och användares maskiner inte i samma region. Hur kan vi få samma typsnitt som användarna vill för filbehandling?

Vi måste ställa in de regionala systeminställningarna innan filen laddas med egenskapen [**LoadOptions.GetRegion()**](https://reference.aspose.com/cells/go-cpp/loadoptions/getregion/).

Följande kod exempel visar hur man får det lokala tema-teckensnittet.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-MajorMinorFont-1.go" >}}
