---
title: Impostazione della pagina
type: docs
weight: 80
url: /it/reportingservices/page-setup/
---
La configurazione include due sezioni e 8 tipi di proprietà Imposta pagina. Queste proprietà includono name, index, FitToPagesTall, FitToPagesWide, TopMargin, FooterMargin, HeaderMargin, BottomMargin, LeftMargin e RightMargin.

- **nome** rappresenta il nome del report, rappresenta l'intero report quando il nome è vuoto.
- **indice** rappresenta l'indice del foglio di lavoro del file Excel esportato.
- **FitToPagesAlto** rappresenta il numero di pagine alte a cui verrà ridimensionato il foglio di lavoro quando viene stampato.
- **FitToPagesWide** rappresenta il numero di pagine a cui verrà ridimensionato il foglio di lavoro quando viene stampato.
- **Piè di paginaMargin** rappresenta la distanza dal fondo della pagina al piè di pagina, nell'unità di centimetri.
- **IntestazioneMargine** rappresenta la distanza dall'alto della pagina all'intestazione, nell'unità di centimetri.
- **Margine sinistro** rappresenta la dimensione del margine sinistro, nell'unità di centimetri.
- **Margine destro** rappresenta la dimensione del margine destro, nell'unità di centimetri.
- **Margine superiore** rappresenta la dimensione del margine superiore, nell'unità di centimetri.
- **Margine inferiore**rappresenta la dimensione del margine inferiore, nell'unità di centimetri.

Esempio di configurazione di PageSetup:

{{code  lang="xml" }}
<PageSetup>
<Report name=”report name” FitToPagesTall=”0” FitToPagesWide =”1” TopMargin =”1.0” FooterMargin =” 1.0” HeaderMargin =” 1.0” BottomMargin =” 1.0” LeftMargin =” 1.0” RightMargin =” 1.0”>
<Sheet index=”0” FitToPagesTall=”1” FitToPagesWide =”1” TopMargin =”1.0” FooterMargin =” 1.0” HeaderMargin =” 1.0” BottomMargin =” 1.0” LeftMargin =” 1.0” RightMargin =” 1.0”/>
<Sheet index=”1” FitToPagesTall=”0” FitToPagesWide =”1” TopMargin =”1.0” FooterMargin =” 1.0” HeaderMargin =” 1.0” BottomMargin =” 1.0” LeftMargin =” 1.0” RightMargin =” 1.0”/>
</Report>
</PageSetup>

{{code}}
