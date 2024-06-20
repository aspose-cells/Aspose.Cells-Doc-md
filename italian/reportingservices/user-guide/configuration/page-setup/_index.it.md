---
title: Impostazioni pagina
type: docs
weight: 80
url: /it/reportingservices/page-setup/
---

La configurazione include due sezioni e 8 tipi di proprietà Impostazioni pagina. Queste proprietà includono nome, indice, FitToPagesTall, FitToPagesWide, TopMargin, FooterMargin, HeaderMargin, BottomMargin, LeftMargin e RightMargin.

- **nome** rappresenta il nome del report, rappresenta l'intero report quando il nome è vuoto.
- **indice** rappresenta l'indice del foglio di lavoro del file Excel esportato.
- **FitToPagesTall** rappresenta il numero di pagine in altezza a cui il foglio di lavoro verrà ridimensionato quando viene stampato.
- **FitToPagesWide** rappresenta il numero di pagine in larghezza a cui il foglio di lavoro verrà ridimensionato quando viene stampato.
- **FooterMargin** rappresenta la distanza dal basso della pagina al piè di pagina, in unità di centimetri.
- **HeaderMargin** rappresenta la distanza dall'alto della pagina all'intestazione, in unità di centimetri.
- **LeftMargin** rappresenta la dimensione del margine sinistro, in unità di centimetri.
- **RightMargin** rappresenta la dimensione del margine destro, nell'unità di centimetri.
- **TopMargin** rappresenta la dimensione del margine superiore, nell'unità di centimetri.
- **BottomMargin** rappresenta la dimensione del margine inferiore, nell'unità di centimetri.

Esempio di configurazione di PageSetup:

{{code  lang="xml" }}
<PageSetup>
<Report name=”report name” FitToPagesTall=”0” FitToPagesWide =”1” TopMargin =”1.0” FooterMargin =” 1.0” HeaderMargin =” 1.0” BottomMargin =” 1.0” LeftMargin =” 1.0” RightMargin =” 1.0”>
<Sheet index=”0” FitToPagesTall=”1” FitToPagesWide =”1” TopMargin =”1.0” FooterMargin =” 1.0” HeaderMargin =” 1.0” BottomMargin =” 1.0” LeftMargin =” 1.0” RightMargin =” 1.0”/>
<Sheet index=”1” FitToPagesTall=”0” FitToPagesWide =”1” TopMargin =”1.0” FooterMargin =” 1.0” HeaderMargin =” 1.0” BottomMargin =” 1.0” LeftMargin =” 1.0” RightMargin =” 1.0”/>
</Report>
</PageSetup>

{{code}}
