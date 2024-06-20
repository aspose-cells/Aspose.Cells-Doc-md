---
title: Tabelle e intervalli
type: docs
weight: 50
url: /it/net/tables-and-ranges/
---

## **Introduzione**

A volte si crea una tabella in Microsoft Excel e non si desidera continuare a lavorare con la funzionalità di tabella che la accompagna. Piuttosto, si desidera qualcosa che assomigli a una tabella. Per mantenere i dati in una tabella senza perdere la formattazione, convertire la tabella in un intervallo regolare di dati.
Aspose.Cells supporta questa funzionalità di Microsoft Excel per tabelle e oggetti elenco.

## **Utilizzando Microsoft Excel**

Utilizzare la funzionalità **Converti in Intervallo** per convertire rapidamente una tabella in un intervallo senza perdere la formattazione. In Microsoft Excel 2007/2010:

1. Fare clic ovunque nella tabella per garantire che la cella attiva sia in una colonna della tabella.
1. Sulla scheda **Design**, nel gruppo **Strumenti**, fare clic su **Converti in intervallo**.

## **Usare Aspose.Cells**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Tables-ConvertTableToRange-1.cs" >}}

{{% alert color="primary" %}}

Le funzionalità della tabella non sono più disponibili dopo che la tabella è stata convertita in un intervallo. Ad esempio, le intestazioni di riga non includono più le frecce di ordinamento e filtro, e i riferimenti strutturati (riferimenti che usano i nomi delle tabelle) usati nelle formule diventano riferimenti di celle regolari.

{{% /alert %}}

## **Converti Tabella in Intervallo con Opzioni**

Aspose.Cells fornisce opzioni aggiuntive durante la conversione della tabella in un intervallo tramite la classe [**TableToRangeOptions**](https://reference.aspose.com/cells/net/aspose.cells.tables/tabletorangeoptions). La classe [**TableToRangeOptions**](https://reference.aspose.com/cells/net/aspose.cells.tables/tabletorangeoptions) fornisce la proprietà [**LastRow**](https://reference.aspose.com/cells/net/aspose.cells.tables/tabletorangeoptions/properties/lastrow) che consente di impostare l'ultimo indice della riga della tabella. La formattazione della tabella verrà mantenuta fino all'indice di riga specificato e il resto della formattazione verrà rimossa.

Il codice di esempio qui sotto dimostra l'uso della classe [**TableToRangeOptions**](https://reference.aspose.com/cells/net/aspose.cells.tables/tabletorangeoptions).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Tables-ConvertTableToRangeWithOptions-1.cs" >}}
