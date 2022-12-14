---
title: Tabelle e intervalli
type: docs
weight: 50
url: /it/net/tables-and-ranges/
---
## **introduzione**

A volte crei una tabella in Microsoft Excel e non vuoi continuare a lavorare con la funzionalità della tabella che ne deriva. Invece, vuoi qualcosa che assomigli a un tavolo. Per mantenere i dati in una tabella senza perdere la formattazione, convertire la tabella in un normale intervallo di dati.
Aspose.Cells supporta questa funzionalità di Microsoft Excel per tabelle e oggetti elenco.

## **Utilizzando Microsoft Excel**

 Utilizzare il**Converti in intervallo** funzionalità per convertire rapidamente una tabella in un intervallo senza perdere la formattazione. In Microsoft Excel 2007/2010:

1. Fare clic in un punto qualsiasi della tabella per assicurarsi che la cella attiva sia in una colonna della tabella.
1.  Sul**Disegno** scheda, nel**Strumenti** gruppo, fare clic**Converti in intervallo**.

## **Utilizzando Aspose.Cells**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Tables-ConvertTableToRange-1.cs" >}}

{{% alert color="primary" %}}

Le funzionalità della tabella non sono più disponibili dopo che la tabella è stata convertita in un intervallo. Ad esempio, le intestazioni di riga non includono più le frecce di ordinamento e filtro e i riferimenti strutturati (riferimenti che utilizzano nomi di tabella) utilizzati nelle formule si trasformano in normali riferimenti di cella.

{{% /alert %}}

## **Converti tabella in intervallo con le opzioni**

Aspose.Cells fornisce opzioni aggiuntive durante la conversione della tabella in intervallo attraverso il[**TableToRangeOptions**](https://reference.aspose.com/cells/net/aspose.cells.tables/tabletorangeoptions) classe. Il[**TableToRangeOptions**](https://reference.aspose.com/cells/net/aspose.cells.tables/tabletorangeoptions)la classe fornisce[**Ultima riga**](https://reference.aspose.com/cells/net/aspose.cells.tables/tabletorangeoptions/properties/lastrow)proprietà che consente di impostare l'ultimo indice della riga della tabella. La formattazione della tabella verrà mantenuta fino all'indice di riga specificato e il resto della formattazione verrà rimosso.

Il codice di esempio fornito di seguito dimostra l'uso di[**TableToRangeOptions**](https://reference.aspose.com/cells/net/aspose.cells.tables/tabletorangeoptions)classe.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Tables-ConvertTableToRangeWithOptions-1.cs" >}}
