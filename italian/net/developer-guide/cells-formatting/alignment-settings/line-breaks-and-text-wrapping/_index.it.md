---
title: Interruzioni di riga e ritorno a capo del testo
type: docs
weight: 60
url: /it/net/line-breaks-and-text-wrapping/
---
{{% alert color="primary" %}}

Per garantire che il testo in una cella possa essere letto, è possibile applicare interruzioni di riga esplicite e ritorno a capo automatico. Il ritorno a capo trasforma una riga in più righe in una cella, che le interruzioni di riga esplicite inseriscono nelle interruzioni esattamente dove le desideri.

{{% /alert %}}

## **Per avvolgere il testo in un Cell**

 Per disporre il testo in una cella, utilizzare il[**Aspose.Cells.Style.IsTextWrapped**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/istextwrapped)proprietà.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LineBreakTextWrapping-WrapText-1.cs" >}}

## **Per utilizzare interruzioni di riga esplicite**

È possibile utilizzare '\n' in C# e 'vbLf' in VB.NET per inserire interruzioni di riga esplicite in una cella.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LineBreakTextWrapping-UseExplicitLineBreaks-1.cs" >}}
