---
title: Proteggere e Difendere il Foglio di Lavoro
type: docs
weight: 50
url: /it/java/protect-and-unprotect-worksheet/
---

## **Proteggere i fogli di lavoro**

Quando un foglio di lavoro è protetto, le azioni che un utente può compiere sono limitate. Ad esempio, non possono inserire dati, inserire o eliminare righe o colonne, ecc. Le opzioni generali di protezione in Microsoft Excel sono:

- Contenuti
- Oggetti
- Scenari

I fogli di lavoro protetti non nascondono o proteggono dati sensibili, quindi è diverso dalla crittografia del file. In generale, la protezione del foglio di lavoro è adatta per scopi di presentazione. Impedisce all'utente finale di modificare i dati, il contenuto e la formattazione nel foglio di lavoro.

### **Aggiunta o Rimozione della Protezione**

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), che rappresenta un file Microsoft Excel. La classe Workbook contiene una WorksheetCollection che consente di accedere a ciascun foglio di lavoro in un file di Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet).

La classe Worksheet fornisce il metodo [**Protect**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#protect(int)) che viene utilizzato per applicare la protezione a un foglio di lavoro. Il metodo Protect accetta i seguenti parametri:

- Tipo di Protezione, il tipo di protezione da applicare al foglio di lavoro. Il tipo di protezione è applicato con l'aiuto dell'enumerazione [**ProtectionType**](https://reference.aspose.com/cells/java/com.aspose.cells/ProtectionType).
- Nuova password, la nuova password utilizzata per proteggere il foglio di lavoro.
- Vecchia Password, la vecchia password, se il foglio di lavoro è già protetto da password. Se il foglio di lavoro non è già protetto, passare semplicemente un valore null.

L'enumerazione ProtectionType contiene i seguenti tipi di protezione predefiniti:

|**Tipi di protezione**|**Descrizione**|
| :- | :- |
|[**ALL**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#ALL)|L'utente non può modificare nulla in questo foglio di lavoro|
|[**CONTENTS**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#CONTENTS)|L'utente non può inserire dati in questo foglio di lavoro|
|[**OBJECTS**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#OBJECTS)|L'utente non può modificare gli oggetti disegnati|
|[**SCENARIOS**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#SCENARIOS)|L'utente non può modificare gli scenari salvati|
|[**STRUCTURE**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#STRUCTURE)|L'utente non può modificare la struttura salvata|
|[**WINDOWS**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#WINDOWS)|L'utente non può modificare le finestre salvate|
|[**NONE**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#NONE)|Nessuna protezione|

L'esempio seguente mostra come proteggere un foglio di lavoro con una password.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ProtectingWorksheet-ProtectingWorksheet.java" >}}

Dopo aver utilizzato il codice precedente per proteggere il foglio di lavoro, controllare la protezione sul foglio di lavoro aprendolo. Una volta aperto il file e cercare di aggiungere dei dati al foglio di lavoro, verrà visualizzata la seguente finestra di dialogo:

**Una finestra di dialogo che avverte che un utente non può modificare il foglio di lavoro** 

![todo:image_alt_text](protect-and-unprotect-worksheet_1.png)

Per lavorare sul foglio di lavoro, rimuovere la protezione selezionando **Protezione**, quindi **Rimuovi Protezione Foglio** dal menu **Strumenti** come mostrato di seguito.

**Selezione dell'opzione di menu Rimuovi Protezione Foglio** 

![todo:image_alt_text](protect-and-unprotect-worksheet_2.png)

Si apre un dialogo che richiede una password.

**Immettere la password per sbloccare il foglio di lavoro** 

![todo:image_alt_text](protect-and-unprotect-worksheet_3.png)

### **Proteggere alcune celle**

Potrebbero esserci certi scenari in cui è necessario bloccare solo alcune celle nel foglio di lavoro. Se si desidera bloccare alcune celle specifiche nel foglio di lavoro, è necessario sbloccare tutte le altre celle nel foglio di lavoro. Tutte le celle in un foglio di lavoro sono già inizializzate per il blocco, è possibile verificare ciò aprendo qualsiasi file excel in MS Excel e cliccando su **Formato | Celle...** per mostrare la finestra di dialogo **Formato celle** e quindi fare clic sulla scheda Protezione e vedere che la casella di controllo denominata "Bloccata" è già spuntata per impostazione predefinita.

Di seguito sono illustrate le due modalità per implementare il compito.

**Metodo1:**

I punti seguenti descrivono come bloccare alcune celle utilizzando MS Excel. Questo metodo si applica a Microsoft Office Excel 97, 2000, 2002, 2003 e versioni superiori.

1. Seleziona l'intero foglio di lavoro facendo clic sul pulsante Seleziona tutto (il rettangolo grigio direttamente sopra il numero di riga per la riga 1 e alla sinistra della lettera della colonna A).
1. Fare clic su Celle nel menu Formato, fare clic sulla scheda Protezione e quindi deselezionare la casella di controllo Bloccata.

   Questo sblocca tutte le celle sul foglio di lavoro

{{% alert color="primary" %}}

Se il comando celle non è disponibile, alcune parti del foglio di lavoro potrebbero già essere bloccate. Nel menu Strumenti, passare a Protezione e quindi fare clic su Annulla protezione foglio.

{{% /alert %}}

1. Selezionare solo le celle che si desidera bloccare e ripetere il passaggio 2, ma questa volta selezionare la casella di controllo Bloccata.
1. Nel menu **Strumenti**, selezionare **Protezione**, fare clic su **Proteggi foglio** e poi su **OK**.

{{% alert color="primary" %}}

Nella finestra di dialogo Proteggi foglio, hai la possibilità di specificare una password e selezionare gli elementi che desideri che gli utenti possano modificare.

{{% /alert %}}

**Metodo2:**

In questo metodo, utilizziamo solo l'API Aspose.Cells per eseguire il compito.

L'esempio seguente mostra come proteggere alcune celle nel foglio di lavoro. Sblocca tutte le celle nel foglio di lavoro e quindi blocca 3 celle (A1, B1, C1) in esso. Infine, protegge il foglio di lavoro. Una riga/colonna ha un'API Style che contiene ulteriormente un metodo setLocked . È possibile utilizzare questo metodo per bloccare o sbloccare la riga/colonna.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ProtectingSpecificCellsinaWorksheet-ProtectingSpecificCellsinaWorksheet.java" >}}

### **Proteggere una riga nel foglio di lavoro**

Aspose.Cells consente di bloccare facilmente qualsiasi riga nel foglio di lavoro. Qui, possiamo utilizzare il metodo [**applyStyle()**](https://reference.aspose.com/cells/java/com.aspose.cells/row#applyStyle(com.aspose.cells.Style,%20com.aspose.cells.StyleFlag)) della classe [**Row**](https://reference.aspose.com/cells/java/com.aspose.cells/Row) per applicare uno stile a una riga specifica nel foglio di lavoro. Questo metodo richiede due argomenti: un oggetto [**Style**](https://reference.aspose.com/cells/java/com.aspose.cells/Style) e una struttura [**StyleFlag**](https://reference.aspose.com/cells/java/com.aspose.cells/StyleFlag) che ha tutti i membri relativi alla formattazione applicata.

L'esempio seguente mostra come proteggere una riga nel foglio di lavoro. Sblocca tutte le celle nel foglio di lavoro e quindi blocca la prima riga. Infine protegge il foglio di lavoro. Una riga/colonna ha un'API Style che contiene ulteriormente un metodo setCellLocked . È possibile bloccare o sbloccare la riga/colonna utilizzando la struttura StyleFlag.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ProtectRowWorksheet-ProtectRowWorksheet.java" >}}

### **Proteggere una colonna nel foglio di lavoro**

Aspose.Cells consente di bloccare facilmente qualsiasi colonna nel foglio di lavoro. Qui possiamo utilizzare il metodo [**applyStyle()**](https://reference.aspose.com/cells/java/com.aspose.cells/column#applyStyle(com.aspose.cells.Style,%20com.aspose.cells.StyleFlag)) della classe [**Column**](https://reference.aspose.com/cells/java/com.aspose.cells/Column) per applicare uno stile a una colonna specifica nel foglio di lavoro. Questo metodo richiede due argomenti: un oggetto [**Style**](https://reference.aspose.com/cells/java/com.aspose.cells/Style) e una struttura [**StyleFlag**](https://reference.aspose.com/cells/java/com.aspose.cells/StyleFlag) che contiene tutti i membri relativi al formato applicato.

L'esempio seguente mostra come proteggere una colonna nel foglio di lavoro. Sblocca prima tutte le celle nel foglio di lavoro e quindi blocca la prima colonna. Infine, protegge il foglio di lavoro. Una riga/colonna ha una API di stile che contiene il metodo set Locked. È possibile bloccare o sbloccare la riga/colonna utilizzando la struttura StyleFlag.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ProtectColumnWorksheet-ProtectColumnWorksheet.java" >}}

## **Sblocca un foglio di lavoro**

[Protezione dei fogli di lavoro](/cells/it/java/protect-and-unprotect-worksheet/#protect-worksheets) e [Impostazioni di protezione avanzate da Excel XP in poi](/cells/it/java/protect-and-unprotect-worksheet/#advanced-protection-settings-since-excel-xp) discutono approcci diversi per proteggere i fogli di lavoro. Cosa succede se uno sviluppatore ha bisogno di rimuovere la protezione da un foglio di lavoro protetto durante l'esecuzione in modo che possano apportare alcune modifiche al file? Questo può essere facilmente fatto con Aspose.Cells.

### **Utilizzando Microsoft Excel**

Per rimuovere la protezione da un foglio di lavoro:

Dal menu **Strumenti**, seleziona **Protezione** seguito da **Sblocca foglio**.

**Selezione di Sblocca foglio** 

![todo:image_alt_text](protect-and-unprotect-worksheet_4.png)

La protezione viene rimossa, a meno che il foglio di lavoro sia protetto da password. In tal caso, compare un messaggio che richiede la password.

**Immettere la password per sbloccare il foglio di lavoro** 

![todo:image_alt_text](protect-and-unprotect-worksheet_5.png)

### **Usare Aspose.Cells**

Un foglio di lavoro può essere sbloccato chiamando il metodo [**Unprotect**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#unprotect--) della classe [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). Il metodo [**Unprotect**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#unprotect--) può essere utilizzato in due modi, descritti di seguito.

### **Sbloccare un foglio di lavoro semplicemente protetto**

Un foglio di lavoro semplicemente protetto è uno che non è protetto da password. Tali fogli di lavoro possono essere sbloccati chiamando il metodo sblocca senza passare un parametro.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-UnprotectingSimplyProtectedWorksheet-UnprotectingSimplyProtectedWorksheet.java" >}}

### **Sbloccare un foglio di lavoro protetto da password**

Un foglio di lavoro protetto da password è uno protetto da una password. Tali fogli di lavoro possono essere sbloccati chiamando una versione sovraccaricata del metodo sblocca che richiede la password come parametro.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-UnprotectProtectSheet-UnprotectProtectSheet.java" >}}

## **Impostazioni di protezione avanzate da Excel XP in poi**

[Protezione dei fogli di lavoro](/cells/it/java/protect-and-unprotect-worksheet/#protect-worksheets) discute della protezione di un foglio di lavoro in Microsoft Excel 97 e 2000. Ma dal rilascio di Excel 2002 o XP, Microsoft ha aggiunto molte impostazioni di protezione avanzate. Queste impostazioni di protezione limitano o consentono agli utenti di:

- Eliminare righe o colonne.
- Modificare contenuti, oggetti o scenari.
- Formattare celle, righe o colonne.
- Inserire righe, colonne o collegamenti ipertestuali.
- Selezionare celle bloccate o sbloccate.
- Usare tabelle pivot e molto altro.

Aspose.Cells supporta tutte le impostazioni avanzate di protezione offerte da Excel XP e versioni successive.

### **Impostazioni di protezione avanzate utilizzando Excel XP e versioni successive**

Per visualizzare le impostazioni di protezione disponibili in Excel XP:

1. Dal menu **Strumenti**, seleziona **Protezione** seguito da **Proteggi foglio**.
   Viene visualizzata una finestra di dialogo.

   **Finestra di dialogo per mostrare le opzioni di protezione in Excel XP**

![todo:image_alt_text](protect-and-unprotect-worksheet_6.png)

1. Consentire o limitare le funzionalità dei fogli di lavoro o applicare una password.

### **Impostazioni di protezione avanzate utilizzando Aspose.Cells**

Aspose.Cells supporta tutte le impostazioni avanzate di protezione.

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), che rappresenta un file Microsoft Excel. La classe Workbook contiene una raccolta WorksheetCollection che consente l'accesso a ogni foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet).

La classe Worksheet fornisce la proprietà Protection che viene utilizzata per applicare queste impostazioni di protezione avanzate. La proprietà Protection è infatti un oggetto della classe [**Protection**](https://reference.aspose.com/cells/java/com.aspose.cells/protection) che racchiude diverse proprietà booleane per disabilitare o abilitare le restrizioni.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AdvancedProtectionSettingsUsingAsposeCells-AdvancedProtectionSettingsUsingAsposeCells.java" >}}

Di seguito è riportato un piccolo esempio di applicazione. Apre un file Excel e utilizza la maggior parte delle impostazioni avanzate di protezione supportate da Excel XP e versioni successive.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AdvancedProtection-AdvancedProtection.java" >}}

{{% alert color="primary" %}}

Salva il file in formato EXCEL97TO2003 o XLSX perché queste impostazioni avanzate di protezione sono supportate solo dalle versioni di MS Excel XP e successive.

{{% /alert %}}

### **Problema di blocco delle celle**

Se si desidera impedire agli utenti di modificare le celle, le celle devono essere bloccate prima di applicare qualsiasi impostazione di protezione. In caso contrario, le celle possono essere modificate anche se il foglio di lavoro è protetto. In Microsoft Excel XP, le celle possono essere bloccate attraverso la seguente finestra di dialogo:

**Finestra di dialogo per bloccare le celle in Excel XP** 

![todo:image_alt_text](protect-and-unprotect-worksheet_7.png)

È possibile bloccare le celle anche utilizzando l'API Aspose.Cells. Ogni cella ha un'API di stile che contiene ulteriori un metodo setLocked. Usalo per bloccare o sbloccare le celle.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-LockCell-LockCell.java" >}}
