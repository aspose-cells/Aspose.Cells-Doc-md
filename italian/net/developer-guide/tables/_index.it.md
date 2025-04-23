---
title: Creare e gestire tabelle di file Microsoft Excel.
linktitle: Tabelle
type: docs
weight: 150
url: /it/net/create-and-format-table/
description: Inserisci, ridimensiona, modifica, elimina, formatta la tabella dei file Excel utilizzando la libreria Aspose.Cells.
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

- Selezione dell'intervallo di dati per la creazione di un oggetto elenco
- Questo visualizza il dialogo Crea elenco.
- Implementare l'oggetto Elenco per i dati e specificare la riga totale (Seleziona **Dati**, quindi **Elenco**, seguito da **Riga totale**).

### **Utilizzando l'API di Aspose.Cells**

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), che rappresenta un file di Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contiene una raccolta di [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) che consente l'accesso a ciascun foglio di calcolo in un file di Excel.

Un foglio di calcolo è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) fornisce una vasta gamma di proprietà e metodi per la gestione di un foglio di calcolo. Per creare un [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) in un foglio di calcolo, utilizzare la proprietà di raccolta [**ListObjects**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/listobjects) della classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). Ciascun [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) è, infatti, un oggetto della classe [**ListObjectCollection**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobjectcollection), che fornisce ulteriormente il metodo [**Add**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobjectcollection/methods/add/index) per aggiungere un oggetto Elenco e specificare un intervallo di celle per l'elenco.

Secondo l'intervallo specificato di celle, l'oggetto Elenco è creato da Aspose.Cells. Utilizzare attributi (ad esempio, [**ShowTotals**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/properties/showtotals), [**ListColumns**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/properties/listcolumns), ecc.) della classe [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) per controllare l'elenco.

Nell'esempio riportato di seguito, abbiamo creato lo stesso [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) utilizzando l'API di Aspose.Cells come abbiamo creato utilizzando Microsoft Excel nella sezione precedente.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Tables-CreatingListObject-1.cs" >}}

## **Formattare una tabella**

Per gestire e analizzare un gruppo di dati correlati, è possibile trasformare un intervallo di celle in un oggetto elenco (noto anche come tabella di Excel). Una tabella è una serie di righe e colonne che contengono dati correlati gestiti indipendentemente dai dati in altre righe e colonne. Per impostazione predefinita, ogni colonna nella tabella ha abilitata la funzione di filtro nella riga di intestazione in modo da poter filtrare o ordinare rapidamente i dati dell'oggetto elenco. È possibile aggiungere una riga totale (una riga speciale in un elenco che fornisce una selezione di funzioni aggregate utili per lavorare con dati numerici) all'oggetto elenco che fornisce un elenco a discesa di funzioni aggregate per ogni cella di riga totale. Aspose.Cells fornisce opzioni per la creazione e la gestione di elenchi (o tabelle).

### **Formattazione di un oggetto elenco**

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), che rappresenta un file di Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contiene una raccolta di [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) che consente l'accesso a ciascun foglio di calcolo in un file di Excel.

Un foglio di calcolo è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) fornisce una vasta gamma di proprietà e metodi per la gestione dei fogli di calcolo. Per creare un [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) in un foglio di calcolo, utilizzare la proprietà di raccolta [**ListObjects**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/listobjects) della classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). Ciascun [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) è, infatti, un oggetto della classe [**ListObjectCollection**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobjectcollection), che fornisce ulteriormente il metodo [**Add**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobjectcollection/methods/add/index) per aggiungere un oggetto Elenco e specificare l'intervallo di celle che dovrebbe comprendere. Secondo l'intervallo specificato di celle, viene creato un [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) nel foglio di calcolo da Aspose.Cells. Utilizzare attributi (ad esempio, [**TableStyleType**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/properties/tablestyletype)) della classe [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) per formattare la tabella in base alle proprie esigenze.

L'esempio riportato di seguito aggiunge dati di esempio a un foglio di calcolo, aggiunge un [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) e applica gli stili predefiniti ad esso. Gli stili di [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) sono supportati da Microsoft Excel 2007/2010.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Tables-FormataListObject-1.cs" >}}

## **Argomenti avanzati**
- [Convertire la tabella in ODS](/cells/it/net/convert-table-to-ods/)
- [Trova query tabelle e oggetti elenco relativi alle connessioni esterne dei dati](/cells/it/net/find-query-tables-and-list-objects-related-to-external-data-connections/)
- [Leggere e scrivere una tabella con dati della tabella di query](/cells/it/net/read-and-write-table-with-query-table-data-source/)
- [Imposta il commento della tabella o dell'oggetto lista all'interno del foglio di lavoro](/cells/it/net/set-the-comment-of-table-or-list-object-inside-the-worksheet/)
- [Tabelle e intervalli](/cells/it/net/tables-and-ranges/)

{{< app/cells/assistant language="csharp" >}}
