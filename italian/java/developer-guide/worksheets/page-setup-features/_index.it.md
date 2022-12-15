---
title: Funzioni di impostazione della pagina
type: docs
weight: 40
url: /it/java/page-setup-features/
---
A volte, è necessario configurare le impostazioni di impostazione della pagina per i fogli di lavoro per controllare la stampa. Queste impostazioni di configurazione della pagina offrono varie opzioni.

**Opzioni pagina** 

![cose da fare:immagine_alt_testo](page-setup-features_1.png)

Le opzioni di impostazione della pagina sono completamente supportate in Aspose.Cells. Questo articolo spiega come impostare le opzioni della pagina con Aspose.Cells.

## **Impostazione delle opzioni della pagina**

 Aspose.Cells offre un corso,[**Cartella di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , che rappresenta un file Microsoft Excel. La classe Workbook contiene una raccolta di fogli di lavoro che consente l'accesso a ciascun foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato da[**Foglio di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) classe.

La classe Worksheet fornisce la proprietà PageSetup, utilizzata per impostare le opzioni di impostazione della pagina. Infatti, la proprietà PageSetup è un oggetto della classe PageSetup che rende possibile impostare le opzioni di layout di pagina per un foglio di lavoro stampato. La classe PageSetup fornisce varie proprietà utilizzate per impostare le opzioni di impostazione della pagina. Alcune di queste proprietà sono discusse di seguito.

### **Orientamento della pagina**

 L'orientamento della pagina può essere impostato su verticale o orizzontale utilizzando il[**Impostazione della pagina**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) classe'[**setOrientation(PageOrientationType)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Orientation) metodo. Il[**setOrientation(PageOrientationType)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Orientation) metodo prende il[**TipoOrientamentoPagina**](https://reference.aspose.com/cells/java/com.aspose.cells/PageOrientationType) enumerazione come parametro. I membri del[**TipoOrientamentoPagina**](https://reference.aspose.com/cells/java/com.aspose.cells/PageOrientationType)enumerazione sono elencati di seguito.

|**Tipi di orientamento della pagina**|**Descrizione**|
|:- |:- |
|[**PAESAGGIO**](https://reference.aspose.com/cells/java/com.aspose.cells/pageorientationtype#LANDSCAPE)|Orientamento orizzontale|
|[**RITRATTO**](https://reference.aspose.com/cells/java/com.aspose.cells/pageorientationtype#PORTRAIT)|Orientamento verticale|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-PageOrientation-PageOrientation.java" >}}

### **Fattore di scala**

 È possibile ridurre o ingrandire le dimensioni di un foglio di lavoro regolando il fattore di scala con il[**setZoom**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Zoom) metodo del[**Impostazione della pagina**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) classe.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ScalingFactor-ScalingFactor.java" >}}

### **Opzioni FitToPages**

 Per adattare il contenuto del foglio di lavoro a un numero specifico di pagine, utilizzare il file[**Impostazione della pagina**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) classe'[**setFitToPagesTall**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FitToPagesTall) e[**setFitToPagesWide**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FitToPagesWide) metodi. Questi metodi vengono utilizzati anche per ridimensionare i fogli di lavoro.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-FitToPagesOptions-FitToPagesOptions.java" >}}

### **Dimensioni del foglio**

 Impostare il formato carta su cui verranno stampati i fogli di lavoro utilizzando il file[**Impostazione della pagina**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) classe'[**Dimensioni del foglio**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PaperSize) proprietà. La proprietà PaperSize accetta uno dei valori predefiniti in[**PaperSizeType**](https://reference.aspose.com/cells/java/com.aspose.cells/PaperSizeType) enumerazione, di seguito elencati.

|**Tipi di formato carta**|**Descrizione**|
|:- |:- |
|Carta 10x14|10 pollici x 14 pollici|
|Carta 11x17|11 pollici x 17 pollici|
|CartaA3|A3 (297 mm x 420 mm)|
|CartaA4|A4 (210 x 297 mm)|
|CartaA4Piccolo|A4 piccolo (210 mm x 297 mm)|
|Carta A5|A5 (148 mm x 210 mm)|
|CartaB3|B3 (13,9 x 19,7 pollici)|
|CartaB4|B4 (250 x 354 mm)|
|Carta B5|B5 (182 x 257 mm)|
|CartaBusinessCard|Biglietto da visita (90 mm x 55 mm)|
|CartaCFoglio|Foglio formato C|
|CartaDFoglio|Foglio di dimensione D|
|Busta di carta10|Busta n. 10 (4-1/8 pollici x 9-1/2 pollici)|
|Busta di carta11|Busta n. 11 (4-1/2 pollici x 10-3/8 pollici)|
|Busta di carta12|Busta n. 12 (4-1/2 pollici x 11 pollici)|
|Busta di carta14|Busta n. 14 (5 pollici x 11-1/2 pollici)|
|Busta di carta9|Busta n. 9 (3-7/8 pollici x 8-7/8 pollici)|
|Busta di cartaB4|Busta B4 (250 mm x 353 mm)|
|Busta di cartaB5|Busta B5 (176 mm x 250 mm)|
|Busta di cartaB6|Busta B6 (176 mm x 125 mm)|
|Busta di cartaC3|Busta C3 (324 mm x 458 mm)|
|Busta di cartaC4|Busta C4 (229 mm x 324 mm)|
|Busta di cartaC5|Busta C5 (162 mm x 229 mm)|
|Busta di cartaC6|Busta C6 (114 mm x 162 mm)|
|Busta di cartaC65|Busta C65 (114 mm x 229 mm)|
|Busta di cartaDL|Busta DL (110 mm x 220 mm)|
|CartaBustaItalia|Busta Italia (110 mm x 230 mm)|
|Busta di cartaMonarca|Busta Monarch (3-7/8 pollici x 7-1/2 pollici)|
|Busta di carta Personale|Busta (3-5/8 pollici x 6-1/2 pollici)|
|CartaEFoglio|Foglio taglia E|
|PaperExecutive|Esecutivo (7-1/2 pollici x 10-1/2 pollici)|
|PaperFanfoldLegaleTedesco|Fanfold legale tedesco (8-1/2 pollici x 13 pollici)|
|PaperFanfoldStdTedesco|Standard tedesco Fanfold (8-1/2 in. x 12 in.)|
|PaperFanfoldUS|Standard statunitense a modulo continuo (14-7/8 pollici x 11 pollici)|
|CartaFolio|Folio (8-1/2 pollici x 13 pollici)|
|PaperLedger|Libro mastro (17 pollici x 11 pollici)|
|PaperLegal|Legale (8-1/2 pollici x 14 pollici)|
|CartaLettera|Lettera (8-1/2 pollici x 11 pollici)|
|CartaLetteraPiccolo|Lettera piccola (8-1/2 pollici x 11 pollici)|
|CartaNota|Nota (8-1/2 pollici x 11 pollici)|
|PaperQuarto|Quarto (215 mm x 275 mm)|
|Dichiarazione cartacea|Dichiarazione (5-1/2 pollici x 8-1/2 pollici)|
|Carta Tabloid|Tabloid (11 pollici x 17 pollici)|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ManagePaperSize-ManagePaperSize.java" >}}

### **Qualità di stampa**

 Impostare la qualità di stampa dei fogli di lavoro da stampare con il[**Impostazione della pagina**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) classe'[**setPrintQuality**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintQuality) metodo. L'unità di misura per la qualità di stampa è punti per pollice (DPI).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetPrintQuality-SetPrintQuality.java" >}}

### **Numero prima pagina**

 Avviare la numerazione delle pagine del foglio di lavoro utilizzando il file[**Impostazione della pagina**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) classe'[**setNumeroPrimaPagina**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FirstPageNumber) metodo. Il metodo setFirstPageNumber imposta il numero di pagina della prima pagina del foglio di lavoro e le pagine successive sono numerate in ordine crescente.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetFirstPageNumber-SetFirstPageNumber.java" >}}

## **Impostazione dei margini**

Aspose.Cells supporta completamente le opzioni di impostazione della pagina di Microsoft Excel. Gli sviluppatori potrebbero dover configurare le impostazioni di configurazione della pagina per i fogli di lavoro per controllare il processo di stampa. Questo argomento illustra come utilizzare Aspose.Cells per configurare i margini della pagina.

**Margini della pagina in Microsoft Excel**

![cose da fare:immagine_alt_testo](page-setup-features_2.png)

 Aspose.Cells offre un corso,[**Cartella di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)che rappresenta un file Microsoft Excel. La classe Workbook contiene la raccolta Worksheets che consente l'accesso a ciascun foglio di lavoro in un file Excel. Un foglio di lavoro è rappresentato da[**Foglio di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) classe.

 La classe Worksheet fornisce la proprietà PageSetup, utilizzata per impostare le opzioni di impostazione della pagina. L'attributo PageSetup è un oggetto di[**Impostazione della pagina**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) class che rende possibile impostare diverse opzioni di layout di pagina per un foglio di lavoro stampato. La classe PageSetup fornisce varie proprietà e metodi utilizzati per impostare le opzioni di impostazione della pagina.

### **Margini della pagina**

 Imposta i margini (sinistro, destro, superiore, inferiore) di una pagina con[**Impostazione della pagina**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) membri della classe. Di seguito sono elencati alcuni dei metodi utilizzati per specificare i margini della pagina:

- [**setLeftMargin(int)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#LeftMargin)
- [**setRightMargin(int)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#RightMargin)
- [**setTopMargin(int)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#TopMargin)
- [**setBottomMargin(int)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#BottomMargin)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetMargins-SetMargins.java" >}}

### **Centra sulla pagina**

 È possibile centrare qualcosa su una pagina orizzontalmente e verticalmente. Il[**Impostazione della pagina**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) la classe ha membri per questo scopo:[**setCenterHorizontally**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#CenterHorizontally) e[**setCenterVerticalmente**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#CenterVertically).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-CenterOnPage-CenterOnPage.java" >}}

### **Margini di intestazione e piè di pagina**

Imposta i margini di intestazione e piè di pagina con[**Impostazione della pagina**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) membri come[**setHeaderMargin**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#HeaderMargin) e[**setFooterMargin**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FooterMargin).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-HeaderAndFooterMargins-HeaderAndFooterMargins.java" >}}

## **Impostazione di intestazioni e piè di pagina**

Intestazioni e piè di pagina sono le sezioni di testo e immagini sopra il margine superiore o sotto il margine inferiore di una pagina. È anche possibile aggiungere intestazioni e piè di pagina ai fogli di lavoro. Intestazioni e piè di pagina possono essere utilizzati per visualizzare qualsiasi tipo di informazione utile, ad esempio numero di pagina, nome dell'autore, titolo del documento o data e ora. Anche intestazioni e piè di pagina vengono gestiti utilizzando la finestra di dialogo Imposta pagina.

**La finestra di dialogo Imposta pagina** 

![cose da fare:immagine_alt_testo](page-setup-features_3.png)

Aspose.Cells consente di aggiungere intestazioni e piè di pagina ai fogli di lavoro in fase di esecuzione, ma si consiglia di impostare manualmente intestazioni e piè di pagina in un file preimpostato per la stampa. È possibile utilizzare Microsoft Excel come strumento GUI per impostare facilmente intestazioni e piè di pagina per ridurre i tempi di sviluppo. Aspose.Cells può importare il file e riservare queste impostazioni.

Per aggiungere intestazioni e piè di pagina in fase di esecuzione, Aspose.Cells fornisce classi speciali e alcuni comandi di script per controllare la formattazione.

### **Comandi di script**

I comandi di script sono comandi speciali forniti da Aspose.Cells che consentono agli sviluppatori di formattare intestazioni e piè di pagina.

|**Comandi di script**|**Descrizione**|
|:- |:- |
|&P|Il numero di pagina corrente.|
|&G|Una foto.|
|&N|Il numero totale di pagine.|
|&D|La data corrente.|
|&T|L'ora corrente.|
|&UN|Il nome del foglio di lavoro.|
|&F|Il nome del file senza il percorso.|
|&"\<FontName>"|Un nome di carattere. Ad esempio: &"Arial"|
|&"\<FontName>, \<FontStyle>"|Un nome di carattere con uno stile. Ad esempio: &"Arial,Grassetto"|
|&\<FontSize>|Rappresenta la dimensione del carattere. Ad esempio: "&14abc". Tuttavia, se questo comando è seguito da un numero in chiaro da stampare nell'intestazione, questo dovrebbe essere separato con un carattere di spazio dalla dimensione del carattere. Ad esempio: "&14 123".|

### **Imposta intestazioni e piè di pagina**

 Il[**Impostazione della pagina**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) la classe fornisce il metodo[**setHeader**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setHeader(int,%20java.lang.String) per aggiungere un'intestazione e[**setFooter**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setFooter(int,%20java.lang.String)) per aggiungere un piè di pagina a un foglio di lavoro. Lo script viene utilizzato come argomento per tutti i metodi sopra menzionati. Rappresenta lo script da utilizzare per l'intestazione o il piè di pagina. Questo script contiene comandi di script per formattare intestazioni o piè di pagina.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetHeadersAndFooters-SetHeadersAndFooters.java" >}}

### **Inserisci una grafica in un'intestazione o in un piè di pagina**

 Il[**Impostazione della pagina**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) class ha i metodi[**setHeadPicture**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setHeaderPicture(int,%20byte[]) ) e[**setFooterPicture**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setFooterPicture(int,%20byte[])) per aggiungere immagini all'intestazione e al piè di pagina di un foglio di lavoro. Questi metodi accettano due parametri:

- **Sezione**, la sezione dell'intestazione o del piè di pagina in cui verrà posizionata l'immagine. Ci sono tre sezioni: sinistra, centro e destra, rappresentate rispettivamente dai valori numerici 0, 1 e 2.
- **File InputStream**, i dati grafici. I dati binari devono essere scritti nel buffer di un array di byte.

Dopo aver eseguito il codice e aperto il file, controlla l'intestazione del foglio di lavoro in Microsoft Excel:

1.  Sul**File** menù, selezionare**Impostazione della pagina**.
1.  Nella finestra di dialogo Imposta pagina, selezionare il**Intestazione/piè di pagina** scheda.

**Inserimento di un grafico in un'intestazione/piè di pagina** 

![cose da fare:immagine_alt_testo](page-setup-features_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-InsertImageInHeaderFooter-InsertImageInHeaderFooter.java" >}}

### **Inserisci un'immagine solo nell'intestazione della prima pagina**

 Il[**Impostazione della pagina**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) class ha anche altri metodi utili, per esempio[**setPicture**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setPicture(boolean,%20boolean,%20boolean,%20int,%20byte[])), [**setFirstPageHeader**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setFirstPageHeader(int,%20java.lang.String)), [**setFirstPageFooter**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setFirstPageFooter(int,%20java.lang.String)), per aggiungere immagini nell'intestazione/piè di pagina della prima pagina di un foglio di lavoro. La prima pagina è una pagina speciale: è comune volere che mostri informazioni speciali, ad esempio un logo aziendale.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-InsertGraphicinFirstPageHeaderOnly-InsertGraphicinFirstPageHeaderOnly.java" >}}

## **Impostazione delle opzioni di stampa**

Le impostazioni di impostazione della pagina di Microsoft Excel forniscono diverse opzioni di stampa (dette anche opzioni del foglio) che consentono agli utenti di controllare come vengono stampate le pagine del foglio di lavoro. Queste opzioni di stampa consentono agli utenti di:

- Selezionare un'area di stampa specifica su un foglio di lavoro.
- Stampa titoli.
- Stampa griglia.
- Stampa le intestazioni di righe e colonne
- Ottieni una bozza di qualità.
- Stampa commenti.
- Stampa gli errori della cella.
- Definire l'ordine delle pagine.

Tutte queste opzioni di stampa sono mostrate di seguito.

**Opzioni di stampa (foglio).** 

![cose da fare:immagine_alt_testo](page-setup-features_5.png)

### **Impostazione delle opzioni di stampa e foglio**

 spose.Cells supporta tutte le opzioni di stampa offerte da Microsoft Excel e gli sviluppatori possono facilmente configurare queste opzioni per i fogli di lavoro utilizzando le proprietà offerte dal[**Impostazione della pagina**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup)classe. Il modo in cui queste proprietà vengono utilizzate è discusso di seguito in modo più dettagliato.

### **Imposta area di stampa**

Per impostazione predefinita, solo l'area di stampa incorpora tutte le aree del foglio di lavoro che contengono dati. Gli sviluppatori possono stabilire un'area di stampa specifica del foglio di lavoro.

 Per selezionare un'area di stampa specifica, utilizzare il[**Impostazione della pagina**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) classe'[**setPrintArea**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintArea) proprietà. Assegnare a questa proprietà un'area di celle che definisce l'area di stampa.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetPrintArea-SetPrintArea.java" >}}

### **Imposta i titoli di stampa**

 Aspose.Cells consente di designare le intestazioni di riga e colonna da ripetere su tutte le pagine di un foglio di lavoro stampato. Per farlo, usa il[**Impostazione della pagina**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) classe'[**setPrintTitleColumns**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintTitleColumns) e[**setPrintTitleRows**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintTitleRows) proprietà.

Le righe o le colonne che verranno ripetute vengono definite passando i loro numeri di riga o colonna. Ad esempio, le righe sono definite come $1:$2 e le colonne sono definite come $A:$B.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetPrintTitle-SetPrintTitle.java" >}}

### **Imposta altre opzioni di stampa**

 Il[**Impostazione della pagina**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) class fornisce anche diverse altre proprietà per impostare le opzioni di stampa generali come segue:

- [**setPrintGridlines**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintGridlines), una proprietà booleana che definisce se stampare o meno le linee della griglia.
- [*setPrintHeadings*](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintHeadings), una proprietà booleana che definisce se stampare o meno le intestazioni di righe e colonne.
- [**setBlackAndWhite**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#BlackAndWhite), una proprietà booleana che definisce se stampare il foglio di lavoro in modalità bianco e nero o meno.
- [**setPrintComments**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintComments), definisce se visualizzare i commenti di stampa sul foglio di lavoro o alla fine del foglio di lavoro.
- [**setStampaBozza**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintDraft), una proprietà booleana che definisce se stampare il foglio di lavoro in qualità bozza o meno.
- [**setPrintErrors**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintErrors), definisce se stampare gli errori della cella come visualizzato, vuoto, trattino o N/D.

 Per impostare il[**StampaCommenti**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintComments) e[**Errori di stampa**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintErrors) properties, Aspose.Cells fornisce anche due enumerazioni,[**PrintCommentsType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintCommentsType) e[**PrintErrorsType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintErrorsType) che contengono valori predefiniti da assegnare al file[**setPrintComments**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintComments) e[**setPrintErrors**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintErrors) proprietà rispettivamente.

 I valori predefiniti in[**PrintCommentsType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintCommentsType) enumerazione sono descritti di seguito.

|**Stampa tipi di commenti**|**Descrizione**|
|:- |:- |
|[**STAMPA_IN_PLACE**](https://reference.aspose.com/cells/java/com.aspose.cells/printcommentstype#PRINT_IN_PLACE)|Specifica di stampare i commenti come visualizzati sul foglio di lavoro.|
|[**PRINT_NO_COMMENTI**](https://reference.aspose.com/cells/java/com.aspose.cells/printcommentstype#PRINT_NO_COMMENTS)|Specifica di non stampare i commenti.|
|[**PRINT_SHEET_END**](https://reference.aspose.com/cells/java/com.aspose.cells/printcommentstype#PRINT_SHEET_END)|Specifica di stampare i commenti alla fine del foglio di lavoro.|

 I valori predefiniti di[**PrintErrorsType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintErrorsType) enumerazione sono descritti di seguito.

|**Tipi di errori di stampa**|**Descrizione**|
|:- |:- |
|[*PRINT_ERRORS_BLANK*](https://reference.aspose.com/cells/java/com.aspose.cells/printerrorstype#PRINT_ERRORS_BLANK)|Specifica di non stampare gli errori.|
|[**PRINT_ERRORS_DASH**](https://reference.aspose.com/cells/java/com.aspose.cells/printerrorstype#PRINT_ERRORS_DASH)|Specifica di stampare gli errori come "--".|
|[**PRINT_ERRORS_DISPLAYED**](https://reference.aspose.com/cells/java/com.aspose.cells/printerrorstype#PRINT_ERRORS_DISPLAYED)|Specifica di stampare gli errori come visualizzati.|
|[**PRINT_ERRORS_NA**](https://reference.aspose.com/cells/java/com.aspose.cells/printerrorstype#PRINT_ERRORS_NA)|Specifica di stampare gli errori come "#N/D".|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-OtherPrintOptions-OtherPrintOptions.java" >}}

### **Imposta l'ordine delle pagine**

 Il[**Impostazione della pagina**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) la classe fornisce il[**setOrder**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Order) proprietà utilizzata per ordinare la stampa di più pagine del foglio di lavoro. Ci sono due possibilità per ordinare le pagine come segue:

- **Giù poi sopra** stampa tutte le pagine in basso prima di stampare quelle a destra.
- **Sopra e poi giù** stampa le pagine da sinistra a destra prima di stampare le pagine sottostanti.

 Aspose.Cells fornisce un'enumerazione,[**PrintOrderType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintOrderType) , che contiene tutti i tipi di ordine predefiniti da assegnare[**setOrder**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Order) metodo.

 I valori predefiniti di[**PrintOrderType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintOrderType) enumerazione sono descritti di seguito.

|**Tipi di ordini di stampa**|**Descrizione**|
|:- |:- |
|[**DOWN_THEN_OVER**](https://reference.aspose.com/cells/java/com.aspose.cells/printordertype#DOWN_THEN_OVER)|Stampa verso il basso, poi di nuovo.|
|[**OVER_THEN_DOWN**](https://reference.aspose.com/cells/java/com.aspose.cells/printordertype#OVER_THEN_DOWN)|Stampa sopra, poi giù.|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetPageOrder-SetPageOrder.java" >}}

## **Rimuovi le impostazioni della stampante esistente dei fogli di lavoro nel file Excel**

Si prega di consultare questo articolo relativo a questo argomento.

## **Argomenti avanzati**
- [Calcola il fattore di scala dell'impostazione della pagina](/cells/it/java/calculate-page-setup-scaling-factor/)
- [Copia le impostazioni di impostazione della pagina dal foglio di lavoro di origine nel foglio di lavoro di destinazione](/cells/it/java/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/)
- [Determinare se il formato carta del foglio di lavoro è automatico](/cells/it/java/determine-if-paper-size-of-worksheet-is-automatic/)
- [Ottieni larghezza e altezza della carta da PageSetup del foglio di lavoro](/cells/it/java/get-paper-width-and-height-from-pagesetup-of-worksheet/)
- [Implementa il formato carta personalizzato del foglio di lavoro per il rendering](/cells/it/java/implement-custom-paper-size-of-worksheet-for-rendering/)
- [Impostazioni di pagina e opzioni di stampa](/cells/it/java/page-setup-and-printing-options/)
- [Rimuovi le impostazioni della stampante esistente dei fogli di lavoro nel file Excel](/cells/it/java/remove-existing-printersettings-of-worksheets-in-excel-file/)
