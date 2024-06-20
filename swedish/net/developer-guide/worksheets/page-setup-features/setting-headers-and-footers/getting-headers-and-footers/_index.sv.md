---
title: Att få headers eller footers
type: docs
weight: 30
url: /sv/net/get-headers-or-footers/
description: Denna artikel förklarar hur man programmeratiskt får header och footers från Excel eller OpenOffice filer med hjälp av C# API eller .NET biblioteket.
---

{{% alert color="primary" %}}

Headers och footers visas endast i vy för sidlayout, utskriftsvisning och på utskrifter. 

Du kan också använda dialogrutan Sidlayout om du vill visa headers eller footers för mer än ett kalkylblad åt gången. 

För andra bladtyper, såsom kalkylblad eller diagram, kan du infoga headers och footers endast genom att använda dialogrutan Sidlayout.

{{% /alert %}}

## **Hämta sidhuvuden och sidfötter i MS Excel**
1. Klicka på kalkylarket där du vill visa eller ändra sidhuvuden eller sidfötter.
2. På fliken Visa, i gruppen Arbetsboksvisningar, klicka på Sidlayout.
  Excel visar kalkylarket i Sidlayoutvy.
3. För att visa eller redigera en sidhuvud eller sidfot, klicka i vänster-, mitt- eller höger sidhuvud- eller sidfotstextruta längst upp eller längst ned på kalkylarket (under Sidhuvud eller ovanför Sidfot).


## **Hämta sidhuvuden och sidfötter med hjälp av Aspose.Cells för .Net**
Med [**Worksheet.GetHeader**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/GetHeader/) och [**Worksheet.GetFooter**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/GetFooter/) metoder kan .Net-utvecklare enkelt hämta sidhuvuden eller sidfötter från filen.

1. Konstruera Arbetsbok för att öppna filen.
2. Hämta kalkylarket där du vill hämta sidhuvuden eller sidfot.
3. Hämta sidhuvud eller sidfot med specifik avsnitts-id.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Gets-Header-Footer.cs" >}}

## **Parera sidhuvuden och sidfötter till kommandolista**
Sidhuvud- eller sidfotstexten kan innehålla specialkommandon, till exempel en platshållare för sidnumret, aktuellt datum eller textformateringsattribut.

Specialkommandon representeras av enstaka bokstav med ett ledande et-tecken ("&").

Sidhuvud- och sidfotsträngarna är konstruerade med hjälp av ABNF-grammatik. Det är inte lätt att förstå utan en visningsapparat.

Aspose.Cells för .Net tillhandahåller [**Worksheet.GetCommands**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/GetCommands/) metod för att parsa sidhuvuden och sidfötter som kommandolista.

Följande koder visar hur man parsa sidhuvud eller sidfot som kommandolista och bearbeta kommandon:

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Parses-Header-Footer.cs" >}}
