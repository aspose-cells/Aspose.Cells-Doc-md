---
title: Interruzioni di riga e ritorno a capo del testo
description: Come implementare il ritorno a capo automatico del testo e delle parole utilizzando la libreria Aspose.Cells in C#. Utilizzando la libreria Aspose.Cells, puoi facilmente inserire testo nelle celle e impostare il metodo di ritorno a capo automatico del testo, come il ritorno a capo automatico manuale, il ritorno a capo automatico, ecc. Questo documento descrive in dettaglio come per implementare queste funzionalità e fornisce codice di esempio come riferimento.
keywords: Aspose.Cells, line breaks, text wraps, text layout
type: docs
weight: 60
url: /it/net/line-breaks-and-text-wrapping/
---
{{% alert color="primary" %}}

Per garantire che il testo in una cella possa essere letto, è possibile applicare interruzioni di riga esplicite e andata a capo del testo. Il ritorno a capo del testo trasforma una riga in più righe in una cella, le quali interruzioni di riga esplicite vengono inserite esattamente dove desideri.

{{% /alert %}}

##  **Per racchiudere il testo in Cell**

Per mandare a capo il testo in una cella, utilizzare il comando[**Aspose.Cells.Style.IsTextWrapped**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/istextwrapped)proprietà.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LineBreakTextWrapping-WrapText-1.cs" >}}

##  **Per utilizzare interruzioni di riga esplicite**

È possibile utilizzare '\n' in C# e ' vbLf' in VB.NET per inserire interruzioni di riga esplicite in una cella.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LineBreakTextWrapping-UseExplicitLineBreaks-1.cs" >}}
