---
title: Inserire collegamenti ipertestuali in Excel o OpenOffice
linktitle: Gestione dei collegamenti ipertestuali
type: docs
weight: 45
url: /it/python-net/insert-hyperlinks-to-excel/
description: Come inserire collegamenti ipertestuali in un file Excel con la libreria Aspose.Cells for Python via .NET senza MS Excel.
keywords: Libreria Python Excel, Inserimento di collegamenti ipertestuali in Excel con Python, Aggiunta o Inserimento di collegamenti ipertestuali con Python, Aggiunta o Inserimento di un collegamento a un URL con Python, Aggiunta o Inserimento di un collegamento a una cella con Python, Aggiunta di un collegamento a un file esterno con Python
---

{{% alert color="primary" %}} 

Un collegamento ipertestuale viene utilizzato per creare un collegamento tra due entità. Tutti sono familiari con l'uso dei collegamenti ipertestuali, specialmente sui siti web.
Usando Aspose.Cells for Python via .NET, gli sviluppatori possono creare diversi tipi di collegamenti ipertestuali nei file Microsoft Excel. Questo argomento discute quali tipi di collegamenti ipertestuali sono supportati da Aspose.Cells for Python via .NET e come possono essere utilizzati nei nostri file Excel.

{{% /alert %}} 
## **Come Aggiungere Collegamenti Ipotestuali**
Aspose.Cells for Python via .NET consente agli sviluppatori di aggiungere collegamenti ipertestuali ai file Excel utilizzando l'API o fogli di lavoro del designer (fogli di lavoro in cui i collegamenti ipertestuali vengono creati manualmente e Aspose.Cells for Python via .NET viene utilizzato per importarli in altri fogli di lavoro).

Aspose.Cells for Python via .NET fornisce una classe, [Workbook](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) che rappresenta un file Microsoft Excel. La classe [Workbook](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) contiene una [WorksheetCollection](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection) che consente l'accesso a ciascun foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato dalla classe [Worksheet](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). La classe [Worksheet](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) fornisce diversi metodi per aggiungere diversi collegamenti ipertestuali ai file Excel.

## **Come Aggiungere un Collegamento a un URL**
La classe [Worksheet](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) contiene una raccolta [hyperlinks](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/hyperlinks/). Ogni elemento nella raccolta [hyperlinks](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/hyperlinks/) rappresenta un [Hyperlink](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlink). Aggiungi collegamenti ipertestuali agli URL chiamando il metodo [add](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlinkcollection/add/#int-int-int-int-str) della raccolta [hyperlinks](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/hyperlinks/). Il metodo [add](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlinkcollection/add/#int-int-int-int-str) prende i seguenti parametri:

- Nome della cella, il nome della cella a cui verrà aggiunto il collegamento ipertestuale.
- Numero di righe, il numero di righe in questo intervallo di collegamenti ipertestuali.
- Numero di colonne, il numero di colonne in questo intervallo di collegamento ipertestuale
- URL, l'indirizzo URL.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Hyperlinks-AddingLinkToURL-1.py" >}}

{{% alert color="primary" %}} 

Nell'esempio precedente, è stato aggiunto un collegamento ipertestuale a un URL in una cella vuota, **A1**. In tali casi, se una cella è vuota, l'indirizzo URL viene aggiunto anche a quella cella vuota come suo valore. Se la cella non è vuota e viene aggiunto un collegamento ipertestuale, il valore della cella appare come testo semplice. Per farlo apparire come un collegamento ipertestuale, applicare le impostazioni di formattazione appropriate su quella cella.

{{% /alert %}} 

## **Come Aggiungere un Collegamento a una Cellula nello Stesso File**
È possibile aggiungere collegamenti ipertestuali alle celle nello stesso file Excel chiamando il metodo [add](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlinkcollection/add/#int-int-int-int-str) della raccolta [hyperlinks](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/hyperlinks/). Il metodo [add](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlinkcollection/add/#int-int-int-int-str) funziona sia per i collegamenti ipertestuali interni che esterni. Una versione del metodo sovraccaricata prende i seguenti parametri:

- Nome della cella, il nome della cella alla quale verrà aggiunto il collegamento ipertestuale.
- Numero di righe, il numero di righe in questo intervallo di collegamenti ipertestuali.
- Numero di colonne, il numero di colonne in questo intervallo di collegamenti ipertestuali.
- URL, l'indirizzo della cella di destinazione.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Hyperlinks-AddingLinkToAnotherCell-1.py" >}}

## **Come aggiungere un collegamento a un file esterno**
E' possibile aggiungere collegamenti ipertestuali a file Excel esterni chiamando il metodo [hyperlinks](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/hyperlinks/) della collezione e il metodo [add](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlinkcollection/add/#int-int-int-int-str). Il metodo [add](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlinkcollection/add/#int-int-int-int-str) richiede i seguenti parametri:

- Nome della cella, il nome della cella a cui verrà aggiunto il collegamento ipertestuale.
- Numero di righe, il numero di righe in questo intervallo di collegamenti ipertestuali.
- Numero di colonne, il numero di colonne in questo intervallo di collegamenti ipertestuali.
- URL, l'indirizzo di destinazione, file Excel esterno.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Hyperlinks-AddingLinkToExternalFile-1.py" >}}

## **Argomenti avanzati**
- [Aggiungi collegamenti ipertestuali alle immagini](/cells/it/python-net/add-image-hyperlinks/)
- [Rilevare il tipo di collegamento ipertestuale](/cells/it/python-net/detect-hyperlink-type/)
- [Modifica dei collegamenti ipertestuali del foglio di lavoro](/cells/it/python-net/editing-hyperlinks-of-worksheet/)
- [Ottieni i collegamenti ipertestuali nell'intervallo](/cells/it/python-net/get-hyperlinks-in-range/)

{{< app/cells/assistant language="python-net" >}}
