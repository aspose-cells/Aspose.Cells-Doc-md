---
title: Creare e formattare una tabella
type: docs
weight: 10
url: /it/cpp/create-and-format-table/
---

## **Creare una tabella**
Uno dei vantaggi dei fogli di calcolo è che consentono di creare diversi tipi di elenchi, ad esempio elenchi telefonici, elenchi delle attività, elenchi di transazioni, attivi o passivi. Diversi utenti possono lavorare insieme per utilizzare, creare e mantenere vari elenchi.

Aspose.Cells supporta la creazione e la gestione di elenchi.
### **Vantaggi di un oggetto elenco**
Ci sono diversi vantaggi quando si converte un elenco di dati in un vero oggetto elenco

- Nuove righe e colonne vengono automaticamente incluse.
- Una riga di totale in fondo al tuo elenco può essere facilmente aggiunta per visualizzare SOMMA, MEDIA, CONTEGGIO, ecc.
- Le colonne aggiunte a destra vengono automaticamente incorporate nell'oggetto Elenco.
- I grafici basati su righe e colonne verranno espansi automaticamente.
- I nomi definiti assegnati a righe e colonne verranno espansi automaticamente.
- L'elenco è protetto dalla cancellazione accidentale di righe e colonne.
### **Creazione di un oggetto elenco utilizzando Microsoft Excel**

|**Selezione del intervallo di dati per la creazione dell'oggetto Lista**|
| :- |
|![todo:image_alt_text](jHcNq4o.png)|
Questo visualizza il dialogo Crea elenco.

|**Dialogo Crea Lista**|
| :- |
|![todo:image_alt_text](kJmukRF.png)|
Implementazione dell'oggetto List per i dati e specifica della riga totale (Selezionare **Dati**, poi **Lista**, seguito da **Riga Totale**).

|**Creazione di un oggetto lista**|
| :- |
|![todo:image_alt_text](ECSGVdR.png)|
### **Utilizzando l'API di Aspose.Cells**
Aspose.Cells fornisce una classe [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) che rappresenta un file Microsoft Excel. La classe [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) contiene una collezione [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) che consente di accedere a ogni foglio di lavoro in un file Excel.

Un foglio di lavoro è rappresentato dalla classe [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La classe [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) fornisce un'ampia gamma di metodi per la gestione di un foglio di lavoro. Per creare un [ListObject](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/) in un foglio di lavoro, utilizzare il metodo di collezione [GetListObjects](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getlistobjects/) della classe [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). Ogni `[ListObject]` è infatti un oggetto della classe [ListObjectCollection](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobjectcollection/), che fornisce ulteriormente il metodo [Add](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobjectcollection/add/) per aggiungere un oggetto `[ListObject]` e specificare un intervallo di celle per la lista.

In base all'intervallo di celle specificato, l'oggetto `[ListObject]` è creato da Aspose.Cells. Utilizzare attributi (ad esempio [SetShowTotals](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/setshowtotals/) e [GetListColumns](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/getlistcolumns/) ecc.) della classe `[ListObject]` per controllare la lista.

Nell'esempio riportato di seguito, abbiamo creato lo stesso `[ListObject]` utilizzando l'API Aspose.Cells come abbiamo creato utilizzando Microsoft Excel nella sezione precedente.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-CreatingListObjects-new.cpp" >}}
## **Formattare una tabella**
Per gestire ed analizzare un gruppo di dati correlati, è possibile trasformare un intervallo di celle in un oggetto lista (noto anche come tabella Excel). Una tabella è una serie di righe e colonne che contengono dati correlati gestiti in modo indipendente dai dati in altre righe e colonne. Per impostazione predefinita, ogni colonna nella tabella ha abilitato il filtro nella riga dell'intestazione in modo da poter filtrare o ordinare rapidamente i dati della lista. È possibile aggiungere una riga totale (una riga speciale in una lista che fornisce una selezione di funzioni aggregate utili per lavorare con dati numerici) all'oggetto lista che fornisce un elenco a discesa di funzioni aggregate per ciascuna cella di riga totale. Aspose.Cells fornisce opzioni per creare e gestire liste (o tabelle).
### **Formattazione di un oggetto elenco**
Aspose.Cells fornisce una classe [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) che rappresenta un file Microsoft Excel. La classe [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) contiene una collezione [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) che consente di accedere a ogni foglio di lavoro in un file Excel.

Un foglio di lavoro è rappresentato dalla classe [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La classe [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) fornisce un'ampia gamma di metodi per la gestione di fogli di lavoro. Per creare un *ListObject* in un foglio di lavoro, utilizzare `ListObjectCollection`. Ogni `[ListObject]` è infatti un oggetto della classe `ListObjectCollection`, che fornisce ulteriormente il metodo [Add](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobjectcollection/add/) per aggiungere un `[ListObject]` e specificare l'intervallo di celle che dovrebbe raggruppare. In base all'intervallo di celle specificato, viene creato un *ListObject* nel foglio di lavoro da Aspose.Cells. Utilizzare attributi (ad esempio, [SetTableStyleType](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/settablestyletype/)) della classe `[ListObject]` per formattare la tabella secondo le vostre esigenze.

Nell'esempio sottostante vengono aggiunti dati di esempio a un foglio di lavoro, viene aggiunto un `[ListObject]` e vengono applicati stili predefiniti ad esso. Gli stili `[ListObject]` sono supportati da Microsoft Excel 2007/2010.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-FormatTable-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
