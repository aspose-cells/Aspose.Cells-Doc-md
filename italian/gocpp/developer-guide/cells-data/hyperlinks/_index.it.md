---
title: Inserisci collegamenti ipertestuali in Excel o OpenOffice con Golang tramite C++
linktitle: Gestione dei collegamenti ipertestuali
type: docs
weight: 45
url: /it/go-cpp/insert-hyperlinks-to-excel/
description: Come inserire link ipertestuali nel file Excel con la libreria Aspose.Cells senza MS Excel usando C++.
keywords: Inserire collegamenti ipertestuali in Excel, Aggiungere o Inserire collegamenti ipertestuali, Aggiungi o Inserisci un collegamento a un URL, Aggiungi o Inserisci un collegamento in una cella, Aggiungi un collegamento a un file esterno
---

{{% alert color="primary" %}} 

Un collegamento ipertestuale viene utilizzato per creare un collegamento tra due entità. Tutti sono familiari con l'uso dei collegamenti ipertestuali, specialmente sui siti web.
Utilizzando Aspose.Cells, gli sviluppatori possono creare diversi tipi di collegamenti ipertestuali nei file Microsoft Excel. Questo argomento discute quali tipi di collegamenti ipertestuali sono supportati da Aspose.Cells e come possono essere utilizzati nei nostri file Excel.

{{% /alert %}} 

## **Aggiunta di Collegamenti Ipotestuali**
Aspose.Cells consente agli sviluppatori di aggiungere collegamenti ipertestuali ai file Excel usando l'API o fogli di calcolo creati manualmente (fogli di calcolo in cui i collegamenti vengono creati manualmente e Aspose.Cells viene usato per importarli in altri fogli).

Aspose.Cells fornisce una classe, [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) che rappresenta un file Microsoft Excel. La classe [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) contiene una [WorksheetCollection](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) che consente l'accesso a ogni foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato dalla classe [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La classe [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) fornisce diversi metodi per aggiungere diversi collegamenti ipertestuali ai file Excel.

## **Aggiunta di un link a un URL**
La classe [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) contiene una collezione [GetHyperlinks()](https://reference.aspose.com/cells/go-cpp/worksheet/gethyperlinks/). Ogni elemento nella collezione [GetHyperlinks()](https://reference.aspose.com/cells/go-cpp/worksheet/gethyperlinks/) rappresenta un [Hyperlink](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlink/). Aggiungi collegamenti ipertestuali a URL chiamando il metodo [Add](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/add/) della collezione [Hyperlinks](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/). Il metodo [Add](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/add/) prende i seguenti parametri:

- Nome della cella, il nome della cella a cui verrà aggiunto il collegamento ipertestuale.
- Numero di righe, il numero di righe in questo intervallo di collegamenti ipertestuali.
- Numero di colonne, il numero di colonne in questo intervallo di collegamenti ipertestuali.
- URL, l'indirizzo URL.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Hyperlinks.go" >}}
{{% alert color="primary" %}} 

Nell'esempio precedente, è stato aggiunto un collegamento ipertestuale a un URL in una cella vuota, **A1**. In tali casi, se una cella è vuota, l'indirizzo URL viene aggiunto anche a quella cella vuota come suo valore. Se la cella non è vuota e viene aggiunto un collegamento ipertestuale, il valore della cella appare come testo semplice. Per farlo apparire come un collegamento ipertestuale, applicare le impostazioni di formattazione appropriate su quella cella.

{{% /alert %}} 

## **Aggiunta di un link a una cella nello stesso file**
È possibile aggiungere collegamenti ipertestuali alle celle nello stesso file Excel chiamando il metodo [Add](https://reference.aspose.com/cells/go-cpp/hyperlinkcollection/add/) della collezione [Hyperlinks](https://reference.aspose.com/cells/go-cpp/hyperlinkcollection/). Il metodo [Add](https://reference.aspose.com/cells/go-cpp/hyperlinkcollection/add/) funziona sia per collegamenti ipertestuali interni che esterni. Una versione del metodo sovraccarico prende i seguenti parametri:

- Nome della cella, il nome della cella a cui verrà aggiunto il collegamento ipertestuale.
- Numero di righe, il numero di righe in questo intervallo di collegamenti ipertestuali.
- Numero di colonne, il numero di colonne in questo intervallo di collegamenti ipertestuali.
- URL, l'indirizzo della cella di destinazione.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Hyperlinks-1.go" >}}
## **Aggiunta di un link a un file esterno**
È possibile aggiungere collegamenti ipertestuali a file Excel esterni chiamando il metodo [Add](https://reference.aspose.com/cells/go-cpp/hyperlinkcollection/add/) della collezione [Hyperlinks](https://reference.aspose.com/cells/go-cpp/hyperlinkcollection/). Il metodo [Add](https://reference.aspose.com/cells/go-cpp/hyperlinkcollection/add/) prende i seguenti parametri:

- Nome della cella, il nome della cella a cui verrà aggiunto il collegamento ipertestuale.
- Numero di righe, il numero di righe in questo intervallo di collegamenti ipertestuali.
- Numero di colonne, il numero di colonne in questo intervallo di collegamenti ipertestuali.
- URL, l'indirizzo di destinazione, file Excel esterno.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Hyperlinks-2.go" >}}
## **Argomenti avanzati**
- [Aggiungi collegamenti ipertestuali alle immagini](/cells/it/cpp/add-image-hyperlinks/)
- [Rilevare il tipo di collegamento ipertestuale](/cells/it/cpp/detect-hyperlink-type/)
- [Modifica dei collegamenti ipertestuali del foglio di lavoro](/cells/it/cpp/editing-hyperlinks-of-worksheet/)
- [Ottieni i collegamenti ipertestuali nell'intervallo](/cells/it/cpp/get-hyperlinks-in-range/)
