---
title: Riutilizzo degli oggetti di stile
type: docs
weight: 3000
url: /it/net/reusing-style-objects/
---
{{% alert color="primary" %}}

Il riutilizzo degli oggetti di stile può risparmiare memoria e rendere più veloce un programma.

{{% /alert %}}

Per applicare una formattazione a un'ampia gamma di celle in un foglio di lavoro:

1. Crea un oggetto di stile.
1. Specificare gli attributi.
1. Applicare lo stile alle celle nell'intervallo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-ReusingStyleObjects-ReusingStyleObjects.cs" >}}

{{% alert color="primary" %}}

 Perché il[**Cell.GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle)/[**Cell.SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) L'approccio utilizza molta meno memoria ed è efficiente, la vecchia proprietà Cell.Style che consumava molta memoria non necessaria, è stata rimossa con il rilascio di Aspose.Cells 7.1.0.

{{% /alert %}}
