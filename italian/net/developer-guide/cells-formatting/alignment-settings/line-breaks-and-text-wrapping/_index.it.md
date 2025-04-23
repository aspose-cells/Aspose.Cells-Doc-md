---
title: Interruzioni di riga e a capo automatico del testo
description: Come implementare l a capo automatico del testo e il ritorno a capo usando la libreria Aspose.Cells in C#. Utilizzando la libreria Aspose.Cells, è possibile inserire facilmente del testo nelle celle e impostare il metodo di a capo automatico del testo, come ritorno a capo manuale, ritorno a capo automatico, ecc. Questo documento dettaglia come implementare queste funzionalità e fornisce del codice di esempio per il riferimento.
keywords: Aspose.Cells, interruzioni di riga, ritorno a capo, layout testo
type: docs
weight: 60
url: /it/net/line-breaks-and-text-wrapping/
---

{{% alert color="primary" %}}

Per garantire che il testo in una cella possa essere letto, possono essere applicati ritorni a capo espliciti e a capo automatico del testo. Il ritorno a capo del testo trasforma una riga in più in una cella, mentre i ritorni a capo espliciti inseriscono spazi esattamente dove si desidera.

{{% /alert %}}

## **Per incapsulare il testo in una cella**

Per incapsulare il testo in una cella, utilizzare la proprietà [**Aspose.Cells.Style.IsTextWrapped**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/istextwrapped).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LineBreakTextWrapping-WrapText-1.cs" >}}

## **Per utilizzare ritorni a capo espliciti**

Puoi utilizzare '\n' in C# e ' vbLf' in VB.NET per inserire ritorni a capo espliciti in una cella.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LineBreakTextWrapping-UseExplicitLineBreaks-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
