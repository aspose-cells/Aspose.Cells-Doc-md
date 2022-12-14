---
title: Utskriftsformat
type: docs
weight: 80
url: /sv/reportingservices/page-setup/
---
Konfigurationen inkluderar två sektioner och 8 typer av sidinställningar. Dessa egenskaper inkluderar namn, index, FitToPagesTall, FitToPagesWide, TopMargin, FooterMargin, HeaderMargin, BottomMargin, LeftMargin och RightMargin.

- **namn** representerar rapportens namn, det representerar hela rapporten när namnet är tomt.
- **index** representerar kalkylbladsindex för den exporterade Excel-filen.
- **FitToPagesTall** representerar antalet sidor som kalkylbladet skalas till när det skrivs ut.
- **FitToPagesWide** representerar antalet sidor brett som kalkylbladet skalas till när det skrivs ut.
- **FooterMargin**representerar avståndet från botten av sidan till sidfoten, i enheten centimeter.
- **HeaderMargin** representerar avståndet från toppen av sidan till sidhuvudet, i centimeterenhet.
- **Vänster marginal** representerar storleken på den vänstra marginalen, i enheten centimeter.
- **Högermarginal** representerar storleken på högermarginalen, i enheten centimeter.
- **TopMargin** representerar storleken på den övre marginalen, i enheten centimeter.
- **Bottenmarginal** representerar storleken på bottenmarginalen, i enheten centimeter.

Exempel på konfiguration av sidinställningar:

{{code  lang="xml" }}
<PageSetup>
<Report name=”report name” FitToPagesTall=”0” FitToPagesWide =”1” TopMargin =”1.0” FooterMargin =” 1.0” HeaderMargin =” 1.0” BottomMargin =” 1.0” LeftMargin =” 1.0” RightMargin =” 1.0”>
<Sheet index=”0” FitToPagesTall=”1” FitToPagesWide =”1” TopMargin =”1.0” FooterMargin =” 1.0” HeaderMargin =” 1.0” BottomMargin =” 1.0” LeftMargin =” 1.0” RightMargin =” 1.0”/>
<Sheet index=”1” FitToPagesTall=”0” FitToPagesWide =”1” TopMargin =”1.0” FooterMargin =” 1.0” HeaderMargin =” 1.0” BottomMargin =” 1.0” LeftMargin =” 1.0” RightMargin =” 1.0”/>
</Report>
</PageSetup>

{{code}}
