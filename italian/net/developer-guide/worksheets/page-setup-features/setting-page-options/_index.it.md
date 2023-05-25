---
title: Impostazione delle opzioni della pagina
type: docs
weight: 10
url: /it/net/setting-page-options/
description: Questo articolo fornisce codice di esempio per impostare le opzioni di pagina dei fogli di lavoro di Excel a livello di codice usando la libreria C# API e .NET. Sarai in grado di impostare l'orientamento della pagina, il fattore di scala, le opzioni FitToPages, il formato carta, la qualità di stampa, il numero della prima pagina.
keywords: set excel page orientation c#, set excel scaling factor c#, set excel worksheets paper size c#
---
{{% alert color="primary" %}}

A volte, è necessario configurare le impostazioni di impostazione della pagina per i fogli di lavoro per controllare la stampa. Queste impostazioni di configurazione della pagina offrono varie opzioni.

{{% /alert %}}

##  **Impostazione delle opzioni della pagina**

Le opzioni di impostazione della pagina sono completamente supportate in Aspose.Cells. Questo articolo spiega come impostare le opzioni della pagina con Aspose.Cells e mostra esempi di codice per l'impostazione:

 Aspose.Cells offre un corso,[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) che rappresenta un file Excel Microsoft. IL[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la classe contiene un[**Fogli di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) raccolta che consente l'accesso a ciascun foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato da[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)classe.

 IL[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) la classe fornisce il[**Impostazione della pagina**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) proprietà utilizzata per impostare le opzioni di impostazione della pagina del foglio di lavoro. In effetti, questo[**Impostazione della pagina**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) la proprietà è un oggetto di[**Impostazione della pagina**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) classe utilizzata per impostare diverse opzioni di layout di pagina per un foglio di lavoro stampato. IL[**Impostazione della pagina**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)class fornisce varie proprietà utilizzate per impostare le opzioni di impostazione della pagina. Alcune di queste proprietà sono discusse di seguito.

###  **Orientamento della pagina**

 L'orientamento della pagina può essere impostato su verticale o orizzontale utilizzando il[**Impostazione della pagina**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) classe'[**Orientamento**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/orientation) proprietà. IL[**Orientamento**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/orientation) La proprietà accetta uno dei valori predefiniti in[**TipoOrientamentoPagina**](https://reference.aspose.com/cells/net/aspose.cells/pageorientationtype)enumerazione, di seguito elencati.

|**Tipi di orientamento della pagina**|**Descrizione**|
| :- | :- |
|Paesaggio|Orientamento orizzontale|
|Ritratto|Orientamento verticale|

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-PageOrientation-1.cs" >}}

###  **Fattore di scala**

 È possibile ridurre o ingrandire le dimensioni di un foglio di lavoro regolando il fattore di scala con il[**PageSetup.Zoom**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/zoom)proprietà.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-ScalingFactor-1.cs" >}}

###  **Opzioni FitToPages**

 Per adattare il contenuto del foglio di lavoro a un numero specifico di pagine, utilizzare il file[**Impostazione della pagina**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) classe'[**FitToPagesAlto**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopagestall) E[**FitToPagesWide**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopageswide)proprietà. Queste proprietà vengono utilizzate anche per ridimensionare i fogli di lavoro.

{{% alert color="primary" %}}

 Puoi scegliere il[**FitToPagesAlto**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopagestall)/[**FitToPagesWide**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopageswide) o il[**Ingrandisci**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/zoom) proprietà ma non entrambi allo stesso tempo.

{{% /alert %}}

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-FitToPagesOptions-1.cs" >}}

###  **Dimensioni del foglio**

 Impostare il formato carta su cui verranno stampati i fogli di lavoro utilizzando il file[**Impostazione della pagina**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) classe'[**Dimensioni del foglio**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/papersize) proprietà. IL[**Dimensioni del foglio**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/papersize) La proprietà accetta uno dei valori predefiniti in[**PaperSizeType**](https://reference.aspose.com/cells/net/aspose.cells/papersizetype)enumerazione, di seguito elencati.

|**Tipi di formato carta**|**Descrizione**|
| :- | :- |
|CartaLettera|Lettera (8-1/2 pollici x 11 pollici)|
|CartaLetteraPiccolo|Lettera piccola (8-1/2 pollici x 11 pollici)|
|Carta Tabloid|Tabloid (11 pollici x 17 pollici)|
|PaperLedger|Libro mastro (17 pollici x 11 pollici)|
|PaperLegal|Legale (8-1/2 pollici x 14 pollici)|
|Dichiarazione cartacea|Dichiarazione (5-1/2 pollici x 8-1/2 pollici)|
|PaperExecutive|Esecutivo (7-1/4 pollici x 10-1/2 pollici)|
|CartaA3|A3 (297 mm x 420 mm)|
|CartaA4|A4 (210 x 297 mm)|
|CartaA4Piccolo|A4 piccolo (210 mm x 297 mm)|
|Carta A5|A5 (148 mm x 210 mm)|
|CartaB4|JIS B4 (257 mm x 364 mm)|
|CartaB5|JIS B5 (182 mm x 257 mm)|
|CartaFolio|Folio (8-1/2 pollici x 13 pollici)|
|PaperQuarto|Quarto (215 mm x 275 mm)|
|Carta 10x14|10 pollici x 14 pollici|
|Carta 11x17|11 pollici x 17 pollici|
|CartaNota|Nota (8-1/2 pollici x 11 pollici)|
|Busta di carta9|Busta n. 9 (3-7/8 pollici x 8-7/8 pollici)|
|Busta di carta10|Busta n. 10 (4-1/8 pollici x 9-1/2 pollici)|
|Busta di carta11|Busta n. 11 (4-1/2 pollici x 10-3/8 pollici)|
|Busta di carta12|Busta n. 12 (4-1/2 pollici x 11 pollici)|
|Busta di carta14|Busta n. 14 (5 pollici x 11-1/2 pollici)|
|CartaCFoglio|Foglio formato C|
|CartaDFoglio|Foglio di dimensione D|
|CartaEFoglio|Foglio taglia E|
|Busta di cartaDL|Busta DL (110 mm x 220 mm)|
|Busta di cartaC5|Busta C5 (162 mm x 229 mm)|
|Busta di cartaC3|Busta C3 (324 mm x 458 mm)|
|Busta di cartaC4|Busta C4 (229 mm x 324 mm)|
|Busta di cartaC6|Busta C6 (114 mm x 162 mm)|
|Busta di cartaC65|Busta C65 (114 mm x 229 mm)|
|Busta di cartaB4|Busta B4 (250 mm x 353 mm|
|Busta di cartaB5|Busta B5 (176 mm x 250 mm)|
|Busta di cartaB6|Busta B6 (176 mm x 125 mm)|
|CartaBustaItalia|Busta Italia (110 mm x 230 mm)|
|Busta di cartaMonarca|Busta Monarch (3-7/8 pollici x 7-1/2 pollici)|
|Busta di carta Personale|Busta (3-5/8 pollici x 6-1/2 pollici)|
|PaperFanfoldUS|Standard statunitense a modulo continuo (14-7/8 pollici x 11 pollici)|
|PaperFanfoldStdTedesco|Standard tedesco Fanfold (8-1/2 in. x 12 in.)|
|PaperFanfoldLegaleTedesco|Fanfold legale tedesco (8-1/2 pollici x 13 pollici)|
|CartaISOB4|B4 (ISO) 250 x 353 mm|
|CartaGiapponeseCartolina|Cartolina giapponese (100 mm x 148 mm)|
|Carta9x11|9 pollici x 11 pollici|
|Carta 10x11|10 pollici x 11 pollici|
|Carta 15x11|15 pollici x 11 pollici|
|Busta di cartaInvito|Invito a busta (220 mm x 220 mm)|
|CartaLetteraExtra|Lettera USA Extra 9 \275 x 12 pollici|
|CartaLegaleExtra|US Legal Extra 9 \275 x 15 pollici|
|CartaTabloidExtra|Tabloid USA Extra 11,69 x 18 pollici|
|Carta A4Extra|A4 Extra 9,27 x 12,69 pollici|
|CartaLetteraTrasversale|Lettera trasversale 8 \275 x 11 pollici|
|Carta A4Trasversale|A4 trasversale 210 x 297 mm|
|PaperLetterExtraTransverse|Lettera Extra Trasversale 9\275 x 12 pollici|
|CartaSuperA|SuperA/SuperA/A4 227 x 356 mm|
|CartaSuperB|SuperB/SuperB/A3 305 x 487 mm|
|PaperLetterPlus|Lettera USA più 8,5 x 12,69 pollici|
|CartaA4Plus|A4 Plus 210 x 330 mm|
|Carta A5Trasversale|A5 trasversale 148 x 210 mm|
|CartaJISB5Trasversale|B5 (JIS) Trasversale 182 x 257 mm|
|CartaA3Extra|A3 extra 322 x 445 mm|
|Carta A5Extra|A5 Extra 174 x 235 mm|
|CartaISOB5Extra|B5 (ISO) Extra 201 x 276 mm|
|CartaA2|Formato A2 420 x 594 mm|
|Carta A3Trasversale|A3 trasversale 297 x 420 mm|
|Carta A3ExtraTrasversale|A3 Extra trasversale 322 x 445 mm|
|CartaGiapponeseDoppiaCartolina|Cartolina doppia giapponese 200 x 148 mm|
|CartaA6|Formato A6 105 x 148 mm|
|CartaGiapponeseBustaKaku2|Busta giapponese Kaku #2|
|CartaGiapponeseBustaKaku3|Busta giapponese Kaku #3|
|CartaGiapponeseBustaChou3|Busta giapponese Chou #3|
|CartaGiapponeseBustaChou4|Busta giapponese Chou #4|
|CartaLetteraRuotata|11 pollici x 8,5 pollici|
|PaperA3Ruotato|420 mm x 297 mm|
|Carta A4 Ruotato|297 mm x 210 mm|
|Carta A5Ruotata|210 mm x 148 mm|
|CartaJISB4Ruotata|B4 (JIS) Ruotato 364 x 257 mm|
|CartaJISB5Ruotata|B5 (JIS) Ruotato 257 x 182 mm|
|CartaGiapponeseCartolinaRuotata|Cartolina giapponese ruotata 148 x 100 mm|
|CartaGiapponeseDoppiaCartolinaRuotata|Cartolina giapponese doppia ruotata 148 x 200 mm|
|Carta A6Ruotata|A6 ruotato 148 x 105 mm|
|CartaGiapponeseBustaKaku2Ruotato|Busta giapponese Kaku n. 2 ruotata|
|CartaGiapponeseBustaKaku3Ruotato|Busta giapponese Kaku n. 3 ruotata|
|CartaGiapponeseBustaChou3Ruotata|Busta giapponese Chou #3 ruotata|
|CartaGiapponeseBustaChou4Ruotato|Busta giapponese Chou #4 ruotata|
|CartaJISB6|B6 (JIS) 128 x 182 mm|
|CartaJISB6Ruotata|B6 (JIS) Ruotato 182 x 128 mm|
|Carta 12x11|12 x 11 pollici|
|CartaGiapponeseBustaYou4|Busta giapponese You #4|
|CartaGiapponeseBustaYou4Ruotato|Busta giapponese You #4 ruotata|
|CartaPRC16K|PRC 16K 146 x 215 mm|
|CartaPRC32K|PRC 32K 97 x 151 mm|
|PaperPRCBig32K|PRC 32K(Grande) 97 x 151 mm|
|CartaPRCEbusta1|PRC Busta n. 1 102 x 165 mm|
|CartaPRCEbusta2|PRC Busta n. 2 102 x 176 mm|
|CartaPRCEbusta3|PRC Busta n. 3 125 x 176 mm|
|CartaPRCEbusta4|RPC Busta n. 4 110 x 208 mm|
|CartaPRCEbusta5|PRC Busta n. 5 110 x 220 mm|
|CartaPRCEbusta6|PRC Busta n. 6 120 x 230 mm|
|CartaPRCEbusta7|PRC Busta n. 7 160 x 230 mm|
|CartaPRCEbusta8|PRC Busta n. 8 120 x 309 mm|
|CartaPRCEbusta9|PRC Busta n. 9 229 x 324 mm|
|CartaPRCEbusta10|PRC Busta n. 10 324 x 458 mm|
|CartaPRC16KRuotato|PRC 16K ruotato|
|CartaPRC32KRuotato|PRC 32K ruotato|
|PaperPRCBig32KRuotato|PRC 32K (grande) ruotato|
|CartaPRCEbusta1Ruotata|Busta PRC n. 1 ruotata 165 x 102 mm|
|CartaPRCEbusta2Ruotata|Busta PRC n. 2 ruotata 176 x 102 mm|
|CartaPRCEbusta3Ruotata|Busta PRC n. 3 ruotata 176 x 125 mm|
|CartaPRCEbusta4Ruotata|Busta PRC n. 4 ruotata 208 x 110 mm|
|CartaPRCEbusta5Ruotata|Busta PRC n. 5 ruotata 220 x 110 mm|
|CartaPRCEbusta6Ruotata|Busta PRC n. 6 ruotata 230 x 120 mm|
|CartaPRCEbusta7Ruotata|Busta PRC n. 7 ruotata 230 x 160 mm|
|CartaPRCEbusta8Ruotata|Busta PRC n. 8 ruotata 309 x 120 mm|
|CartaPRCEbusta9Ruotata|Busta PRC n. 9 ruotata 324 x 229 mm|
|CartaPRCEbusta10Ruotata|Busta PRC n. 10 ruotata 458 x 324 mm|
|CartaB3|solito B3 (13,9 x 19,7 pollici)|
|CartaBusinessCard|Biglietto da visita (90 mm x 55 mm)|
|Carta termica|Termico (3 x 11 pollici)|
|Costume|Rappresenta il formato carta personalizzato.|

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-ManagePaperSize-1.cs" >}}

###  **Qualità di stampa**

 Impostare la qualità di stampa dei fogli di lavoro da stampare con il[**Impostazione della pagina**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) classe'[**Qualità di stampa**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printquality)proprietà. L'unità di misura per la qualità di stampa è Dots Per Inch (DPI).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetPrintQuality-1.cs" >}}

###  **Numero prima pagina**

 Avviare la numerazione delle pagine del foglio di lavoro utilizzando il file[**Impostazione della pagina**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) classe'[**Numero prima pagina**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/firstpagenumber) proprietà. IL[**Numero prima pagina**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/firstpagenumber)La proprietà imposta il numero di pagina della prima pagina del foglio di lavoro e le pagine successive sono numerate in ordine crescente.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetFirstPageNumber-1.cs" >}}
