---
title: Convertire il testo in colonne usando Aspose.Cells
type: docs
weight: 30
url: /it/net/convert-text-to-columns-using-aspose-cells/
---

## **Possibili Scenari di Utilizzo**

Puoi convertire il tuo testo in colonne utilizzando Microsoft Excel. Questa funzione è disponibile da *Strumenti dati* nella scheda *Dati*. Per dividere i contenuti di una colonna in più colonne, i dati devono contenere un delimitatore specifico come una virgola (o qualsiasi altro carattere) in base al quale Microsoft Excel dividerà i contenuti di una cella in più celle. Anche Aspose.Cells fornisce questa funzione tramite il metodo [**Worksheet.Cells.TextToColumns()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/texttocolumns)

## **Converti testo in colonne utilizzando Aspose.Cells**

Il codice di esempio seguente spiega l'uso del metodo [**Worksheet.Cells.TextToColumns()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/texttocolumns). Il codice prima aggiunge alcune persone nel nome della colonna A del primo foglio di lavoro. Il nome e cognome sono separati dal carattere spazio. Quindi applica il metodo [**Worksheet.Cells.TextToColumns()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/texttocolumns) sulla colonna A e lo salva come file di output excel. Se apri il [file di output excel](25395213.xlsx), vedrai che i nomi sono nella colonna A mentre i cognomi sono nella colonna B come mostrato in questa schermata.

![todo:image_alt_text](convert-text-to-columns-using-aspose-cells_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-ConvertTextToColumns.cs" >}}
