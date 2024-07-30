---
title: Impostazione Intestazioni e piè di pagina
type: docs
weight: 30
url: /it/python-net/setting-headers-and-footers/
description: Questo articolo spiega come inserire programmaticamente un immagine nell intestazione e nel piè di pagina dei fogli di lavoro di Excel impostando l intestazione e il piè di pagina con comandi di script utilizzando l API Aspose.Cells per Python via .NET.
keywords: Libreria Excel Python, inserire immagine nell intestazione e nel piè di pagina di Excel, impostare comandi di script per l intestazione e il piè di pagina di Excel usando Python.
---

{{% alert color="primary" %}}

Le intestazioni e i piè di pagina sono le linee di testo visualizzate sotto il margine superiore o sopra il margine inferiore rispettivamente. È possibile aggiungere intestazioni e piè di pagina anche ai fogli di lavoro. Le intestazioni e i piè di pagina possono essere utilizzati per visualizzare informazioni utili come il numero di pagina, il nome dell'autore, il nome del tema o la data e l'ora. Le intestazioni e i piè di pagina sono gestiti utilizzando le impostazioni della pagina di setup.

{{% /alert %}}

## **Impostazione di intestazioni e piè di pagina**

Aspose.Cells per Python via .NET consente di aggiungere intestazioni e piè di pagina ai fogli di lavoro in fase di esecuzione, ma consigliamo di impostare manualmente le intestazioni e i piè di pagina in un file pre-progettato per la stampa. Puoi utilizzare Microsoft Excel come strumento GUI per impostare intestazioni e piè di pagina per risparmiare sforzi e tempo di sviluppo. Aspose.Cells per Python via .NET può importare il file e salvare le impostazioni.

Per aggiungere intestazioni e piè di pagina in fase di esecuzione, Aspose.Cells per Python via .NET fornisce chiamate API speciali e comandi di script per formattare intestazioni e piè di pagina.

### **Comandi di script**

I comandi di script sono comandi speciali che consentono di impostare la formattazione di intestazioni e piè di pagina.

|**Comandi di script**|**Descrizione**|
| :- | :- |
|&P|Numero di pagina corrente|
|&G|Un'immagine|
|&N|Il numero totale di pagine|
|&D|La data corrente|
|&T|L'orario corrente|
|&A|Il nome del foglio di lavoro|
|&F|Il nome del file senza percorso|
|&"\<FontName>"|Rappresenta un nome di carattere. Ad esempio: &"Arial"|
|&"\<FontName>, \<FontStyle>"|Rappresenta il nome del carattere con lo stile. Ad esempio: &"Arial,Grassetto"|
|&\<FontSize>|Rappresenta la dimensione del carattere. Ad esempio: “&14abc”. Ma, se questo comando è seguito da un numero normale da stampare nell'intestazione, questo dovrebbe essere separato da un carattere spazio dalla dimensione del carattere. Ad esempio: “&14 123”.|

### **Come impostare Intestazioni e Piè di Pagina**

La classe [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) fornisce due metodi, [**set_header**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/set_header/#int-str) e [**set_footer**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/set_footer/#int-str), utilizzati per aggiungere un'intestazione e un piè di pagina a un foglio di lavoro. Questi metodi richiedono solo due parametri:

- **Sezione** – la sezione in cui dovrebbe essere posizionata l'intestazione o il piè di pagina. Ci sono tre sezioni: sinistra, centro e destra, rappresentate rispettivamente da 0, 1 e 2.
- **Script** – lo script da utilizzare per l'intestazione o il piè di pagina. Questo script contiene comandi di script per formattare l'intestazione o il piè di pagina.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-SetHeadersAndFooters-1.py" >}}

### **Come Inserire un'Immagine in un'intestazione o piè di pagina**

La classe [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) ha due metodi aggiuntivi, [**set_header_picture**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/set_header_picture/#int-bytes) e [**set_footer_picture**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/set_footer_picture/#int-bytes), utilizzati per aggiungere immagini all'intestazione e al piè di pagina. Questi metodi accettano i parametri:

- **Sezione** – la sezione dell'intestazione o del piè di pagina in cui verrà posizionata l'immagine. Ci sono tre sezioni, sinistra, centro e destra, rappresentate dai valori 0, 1 e 2 rispettivamente.
- **Array di byte** – i dati grafici (i dati binari devono essere scritti nel buffer di un array di byte).

Dopo aver eseguito il codice sottostante e aperto il file, controlla l'intestazione del foglio di lavoro:

1. Nel menu **File**, seleziona **Imposta pagina**. Verrà visualizzata una finestra di dialogo.
1. Seleziona la scheda **Intestazione/Piè di pagina**.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-InsertImageInHeaderFooter-1.py" >}}
