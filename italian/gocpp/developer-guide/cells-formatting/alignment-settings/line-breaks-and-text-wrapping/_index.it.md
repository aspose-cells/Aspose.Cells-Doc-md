---
title: Interruzioni di riga e avvolgimento del testo con Golang tramite C++
description: Come implementare l adattamento del testo e il word wrap usando la libreria Aspose.Cells in C++. Utilizzando la libreria Aspose.Cells, puoi facilmente inserire testo nelle celle e impostare il metodo di adattamento del testo, come il word wrap manuale, il word wrap, ecc. Questo documento dettaglia come implementare queste funzionalità e fornisce codice di esempio per il tuo riferimento.
keywords: Aspose.Cells, interruzioni di riga, ritorno a capo, layout testo
type: docs
weight: 60
url: /it/go-cpp/line-breaks-and-text-wrapping/
---

{{% alert color="primary" %}}

Per garantire che il testo in una cella possa essere letto, possono essere applicati ritorni a capo espliciti e a capo automatico del testo. Il ritorno a capo del testo trasforma una riga in più in una cella, mentre i ritorni a capo espliciti inseriscono spazi esattamente dove si desidera.

{{% /alert %}}

## **Per incapsulare il testo in una cella**

Per avvolgere il testo in una cella, usa la proprietà [**Aspose.Cells.Style.IsTextWrapped**](https://reference.aspose.com/cells/go-cpp/style/istextwrapped/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-LineBreaksAndTextWrapping.go" >}}
## **Per utilizzare ritorni a capo espliciti**

Puoi usare '\n' in C++ per inserire interruzioni di riga esplicite in una cella.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-LineBreaksAndTextWrapping-1.go" >}}
