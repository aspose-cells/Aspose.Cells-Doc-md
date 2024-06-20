---
title: Inserire collegamenti ipertestuali in Excel o OpenOffice
linktitle: Gestione dei collegamenti ipertestuali
type: docs
weight: 160
url: /it/java/insert-hyperlinks-to-excel/
---

## **Aggiunta di collegamenti ipertestuali per collegare i dati**
{{% alert color="primary" %}} 

Un collegamento ipertestuale viene utilizzato per creare un collegamento tra due entità. Tutti sono familiari con l'uso dei collegamenti ipertestuali, specialmente sui siti web.

Utilizzando Aspose.Cells, gli sviluppatori possono creare diversi tipi di collegamenti ipertestuali nei file Microsoft Excel. Questo argomento discute quali tipi di collegamenti ipertestuali sono supportati da Aspose.Cells e come possono essere utilizzati nei nostri file Excel.

{{% /alert %}} 
## **Aggiunta di Collegamenti Ipotestuali**
Tre tipi di collegamento ipertestuale possono essere aggiunti a una cella utilizzando Aspose.Cells:

- [Aggiunta di un collegamento a un URL](/cells/it/java/working-with-hyperlinks-to-link-data/).
- [Aggiunta di un collegamento a un'altra cella nello stesso file](/cells/it/java/working-with-hyperlinks-to-link-data/).
- [Aggiunta di un collegamento a un file esterno](/cells/it/java/working-with-hyperlinks-to-link-data/).

Aspose.Cells consente ai programmatori di aggiungere collegamenti ipertestuali ai file di Excel utilizzando l'API o [fogli di calcolo del designer](/cells/it/java/what-is-a-designer-spreadsheet/) (fogli di calcolo in cui i collegamenti ipertestuali vengono creati manualmente e Aspose.Cells viene utilizzato per importarli in altri fogli di calcolo).

Aspose.Cells fornisce una classe, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) che rappresenta un file Microsoft Excel. La classe [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) contiene una [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) che consente di accedere a ciascun foglio di lavoro nel file di Excel. Un foglio di lavoro è rappresentato dalla classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). La classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) fornisce diversi metodi per aggiungere diversi collegamenti ipertestuali ai file di Excel.
## **Aggiunta di un link a un URL**
La classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) contiene una collezione [Hyperlinks](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection). Ciascun elemento della collezione [Hyperlinks](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection) rappresenta un [Hyperlink](https://reference.aspose.com/cells/java/com.aspose.cells/Hyperlink). Aggiungere collegamenti ipertestuali a URL chiamando il metodo [Add ](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\))della collezione [Hyperlinks](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Hyperlinks). Il metodo [Add ](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\)) prende i seguenti parametri:

- Nome della cella, il nome della cella a cui verrà aggiunto il collegamento ipertestuale.
- Numero di righe, il numero di righe in questo intervallo di collegamenti ipertestuali.
- Numero di colonne, il numero di colonne di questo intervallo di collegamento ipertestuale
- URL, l'indirizzo URL.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingLinkToURL-AddingLinkToURL.java" >}}


Nell'esempio sopra, viene aggiunto un collegamento ipertestuale a un URL in una cella vuota, **A1**. In tali casi, se una cella è vuota, l'indirizzo URL viene aggiunto anche a quella cella vuota come il suo valore. Se la cella non è vuota e viene aggiunto un collegamento ipertestuale, il valore della cella appare come testo normale. Per farlo sembrare un collegamento ipertestuale, applicare le impostazioni di formattazione appropriate su quella cella.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingLinkToURLNotEmpty-AddingLinkToURLNotEmpty.java" >}}



## **Aggiunta di un link a una cella nello stesso file**
È possibile aggiungere collegamenti ipertestuali alle celle nello stesso file Excel chiamando il [Hyperlinks](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection) collezione's [Aggiungi ](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\))metodo. Il [Aggiungi ](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\))metodo funziona sia per collegamenti interni che esterni. Una versione del metodo sovraccaricato richiede i seguenti parametri:

- Nome della cella, il nome della cella a cui verrà aggiunto il collegamento ipertestuale.
- Numero di righe, il numero di righe in questo intervallo di collegamenti ipertestuali.
- Numero di colonne, il numero di colonne in questo intervallo di collegamenti ipertestuali.
- URL, l'indirizzo della cella di destinazione.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingLinkToAnotherCell-AddingLinkToAnotherCell.java" >}}



## **Aggiunta di un link a un file esterno**
È possibile aggiungere collegamenti ipertestuali a file Excel esterni chiamando il [Hyperlinks](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection) collezione's [Aggiungi ](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\))metodo. Il [Aggiungi ](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\))metodo richiede i seguenti parametri:

- Nome della cella, il nome della cella a cui verrà aggiunto il collegamento ipertestuale.
- Numero di righe, il numero di righe in questo intervallo di collegamenti ipertestuali.
- Numero di colonne, il numero di colonne in questo intervallo di collegamenti ipertestuali.
- URL, l'indirizzo di destinazione, file Excel esterno.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingLinkToExternalFile-AddingLinkToExternalFile.java" >}}

## **Argomenti avanzati**
- [Aggiungi collegamenti ipertestuali alle immagini](/cells/it/java/add-image-hyperlinks/)
- [Rilevare il tipo di collegamento ipertestuale](/cells/it/java/detect-hyperlink-type/)
- [Modifica dei collegamenti ipertestuali del foglio di lavoro](/cells/it/java/editing-hyperlinks-of-worksheet/)
- [Ottieni i collegamenti ipertestuali nell'intervallo](/cells/it/java/get-hyperlinks-in-range/)


