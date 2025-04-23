---
title: Caratteristiche della configurazione pagina
type: docs
weight: 40
url: /it/java/page-setup-features/
---

A volte è necessario configurare le impostazioni di impostazione pagina per i fogli di lavoro per controllare la stampa. Queste impostazioni di impostazione pagina offrono varie opzioni.

**Opzioni di pagina** 

![todo:image_alt_text](page-setup-features_1.png)

Le opzioni di impostazione pagina sono completamente supportate in Aspose.Cells. Questo articolo spiega come impostare le opzioni di pagina con Aspose.Cells.

## **Impostazioni pagina**

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), che rappresenta un file Microsoft Excel. La classe Workbook contiene una raccolta Worksheets che consente l'accesso a ciascun foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet).

La classe Worksheet fornisce la proprietà PageSetup, utilizzata per impostare le opzioni di impostazione pagina. Infatti, la proprietà PageSetup è un oggetto della classe PageSetup che consente di impostare le opzioni di layout pagina per un foglio di lavoro stampato. La classe PageSetup fornisce varie proprietà utilizzate per impostare le opzioni di impostazione pagina. Alcune di queste proprietà sono discusse di seguito.

### **Orientamento pagina**

L'orientamento pagina può essere impostato in verticale o orizzontale utilizzando il metodo [**setOrientation(PageOrientationType)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Orientation) della classe [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup). Il metodo [**setOrientation(PageOrientationType)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Orientation) richiede l'enumerazione [**PageOrientationType**](https://reference.aspose.com/cells/java/com.aspose.cells/PageOrientationType) come parametro. Di seguito sono elencati i membri dell'enumerazione [**PageOrientationType**](https://reference.aspose.com/cells/java/com.aspose.cells/PageOrientationType).

|**Tipi di orientamento pagina**|**Descrizione**|
| :- | :- |
|[**ORIZZONTALE**](https://reference.aspose.com/cells/java/com.aspose.cells/pageorientationtype#LANDSCAPE)|Orientamento orizzontale|
|[**VERTICALE**](https://reference.aspose.com/cells/java/com.aspose.cells/pageorientationtype#PORTRAIT)|Orientamento verticale|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-PageOrientation-PageOrientation.java" >}}

### **Fattore di scala**

È possibile ridurre o ingrandire le dimensioni di un foglio di lavoro regolando il fattore di scalatura con il metodo [**setZoom**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Zoom) della classe [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ScalingFactor-ScalingFactor.java" >}}

### **Opzioni di AdattaPagina**

Per adattare i contenuti del foglio di lavoro a un numero specifico di pagine, utilizzare i metodi [**setFitToPagesTall**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FitToPagesTall) e [**setFitToPagesWide**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FitToPagesWide) della classe [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup). Questi metodi vengono utilizzati anche per ridimensionare i fogli di lavoro.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-FitToPagesOptions-FitToPagesOptions.java" >}}

### **Formato Carta**

Imposta il formato carta su cui verranno stampati i fogli di lavoro utilizzando la proprietà [**PaperSize**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PaperSize) della classe [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup). La proprietà FormatoCarta accetta uno dei valori predefiniti nell'enumerazione [**PaperSizeType**](https://reference.aspose.com/cells/java/com.aspose.cells/PaperSizeType), elencati di seguito.

|**Tipi di Formato Carta**|**Descrizione**|
| :- | :- |
|Paper10x14|10 in. x 14 in.|
|Paper11x17|11 in. x 17 in.|
|PaperA3|A3 (297 mm x 420 mm)|
|PaperA4|A4 (210 mm x 297 mm)|
|PaperA4Small|A4 Small (210 mm x 297 mm)|
|PaperA5|A5 (148 mm x 210 mm)|
|PaperB3|B3 (13.9 x 19.7 inches)|
|PaperB4|B4 (250 mm x 354 mm)|
|PaperB5|B5 (182 mm x 257 mm)|
|PaperBusinessCard|Business Card (90 mm x 55 mm)|
|PaperCSheet|C size sheet|
|PaperDSheet|D size sheet|
|PaperEnvelope10|Envelope #10 (4-1/8 in. x 9-1/2 in.)|
|PaperEnvelope11|Envelope #11 (4-1/2 in. x 10-3/8 in.)|
|PaperEnvelope12|Envelope #12 (4-1/2 in. x 11 in.)|
|PaperEnvelope14|Envelope #14 (5 in. x 11-1/2 in.)|
|PaperEnvelope9|Envelope #9 (3-7/8 in. x 8-7/8 in.)|
|PaperEnvelopeB4|Envelope B4 (250 mm x 353 mm)|
|PaperEnvelopeB5|Envelope B5 (176 mm x 250 mm)|
|PaperEnvelopeB6|Envelope B6 (176 mm x 125 mm)|
|PaperEnvelopeC3|Envelope C3 (324 mm x 458 mm)|
|PaperEnvelopeC4|Envelope C4 (229 mm x 324 mm)|
|PaperEnvelopeC5|Envelope C5 (162 mm x 229 mm)|
|PaperEnvelopeC6|Envelope C6 (114 mm x 162 mm)|
|PaperEnvelopeC65|Envelope C65 (114 mm x 229 mm)|
|PaperEnvelopeDL|Envelope DL (110 mm x 220 mm)|
|PaperEnvelopeItaly|Envelope Italy (110 mm x 230 mm)|
|PaperEnvelopeMonarch|Envelope Monarch (3-7/8 in. x 7-1/2 in.)|
|PaperEnvelopePersonal|Envelope (3-5/8 in. x 6-1/2 in.)|
|PaperESheet|E size sheet|
|PaperExecutive|Executive (7-1/2 in. x 10-1/2 in.)|
|PaperFanfoldLegalGerman|German Legal Fanfold (8-1/2 in. x 13 in.)|
|PaperFanfoldStdGerman|German Standard Fanfold (8-1/2 in. x 12 in.)|
|PaperFanfoldUS|U.S. Standard Fanfold (14-7/8 in. x 11 in.)|
|PaperFolio|Folio (8-1/2 in. x 13 in.)|
|PaperLedger|Ledger (17 in. x 11 in.)|
|PaperLegal|Legal (8-1/2 in. x 14 in.)|
|PaperLetter|Letter (8-1/2 in. x 11 in.)|
|PaperLetterSmall|Letter Small (8-1/2 in. x 11 in.)|
|PaperNote|Note (8-1/2 in. x 11 in.)|
|PaperQuarto|Quarto (215 mm x 275 mm)|
|PaperStatement|Statement (5-1/2 in. x 8-1/2 in.)|
|PaperTabloid|Tabloid (11 in. x 17 in.)|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ManagePaperSize-ManagePaperSize.java" >}}

### **Qualità di Stampa**

Imposta la qualità di stampa dei fogli di lavoro da stampare con il metodo [**setPrintQuality**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintQuality) della classe [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup). L'unità di misura della qualità di stampa è il punto per pollice (DPI).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetPrintQuality-SetPrintQuality.java" >}}

### **Numero della Prima Pagina**

Inizia la numerazione delle pagine del foglio di lavoro utilizzando il metodo [**setFirstPageNumber**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FirstPageNumber) della classe [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup). Il metodo setFirstPageNumber imposta il numero di pagina del primo foglio di lavoro e le pagine successive vengono numerate in ordine crescente.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetFirstPageNumber-SetFirstPageNumber.java" >}}

## **Impostazione margini**

Aspose.Cells supporta completamente le opzioni di impostazione della pagina di Microsoft Excel. Gli sviluppatori potrebbero dover configurare le impostazioni del layout di pagina per controllare il processo di stampa dei fogli di lavoro. Questo argomento discute come utilizzare Aspose.Cells per configurare i margini di pagina.

**Margini di Pagina in Microsoft Excel**

![todo:image_alt_text](page-setup-features_2.png)

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), che rappresenta un file di Microsoft Excel. La classe Workbook contiene la raccolta Worksheets che consente l'accesso a ciascun foglio di lavoro in un file Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet).

La classe Worksheet fornisce la proprietà ImpostazioniPagina, utilizzata per impostare le opzioni del layout di pagina. L'attributo ImpostazioniPagina è un oggetto della classe [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) che consente di impostare diverse opzioni di layout di pagina per un foglio di lavoro stampato. La classe ImpostazioniPagina fornisce varie proprietà e metodi utilizzati per impostare le opzioni del layout di pagina.

### **Margini di Pagina**

Imposta i margini (sinistro, destro, superiore, inferiore) di una pagina con i membri della classe [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup). Alcuni dei metodi utilizzati per specificare i margini di pagina sono elencati di seguito:

- [**setLeftMargin(int)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#LeftMargin)
- [**setRightMargin(int)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#RightMargin)
- [**setTopMargin(int)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#TopMargin)
- [**setBottomMargin(int)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#BottomMargin)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetMargins-SetMargins.java" >}}

### **Centra sulla Pagina**

È possibile centrare qualcosa orizzontalmente e verticalmente in una pagina. La classe [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) ha membri a tal fine: [**setCenterHorizontally**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#CenterHorizontally) e [**setCenterVertically**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#CenterVertically).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-CenterOnPage-CenterOnPage.java" >}}

### **Margini Intestazione e Piè di Pagina**

Imposta i margini dell'intestazione e del piè di pagina con [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) membri come [**setHeaderMargin**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#HeaderMargin) e [**setFooterMargin**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FooterMargin).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-HeaderAndFooterMargins-HeaderAndFooterMargins.java" >}}

## **Impostazione di intestazioni e piè di pagina**

Intestazioni e piè di pagina sono le sezioni di testo e immagini sopra il margine superiore o sotto il margine inferiore di una pagina. È possibile aggiungere intestazioni e piè di pagina anche ai fogli di lavoro. Le intestazioni e i piè di pagina possono essere utilizzati per visualizzare qualsiasi tipo di informazione utile, ad esempio numero di pagina, nome dell'autore, titolo del documento o data e ora. Le intestazioni e i piè di pagina vengono gestiti anche utilizzando la finestra di impostazioni pagina.

**La finestra di impostazione pagina** 

![todo:image_alt_text](page-setup-features_3.png)

Aspose.Cells consente di aggiungere intestazioni e piè di pagina ai fogli di lavoro in fase di esecuzione, ma è consigliabile impostare manualmente le intestazioni e i piè di pagina in un file pre-progettato per la stampa. È possibile utilizzare Microsoft Excel come strumento GUI per impostare facilmente intestazioni e piè di pagina per ridurre il tempo di sviluppo. Aspose.Cells può importare il file e conservare queste impostazioni.

Per aggiungere intestazioni e piè di pagina in fase di esecuzione, Aspose.Cells fornisce classi speciali e alcuni comandi di script per controllare la formattazione.

### **Comandi di script**

I comandi di script sono comandi speciali forniti da Aspose.Cells che consentono agli sviluppatori di formattare intestazioni e piè di pagina.

|**Comandi di script**|**Descrizione**|
| :- | :- |
|&P|Numero di pagina corrente.
|&G|Un'immagine.
|&N|Il numero totale di pagine.
|&D|La data corrente.
|&T|L'ora corrente.
|&A|Il nome del foglio di lavoro.
|&F|Il nome del file senza il percorso.
|&&Testo|Mostra &Testo. Per esempio: &&WO sarà visualizzato come &WO|
|&"\<FontName>"|Un nome di font. Ad esempio: &"Arial"|
|&"\<FontName>, \<FontStyle>"|Un nome di font con uno stile. Ad esempio: &"Arial,Grassetto"|
|&\<FontSize>|Rappresenta la dimensione del carattere. Ad esempio: “&14abc”. Ma, se questo comando è seguito da un numero normale da stampare nell'intestazione, questo dovrebbe essere separato da un carattere spazio dalla dimensione del carattere. Ad esempio: “&14 123”.|

### **Imposta Intestazioni e Piè di Pagina**

La classe [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) fornisce il metodo [**setHeader**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setHeader-int-java.lang.String-) per aggiungere un'intestazione e [**setFooter**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setFooter-int-java.lang.String-) per aggiungere un piè di pagina a un foglio di lavoro. Lo script viene utilizzato come un argomento per tutti i metodi sopra citati. Rappresenta lo script da utilizzare per l'intestazione o il piè di pagina. Questo script contiene comandi di script per formattare intestazioni o piè di pagina.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetHeadersAndFooters-SetHeadersAndFooters.java" >}}

### **Inserire una grafica in un'intestazione o piè di pagina**

La classe [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) ha i metodi [**setHeadPicture**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setHeaderPicture-int-byte[]-) e [**setFooterPicture**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setFooterPicture-int-byte[]-) per aggiungere immagini a intestazioni e piè di pagina di un foglio di lavoro. Questi metodi richiedono due parametri:

- **Sezione**, la sezione dell'intestazione o del piè di pagina in cui verrà posizionata l'immagine. Ci sono tre sezioni: sinistra, centro e destra, rappresentate dai valori numerici 0, 1 e 2 rispettivamente.
- **File InputStream**, i dati grafici. I dati binari dovrebbero essere scritti nel buffer di un array di byte.

Dopo aver eseguito il codice e aperto il file, controlla l'intestazione del foglio di lavoro in Microsoft Excel:

1. Nel menu **File**, seleziona **Imposta pagina**.
1. Nella finestra di dialogo Imposta pagina, seleziona la scheda **Intestazione/Piè di pagina**.

**Inserimento di una grafica in un'intestazione/piè di pagina** 

![todo:image_alt_text](page-setup-features_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-InsertImageInHeaderFooter-InsertImageInHeaderFooter.java" >}}

### **Inserire una grafica solo nell'intestazione della prima pagina**

La classe [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) ha anche altri metodi utili, ad esempio [**setPicture**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setPicture-boolean-boolean-boolean-int-byte[]-), [**setFirstPageHeader**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setFirstPageHeader-int-java.lang.String-), [**setFirstPageFooter**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setFirstPageFooter-int-java.lang.String-), per aggiungere immagini nell'intestazione/piè di pagina della prima pagina di un foglio di lavoro. La prima pagina è una pagina speciale: è comune voler visualizzare informazioni speciali, ad esempio un logo aziendale.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-InsertGraphicinFirstPageHeaderOnly-InsertGraphicinFirstPageHeaderOnly.java" >}}

## **Opzioni di stampa**

Le impostazioni di impaginazione di Microsoft Excel forniscono diverse opzioni di stampa (anche chiamate opzioni di foglio) che consentono agli utenti di controllare come le pagine del foglio di lavoro vengono stampate. Queste opzioni di stampa permettono agli utenti di:

- Selezionare un'area di stampa specifica su un foglio di lavoro.
- Stampare i titoli.
- Stampare le linee di griglia.
- Stampare intestazioni di riga e colonna
- Ottenere una qualità di bozza.
- Stampare commenti.
- Stampare errori di cella.
Definire l'ordinamento delle pagine.

Tutte queste opzioni di stampa sono mostrate di seguito.

Opzioni di stampa (foglio) 

![todo:image_alt_text](page-setup-features_5.png)

### **Impostare opzioni di stampa e foglio**

spose.Cells supporta tutte le opzioni di stampa offerte da Microsoft Excel e gli sviluppatori possono configurare facilmente queste opzioni per i fogli di lavoro utilizzando le proprietà offerte dalla classe [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup). Come utilizzare queste proprietà viene discusso di seguito in modo più dettagliato.

### **Impostare l'area di stampa**

Per impostazione predefinita, solo l'area di stampa comprende tutte le aree del foglio di lavoro che contengono dati. Gli sviluppatori possono stabilire un'area di stampa specifica del foglio di lavoro.

Per selezionare una specifica area di stampa, utilizzare la proprietà [**setPrintArea**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintArea) della classe [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup). Assegnare a questa proprietà un intervallo di celle che definisce l'area di stampa.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetPrintArea-SetPrintArea.java" >}}

### **Impostare i titoli di stampa**

Aspose.Cells consente di designare l'intestazione delle righe e delle colonne da ripetere su tutte le pagine di un foglio di lavoro stampato. Per farlo, utilizzare le proprietà [**setPrintTitleColumns**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintTitleColumns) e [**setPrintTitleRows**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintTitleRows) della classe [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup).

Le righe o le colonne che verranno ripetute sono definite passando il loro numero di riga o colonna. Ad esempio, le righe sono definite come $1:$2 e le colonne sono definite come $A:$B.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetPrintTitle-SetPrintTitle.java" >}}

### **Impostare altre opzioni di stampa**

La classe [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) fornisce anche diverse altre proprietà per impostare le opzioni di stampa generali come segue:

- [**setPrintGridlines**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintGridlines), una proprietà booleana che definisce se stampare o non stampare le griglie.
- setPrintHeadings, una proprietà booleana che definisce se stampare o meno le intestazioni di riga e colonna.
- [**setBlackAndWhite**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#BlackAndWhite), una proprietà booleana che definisce se stampare o meno il foglio di lavoro in modalità bianco e nero.
- [**setPrintComments**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintComments), definisce se visualizzare i commenti di stampa sul foglio di lavoro o alla fine del foglio di lavoro.
- [**setPrintDraft**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintDraft), una proprietà booleana che definisce se stampare o meno il foglio di lavoro in modalità bozza.
- [**setPrintErrors**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintErrors), definisce se stampare gli errori delle celle come visualizzati, vuoti, trattini o N/D.

Per impostare le proprietà [**PrintComments**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintComments) e [**PrintErrors**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintErrors), Aspose.Cells fornisce anche due enumerazioni, [**PrintCommentsType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintCommentsType) e [**PrintErrorsType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintErrorsType), che contengono valori predefiniti da assegnare alle proprietà [**setPrintComments**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintComments) e [**setPrintErrors**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintErrors) rispettivamente.

I valori predefiniti nell'enumerazione [**PrintCommentsType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintCommentsType) sono descritti di seguito.

|**Tipi di Commenti di Stampa**|**Descrizione**|
| :- | :- |
|[**PRINT_IN_PLACE**](https://reference.aspose.com/cells/java/com.aspose.cells/printcommentstype#PRINT-IN-PLACE)|Specificare di stampare i commenti come visualizzati sul foglio di lavoro.|
|[**PRINT_NO_COMMENTS**](https://reference.aspose.com/cells/java/com.aspose.cells/printcommentstype#PRINT-NO-COMMENTS)|Specificare di non stampare i commenti.|
|[**PRINT_SHEET_END**](https://reference.aspose.com/cells/java/com.aspose.cells/printcommentstype#PRINT-SHEET-END)|Specificare di stampare i commenti alla fine del foglio di lavoro.|

I valori predefiniti dell'enumerazione [**PrintErrorsType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintErrorsType) sono descritti di seguito.

|**Tipi di Errori di Stampa**|**Descrizione**|
| :- | :- |
|[**PRINT_ERRORS_BLANK**](https://reference.aspose.com/cells/java/com.aspose.cells/printerrorstype#PRINT-ERRORS-BLANK)|Specificare di non stampare gli errori.|
|[**PRINT_ERRORS_DASH**](https://reference.aspose.com/cells/java/com.aspose.cells/printerrorstype#PRINT-ERRORS-DASH)|Specificare di stampare gli errori come "--".|
|[**PRINT_ERRORS_DISPLAYED**](https://reference.aspose.com/cells/java/com.aspose.cells/printerrorstype#PRINT-ERRORS-DISPLAYED)|Specificare di stampare gli errori come visualizzati.|
|[**PRINT_ERRORS_NA**](https://reference.aspose.com/cells/java/com.aspose.cells/printerrorstype#PRINT-ERRORS-NA)|Specificare di stampare gli errori come "#N/A".|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-OtherPrintOptions-OtherPrintOptions.java" >}}

### **Imposta l'Ordine delle Pagine**

La classe [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) fornisce la proprietà [**setOrder**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Order) che viene utilizzata per ordinare la stampa di più pagine del foglio di lavoro. Ci sono due possibilità per ordinare le pagine come segue:

- **Giù poi a destra** stampa tutte le pagine in basso prima di stampare eventuali pagine a destra.
- **A destra poi giù** stampa le pagine da sinistra a destra prima di stampare eventuali pagine sotto.

Aspose.Cells fornisce un'enumerazione, [**PrintOrderType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintOrderType), che contiene tutti i tipi di ordine predefiniti da assegnare al metodo [**setOrder**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Order).

I valori predefiniti dell'enumerazione [**PrintOrderType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintOrderType) sono descritti di seguito.

|**Tipi di Ordine di Stampa**|**Descrizione**|
| :- | :- |
|[**DOWN_THEN_OVER**](https://reference.aspose.com/cells/java/com.aspose.cells/printordertype#DOWN-THEN-OVER)|Stampa prima verso il basso, poi orizzontalmente.|
|[**OVER_THEN_DOWN**](https://reference.aspose.com/cells/java/com.aspose.cells/printordertype#OVER-THEN-DOWN)|Stampa prima orizzontalmente, poi verso il basso.|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetPageOrder-SetPageOrder.java" >}}

## **Rimuovi le impostazioni della stampante esistenti dei fogli di lavoro nel file Excel**

Si prega di visionare questo articolo correlato a questo argomento.

## **Argomenti avanzati**
- [Calcolare il fattore di scala del layout pagina](/cells/it/java/calculate-page-setup-scaling-factor/)
- [Copia le impostazioni del layout pagina dal foglio di origine al foglio di destinazione](/cells/it/java/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/)
- [Determina se le dimensioni del foglio di lavoro sono automatiche](/cells/it/java/determine-if-paper-size-of-worksheet-is-automatic/)
- [Ottieni larghezza e altezza carta dalle impostazioni pagina del foglio di lavoro](/cells/it/java/get-paper-width-and-height-from-pagesetup-of-worksheet/)
- [Implementare un formato carta personalizzato del foglio di lavoro per il rendering](/cells/it/java/implement-custom-paper-size-of-worksheet-for-rendering/)
- [Impostazioni di layout pagina e stampa](/cells/it/java/page-setup-and-printing-options/)
- [Rimuovi le impostazioni della stampante esistenti dei fogli di lavoro nel file Excel](/cells/it/java/remove-existing-printersettings-of-worksheets-in-excel-file/)
{{< app/cells/assistant language="java" >}}
