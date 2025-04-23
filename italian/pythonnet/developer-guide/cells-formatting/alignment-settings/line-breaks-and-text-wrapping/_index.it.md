---
title: Interruzioni di riga e a capo automatico del testo
description: Come implementare l’andamento del testo e il word wrap usando la libreria Aspose.Cells per Python via .NET. Usando questa libreria, puoi facilmente inserire testo nelle celle e impostare il metodo di wrapping del testo, come il word wrap manuale, il word wrap automatico, ecc. Questo documento dettaglia come implementare queste funzionalità e fornisce esempi di codice.
keywords: Aspose.Cells per Python via .NET, interruzioni di riga, wrap del testo, layout del testo
type: docs
weight: 60
url: /it/python-net/line-breaks-and-text-wrapping/
---

{{% alert color="primary" %}}

Per garantire che il testo in una cella possa essere letto, possono essere applicati ritorni a capo espliciti e a capo automatico del testo. Il ritorno a capo del testo trasforma una riga in più in una cella, mentre i ritorni a capo espliciti inseriscono spazi esattamente dove si desidera.

{{% /alert %}}

## **Per incapsulare il testo in una cella**

Per incapsulare il testo in una cella, utilizzare la proprietà [**Style.is_text_wrapped**](https://reference.aspose.com/cells/python-net/aspose.cells/style/is_text_wrapped).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-LineBreakTextWrapping-WrapText-1.py" >}}

## **Per utilizzare ritorni a capo espliciti**

Puoi utilizzare '\n' in C# e ' vbLf' in VB.NET per inserire ritorni a capo espliciti in una cella.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-LineBreakTextWrapping-UseExplicitLineBreaks-1.py" >}}

