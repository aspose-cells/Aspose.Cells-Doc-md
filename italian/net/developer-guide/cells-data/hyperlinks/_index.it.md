---
title: Inserisci collegamenti ipertestuali in Excel o OpenOffice
linktitle: Gestione dei collegamenti ipertestuali
type: docs
weight: 45
url: /it/net/insert-hyperlinks-to-excel/
description: Come inserire collegamenti ipertestuali nel file Excel con la libreria Aspose.Cells senza MS Excel.
---
{{% alert color="primary" %}} 

Un collegamento ipertestuale viene utilizzato per creare un collegamento tra due entità. Tutti hanno familiarità con l'uso dei collegamenti ipertestuali, specialmente sui siti web.
Utilizzando Aspose.Cells, gli sviluppatori possono creare diversi tipi di collegamenti ipertestuali nei file Excel Microsoft. Questo argomento illustra quali tipi di collegamenti ipertestuali sono supportati da Aspose.Cells e come possono essere utilizzati nei nostri file Excel.

{{% /alert %}} 
## **Aggiunta di collegamenti ipertestuali**
Aspose.Cells consente agli sviluppatori di aggiungere collegamenti ipertestuali ai file Excel utilizzando i fogli di calcolo API o designer (fogli di calcolo in cui i collegamenti ipertestuali vengono creati manualmente e Aspose.Cells viene utilizzato per importarli in altri fogli di calcolo).

 Aspose.Cells offre un corso,[Cartella di lavoro](https://reference.aspose.com/cells/net/aspose.cells/workbook) che rappresenta un file Excel Microsoft. Il[Cartella di lavoro](https://reference.aspose.com/cells/net/aspose.cells/workbook) la classe contiene un[Raccolta di fogli di lavoro](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)che consente l'accesso a ciascun foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato da[Foglio di lavoro](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe. Il[Foglio di lavoro](https://reference.aspose.com/cells/net/aspose.cells/worksheet)fornisce diversi metodi per aggiungere diversi collegamenti ipertestuali ai file Excel.
## **Aggiunta di un collegamento a un URL**
 Il[Foglio di lavoro](https://reference.aspose.com/cells/net/aspose.cells/worksheet) la classe contiene un[Collegamenti ipertestuali](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/hyperlinks) collezione. Ogni elemento del[Collegamenti ipertestuali](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/hyperlinks) collezione rappresenta a[Collegamento ipertestuale](https://reference.aspose.com/cells/net/aspose.cells/hyperlink) . Aggiungi collegamenti ipertestuali agli URL chiamando il file[Collegamenti ipertestuali](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection) della collezione[Aggiungere](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index) metodo. Il[Aggiungere](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index)metodo accetta i seguenti parametri:

- Cell nome, il nome della cella a cui verrà aggiunto il collegamento ipertestuale.
- Numero di righe, il numero di righe in questo intervallo di collegamenti ipertestuali.
- Numero di colonne, il numero di colonne in questo intervallo di collegamenti ipertestuali
- URL, l'indirizzo URL.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Hyperlinks-AddingLinkToURL-1.cs" >}}

{{% alert color="primary" %}} 

 Nell'esempio precedente, un collegamento ipertestuale viene aggiunto a un URL in una cella vuota,**A1**. In tali casi, se una cella è vuota, anche l'indirizzo URL viene aggiunto a quella cella vuota come suo valore. Se la cella non è vuota e viene aggiunto un collegamento ipertestuale, il valore della cella appare come testo normale. Per farlo sembrare un collegamento ipertestuale, applica le impostazioni di formattazione appropriate su quella cella.

{{% /alert %}} 
## **Aggiunta di un collegamento a un numero Cell nello stesso file**
 È possibile aggiungere collegamenti ipertestuali alle celle nello stesso file Excel chiamando il file[Collegamenti ipertestuali](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection) della collezione[Aggiungere](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index) metodo. Il[Aggiungere](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index)metodo funziona sia per collegamenti ipertestuali interni che esterni. Una versione del metodo sottoposto a overload accetta i seguenti parametri:

- Cell nome, il nome della cella a cui verrà aggiunto il collegamento ipertestuale.
- Numero di righe, il numero di righe in questo intervallo di collegamenti ipertestuali.
- Numero di colonne, il numero di colonne in questo intervallo di collegamenti ipertestuali.
- URL, l'indirizzo della cella di destinazione.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Hyperlinks-AddingLinkToAnotherCell-1.cs" >}}
## **Aggiunta di un collegamento a un file esterno**
 È possibile aggiungere collegamenti ipertestuali a file Excel esterni chiamando il file[Collegamenti ipertestuali](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection) della collezione[Aggiungere](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index) metodo. Il[Aggiungere](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index)metodo accetta i seguenti parametri:

- Cell nome, il nome della cella a cui verrà aggiunto il collegamento ipertestuale.
- Numero di righe, il numero di righe in questo intervallo di collegamenti ipertestuali.
- Numero di colonne, il numero di colonne in questo intervallo di collegamenti ipertestuali.
- URL, l'indirizzo del file Excel esterno di destinazione.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Hyperlinks-AddingLinkToExternalFile-1.cs" >}}

## **Argomenti avanzati**
- [Aggiungi collegamenti ipertestuali alle immagini](/cells/it/net/add-image-hyperlinks/)
- [Rileva il tipo di collegamento ipertestuale](/cells/it/net/detect-hyperlink-type/)
- [Modifica dei collegamenti ipertestuali del foglio di lavoro](/cells/it/net/editing-hyperlinks-of-worksheet/)
- [Ottieni collegamenti ipertestuali nell'intervallo](/cells/it/net/get-hyperlinks-in-range/)

