---
title: Formatta un Oggetto Elenco  Tabella
type: docs
weight: 50
url: /it/java/format-a-list-object-table/
---

{{% alert color="primary" %}}

Per gestire e analizzare un gruppo di dati correlati, è possibile trasformare un intervallo di celle in un oggetto elenco (noto anche come tabella di Excel). Una tabella è una serie di righe e colonne che contengono dati correlati gestiti indipendentemente dai dati in altre righe e colonne. Per impostazione predefinita, ogni colonna nella tabella ha abilitata la funzione di filtro nella riga di intestazione in modo da poter filtrare o ordinare rapidamente i dati dell'oggetto elenco. È possibile aggiungere una riga totale (una riga speciale in un elenco che fornisce una selezione di funzioni aggregate utili per lavorare con dati numerici) all'oggetto elenco che fornisce un elenco a discesa di funzioni aggregate per ogni cella di riga totale. Aspose.Cells fornisce opzioni per la creazione e la gestione di elenchi (o tabelle).

{{% /alert %}}

## **Formattazione di un oggetto elenco**

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), che rappresenta un file di Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) contiene una raccolta di [**Worksheets**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets) che consente l'accesso a ciascun foglio di calcolo in un file di Excel.

Un foglio di calcolo è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) fornisce una vasta gamma di proprietà e metodi per gestire i fogli di calcolo. Per creare un [**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) in un foglio di calcolo, utilizzare la proprietà di raccolta [**ListObjects**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ListObjects) della classe [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). Ogni [**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) è, infatti, un oggetto della classe [**ListObjectCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/listobjectcollection), che fornisce ulteriormente il metodo add per aggiungere un oggetto Lista e specificare l'intervallo di celle che dovrebbe comprendere. Secondo l'intervallo specificato di celle, viene creato un [**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) nel foglio di calcolo da Aspose.Cells. Utilizzare gli attributi (ad esempio, [**TableStyleType**](https://reference.aspose.com/cells/java/com.aspose.cells/listobject#TableStyleType)) della classe [**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) per formattare la tabella secondo le tue esigenze.

L'esempio di seguito aggiunge dati di esempio a un foglio di calcolo, aggiunge una [**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) e applica stili predefiniti ad essa. [**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) gli stili sono supportati da Microsoft Excel 2007/2010.

L'output seguente viene generato quando il codice viene eseguito.

**Viene creata una tabella formattata nel foglio di calcolo** 

![todo:image_alt_text](format-a-list-object-table_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-tables-FormataListObject-FormataListObject.java" >}}
