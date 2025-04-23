---
title: Inserire collegamenti ipertestuali in Excel o OpenOffice
linktitle: Gestione dei collegamenti ipertestuali
type: docs
weight: 45
url: /it/nodejs-cpp/insert-hyperlinks-to-excel/
description: Come inserire collegamenti ipertestuali nel file Excel con la libreria Aspose.Cells senza MS Excel usando Node.js tramite C++.
keywords: Inserisci collegamenti ipertestuali in Excel Node.js tramite C++, Aggiungi o Inserisci collegamenti ipertestuali Node.js tramite C++, Aggiungi o Inserisci un link a un URL Node.js tramite C++, Aggiungi o Inserisci un link a una cella Node.js tramite C++, Aggiungi un link a un file esterno Node.js tramite C++
---

{{% alert color="primary" %}} 

Un collegamento ipertestuale viene utilizzato per creare un collegamento tra due entità. Tutti sono familiari con l'uso dei collegamenti ipertestuali, specialmente sui siti web.
Utilizzando Aspose.Cells, gli sviluppatori possono creare diversi tipi di collegamenti ipertestuali nei file Microsoft Excel. Questo argomento discute quali tipi di collegamenti ipertestuali sono supportati da Aspose.Cells e come possono essere utilizzati nei nostri file Excel.

{{% /alert %}} 

## **Aggiunta di Collegamenti Ipotestuali**
Aspose.Cells consente agli sviluppatori di aggiungere collegamenti ipertestuali ai file Excel usando l'API o fogli di calcolo creati manualmente (fogli di calcolo in cui i collegamenti vengono creati manualmente e Aspose.Cells viene usato per importarli in altri fogli).

Aspose.Cells fornisce una classe, [Workbook](https://reference.aspose.com/cells/nodejs-cpp/workbook) che rappresenta un file Microsoft Excel. La classe [Workbook](https://reference.aspose.com/cells/nodejs-cpp/workbook) contiene una [WorksheetCollection](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection) che permette di accedere a ogni foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato dalla classe [Worksheet](https://reference.aspose.com/cells/nodejs-cpp/worksheet). La classe [Worksheet](https://reference.aspose.com/cells/nodejs-cpp/worksheet) fornisce diversi metodi per aggiungere vari tipi di collegamenti ipertestuali ai file Excel.
## **Aggiunta di un link a un URL**
La collezione [getHyperlinks()](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getHyperlinks--) della classe [Worksheet](https://reference.aspose.com/cells/nodejs-cpp/worksheet). Ogni elemento in questa collezione rappresenta un [Hyperlink](https://reference.aspose.com/cells/nodejs-cpp/hyperlink). Aggiungi collegamenti ai URL chiamando il metodo [add](https://reference.aspose.com/cells/nodejs-cpp/hyperlinkcollection/#add-string-number-number-string-) della collezione [Hyperlinks](https://reference.aspose.com/cells/nodejs-cpp/hyperlinkcollection). Il metodo [add](https://reference.aspose.com/cells/nodejs-cpp/hyperlinkcollection/#add-string-number-number-string-) prende i seguenti parametri:

- Nome della cella, il nome della cella a cui verrà aggiunto il collegamento ipertestuale.
- Numero di righe, il numero di righe in questo intervallo di collegamenti ipertestuali.
- Numero di colonne, il numero di colonne in questo intervallo di collegamenti ipertestuali.
- URL, l'indirizzo URL.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Hyperlinks-AddLinkToURL.js" >}}


{{% alert color="primary" %}} 

Nell'esempio precedente, è stato aggiunto un collegamento ipertestuale a un URL in una cella vuota, **A1**. In tali casi, se una cella è vuota, l'indirizzo URL viene aggiunto anche a quella cella vuota come suo valore. Se la cella non è vuota e viene aggiunto un collegamento ipertestuale, il valore della cella appare come testo semplice. Per farlo apparire come un collegamento ipertestuale, applicare le impostazioni di formattazione appropriate su quella cella.

{{% /alert %}} 
## **Aggiunta di un link a una cella nello stesso file**
È possibile aggiungere collegamenti ipertestuali alle celle nello stesso file Excel chiamando il metodo [add](https://reference.aspose.com/cells/nodejs-cpp/hyperlinkcollection/#add-string-number-number-string-) della collezione [Hyperlinks](https://reference.aspose.com/cells/nodejs-cpp/hyperlinkcollection). Il metodo [add](https://reference.aspose.com/cells/nodejs-cpp/hyperlinkcollection/#add-string-number-number-string-) funziona sia per collegamenti interni che esterni. Una versione del metodo sovraccarico prende i seguenti parametri:

- Nome della cella, il nome della cella a cui verrà aggiunto il collegamento ipertestuale.
- Numero di righe, il numero di righe in questo intervallo di collegamenti ipertestuali.
- Numero di colonne, il numero di colonne in questo intervallo di collegamenti ipertestuali.
- URL, l'indirizzo della cella di destinazione.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Hyperlinks-AddLinkToCell.js" >}}


## **Aggiunta di un link a un file esterno**
È possibile aggiungere collegamenti ipertestuali a file Excel esterni chiamando il metodo [add](https://reference.aspose.com/cells/nodejs-cpp/hyperlinkcollection/#add-string-number-number-string-) della collezione [Hyperlinks](https://reference.aspose.com/cells/nodejs-cpp/hyperlinkcollection). Il metodo [add](https://reference.aspose.com/cells/nodejs-cpp/hyperlinkcollection/#add-string-number-number-string-) prende i seguenti parametri:

- Nome della cella, il nome della cella a cui verrà aggiunto il collegamento ipertestuale.
- Numero di righe, il numero di righe in questo intervallo di collegamenti ipertestuali.
- Numero di colonne, il numero di colonne in questo intervallo di collegamenti ipertestuali.
- URL, l'indirizzo di destinazione, file Excel esterno.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Hyperlinks-AddLinkToExternalFile.js" >}}



## **Argomenti avanzati**
- [Aggiungi collegamenti ipertestuali alle immagini](/cells/it/nodejs-cpp/add-image-hyperlinks/)
- [Rilevare il tipo di collegamento ipertestuale](/cells/it/nodejs-cpp/detect-hyperlink-type/)
- [Modifica dei collegamenti ipertestuali del foglio di lavoro](/cells/it/nodejs-cpp/editing-hyperlinks-of-worksheet/)
- [Ottieni i collegamenti ipertestuali nell'intervallo](/cells/it/nodejs-cpp/get-hyperlinks-in-range/)

