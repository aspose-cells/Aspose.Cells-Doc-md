---
title: Convertire una tabella Excel in un intervallo di dati
type: docs
weight: 10
url: /it/java/convert-an-excel-table-to-a-range-of-data/
---

{{% alert color="primary" %}}

A volte si crea una tabella in Microsoft Excel e non si desidera continuare a lavorare con la funzionalità di tabella che la accompagna. Piuttosto, si desidera qualcosa che assomigli a una tabella. Per mantenere i dati in una tabella senza perdere la formattazione, convertire la tabella in un intervallo regolare di dati.

Aspose.Cells supporta questa funzionalità di Microsoft Excel per tabelle e oggetti lista.

{{% /alert %}}

## **Utilizzando Microsoft Excel**

Utilizzare la funzionalità **Converti in Intervallo** per convertire rapidamente una tabella in un intervallo senza perdere la formattazione. In Microsoft Excel 2007/2010:

1. Fare clic ovunque nella tabella per garantire che la cella attiva sia in una colonna della tabella.

![todo:image_alt_text](convert-an-excel-table-to-a-range-of-data_1.gif)

1. Sulla scheda **Design**, nel gruppo **Strumenti**, fare clic su **Converti in intervallo**.

![todo:image_alt_text](convert-an-excel-table-to-a-range-of-data_2.gif)

{{% alert color="primary" %}}

Le funzionalità della tabella non sono più disponibili dopo che la tabella è stata convertita in un intervallo. Ad esempio, le intestazioni di riga non includono più le frecce di ordinamento e filtro, e i riferimenti strutturati (riferimenti che usano i nomi delle tabelle) usati nelle formule diventano riferimenti di celle regolari.

{{% /alert %}}

## **Usare Aspose.Cells**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-tables-ConvertTableToRange-ConvertTableToRange.java" >}}

## **Converti Tabella in Intervallo con Opzioni**

Aspose.Cells fornisce opzioni aggiuntive durante la conversione della Tabella in Intervallo tramite la classe [**TableToRangeOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/TableToRangeOptions). La classe [**TableToRangeOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/TableToRangeOptions) fornisce la proprietà [**LastRow**](https://reference.aspose.com/cells/java/com.aspose.cells/tabletorangeoptions#LastRow) che consente di impostare l'ultimo indice della riga della tabella. La formattazione della tabella verrà mantenuta fino all'indice di riga specificato e il resto della formattazione verrà rimossa.

Il codice di esempio qui sotto dimostra l'uso della classe [**TableToRangeOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/TableToRangeOptions).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Tables-ConvertTableToRangeWithOptions-1.java" >}}
