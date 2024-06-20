---
title: Sidinställning
type: docs
weight: 80
url: /sv/reportingservices/page-setup/
---

Konfigurationen inkluderar två avsnitt och 8 typer av sidinställningsegenskaper. Dessa egenskaper inkluderar namn, index, FitToPagesTall, FitToPagesWide, TopMargin, FooterMargin, HeaderMargin, BottomMargin, LeftMargin och RightMargin.

- **namn** representerar rapportnamnet, det representerar hela rapporten när namnet är blankt.
- **index** representerar arkindext för den exporterade Excel-filen.
- **FitToPagesTall** representerar antalet sidor hög som kalkylarket kommer att skalas till när det skrivs ut.
- **FitToPagesWide** representerar antalet sidor bred som kalkylarket kommer att skalas till när det skrivs ut.
- **FooterMargin** representerar avståndet från sidans botten till sidfoten, i enheten centimeter.
- **HeaderMargin** representerar avståndet från sidans topp till sidhuvudet, i enheten centimeter.
- **LeftMargin** representerar storleken på vänster marginal, i enheten centimeter.
- **RightMargin** representerar storleken på höger marginal, i enheten centimeter.
- **TopMargin** representerar storleken på övre marginal, i enheten centimeter.
- **BottomMargin** representerar storleken på nedre marginal, i enheten centimeter.

PageSetup-konfigurations exempel:

{{code  lang="xml" }}
<PageSetup>
<Report name=”report name” FitToPagesTall=”0” FitToPagesWide =”1” TopMargin =”1.0” FooterMargin =” 1.0” HeaderMargin =” 1.0” BottomMargin =” 1.0” LeftMargin =” 1.0” RightMargin =” 1.0”>
<Sheet index=”0” FitToPagesTall=”1” FitToPagesWide =”1” TopMargin =”1.0” FooterMargin =” 1.0” HeaderMargin =” 1.0” BottomMargin =” 1.0” LeftMargin =” 1.0” RightMargin =” 1.0”/>
<Sheet index=”1” FitToPagesTall=”0” FitToPagesWide =”1” TopMargin =”1.0” FooterMargin =” 1.0” HeaderMargin =” 1.0” BottomMargin =” 1.0” LeftMargin =” 1.0” RightMargin =” 1.0”/>
</Report>
</PageSetup>

{{code}}
