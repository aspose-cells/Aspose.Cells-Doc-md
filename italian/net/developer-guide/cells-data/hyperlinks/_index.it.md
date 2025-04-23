---
title: Inserire collegamenti ipertestuali in Excel o OpenOffice
linktitle: Gestione dei collegamenti ipertestuali
type: docs
weight: 45
url: /it/net/insert-hyperlinks-to-excel/
description: Come inserire collegamenti ipertestuali nel file Excel con la libreria Aspose.Cells senza MS Excel.
keywords: Inserire collegamenti ipertestuali in Excel, Aggiungere o Inserire collegamenti ipertestuali, Aggiungi o Inserisci un collegamento a un URL, Aggiungi o Inserisci un collegamento in una cella, Aggiungi un collegamento a un file esterno
---

{{% alert color="primary" %}} 

Un collegamento ipertestuale viene utilizzato per creare un collegamento tra due entità. Tutti sono familiari con l'uso dei collegamenti ipertestuali, specialmente sui siti web.
Utilizzando Aspose.Cells, gli sviluppatori possono creare diversi tipi di collegamenti ipertestuali nei file Microsoft Excel. Questo argomento discute quali tipi di collegamenti ipertestuali sono supportati da Aspose.Cells e come possono essere utilizzati nei nostri file Excel.

{{% /alert %}} 
## **Aggiunta di Collegamenti Ipotestuali**
Aspose.Cells consente ai programmatori di aggiungere collegamenti ipertestuali ai file Excel sia utilizzando l'API che il foglio di calcolo del designer (fogli di calcolo in cui i collegamenti ipertestuali vengono creati manualmente e Aspose.Cells viene utilizzato per importarli in altri fogli di calcolo).

Aspose.Cells fornisce una classe, [Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook) che rappresenta un file Microsoft Excel. La classe [Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook) contiene una [WorksheetCollection](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) che consente l'accesso a ciascun foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato dalla classe [Worksheet](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La classe [Worksheet](https://reference.aspose.com/cells/net/aspose.cells/worksheet) fornisce diversi metodi per aggiungere diversi collegamenti ipertestuali ai file Excel.
## **Aggiunta di un link a un URL**
La classe [Worksheet](https://reference.aspose.com/cells/net/aspose.cells/worksheet) contiene una raccolta di [Hyperlinks](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/hyperlinks). Ogni elemento della raccolta [Hyperlinks](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/hyperlinks) rappresenta un [Hyperlink](https://reference.aspose.com/cells/net/aspose.cells/hyperlink). Aggiungi collegamenti ipertestuali agli URL chiamando il metodo [Add](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index) della raccolta [Hyperlinks](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection). Il metodo [Add](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index) accetta i seguenti parametri:

- Nome della cella, il nome della cella a cui verrà aggiunto il collegamento ipertestuale.
- Numero di righe, il numero di righe in questo intervallo di collegamenti ipertestuali.
- Numero di colonne, il numero di colonne in questo intervallo di collegamento ipertestuale
- URL, l'indirizzo URL.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Hyperlinks-AddingLinkToURL-1.cs" >}}

{{% alert color="primary" %}} 

Nell'esempio precedente, è stato aggiunto un collegamento ipertestuale a un URL in una cella vuota, **A1**. In tali casi, se una cella è vuota, l'indirizzo URL viene aggiunto anche a quella cella vuota come suo valore. Se la cella non è vuota e viene aggiunto un collegamento ipertestuale, il valore della cella appare come testo semplice. Per farlo apparire come un collegamento ipertestuale, applicare le impostazioni di formattazione appropriate su quella cella.

{{% /alert %}} 
## **Aggiunta di un link a una cella nello stesso file**
E' possibile aggiungere collegamenti ipertestuali alle celle nello stesso file Excel chiamando il metodo [Add](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index) della raccolta [Hyperlinks](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection). Il metodo [Add](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index) funziona sia per i collegamenti interni che esterni. Una versione del metodo sovraccaricato accetta i seguenti parametri:

- Nome della cella, il nome della cella alla quale verrà aggiunto il collegamento ipertestuale.
- Numero di righe, il numero di righe in questo intervallo di collegamenti ipertestuali.
- Numero di colonne, il numero di colonne in questo intervallo di collegamenti ipertestuali.
- URL, l'indirizzo della cella di destinazione.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Hyperlinks-AddingLinkToAnotherCell-1.cs" >}}
## **Aggiunta di un link a un file esterno**
E' possibile aggiungere collegamenti ipertestuali a file Excel esterni chiamando il metodo [Add](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index) della raccolta [Hyperlinks](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection). Il metodo [Add](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index) accetta i seguenti parametri:

- Nome della cella, il nome della cella a cui verrà aggiunto il collegamento ipertestuale.
- Numero di righe, il numero di righe in questo intervallo di collegamenti ipertestuali.
- Numero di colonne, il numero di colonne in questo intervallo di collegamenti ipertestuali.
- URL, l'indirizzo di destinazione, file Excel esterno.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Hyperlinks-AddingLinkToExternalFile-1.cs" >}}

## **Argomenti avanzati**
- [Aggiungi collegamenti ipertestuali alle immagini](/cells/it/net/add-image-hyperlinks/)
- [Rilevare il tipo di collegamento ipertestuale](/cells/it/net/detect-hyperlink-type/)
- [Modifica dei collegamenti ipertestuali del foglio di lavoro](/cells/it/net/editing-hyperlinks-of-worksheet/)
- [Ottieni i collegamenti ipertestuali nell'intervallo](/cells/it/net/get-hyperlinks-in-range/)

{{< app/cells/assistant language="csharp" >}}
