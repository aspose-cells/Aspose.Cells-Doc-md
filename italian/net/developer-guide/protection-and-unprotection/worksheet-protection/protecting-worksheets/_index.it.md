---
title: Protezione dei fogli di lavoro
type: docs
weight: 10
url: /it/net/protecting-worksheets/
---

{{% alert color="primary" %}}

Quando un foglio di lavoro è protetto, le azioni che un utente può compiere sono limitate. Ad esempio, non possono inserire dati, inserire o eliminare righe o colonne, ecc.

{{% /alert %}}

## **Proteggere i fogli di lavoro**

### **Introduzione**

Le opzioni generali di protezione in Microsoft Excel sono:

- Contenuti
- Oggetti
- Scenari

I fogli di lavoro protetti non nascondono o proteggono dati sensibili, quindi è diverso dalla crittografia dei file. In generale, la protezione del foglio di lavoro è adatta per scopi di presentazione. Impedisce all'utente finale di modificare i dati, il contenuto e la formattazione nel foglio di lavoro.

### **Proteggere un foglio di lavoro**

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contiene una collezione [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) che consente l'accesso a ciascun foglio di lavoro in un file Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet).

La classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) fornisce il metodo [**Protect**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/protect/index) che viene utilizzato per applicare la protezione sul foglio di lavoro. Il metodo [**Protect**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/protect/methods/1) accetta i seguenti parametri:

