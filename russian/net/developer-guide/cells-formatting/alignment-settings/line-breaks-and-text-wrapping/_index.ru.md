---
title: Разрывы строк и перенос текста
description: Как реализовать перенос текста и слов с помощью библиотеки Aspose.Cells в C#. Используя библиотеку Aspose.Cells, вы можете легко вставлять текст в ячейки и устанавливать метод переноса текста, например ручной перенос слов, перенос слов и т. д. В этом документе подробно описано, как для реализации этих функций и предоставляет вам пример кода.
keywords: Aspose.Cells, line breaks, text wraps, text layout
type: docs
weight: 60
url: /ru/net/line-breaks-and-text-wrapping/
---
{{% alert color="primary" %}}

Чтобы обеспечить возможность чтения текста в ячейке, можно применить явные разрывы строк и перенос текста. Перенос текста превращает одну строку в ячейке в несколько, а явные разрывы строк помещают разрывы именно там, где вы хотите.

{{% /alert %}}

##  **Чтобы обернуть текст в Cell**

Чтобы переместить текст в ячейку, используйте[**Aspose.Cells.Style.IsTextWrapped**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/istextwrapped)свойство.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LineBreakTextWrapping-WrapText-1.cs" >}}

##  **Использование явных разрывов строк**

Вы можете использовать '\n' в C# и 'vbLf' в VB.NET для вставки явных разрывов строк в ячейку.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LineBreakTextWrapping-UseExplicitLineBreaks-1.cs" >}}
