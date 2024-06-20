---
title: Перенос строк и перенос текста
description: Как реализовать перенос текста и перенос слов с использованием библиотеки Aspose.Cells в C#. При использовании библиотеки Aspose.Cells, вы можете легко вставлять текст в ячейки и устанавливать метод переноса текста, такие как ручной перенос слов, перенос слов и т.д. В этом документе подробно описано, как реализовать эти функции и предоставлен образец кода для вашего ознакомления.
keywords: Aspose.Cells, перенос строки, перенос текста, макет текста
type: docs
weight: 60
url: /ru/net/line-breaks-and-text-wrapping/
---

{{% alert color="primary" %}}

Чтобы гарантировать, что текст в ячейке может быть прочитан, можно применить явные разрывы строк и перенос текста. Перенос текста превращает одну строку в несколько в ячейке, а явные разрывы строк устанавливаются точно там, где вы их хотите.

{{% /alert %}}

## **Перенос текста в ячейке**

Чтобы перенести текст в ячейке, используйте свойство [**Aspose.Cells.Style.IsTextWrapped**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/istextwrapped).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LineBreakTextWrapping-WrapText-1.cs" >}}

## **Использование явных переносов строк**

Вы можете использовать '\n' в C# и 'vbLf' в VB.NET для вставки явных переносов строк в ячейку.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LineBreakTextWrapping-UseExplicitLineBreaks-1.cs" >}}
