---
title: Разрывы строк и перенос текста
type: docs
weight: 60
url: /ru/net/line-breaks-and-text-wrapping/
---
{{% alert color="primary" %}}

Чтобы гарантировать, что текст в ячейке может быть прочитан, можно применить явные разрывы строк и перенос текста. Обтекание текстом превращает одну строку в несколько в ячейке, при этом явные разрывы строк помещаются именно там, где вы хотите.

{{% /alert %}}

## **Чтобы обернуть текст в Cell**

 Чтобы перенести текст в ячейку, используйте[**Aspose.Cells.Style.IsTextWrapped**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/istextwrapped)имущество.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LineBreakTextWrapping-WrapText-1.cs" >}}

## **Использование явных разрывов строк**

Вы можете использовать '\n' в C# и ' vbLf' в VB.NET, чтобы вставить явные разрывы строк в ячейке.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LineBreakTextWrapping-UseExplicitLineBreaks-1.cs" >}}
