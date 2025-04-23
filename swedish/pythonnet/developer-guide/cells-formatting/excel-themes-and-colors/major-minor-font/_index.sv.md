---
title: Rubrik och brödtexttema font
description: Aspose.Cells är ett Python bibliotek för att arbeta med kalkylbladsfiler. Det stöder att ställa in rubrik och brödtexttemafonter i Excel dokument, vilket gör att användare kan anpassa utseendet och stilen på dokumentet. Denna artikel introducerar hur man använder Aspose.Cells för Python via .NET biblioteket för att arbeta med rubrik och brödtexttemafonter i Excel dokument.
keywords: Aspose.Cells för Python via .NET, Excel dokument, Rubrik, Brödtext, Temafont, Utseende, Stil
type: docs
weight: 120
url: /sv/python-net/headings-and-body-theme-font/
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
Med Aspose.Cells för Python via .NET kan vi kontrollera om standardfonten är temafont eller ange temafont med [**Font.scheme_type**](https://reference.aspose.com/cells/python-net/aspose.cells/font/scheme_type) egenskapen.

Följande exempelkod visar hur man manipulerar tematypsnitt.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-Headings-and-body-font.py" >}}


## **Dynamiskt hämtar lokal tematypsnitt programmatiskt**
Ibland är våra servrar och användares maskiner inte i samma region. Hur kan vi få samma typsnitt som användarna vill för filbehandling?

Vi måste ställa in systemets regionala inställningar innan vi laddar filen med [**LoadOptions.region**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/region)-egenskapen.

Följande exempelkod visar hur man får lokaltematypsnitt.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-Local-Theme-Font.py" >}}

