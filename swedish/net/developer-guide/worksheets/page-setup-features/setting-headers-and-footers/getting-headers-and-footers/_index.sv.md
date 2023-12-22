---
title: Få sidhuvuden eller sidfötter
type: docs
weight: 30
url: /sv/net/get-headers-or-footers/
description: Den här artikeln förklarar hur du programmatiskt hämtar sidhuvuden och sidfötter från Excel- eller OpenOffice-filer med hjälp av biblioteket C# API eller .NET.
---
{{% alert color="primary" %}}

 Sidhuvuden och sidfötter visas endast i sidlayoutvyn, förhandsgranska och på utskrivna sidor.

 Du kan också använda dialogrutan Utskriftsformat om du vill visa sidhuvuden eller sidfötter för mer än ett kalkylblad åt gången.

För andra arktyper, som diagramblad eller diagram, kan du bara infoga sidhuvuden och sidfötter genom att använda dialogrutan Utskriftsformat.

{{% /alert %}}

##  **Få sidhuvuden och sidfötter i MS Excel**
1. Klicka på kalkylbladet där du vill visa eller ändra sidhuvuden eller sidfötter.
2. På fliken Vie, i gruppen Arbetsbokvyer, klicka på Sidlayout.
Excel visar kalkylbladet i sidlayoutvyn.
3. För att visa eller redigera ett sidhuvud eller en sidfot, klicka på den vänstra, mitten eller högra textrutan för sidhuvud eller sidfot överst eller längst ned på kalkylbladssidan (under sidhuvud eller ovanför sidfot).


##  **Få sidhuvuden och sidfötter med Aspose.Cells för .Net**
 Med[**Arbetsblad.GetHeader**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/GetHeader/) och[**Worksheet.GetFooter**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/GetFooter/) metoder, .Net-utvecklare kan helt enkelt hämta sidhuvuden eller sidfötter från filen.

1. Konstruera arbetsbok för att öppna filen.
2. Hämtar arbetsbladet där du vill ha sidhuvuden eller sidfoten.
3. Hämtar sidhuvud eller sidfot med specifikt avsnitts-id.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Gets-Header-Footer.cs" >}}

##  **Analysera sidhuvuden och sidfötter till kommandolistan**
Sidhuvudet eller sidfoten kan innehålla speciella kommandon, till exempel en platshållare för sidnummer, aktuellt datum eller textformateringsattribut.

Specialkommandon representeras av en bokstav med ett inledande et-tecken ("&").

Sidhuvud- och sidfotssträngarna är konstruerade med hjälp av ABNF-grammatik. Det är inte lätt att förstå utan tittare.

 Aspose.Cells för .Net tillhandahåller[**Worksheet.GetCommands**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/GetCommands/)metod för att analysera sidhuvuden och sidfötter som kommandolista.

Följande koder för hur man tolkar sidhuvud eller sidfot som kommandolista och bearbetar kommandon:

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Parses-Header-Footer.cs" >}}
