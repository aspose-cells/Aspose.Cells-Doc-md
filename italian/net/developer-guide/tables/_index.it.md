---
title: Creare e gestire tabelle di file Microsoft Excel.
linktitle: Tabelle
type: docs
weight: 150
url: /it/net/create-and-format-table/
description: Inserisci, ridimensiona, modifica, elimina, formatta la tabella dei file Excel utilizzando la libreria Aspose.Cells.
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

- Selezione dell'intervallo di dati per la creazione di un oggetto Elenco
- Viene visualizzata la finestra di dialogo Crea elenco.
-  Implementare l'oggetto List per i dati e specificare la riga totale (Select**Dati** , poi**Elenco** , seguito da**Riga totale**).

### **Utilizzo dell'API Aspose.Cells**

 Aspose.Cells offre un corso,[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , che rappresenta un file Microsoft Excel. Il[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la classe contiene un[**Fogli di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)raccolta che consente l'accesso a ciascun foglio di lavoro in un file Excel.

 Un foglio di lavoro è rappresentato da[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe. Il[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) fornisce un'ampia gamma di proprietà e metodi per la gestione di un foglio di lavoro. Per creare un[**ElencoOggetto**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) in un foglio di lavoro, usa il[**ListObjects**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/listobjects) proprietà della collezione del[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe. A testa[**ElencoOggetto**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) è, infatti, un oggetto del[**ListObjectCollection**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobjectcollection) classe, che fornisce inoltre il[**Aggiungere**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobjectcollection/methods/add/index)metodo per aggiungere un oggetto List e specificare un intervallo di celle per l'elenco.

In base all'intervallo di celle specificato, l'oggetto List viene creato da Aspose.Cells. Utilizzare gli attributi (ad esempio,[**Mostra totali**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/properties/showtotals), [**ListColumns**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/properties/listcolumns) , ecc.) del[**ElencoOggetto**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)class per controllare l'elenco.

 Nell'esempio fornito di seguito, abbiamo creato lo stesso[**ElencoOggetto**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)utilizzando l'API Aspose.Cells come abbiamo creato utilizzando Microsoft Excel nella sezione precedente.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Tables-CreatingListObject-1.cs" >}}

## **Formatta una tabella**

Per gestire e analizzare un gruppo di dati correlati, è possibile trasformare un intervallo di celle in un oggetto elenco (noto anche come tabella Excel). Una tabella è una serie di righe e colonne che contengono dati correlati gestiti indipendentemente dai dati in altre righe e colonne. Per impostazione predefinita, ogni colonna della tabella ha il filtro abilitato nella riga di intestazione in modo da poter filtrare o ordinare rapidamente i dati dell'oggetto elenco. È possibile aggiungere una riga totale (una riga speciale in un elenco che fornisce una selezione di funzioni aggregate utili per lavorare con dati numerici) all'oggetto elenco che fornisce un elenco a discesa di funzioni aggregate per ogni cella di riga totale. Aspose.Cells fornisce opzioni per la creazione e la gestione di elenchi (o tabelle).

### **Formattazione di un oggetto elenco**

 Aspose.Cells offre un corso,[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , che rappresenta un file Microsoft Excel. Il[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la classe contiene un[**Fogli di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)raccolta che consente l'accesso a ciascun foglio di lavoro in un file Excel.

 Un foglio di lavoro è rappresentato da[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe. Il[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) fornisce un'ampia gamma di proprietà e metodi per la gestione dei fogli di lavoro. Per creare un[**ElencoOggetto**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) in un foglio di lavoro, usa[**ListObjects**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/listobjects) proprietà della collezione del[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe. A testa[**ElencoOggetto**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) è, infatti, un oggetto del[**ListObjectCollection**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobjectcollection) classe, che fornisce inoltre il[**Aggiungere**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobjectcollection/methods/add/index) metodo per aggiungere un oggetto List e specificare l'intervallo di celle che deve contenere. In base all'intervallo di celle specificato, a[**ElencoOggetto**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)viene creato nel foglio di lavoro da Aspose.Cells. Utilizzare gli attributi (ad esempio,[**TipoStileTabella**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/properties/tablestyletype) ) del[**ElencoOggetto**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)class per formattare la tabella in base alle proprie esigenze.

 L'esempio seguente aggiunge dati di esempio a un foglio di lavoro, aggiunge a[**ElencoOggetto**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) e applicare gli stili predefiniti ad esso.[**ElencoOggetto**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)gli stili sono supportati da Microsoft Excel 2007/2010.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Tables-FormataListObject-1.cs" >}}

## **Argomenti avanzati**
- [Converti tabella in ODS](/cells/it/net/convert-table-to-ods/)
- [Trova tabelle di query e oggetti elenco relativi a connessioni dati esterne](/cells/it/net/find-query-tables-and-list-objects-related-to-external-data-connections/)
- [Leggere e scrivere la tabella con l'origine dati della tabella delle query](/cells/it/net/read-and-write-table-with-query-table-data-source/)
- [Impostare il commento della tabella o dell'oggetto elenco all'interno del foglio di lavoro](/cells/it/net/set-the-comment-of-table-or-list-object-inside-the-worksheet/)
- [Tabelle e intervalli](/cells/it/net/tables-and-ranges/)

