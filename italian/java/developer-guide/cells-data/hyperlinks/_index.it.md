---
title: Inserisci collegamenti ipertestuali in Excel o OpenOffice
linktitle: Gestione dei collegamenti ipertestuali
type: docs
weight: 160
url: /it/java/insert-hyperlinks-to-excel/
---
## **Aggiunta di collegamenti ipertestuali ai dati di collegamento**
{{% alert color="primary" %}} 

Un collegamento ipertestuale viene utilizzato per creare un collegamento tra due entità. Tutti hanno familiarità con l'uso dei collegamenti ipertestuali, specialmente sui siti web.

Utilizzando Aspose.Cells, gli sviluppatori possono creare diversi tipi di collegamenti ipertestuali nei file Excel Microsoft. Questo argomento illustra quali tipi di collegamenti ipertestuali sono supportati da Aspose.Cells e come possono essere utilizzati nei nostri file Excel.

{{% /alert %}} 
## **Aggiunta di collegamenti ipertestuali**
È possibile aggiungere tre tipi di collegamento ipertestuale a una cella utilizzando Aspose.Cells:

- [Aggiunta di un collegamento a un URL](/cells/it/java/working-with-hyperlinks-to-link-data/).
- [Aggiunta di un collegamento a un'altra cella nello stesso file](/cells/it/java/working-with-hyperlinks-to-link-data/).
- [Aggiunta di un collegamento a un file esterno](/cells/it/java/working-with-hyperlinks-to-link-data/).

 Aspose.Cells consente agli sviluppatori di aggiungere collegamenti ipertestuali ai file Excel utilizzando API o[fogli di calcolo del progettista](/cells/it/java/what-is-a-designer-spreadsheet/)(fogli di calcolo in cui i collegamenti ipertestuali vengono creati manualmente e Aspose.Cells viene utilizzato per importarli in altri fogli di calcolo).

Aspose.Cells offre un corso,[Cartella di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) che rappresenta un file Excel Microsoft. Il[Cartella di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)la classe contiene un[Raccolta di fogli di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) che consente l'accesso a ciascun foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato da[Foglio di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) classe. Il[Foglio di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)fornisce diversi metodi per aggiungere diversi collegamenti ipertestuali ai file Excel.
## **Aggiunta di un collegamento a un URL**
 Il[Foglio di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) la classe contiene un[Collegamenti ipertestuali](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection) collezione. Ogni elemento del[Collegamenti ipertestuali](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection) collezione rappresenta a[Collegamento ipertestuale](https://reference.aspose.com/cells/java/com.aspose.cells/Hyperlink) . Aggiungi collegamenti ipertestuali agli URL chiamando il file[Collegamenti ipertestuali](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Hyperlinks) della collezione[Aggiungere](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\) )metodo. Il[Aggiungere](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\))il metodo accetta i seguenti parametri:

- Cell nome, il nome della cella a cui verrà aggiunto il collegamento ipertestuale.
- Numero di righe, il numero di righe in questo intervallo di collegamenti ipertestuali.
- Numero di colonne, il numero di colonne di questo intervallo di collegamenti ipertestuali
- URL, l'indirizzo URL.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingLinkToURL-AddingLinkToURL.java" >}}


 Nell'esempio precedente, un collegamento ipertestuale viene aggiunto a un URL in una cella vuota,**A1**In tali casi, se una cella è vuota, anche l'indirizzo URL viene aggiunto a quella cella vuota come suo valore. Se la cella non è vuota e viene aggiunto un collegamento ipertestuale, il valore della cella appare come testo normale. Per farlo sembrare un collegamento ipertestuale, applica le impostazioni di formattazione appropriate su quella cella.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingLinkToURLNotEmpty-AddingLinkToURLNotEmpty.java" >}}



## **Aggiunta di un collegamento a un numero Cell nello stesso file**
 È possibile aggiungere collegamenti ipertestuali alle celle nello stesso file Excel chiamando il file[Collegamenti ipertestuali](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection) della collezione[Aggiungere](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\) )metodo. Il[Aggiungere](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\)) funziona sia per i collegamenti ipertestuali interni che esterni. Una versione del metodo sottoposto a overload accetta i seguenti parametri:

- Cell nome, il nome della cella a cui verrà aggiunto il collegamento ipertestuale.
- Numero di righe, il numero di righe in questo intervallo di collegamenti ipertestuali.
- Numero di colonne, il numero di colonne in questo intervallo di collegamenti ipertestuali.
- URL, l'indirizzo della cella di destinazione.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingLinkToAnotherCell-AddingLinkToAnotherCell.java" >}}



## **Aggiunta di un collegamento a un file esterno**
 È possibile aggiungere collegamenti ipertestuali a file Excel esterni chiamando il file[Collegamenti ipertestuali](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection) della collezione[Aggiungere](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\) )metodo. Il[Aggiungere](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\))il metodo accetta i seguenti parametri:

- Cell nome, il nome della cella a cui verrà aggiunto il collegamento ipertestuale.
- Numero di righe, il numero di righe in questo intervallo di collegamenti ipertestuali.
- Numero di colonne, il numero di colonne in questo intervallo di collegamenti ipertestuali.
- URL, l'indirizzo del file Excel esterno di destinazione.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingLinkToExternalFile-AddingLinkToExternalFile.java" >}}

## **Argomenti avanzati**
- [Aggiungi collegamenti ipertestuali alle immagini](/cells/it/java/add-image-hyperlinks/)
- [Rileva il tipo di collegamento ipertestuale](/cells/it/java/detect-hyperlink-type/)
- [Modifica dei collegamenti ipertestuali del foglio di lavoro](/cells/it/java/editing-hyperlinks-of-worksheet/)
- [Ottieni collegamenti ipertestuali nell'intervallo](/cells/it/java/get-hyperlinks-in-range/)


