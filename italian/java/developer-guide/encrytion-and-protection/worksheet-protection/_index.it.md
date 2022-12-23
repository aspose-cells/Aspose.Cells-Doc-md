---
title: Proteggi e rimuovi protezione foglio di lavoro
type: docs
weight: 50
url: /it/java/protect-and-unprotect-worksheet/
---
## **Proteggi i fogli di lavoro**

Quando un foglio di lavoro è protetto, le azioni che un utente può eseguire sono limitate. Ad esempio, non possono inserire dati, inserire o eliminare righe o colonne ecc. Le opzioni di protezione generale in Microsoft Excel sono:

- Contenuti
- Oggetti
- Scenari

fogli di lavoro protetti non nascondono né proteggono i dati sensibili, quindi è diverso dalla crittografia dei file. In generale, la protezione del foglio di lavoro è adatta a scopi di presentazione. Impedisce all'utente finale di modificare dati, contenuto e formattazione nel foglio di lavoro.

### **Aggiunta o rimozione della protezione**

 Aspose.Cells offre un corso,[**Cartella di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , che rappresenta un file Excel Microsoft. La classe Workbook contiene un WorksheetCollection che consente di accedere a ciascun foglio di lavoro in un file Excel. Un foglio di lavoro è rappresentato da[**Foglio di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) classe.

 La classe Foglio di lavoro fornisce il[**Proteggere**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#protect(int)) utilizzato per applicare la protezione a un foglio di lavoro. Il metodo Protect accetta i seguenti parametri:

-  Tipo di protezione, il tipo di protezione da applicare al foglio di lavoro. Il tipo di protezione viene applicato con l'aiuto del[**Tipo di protezione**](https://reference.aspose.com/cells/java/com.aspose.cells/ProtectionType) enumerazione.
- Nuova password, la nuova password utilizzata per proteggere il foglio di lavoro.
- Vecchia password, la vecchia password, se il foglio di lavoro è già protetto da password. Se il foglio di lavoro non è già protetto, basta passare un null.

L'enumerazione ProtectionType contiene i seguenti tipi di protezioni predefiniti:

|**Tipi di protezione**|**Descrizione**|
|:- |:- |
|[**TUTTO**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#ALL)|L'utente non può modificare nulla in questo foglio di lavoro|
|[**CONTENUTI**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#CONTENTS)|L'utente non può inserire dati in questo foglio di lavoro|
|[**OGGETTI**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#OBJECTS)|L'utente non può modificare gli oggetti del disegno|
|[**SCENARI**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#SCENARIOS)|L'utente non può modificare gli scenari salvati|
|[**STRUTTURA**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#STRUCTURE)|L'utente non può modificare la struttura salvata|
|[**FINESTRE**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#WINDOWS)|L'utente non può modificare le finestre salvate|
|[**NESSUNO**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#NONE)|Nessuna protezione|

L'esempio seguente mostra come proteggere un foglio di lavoro con una password.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ProtectingWorksheet-ProtectingWorksheet.java" >}}

Dopo che il codice precedente è stato utilizzato per proteggere il foglio di lavoro, controllare la protezione sul foglio di lavoro aprendolo. Una volta aperto il file e provato ad aggiungere alcuni dati al foglio di lavoro, viene visualizzata la seguente finestra di dialogo:

**Una finestra di dialogo che avvisa che un utente non può modificare il foglio di lavoro** 

![cose da fare:immagine_alt_testo](protect-and-unprotect-worksheet_1.png)

Per lavorare sul foglio di lavoro, rimuovere la protezione del foglio di lavoro selezionando il file**Protezione** , poi**Foglio non protetto** dal**Utensili** voce di menu come mostrato di seguito.

**Selezionando la voce di menu Rimuovi protezione foglio** 

![cose da fare:immagine_alt_testo](protect-and-unprotect-worksheet_2.png)

Si apre una finestra di dialogo che richiede una password.

**Immissione della password per rimuovere la protezione del foglio di lavoro** 

![cose da fare:immagine_alt_testo](protect-and-unprotect-worksheet_3.png)

### **Protezione di pochi Cells**

 Potrebbero esserci alcuni scenari in cui è necessario bloccare alcune celle solo nel foglio di lavoro. Se vuoi bloccare alcune celle specifiche nel foglio di lavoro, devi sbloccare tutte le altre celle nel foglio di lavoro. Tutte le celle in un foglio di lavoro sono già inizializzate per il blocco, è possibile verificarlo aprendo qualsiasi file excel in MS Excel e fare clic su**Formato | Cells...** mostrare**Formato Cells** finestra di dialogo e quindi fare clic sulla scheda Protezione e vedere che una casella di controllo denominata "Bloccato" è selezionata per impostazione predefinita.

Di seguito sono riportati i due approcci per implementare l'attività.

**Metodo1:**

seguenti punti descrivono come bloccare alcune celle utilizzando MS Excel. Questo metodo si applica a Microsoft Office Excel 97, 2000, 2002, 2003 e versioni successive.

1. Selezionare l'intero foglio di lavoro facendo clic sul pulsante Seleziona tutto (il rettangolo grigio direttamente sopra il numero di riga per la riga 1 ea sinistra della lettera A della colonna).
1. Scegliere Cells dal menu Formato, fare clic sulla scheda Protezione e quindi deselezionare la casella di controllo Bloccato.

 Questo sblocca tutte le celle del foglio di lavoro

{{% alert color="primary" %}}

Se il comando celle non è disponibile, parti del foglio di lavoro potrebbero già essere bloccate. Nel menu Strumenti, scegliere Protezione e quindi fare clic su Rimuovi protezione foglio.

{{% /alert %}}

1. Seleziona solo le celle che desideri bloccare e ripeti il passaggio 2, ma questa volta seleziona la casella di controllo Bloccato.
1.  Sul**Utensili** menù, selezionare**Protezione** , fare clic**Proteggi Foglio** e quindi fare clic su**OK**.

{{% alert color="primary" %}}

Nella finestra di dialogo Proteggi foglio è possibile specificare una password e selezionare gli elementi che si desidera che gli utenti possano modificare.

{{% /alert %}}

**Metodo2:**

In questo metodo, utilizziamo Aspose.Cells API solo per eseguire l'attività.

L'esempio seguente mostra come proteggere alcune celle nel foglio di lavoro. Sblocca prima tutte le celle nel foglio di lavoro e quindi blocca 3 celle (A1, B1, C1) al suo interno. Infine, protegge il foglio di lavoro. Una riga/colonna ha uno stile API che contiene inoltre un metodo Locked impostato. È possibile utilizzare questo metodo per bloccare o sbloccare la riga/colonna.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ProtectingSpecificCellsinaWorksheet-ProtectingSpecificCellsinaWorksheet.java" >}}

### **Proteggi una riga nel foglio di lavoro**

 Aspose.Cells consente di bloccare facilmente qualsiasi riga nel foglio di lavoro. Qui, possiamo utilizzare[**applicastile()**](https://reference.aspose.com/cells/java/com.aspose.cells/row#applyStyle(com.aspose.cells.Style,%20com.aspose.cells.StyleFlag) ) metodo di[**Riga**](https://reference.aspose.com/cells/java/com.aspose.cells/Row) class per applicare Style a una particolare riga nel foglio di lavoro. Questo metodo accetta due argomenti: a[**Stile**](https://reference.aspose.com/cells/java/com.aspose.cells/Style) oggetto e[**StyleFlag**](https://reference.aspose.com/cells/java/com.aspose.cells/StyleFlag) struct che contiene tutti i membri relativi alla formattazione applicata.

L'esempio seguente mostra come proteggere una riga nel foglio di lavoro. Sblocca prima tutte le celle nel foglio di lavoro e quindi blocca la prima riga al suo interno. Infine, protegge il foglio di lavoro. Una riga/colonna ha uno stile API che contiene inoltre un metodo setCellLocked. Puoi bloccare o sbloccare la riga/colonna utilizzando la struttura StyleFlag.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ProtectRowWorksheet-ProtectRowWorksheet.java" >}}

### **Proteggi una colonna nel foglio di lavoro**

 Aspose.Cells consente di bloccare facilmente qualsiasi colonna nel foglio di lavoro. Qui, possiamo utilizzare[**applicastile()**](https://reference.aspose.com/cells/java/com.aspose.cells/column#applyStyle(com.aspose.cells.Style,%20com.aspose.cells.StyleFlag) ) metodo di[**Colonna**](https://reference.aspose.com/cells/java/com.aspose.cells/Column) class per applicare Style a una particolare colonna nel foglio di lavoro. Questo metodo accetta due argomenti: a[**Stile**](https://reference.aspose.com/cells/java/com.aspose.cells/Style) oggetto e[**StyleFlag**](https://reference.aspose.com/cells/java/com.aspose.cells/StyleFlag) struct che contiene tutti i membri relativi alla formattazione applicata.

L'esempio seguente mostra come proteggere una colonna nel foglio di lavoro. Sblocca prima tutte le celle nel foglio di lavoro e quindi blocca la prima colonna al suo interno. Infine, protegge il foglio di lavoro. Una riga/colonna ha uno stile API che contiene inoltre un metodo Locked impostato. Puoi bloccare o sbloccare la riga/colonna utilizzando la struttura StyleFlag.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ProtectColumnWorksheet-ProtectColumnWorksheet.java" >}}

## **Rimuovere la protezione di un foglio di lavoro**

[Protezione dei fogli di lavoro](/cells/it/java/protect-and-unprotect-worksheet/#protect-worksheets) e[Impostazioni di protezione avanzata da Excel XP](/cells/it/java/protect-and-unprotect-worksheet/#advanced-protection-settings-since-excel-xp) discusso diversi approcci alla protezione dei fogli di lavoro. Cosa succede se uno sviluppatore deve rimuovere la protezione da un foglio di lavoro protetto in fase di esecuzione in modo da poter apportare alcune modifiche al file? Questo può essere fatto facilmente con Aspose.Cells.

### **Utilizzando Microsoft Excel**

Per rimuovere la protezione da un foglio di lavoro:

 Dal**Utensili** menù, selezionare**Protezione** seguito da**Foglio non protetto**.

**Selezionando Rimuovi protezione foglio** 

![cose da fare:immagine_alt_testo](protect-and-unprotect-worksheet_4.png)

La protezione viene rimossa, a meno che il foglio di lavoro non sia protetto da password. In questo caso, una finestra di dialogo richiede la password.

**Immissione della password per rimuovere la protezione del foglio di lavoro** 

![cose da fare:immagine_alt_testo](protect-and-unprotect-worksheet_5.png)

### **Utilizzando Aspose.Cells**

 Un foglio di lavoro può essere non protetto chiamando il metodo[**Foglio di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) classe'[**Non protetto**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#unprotect() ) metodo. Il[**Non protetto**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#unprotect()) può essere utilizzato in due modi, descritti di seguito.

### **Rimozione della protezione di un foglio di lavoro Simply Protected**

Un foglio di lavoro semplicemente protetto è uno che non è protetto da una password. Tali fogli di lavoro possono essere sprotetti chiamando il metodo unprotect senza passare un parametro.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-UnprotectingSimplyProtectedWorksheet-UnprotectingSimplyProtectedWorksheet.java" >}}

### **Rimozione della protezione di un foglio di lavoro protetto da password**

Un foglio di lavoro protetto da password è protetto da una password. Tali fogli di lavoro possono essere sprotetti chiamando una versione di overload del metodo Unprotect che accetta la password come parametro.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-UnprotectProtectSheet-UnprotectProtectSheet.java" >}}

## **Impostazioni di protezione avanzata da Excel XP**

[Protezione dei fogli di lavoro](/cells/it/java/protect-and-unprotect-worksheet/#protect-worksheets) ha discusso della protezione di un foglio di lavoro in Microsoft Excel 97 e 2000. Ma dal rilascio di Excel 2002 o XP, Microsoft ha aggiunto molte impostazioni di protezione avanzate. Queste impostazioni di protezione limitano o consentono agli utenti di:

- Elimina righe o colonne.
- Modifica contenuti, oggetti o scenari.
- Formatta celle, righe o colonne.
- Inserisci righe, colonne o collegamenti ipertestuali.
- Seleziona le celle bloccate o sbloccate.
- Usa le tabelle pivot e molto altro.

Aspose.Cells supporta tutte le impostazioni di protezione avanzate offerte da Excel XP e versioni successive.

### **Impostazioni di protezione avanzata tramite Excel XP e versioni successive**

Per visualizzare le impostazioni di protezione disponibili in Excel XP:

1.  Dal**Utensili** menù, selezionare**Protezione** seguito da**Proteggi Foglio**.
 Viene visualizzata una finestra di dialogo.

   **Finestra di dialogo per mostrare le opzioni di protezione in Excel XP**

![cose da fare:immagine_alt_testo](protect-and-unprotect-worksheet_6.png)

1. Consenti o limita le funzionalità dei fogli di lavoro o applica una password.

### **Impostazioni di protezione avanzata utilizzando Aspose.Cells**

Aspose.Cells supporta tutte le impostazioni di protezione avanzate.

 Aspose.Cells offre un corso,[**Cartella di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , che rappresenta un file Excel Microsoft. La classe Workbook contiene una raccolta WorksheetCollection che consente l'accesso a ogni foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato da[**Foglio di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) classe.

 La classe Worksheet fornisce la proprietà Protection utilizzata per applicare queste impostazioni di protezione avanzate. La proprietà Protection è infatti un oggetto del[**Protezione**](https://reference.aspose.com/cells/java/com.aspose.cells/protection) classe che incapsula diverse proprietà booleane per disabilitare o abilitare le restrizioni.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AdvancedProtectionSettingsUsingAsposeCells-AdvancedProtectionSettingsUsingAsposeCells.java" >}}

Di seguito è riportato un piccolo esempio di applicazione. Apre un file Excel e utilizza la maggior parte delle impostazioni di protezione avanzate supportate da Excel XP e versioni successive.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AdvancedProtection-AdvancedProtection.java" >}}

{{% alert color="primary" %}}

Salvare il file nel formato EXCEL97TO2003 o XLSX poiché queste impostazioni di protezione avanzata sono supportate solo da MS Excel XP e versioni successive.

{{% /alert %}}

### **Cell Problema di blocco**

Se si desidera impedire agli utenti di modificare le celle, le celle devono essere bloccate prima che vengano applicate le impostazioni di protezione. Altrimenti le celle possono essere modificate anche se il foglio di lavoro è protetto. In Microsoft Excel XP, le celle possono essere bloccate tramite la seguente finestra di dialogo:

**Finestra di dialogo per bloccare le celle in Excel XP** 

![cose da fare:immagine_alt_testo](protect-and-unprotect-worksheet_7.png)

È possibile bloccare le celle anche utilizzando lo Aspose.Cells API. Ogni cella ha uno stile API che contiene inoltre un metodo setLocked. Usalo per bloccare o sbloccare le celle.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-LockCell-LockCell.java" >}}