- Tipo di protezione, il tipo di protezione da applicare sul foglio di lavoro. Il tipo di protezione viene applicato con l'aiuto dell'enumerazione [**ProtectionType**](https://reference.aspose.com/cells/net/aspose.cells/protectiontype).
- Nuova password, la nuova password utilizzata per proteggere il foglio di lavoro.
- Vecchia password, la vecchia password, se il foglio di lavoro è già protetto da password. Se il foglio di lavoro non è già protetto, passare semplicemente null.

L'enumerazione [**ProtectionType**](https://reference.aspose.com/cells/net/aspose.cells/protectiontype) contiene i seguenti tipi di protezione predefiniti:

|**Tipi di protezione**|**Descrizione**|
| :- | :- |
|All|L'utente non può modificare nulla in questo foglio di lavoro|
|Contents|L'utente non può inserire dati in questo foglio di lavoro|
|Objects|L'utente non può modificare oggetti disegno|
|Scenarios|L'utente non può modificare scenari salvati|
|Structure|L'utente non può modificare la struttura|
|Windows|La protezione è applicata alle finestre|
|None|Nessuna protezione è applicata|

L'esempio seguente mostra come proteggere un foglio di lavoro con una password.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-ProtectingWorksheet-1.cs" >}}

Dopo che il codice sopra è utilizzato per proteggere il foglio di lavoro, è possibile verificare la protezione sul foglio di lavoro aprendolo. Una volta aperto il file e tentato di aggiungere alcuni dati al foglio di lavoro, si vedrà il seguente dialogo:

|**Un avviso di dialogo che l'utente non può modificare il foglio di lavoro**|
| :- |
|![todo:image_alt_text](protecting-worksheets_1.png)|

Per lavorare sul foglio di lavoro, sblocca il foglio di lavoro selezionando **Protezione**, poi **Sblocca foglio** dal menu **Strumenti**.

Dopo aver selezionato Sblocca foglio nel menu, si aprirà una finestra di dialogo che richiederà di inserire la password in modo da poter lavorare sul foglio di lavoro come mostrato di seguito:

|![todo:image_alt_text](protecting-worksheets_2.png)|

### **Proteggere alcune celle nel foglio di lavoro utilizzando Microsoft Excel**

Potrebbero esserci determinati scenari in cui è necessario bloccare solo alcune celle nel foglio di lavoro. Se si desidera bloccare alcune celle specifiche nel foglio di lavoro, è necessario sbloccare tutte le altre celle del foglio di lavoro. Tutte le celle in un foglio di lavoro sono già inizializzate per essere bloccate, è possibile verificare ciò aprendo qualsiasi file excel in MS Excel e facendo clic su **Formato | Celle...** per visualizzare la finestra di dialogo **Formato celle** e quindi fare clic sulla scheda **Protezione** e verificare se la casella di controllo denominata "Bloccata" è selezionata per impostazione predefinita.

I punti seguenti descrivono come bloccare alcune celle utilizzando MS Excel. Questo metodo si applica a Microsoft Office Excel 97, 2000, 2002, 2003 e versioni superiori.

1. Selezionare l'intero foglio di lavoro facendo clic sul pulsante **Seleziona tutto** (il rettangolo grigio direttamente sopra il numero di riga per la riga 1 e alla sinistra della lettera della colonna A).
1. Fare clic su **Celle** nel menu **Formato**, fare clic sulla scheda **Protezione** e deselezionare la casella di controllo **Bloccata**.
   Questo sblocca tutte le celle sul foglio di lavoro
   Se il comando **Celle** non è disponibile, parti del foglio di lavoro potrebbero già essere bloccate. Nel menu **Strumenti**, posizionarsi su **Protezione**, e quindi fare clic su **Sblocca foglio**.
1. Selezionare solo le celle che si desidera bloccare e ripetere il passaggio 2, ma questa volta selezionare la casella di controllo **Bloccata**.
1. Nel menu **Strumenti**, posizionarsi su **Protezione**, fare clic su **Proteggi foglio** e quindi fare clic su **OK**.
1. Nella finestra di dialogo **Proteggi foglio**, è possibile specificare una password e selezionare gli elementi che si desidera consentire agli utenti di modificare.

### **Proteggere alcune celle nel foglio di lavoro utilizzando Aspose Cells**

In questo metodo, utilizziamo solo l'API Aspose.Cells per eseguire il compito.

Esempio: L'esempio seguente mostra come proteggere alcune celle nel foglio di lavoro. Prima sblocca tutte le celle nel foglio di lavoro e poi blocca 3 celle (A1, B1, C1). Infine, protegge il foglio di lavoro. L'oggetto [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) contiene una proprietà booleana, [**IsLocked**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked). È possibile impostare la proprietà [**IsLocked**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked) su vero o falso e applicare il metodo *Column/Row.ApplyStyle()* per bloccare o sbloccare la riga/colonna con gli attributi desiderati.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-ProtectingSpecificCellsinaWorksheet-1.cs" >}}

### **Proteggere una riga nel foglio di lavoro**

Aspose.Cells consente di bloccare facilmente qualsiasi riga nel foglio di lavoro. Qui, possiamo utilizzare il metodo [**ApplyStyle()**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/applystyle) della classe [**Aspose.Cells.Row**](https://reference.aspose.com/cells/net/aspose.cells/row) per applicare [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) a una particolare riga nel foglio di lavoro. Questo metodo richiede due argomenti: un oggetto [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) e un oggetto [**StyleFlag**](https://reference.aspose.com/cells/net/aspose.cells/styleflag) che ha tutti i membri relativi alla formattazione applicata.

L'esempio seguente mostra come proteggere una riga nel foglio di lavoro. Prima sblocca tutte le celle nel foglio di lavoro e quindi blocca la prima riga in esso. Infine, protegge il foglio di lavoro. L'oggetto [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) contiene una proprietà booleana, [**IsLocked**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked). È possibile impostare la proprietà [**IsLocked**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked) su vero o falso per bloccare o sbloccare la riga/colonna utilizzando l'oggetto [**StyleFlag**](https://reference.aspose.com/cells/net/aspose.cells/styleflag).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-ProtectingSpecificRowInWorksheet-1.cs" >}}

### **Proteggere una colonna nel foglio di lavoro**

Aspose.Cells consente di bloccare facilmente qualsiasi colonna nel foglio di lavoro. Qui, possiamo utilizzare il metodo [**ApplyStyle()**](https://reference.aspose.com/cells/net/aspose.cells/column/methods/applystyle) della classe [**Aspose.Cells.Column**](https://reference.aspose.com/cells/net/aspose.cells/column) per applicare [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) a una particolare colonna nel foglio di lavoro. Questo metodo richiede due argomenti: un oggetto [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) e un oggetto [**StyleFlag**](https://reference.aspose.com/cells/net/aspose.cells/styleflag) che ha tutti i membri relativi alla formattazione applicata.

L'esempio seguente mostra come proteggere una colonna nel foglio di lavoro. Sblocca prima tutte le celle nel foglio di lavoro e quindi blocca la prima colonna in esso. Infine, protegge il foglio di lavoro. L'oggetto [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) contiene una proprietà booleana, [**IsLocked**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked). Puoi impostare la proprietà [**IsLocked**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked) su true o false per bloccare o sbloccare la riga/colonna utilizzando l'oggetto [**StyleFlag**](https://reference.aspose.com/cells/net/aspose.cells/styleflag).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-ProtectColumnWorksheet-1.cs" >}}

### **Consenti agli utenti di modificare intervalli**

L'esempio seguente mostra come consentire agli utenti di modificare un intervallo in un foglio di lavoro protetto.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-EditRangesWorksheet-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
