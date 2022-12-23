---
title: Protezione dei fogli di lavoro
type: docs
weight: 10
url: /it/net/protecting-worksheets/
---
{{% alert color="primary" %}}

Quando un foglio di lavoro è protetto, le azioni che un utente può eseguire sono limitate. Ad esempio, non possono inserire dati, inserire o eliminare righe o colonne ecc.

{{% /alert %}}

## **Proteggi i fogli di lavoro**

### **introduzione**

Le opzioni di protezione generale in Microsoft Excel sono:

- Contenuti
- Oggetti
- Scenari

I fogli di lavoro protetti non nascondono né proteggono i dati sensibili, quindi è diverso dalla crittografia dei file. In generale, la protezione del foglio di lavoro è adatta a scopi di presentazione. Impedisce all'utente finale di modificare dati, contenuto e formattazione nel foglio di lavoro.

### **Proteggi un foglio di lavoro**

 Aspose.Cells offre un corso,[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) che rappresenta un file Excel Microsoft. Il[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la classe contiene un[**Fogli di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) raccolta che consente l'accesso a ciascun foglio di lavoro in un file Excel. Un foglio di lavoro è rappresentato da[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)classe.

 Il[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) la classe fornisce il[**Proteggere**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/protect/index) metodo utilizzato per applicare la protezione al foglio di lavoro.[**Proteggere**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/protect/methods/1) metodo accetta i seguenti parametri:

-  Tipo di protezione, il tipo di protezione da applicare al foglio di lavoro. Il tipo di protezione viene applicato con l'aiuto del[**Tipo di protezione**](https://reference.aspose.com/cells/net/aspose.cells/protectiontype)enumerazione.
- Nuova password, la nuova password utilizzata per proteggere il foglio di lavoro.
- Vecchia password, la vecchia password, se il foglio di lavoro è già protetto da password. Se il foglio di lavoro non è già protetto, basta passare null.

 Il[**Tipo di protezione**](https://reference.aspose.com/cells/net/aspose.cells/protectiontype)L'enumerazione contiene i seguenti tipi di protezioni predefiniti:

|**Tipi di protezione**|**Descrizione**|
|:- |:- |
|Tutti|L'utente non può modificare nulla in questo foglio di lavoro|
|Contenuti|L'utente non può inserire dati in questo foglio di lavoro|
|Oggetti|L'utente non può modificare gli oggetti del disegno|
|Scenari|L'utente non può modificare gli scenari salvati|
|Struttura|L'utente non può modificare la struttura|
|Windows|La protezione viene applicata alle finestre|
|Nessuno|Non viene applicata alcuna protezione|

L'esempio seguente mostra come proteggere un foglio di lavoro con una password.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-ProtectingWorksheet-1.cs" >}}

Dopo che il codice precedente è stato utilizzato per proteggere il foglio di lavoro, è possibile verificare la protezione sul foglio di lavoro aprendolo. Una volta aperto il file e provato ad aggiungere alcuni dati al foglio di lavoro, verrà visualizzata la seguente finestra di dialogo:

|**Una finestra di dialogo che avvisa che un utente non può modificare il foglio di lavoro**|
|:- |
|![cose da fare:immagine_alt_testo](protecting-worksheets_1.png)|

Per lavorare sul foglio di lavoro, rimuovere la protezione del foglio di lavoro selezionando il file**Protezione** , poi**Foglio non protetto** dal**Utensili** elemento del menu.

Dopo aver selezionato la voce di menu Unprotect Sheet, si aprirà una finestra di dialogo che ti chiederà di inserire la password in modo da poter lavorare sul foglio di lavoro come mostrato di seguito:

|![cose da fare:immagine_alt_testo](protecting-worksheets_2.png)|

### **Proteggi alcuni Cells nel foglio di lavoro utilizzando Microsoft Excel**

 Potrebbero esserci alcuni scenari in cui è necessario bloccare alcune celle solo nel foglio di lavoro. Se vuoi bloccare alcune celle specifiche nel foglio di lavoro, devi sbloccare tutte le altre celle nel foglio di lavoro. Tutte le celle in un foglio di lavoro sono già inizializzate per il blocco, è possibile verificarlo aprendo qualsiasi file excel in MS Excel e fare clic su**Formato | Cells...** mostrare**Formato Cells**finestra di dialogo e quindi fare clic su**Protezione** scheda e vedere una casella di controllo denominata "Bloccato" è selezionata per impostazione predefinita.

seguenti punti descrivono come bloccare alcune celle utilizzando MS Excel. Questo metodo si applica a Microsoft Office Excel 97, 2000, 2002, 2003 e versioni successive.

1.  Selezionare l'intero foglio di lavoro facendo clic su**Seleziona tutto** pulsante (il rettangolo grigio direttamente sopra il numero di riga per la riga 1 ea sinistra della lettera A della colonna).
1.  Clic**Cells** sul**Formato** menu, fare clic su**Protezione** scheda, quindi deselezionare il file**Bloccato** casella di controllo.
 Questo sblocca tutte le celle del foglio di lavoro
 Se la**Cells** comando non è disponibile, parti del foglio di lavoro potrebbero già essere bloccate. Sul**Utensili** menu, punta a**Protezione** e quindi fare clic su**Foglio non protetto**.
1.  Seleziona solo le celle che desideri bloccare e ripeti il passaggio 2, ma questa volta seleziona il**Bloccato** casella di controllo.
1.  Sul**Utensili** menu, punta a**Protezione** , fare clic**Proteggi Foglio** e quindi fare clic**OK**.
1.  Nel**Proteggi Foglio** finestra di dialogo, è possibile specificare una password e selezionare gli elementi che si desidera che gli utenti possano modificare.

### **Proteggi alcuni Cells nel foglio di lavoro utilizzando Aspose Cells**

In questo metodo, utilizziamo Aspose.Cells API solo per eseguire l'attività.

 Esempio: l'esempio seguente mostra come proteggere alcune celle nel foglio di lavoro. Sblocca prima tutte le celle nel foglio di lavoro e quindi blocca 3 celle (A1, B1, C1) al suo interno. Infine, protegge il foglio di lavoro. Il[**Stile**](https://reference.aspose.com/cells/net/aspose.cells/style)oggetto contiene una proprietà booleana,[**È bloccato**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked) . Puoi impostare[**È bloccato**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked) proprietà su vero o falso e applicare*Colonna/Riga.ApplyStyle()* metodo per bloccare o sbloccare la riga/colonna con gli attributi desiderati.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-ProtectingSpecificCellsinaWorksheet-1.cs" >}}

### **Proteggi una riga nel foglio di lavoro**

 Aspose.Cells consente di bloccare facilmente qualsiasi riga nel foglio di lavoro. Qui, possiamo utilizzare[**Applicastile()**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/applystyle) metodo di[**Aspose.Cells.Row**](https://reference.aspose.com/cells/net/aspose.cells/row) classe da applicare[**Stile**](https://reference.aspose.com/cells/net/aspose.cells/style) a una particolare riga del foglio di lavoro. Questo metodo accetta due argomenti: a[**Stile**](https://reference.aspose.com/cells/net/aspose.cells/style) oggetto e[**StyleFlag**](https://reference.aspose.com/cells/net/aspose.cells/styleflag) oggetto che ha tutti i membri relativi alla formattazione applicata.

 L'esempio seguente mostra come proteggere una riga nel foglio di lavoro. Sblocca prima tutte le celle nel foglio di lavoro e quindi blocca la prima riga al suo interno. Infine, protegge il foglio di lavoro. Il[**Stile**](https://reference.aspose.com/cells/net/aspose.cells/style) oggetto contiene una proprietà booleana,[**È bloccato**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked) . Puoi impostare[**È bloccato**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked) proprietà su true o false per bloccare o sbloccare la riga/colonna utilizzando il[**StyleFlag**](https://reference.aspose.com/cells/net/aspose.cells/styleflag)oggetto.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-ProtectingSpecificRowInWorksheet-1.cs" >}}

### **Proteggi una colonna nel foglio di lavoro**

 Aspose.Cells consente di bloccare facilmente qualsiasi colonna nel foglio di lavoro. Qui, possiamo utilizzare[**Applicastile()**](https://reference.aspose.com/cells/net/aspose.cells/column/methods/applystyle) metodo di[**Aspose.Cells.Column**](https://reference.aspose.com/cells/net/aspose.cells/column) classe da applicare[**Stile**](https://reference.aspose.com/cells/net/aspose.cells/style) a una particolare colonna del foglio di lavoro. Questo metodo accetta due argomenti: a[**Stile**](https://reference.aspose.com/cells/net/aspose.cells/style) oggetto e[**StyleFlag**](https://reference.aspose.com/cells/net/aspose.cells/styleflag)oggetto che ha tutti i membri relativi alla formattazione applicata.

L'esempio seguente mostra come proteggere una colonna nel foglio di lavoro. Sblocca prima tutte le celle nel foglio di lavoro e quindi blocca la prima colonna al suo interno. Infine, protegge il foglio di lavoro. Il[**Stile**](https://reference.aspose.com/cells/net/aspose.cells/style) oggetto contiene una proprietà booleana,[**È bloccato**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked) . Puoi impostare[**È bloccato**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked) proprietà su true o false per bloccare o sbloccare la riga/colonna utilizzando il[**StyleFlag**](https://reference.aspose.com/cells/net/aspose.cells/styleflag)oggetto.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-ProtectColumnWorksheet-1.cs" >}}

### **Consenti agli utenti di modificare gli intervalli**

L'esempio seguente mostra come consentire agli utenti di modificare un intervallo in un foglio di lavoro protetto.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-EditRangesWorksheet-1.cs" >}}
