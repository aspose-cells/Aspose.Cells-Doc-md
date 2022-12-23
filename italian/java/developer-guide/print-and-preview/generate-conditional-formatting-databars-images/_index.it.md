---
title: Genera immagini DataBars con formattazione condizionale
type: docs
weight: 170
url: /it/java/generate-conditional-formatting-databars-images/
---
{{% alert color="primary" %}}

 A volte, è necessario generare immagini di DataBar a formattazione condizionale. Puoi usare lo Aspose.Cells[**DataBar.toImage()**](https://reference.aspose.com/cells/java/com.aspose.cells/databar#toImage(com.aspose.cells.Cell,%20com.aspose.cells.ImageOrPrintOptions)metodo per generare queste immagini. Questo articolo mostra come generare un'immagine DataBar utilizzando Aspose.Cells.

{{% /alert %}}

## **Esempio**

 Il codice di esempio seguente genera l'immagine DataBar della cella C1. Innanzitutto, accede all'oggetto condizione di formato della cella, quindi da tale oggetto accede all'oggetto DataBar e utilizza il suo[**DataBar.toImage()**](https://reference.aspose.com/cells/java/com.aspose.cells/databar#toImage(com.aspose.cells.Cell,%20com.aspose.cells.ImageOrPrintOptions)) metodo per generare l'immagine della cella. Infine, salva l'immagine su disco.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-GenerateDatabarImage-1.java" >}}
