---
title: Impostazione di intestazioni e piè di pagina
type: docs
weight: 30
url: /it/net/setting-headers-and-footers/
description: Questo articolo spiega come inserire a livello di codice un'immagine nell'intestazione e nel piè di pagina dei fogli di lavoro di Excel impostando l'intestazione e il piè di pagina con i comandi di script utilizzando la libreria C# API o .NET.
keywords: insert image in excel header footer c#, set excel header footer script commands c#
---
{{% alert color="primary" %}}

Intestazioni e piè di pagina sono le righe di testo visualizzate rispettivamente sotto il margine superiore o sopra il margine inferiore. È anche possibile aggiungere intestazioni e piè di pagina ai fogli di lavoro. Intestazioni e piè di pagina possono essere utilizzati per visualizzare informazioni utili come il numero di pagina, il nome dell'autore, il nome dell'argomento o la data e l'ora. Intestazioni e piè di pagina vengono gestiti utilizzando le impostazioni di configurazione della pagina.

{{% /alert %}}

##  **Impostazione di intestazioni e piè di pagina**

Aspose.Cells consente di aggiungere intestazioni e piè di pagina ai fogli di lavoro in fase di esecuzione, ma si consiglia di impostare manualmente intestazioni e piè di pagina in un file predefinito per la stampa. È possibile utilizzare Microsoft Excel come strumento GUI per impostare intestazioni e piè di pagina per risparmiare fatica e tempo di sviluppo. Aspose.Cells può importare il file e salvare le impostazioni.

Per aggiungere intestazioni e piè di pagina in fase di esecuzione, Aspose.Cells fornisce speciali chiamate API e comandi di script per formattare intestazioni e piè di pagina.

###  **Comandi di script**

I comandi di script sono comandi speciali che consentono di impostare la formattazione di intestazioni e piè di pagina.

|**Comandi di script**|**Descrizione**|
| :- | :- |
|&P|Il numero di pagina corrente|
|&G|Una foto|
|&N|Il numero totale di pagine|
|&D|La data corrente|
|&T|L'ora corrente|
|&UN|Il nome del foglio di lavoro|
|&F|Il nome del file senza il relativo percorso|
|&"\<FontName>"|Rappresenta un nome di carattere. Ad esempio: &"Arial"|
|&"\<FontName>, \<FontStyle>"|Rappresenta il nome del carattere con lo stile. Ad esempio: &"Arial,Grassetto"|
|&\<FontSize>|Rappresenta la dimensione del carattere. Ad esempio: "&14abc". Tuttavia, se questo comando è seguito da un numero in chiaro da stampare nell'intestazione, questo dovrebbe essere separato con un carattere di spazio dalla dimensione del carattere. Ad esempio: "&14 123".|

###  **Imposta intestazioni e piè di pagina**

 IL[**Impostazione della pagina**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) class fornisce due metodi,[**Impostaintestazione**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/setheader) E[**Imposta piè di pagina**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/setfooter), utilizzato per aggiungere un'intestazione e un piè di pagina a un foglio di lavoro. Questi metodi accettano solo due parametri:

- **Sezione** – la sezione in cui inserire l'intestazione o il piè di pagina. Ci sono tre sezioni: sinistra, centro e destra, rappresentate rispettivamente da 0, 1 e 2.
- **Sceneggiatura** – lo script da utilizzare per l'intestazione o il piè di pagina. Questo script contiene comandi di script per formattare intestazioni o piè di pagina.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetHeadersAndFooters-1.cs" >}}

###  **Inserisci un'immagine in un'intestazione o in un piè di pagina**

 IL[**Impostazione della pagina**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) class ha due metodi aggiuntivi,[**SetHeaderPicture**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/setheaderpicture) E[**SetFooterPicture**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/setfooterpicture), utilizzato per aggiungere immagini nell'intestazione e nel piè di pagina. Questi metodi accettano i parametri:

- **Sezione**– la sezione dell'intestazione o del piè di pagina in cui verrà posizionata l'immagine. Ci sono tre sezioni, sinistra, centro e destra, rappresentate rispettivamente dai valori 0, 1 e 2.
- **Matrice di byte** – i dati grafici (i dati binari devono essere scritti nel buffer di un array di byte).

Dopo aver eseguito il codice seguente e aperto il file, controlla l'intestazione del foglio di lavoro:

1.  Sul**File** menu, selezionare *Imposta pagina**. Verrà visualizzata una finestra di dialogo.
1.  Seleziona il**Intestazione/piè di pagina** scheda.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-InsertImageInHeaderFooter-1.cs" >}}
