---
title: Genera immagini DataBars con formattazione condizionale
type: docs
weight: 40
url: /it/net/generate-conditional-formatting-databars-images/
---
{{% alert color="primary" %}}

 A volte, è necessario generare immagini di DataBar a formattazione condizionale. Puoi usare lo Aspose.Cells[**DataBar.ToImage()**](https://reference.aspose.com/cells/net/aspose.cells/databar/methods/toimage) metodo per generare queste immagini. Questo articolo mostra come generare un'immagine DataBar utilizzando Aspose.Cells.

{{% /alert %}}

Il codice di esempio seguente genera l'immagine DataBar della cella C1. Innanzitutto, accede all'oggetto condizione di formato della cella, quindi da tale oggetto accede a[**DataBar**](https://reference.aspose.com/cells/net/aspose.cells/databar) oggetto e usa il suo[**Immaginare()**](https://reference.aspose.com/cells/net/aspose.cells/databar/methods/toimage)metodo per generare l'immagine della cella. Infine, salva l'immagine su disco.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageConditionalFormatting-GenerateDatabarImage-1.cs" >}}
