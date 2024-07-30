---
title: Att få headers eller footers
type: docs
weight: 30
url: /sv/python-net/get-headers-or-footers/
description: Denna artikel förklarar hur man programmatiskt får sidhuvuden och sidfötter från Excel eller OpenOffice filer med hjälp av Aspose.Cells for Python via .NET API.
keywords: Python Excel bibliotek, Python få sidhuvuden och sidfötter, Parera sidhuvuden och sidfötter till kommandolista med Python.
---

{{% alert color="primary" %}}

Headers och footers visas endast i vy för sidlayout, utskriftsvisning och på utskrifter. 

Du kan också använda dialogrutan Sidlayout om du vill visa headers eller footers för mer än ett kalkylblad åt gången. 

För andra bladtyper, såsom kalkylblad eller diagram, kan du infoga headers och footers endast genom att använda dialogrutan Sidlayout.

{{% /alert %}}

## **Hur man får sidhuvuden och sidfötter i MS Excel**
1. Klicka på kalkylarket där du vill visa eller ändra sidhuvuden eller sidfötter.
2. På fliken Visa, i gruppen Arbetsboksvisningar, klicka på Sidlayout.
  Excel visar kalkylarket i Sidlayoutvy.
3. För att visa eller redigera en sidhuvud eller sidfot, klicka i vänster-, mitt- eller höger sidhuvud- eller sidfotstextruta längst upp eller längst ned på kalkylarket (under Sidhuvud eller ovanför Sidfot).


## **Hur man får sidhuvuden och sidfötter med Aspose.Cells för Python Excel Library**
Med [**Worksheet.page_setup.get_header**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/get_header/#int) och [**Worksheet.page_setup.get_footer**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/get_footer/#int) metoder kan .Net-utvecklare enkelt hämta sidhuvuden eller sidfötter från filen.

1. Konstruera Arbetsbok för att öppna filen.
2. Hämta kalkylarket där du vill hämta sidhuvuden eller sidfot.
3. Hämta sidhuvud eller sidfot med specifik avsnitts-id.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Gets-Header-Footer.py" >}}

## **Hur man parerar sidhuvuden och sidfötter till kommandolista**
Sidhuvud- eller sidfotstexten kan innehålla specialkommandon, till exempel en platshållare för sidnumret, aktuellt datum eller textformateringsattribut.

Specialkommandon representeras av enstaka bokstav med ett ledande et-tecken ("&").

Sidhuvud- och sidfotsträngarna är konstruerade med hjälp av ABNF-grammatik. Det är inte lätt att förstå utan en visningsapparat.

Aspose.Cells for Python via .NET tillhandahåller en [**Worksheet.page_setup.get_commands**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/get_commands/#str)-metod för att parsa sidhuvuden och sidfötter som kommandolista.

Följande koder visar hur man parsa sidhuvud eller sidfot som kommandolista och bearbeta kommandon:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Parses-Header-Footer.py" >}}
