---
title: Rubrik och brödtexttema font
description: Aspose.Cells är ett .NET bibliotek för att arbeta med kalkylbladsfiler. Det stöder inställning av rubrik och brödtexttemafonter i Exceldokument, vilket möjliggör för användare att anpassa utseendet och stilen på dokumentet. Denna artikel kommer att introducera hur man använder Aspose.Cells biblioteket för att arbeta med rubrik och brödtexttemafonter i Exceldokument.
keywords: Aspose.Cells, Excel dokument, Rubrik, Text, Tema Font, Utseende, Stil
type: docs
weight: 120
url: /sv/net/headings-and-body-theme-font/
---

{{% alert color="primary" %}}

Standardtypsnittet kommer automatiskt att ändras när regoinställningen ändras. 

Om standardtypsnittet ändras, ändras också radhöjd och kolumnbredd, och det kan till och med förstöra sidlayouten.

Vad orsakade att standardtypsnittet ändrades?

Om Excel-tematypsnitt är inställt, kommer Excel automatiskt att växla mellan olika typsnitt baserat på den aktuella språkmiljön.


{{% /alert %}}

## **Rubrik- och brödtematypsnitt i Excel**

I Excel, välj fliken Hem, klicka på typsnittslistrutan, du kommer att se "Tematypsnitt" med två tematypsnitt: Calibri Light (Rubriker) och Calibri (Brödtext) längst upp med engelsk regoinställning.

**![Tema Typsnitt](Tema-Typsnitt.png)**

Om tematypsnitt väljs, kommer typsnittsnamnet att visas olika i olika regioner.
Om du inte vill att typsnittet automatiskt ändras i olika regioner, välj inte de två tematypsnitten.


## **Ändra Rubriker och brösttypsnitt programmatiskt**
Med Aspose.Cells för .Net kan vi kontrollera om standardtypsnittet är tematypsnitt eller ställa in tematypsnitt med [**Font.SchemeType**](https://reference.aspose.com/cells/net/aspose.cells/font/schemetype/)-egenskapen.

Följande exempelkod visar hur man manipulerar tematypsnitt.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Headings-and-body-font.cs" >}}


## **Dynamiskt hämtar lokal tematypsnitt programmatiskt**
Ibland är våra servrar och användares maskiner inte i samma region. Hur kan vi få samma typsnitt som användarna vill för filbehandling?

Vi måste ställa in systemets regionala inställningar innan vi laddar filen med [**LoadOptions.Region**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/region/)-egenskapen.

Följande exempelkod visar hur man får lokaltematypsnitt.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Local-Theme-Font.cs" >}}
{{< app/cells/assistant language="csharp" >}}
