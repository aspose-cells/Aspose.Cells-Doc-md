---
title: Genera immagini di formattazione condizionale DataBars
type: docs
weight: 170
url: /it/java/generate-conditional-formatting-databars-images/
---

{{% alert color="primary" %}}

A volte è necessario generare immagini delle barre di dati formattate condizionalmente. È possibile utilizzare il [**DataBar.toImage()**](https://reference.aspose.com/cells/java/com.aspose.cells/databar#toImage-com.aspose.cells.Cell-com.aspose.cells.ImageOrPrintOptions-) metodo di Aspose.Cells per generare queste immagini. Questo articolo mostra come generare un'immagine di DataBar utilizzando Aspose.Cells.

{{% /alert %}}

## **Esempio**

Il seguente codice di esempio genera l'immagine DataBar della cella C1. Prima, accede all'oggetto condizione formato della cella, e poi da quell'oggetto, accede all'oggetto DataBar e utilizza il suo metodo [**DataBar.toImage()**](https://reference.aspose.com/cells/java/com.aspose.cells/databar#toImage-com.aspose.cells.Cell-com.aspose.cells.ImageOrPrintOptions-) per generare l'immagine della cella. Infine, salva l'immagine su disco.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-GenerateDatabarImage-1.java" >}}
{{< app/cells/assistant language="java" >}}
