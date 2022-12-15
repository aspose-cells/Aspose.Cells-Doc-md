---
title: Crea e formatta la tabella
type: docs
weight: 10
url: /it/cpp/create-and-format-table/
---
## **Crea tabella**
Uno dei vantaggi dei fogli di calcolo è che consentono di creare diversi tipi di elenchi, ad esempio elenchi telefonici, elenchi di attività, elenchi di transazioni, attività o passività. Diversi utenti possono lavorare insieme per utilizzare, creare e mantenere vari elenchi.

Aspose.Cells supporta la creazione e la gestione di Liste.
### **Vantaggi di un oggetto elenco**
Ci sono alcuni vantaggi quando si converte un elenco di dati in un vero oggetto elenco

- Nuove righe e colonne vengono incluse automaticamente.
- È possibile aggiungere facilmente una riga totale in fondo all'elenco per visualizzare SUM, AVERAGE, COUNT, ecc.
- Le colonne aggiunte a destra vengono incorporate automaticamente nell'oggetto List.
- I grafici basati su righe e colonne verranno espansi automaticamente.
- Gli intervalli denominati assegnati a righe e colonne verranno espansi automaticamente.
- L'elenco è protetto dall'eliminazione accidentale di righe e colonne.
### **Creazione di un oggetto elenco utilizzando Microsoft Excel**

|**Selezione dell'intervallo di dati per la creazione dell'oggetto Elenco**|
|:- |
|![cose da fare:immagine_alt_testo](jHcNq4o.png)|
Viene visualizzata la finestra di dialogo Crea elenco.

|**Finestra di dialogo Crea elenco**|
|:- |
|![cose da fare:immagine_alt_testo](kJmukRF.png)|
 Implementazione dell'oggetto List per i dati e specifica della riga totale (Select**Dati** , poi**Elenco** , seguito da**Riga totale**).

|**Creazione di un oggetto elenco**|
|:- |
|![cose da fare:immagine_alt_testo](ECSGVdR.png)|
### **Utilizzo dell'API Aspose.Cells**
 Aspose.Cells offre un corso[Cartella di lavoro](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) che rappresenta un file Microsoft Excel. Il[Cartella di lavoro](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) la classe contiene un[Fogli di lavoro](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)raccolta che consente l'accesso a ciascun foglio di lavoro in un file Excel.

 Un foglio di lavoro è rappresentato da[Foglio di lavoro](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) classe. Il[Foglio di lavoro](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) fornisce una vasta gamma di metodi per la gestione di un foglio di lavoro. Per creare un[IListOggetto](https://reference.aspose.com/cells/cpp/class/aspose.cells.tables.i_list_object) in un foglio di lavoro, usa il[GetIListObjects](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#a4356bc4b8cffee624891f10ea49a4705) metodo di raccolta del[Foglio di lavoro](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) classe. Ogni `[IListObject]` è infatti un oggetto del[IListObjectCollection](https://reference.aspose.com/cells/cpp/class/aspose.cells.tables.i_list_object_collection) classe, che fornisce inoltre il[Aggiungere](https://reference.aspose.com/cells/cpp/class/aspose.cells.tables.i_list_object_collection#ae4afda31b69b75a78558a65bef65ee42)metodo per aggiungere un oggetto `[IListObject]` e specificare un intervallo di celle per l'elenco.

 In base all'intervallo di celle specificato, l'oggetto `[IListObject]` viene creato da Aspose.Cells. Utilizzare gli attributi (ad esempio[Mostra totali](https://reference.aspose.com/cells/cpp/class/aspose.cells.tables.i_list_object#a9026460927f035f374f5e1ea74e639f2) e[ListColumns](https://reference.aspose.com/cells/cpp/class/aspose.cells.tables.i_list_object#afeeb7bfabd0971e9fe34a09f0b83ae73)ecc.) della classe `[IListObject]` per controllare la lista.

Nell'esempio fornito di seguito, abbiamo creato lo stesso `[IListObject]` utilizzando l'API Aspose.Cells che abbiamo creato utilizzando Microsoft Excel nella sezione precedente.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-CreatingListObjects.cpp" >}}
## **Formatta una tabella**
Per gestire e analizzare un gruppo di dati correlati, è possibile trasformare un intervallo di celle in un oggetto elenco (noto anche come tabella Excel). Una tabella è una serie di righe e colonne che contengono dati correlati gestiti indipendentemente dai dati in altre righe e colonne. Per impostazione predefinita, ogni colonna della tabella ha il filtro abilitato nella riga di intestazione in modo da poter filtrare o ordinare rapidamente i dati dell'oggetto elenco. È possibile aggiungere una riga totale (una riga speciale in un elenco che fornisce una selezione di funzioni di aggregazione utili per lavorare con dati numerici) all'oggetto elenco che fornisce un elenco a discesa di funzioni di aggregazione per ogni cella di riga dei totali. Aspose.Cells fornisce opzioni per la creazione e la gestione di elenchi (o tabelle).
### **Formattazione di un oggetto elenco**
 Aspose.Cells offre un corso[Cartella di lavoro](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) che rappresenta un file Microsoft Excel. Il[Cartella di lavoro](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) la classe contiene un[Fogli di lavoro](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)raccolta che consente l'accesso a ciascun foglio di lavoro in un file Excel.

 Un foglio di lavoro è rappresentato da[Foglio di lavoro](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) classe. Il[Foglio di lavoro](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) fornisce una vasta gamma di metodi per la gestione dei fogli di lavoro. Per creare un*ElencoOggetto*in un foglio di lavoro, usa `IListObjectCollection`. Ogni `[IListObject]` è infatti un oggetto della classe `IListObjectCollection`, che fornisce inoltre il[Aggiungere](https://reference.aspose.com/cells/cpp/class/aspose.cells.tables.i_list_object_collection#ae4afda31b69b75a78558a65bef65ee42)metodo per aggiungere un oggetto `[IListObject]` e specificare l'intervallo di celle che deve comprendere. In base all'intervallo di celle specificato, a*ElencoOggetto* viene creato nel foglio di lavoro da Aspose.Cells. Utilizzare gli attributi (ad esempio,[TipoStileTabella](https://reference.aspose.com/cells/cpp/class/aspose.cells.tables.i_list_object#a5de8b5321b0ccb30dfb09cefe6536462)) della classe `[IListObject]` per formattare la tabella in base alle proprie esigenze.

L'esempio seguente aggiunge dati di esempio a un foglio di lavoro, aggiunge un `[IListObject]` e vi applica gli stili predefiniti. Gli stili `[IListObject]` sono supportati da Microsoft Excel 2007/2010.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-FormatTable.cpp" >}}
