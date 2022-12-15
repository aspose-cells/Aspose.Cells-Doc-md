---
title: Formatta un oggetto elenco - tabella
type: docs
weight: 50
url: /it/java/format-a-list-object-table/
---
{{% alert color="primary" %}}

Per gestire e analizzare un gruppo di dati correlati, è possibile trasformare un intervallo di celle in un oggetto elenco (noto anche come tabella Excel). Una tabella è una serie di righe e colonne che contengono dati correlati gestiti indipendentemente dai dati in altre righe e colonne. Per impostazione predefinita, ogni colonna della tabella ha il filtro abilitato nella riga di intestazione in modo da poter filtrare o ordinare rapidamente i dati dell'oggetto elenco. È possibile aggiungere una riga totale (una riga speciale in un elenco che fornisce una selezione di funzioni aggregate utili per lavorare con dati numerici) all'oggetto elenco che fornisce un elenco a discesa di funzioni aggregate per ogni cella di riga totale. Aspose.Cells fornisce opzioni per la creazione e la gestione di elenchi (o tabelle).

{{% /alert %}}

## **Formattazione di un oggetto elenco**

 Aspose.Cells offre un corso,[**Cartella di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , che rappresenta un file Microsoft Excel. Il[**Cartella di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) la classe contiene un[**Fogli di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets)raccolta che consente l'accesso a ciascun foglio di lavoro in un file Excel.

 Un foglio di lavoro è rappresentato da[**Foglio di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) classe. Il[**Foglio di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) fornisce un'ampia gamma di proprietà e metodi per la gestione dei fogli di lavoro. Per creare un[**ElencoOggetto**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) in un foglio di lavoro, usa[**ListObjects**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ListObjects) proprietà della collezione del[**Foglio di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) classe. A testa[**ElencoOggetto**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) è, infatti, un oggetto del[**ListObjectCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/listobjectcollection)class, che fornisce inoltre il metodo add per aggiungere un oggetto List e specificare l'intervallo di celle che deve comprendere. In base all'intervallo di celle specificato, a[**ElencoOggetto**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) viene creato nel foglio di lavoro da Aspose.Cells. Utilizzare gli attributi (ad esempio,[**TipoStileTabella**](https://reference.aspose.com/cells/java/com.aspose.cells/listobject#TableStyleType) ) del[**ElencoOggetto**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject)class per formattare la tabella in base alle proprie esigenze.

 L'esempio seguente aggiunge dati di esempio a un foglio di lavoro, aggiunge a[**ElencoOggetto**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) e vi applica gli stili predefiniti.[**ElencoOggetto**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject)gli stili sono supportati da Microsoft Excel 2007/2010.

Il seguente output viene generato quando il codice viene eseguito.

**Nel foglio di lavoro viene creata una tabella formattata** 

![cose da fare:immagine_alt_testo](format-a-list-object-table_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-tables-FormataListObject-FormataListObject.java" >}}
