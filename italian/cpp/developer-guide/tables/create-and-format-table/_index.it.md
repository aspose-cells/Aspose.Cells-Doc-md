---
title: Crea e formatta tabella
type: docs
weight: 10
url: /it/cpp/create-and-format-table/
---
##  **Crea tabella**
Uno dei vantaggi dei fogli di calcolo è che consentono di creare diversi tipi di elenchi, ad esempio elenchi telefonici, elenchi di attività, elenchi di transazioni, attività o passività. Diversi utenti possono lavorare insieme per utilizzare, creare e mantenere vari elenchi.

Aspose.Cells supporta la creazione e la gestione delle Liste.
###  **Vantaggi di un oggetto elenco**
Ci sono alcuni vantaggi quando si converte un elenco di dati in un oggetto elenco effettivo

- Le nuove righe e colonne vengono incluse automaticamente.
- È possibile aggiungere facilmente una riga totale in fondo all'elenco per visualizzare SOMMA, MEDIA, CONTEGGIO, ecc.
- Le colonne aggiunte a destra vengono automaticamente incorporate nell'oggetto Elenco.
- I grafici basati su righe e colonne verranno espansi automaticamente.
- Gli intervalli denominati assegnati a righe e colonne verranno espansi automaticamente.
- L'elenco è protetto dalla cancellazione accidentale di righe e colonne.
###  **Creazione di un oggetto elenco utilizzando Microsoft Excel**

|**Selezione dell'intervallo di dati per la creazione dell'oggetto Elenco**|
| :- |
|![cose da fare:immagine_alt_testo](jHcNq4o.png)|
Verrà visualizzata la finestra di dialogo Crea elenco.

|**Finestra di dialogo Crea elenco**|
| :- |
|![cose da fare:immagine_alt_testo](kJmukRF.png)|
Implementare l'oggetto Elenco per i dati e specificare la riga totale (selezionare *Dati**, quindi *Elenco**, seguito da *Riga totale**).

|**Creazione di un oggetto elenco**|
| :- |
|![cose da fare:immagine_alt_testo](ECSGVdR.png)|
###  **Utilizzando Aspose.Cells API**
 Aspose.Cells fornisce una lezione[Cartella di lavoro](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) che rappresenta un file Excel Microsoft. IL[Cartella di lavoro](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) la classe contiene un[Fogli di lavoro](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)raccolta che consente l'accesso a ciascun foglio di lavoro in un file Excel.

Un foglio di lavoro è rappresentato da[Foglio di lavoro](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) classe. IL[Foglio di lavoro](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) La classe fornisce un'ampia gamma di metodi per la gestione di un foglio di lavoro. Per creare un[ElencoOggetto](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/) in un foglio di lavoro, utilizzare il file[OttieniListObjects](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getlistobjects/) metodo di raccolta del[Foglio di lavoro](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) classe. Ogni `[ListObject]` è infatti, un oggetto del[ListaOggettiCollezione](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobjectcollection/) classe, che fornisce ulteriormente il file[Aggiungere](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobjectcollection/add/)metodo per aggiungere un oggetto `[ListObject]` e specificare un intervallo di celle per l'elenco.

 In base all'intervallo di celle specificato, l'oggetto `[ListObject]` viene creato da Aspose.Cells. Utilizzare gli attributi (ad esempio[ImpostaMostraTotali](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/setshowtotals/) E[OttieniColonneLista](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/getlistcolumns/)ecc.) della classe `[ListObject]` per controllare la lista.

Nell'esempio riportato di seguito, abbiamo creato lo stesso `[ListObject]` utilizzando Aspose.Cells API come abbiamo creato utilizzando Microsoft Excel nella sezione precedente.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-CreatingListObjects-new.cpp" >}}
##  **Formattare una tabella**
Per gestire e analizzare un gruppo di dati correlati, è possibile trasformare un intervallo di celle in un oggetto elenco (noto anche come tabella Excel). Una tabella è una serie di righe e colonne che contengono dati correlati gestiti indipendentemente dai dati presenti in altre righe e colonne. Per impostazione predefinita, ogni colonna nella tabella ha il filtro abilitato nella riga di intestazione in modo da poter filtrare o ordinare rapidamente i dati degli oggetti dell'elenco. È possibile aggiungere una riga totale (una riga speciale in un elenco che fornisce una selezione di funzioni aggregate utili per lavorare con dati numerici) all'oggetto elenco che fornisce un elenco a discesa di funzioni aggregate per ciascuna cella della riga dei totali. Aspose.Cells fornisce opzioni per creare e gestire elenchi (o tabelle).
###  **Formattazione di un oggetto elenco**
 Aspose.Cells fornisce una lezione[Cartella di lavoro](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) che rappresenta un file Excel Microsoft. IL[Cartella di lavoro](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) la classe contiene un[Fogli di lavoro](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)raccolta che consente l'accesso a ciascun foglio di lavoro in un file Excel.

Un foglio di lavoro è rappresentato da[Foglio di lavoro](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) classe. IL[Foglio di lavoro](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) La classe fornisce un'ampia gamma di metodi per la gestione dei fogli di lavoro. Per creare un*ElencoOggetto*in un foglio di lavoro, utilizzare `ListObjectCollection`. Ogni `[ListObject]` è infatti un oggetto della classe `ListObjectCollection`, che fornisce inoltre il[Aggiungere](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobjectcollection/add/)metodo per aggiungere un oggetto `[ListObject]` e specificare l'intervallo di celle che dovrebbe comprendere. In base all'intervallo di celle specificato, a*ElencoOggetto* viene creato nel foglio di lavoro da Aspose.Cells. Utilizzare gli attributi (ad esempio,[SetTableStyleType](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/settablestyletype/)) della classe `[ListObject]` per formattare la tabella secondo le vostre esigenze.

L'esempio seguente aggiunge dati di esempio a un foglio di lavoro, aggiunge un `[ListObject]` e vi applica gli stili predefiniti. Gli stili `[ListObject]` sono supportati da Microsoft Excel 2007/2010.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-FormatTable-new.cpp" >}}
