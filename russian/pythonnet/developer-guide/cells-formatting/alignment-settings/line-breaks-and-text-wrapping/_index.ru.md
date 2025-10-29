---
title: Перенос строк и перенос текста
description: Как реализовать перенос текста и автоматическую подгонку слов с помощью библиотеки Aspose.Cells для Python via .NET. Используя библиотеку Aspose.Cells для Python via .NET, вы можете легко вставлять текст в ячейки и настраивать метод переноса, например ручной перенос, автоматическую подгонку и т.д. В этом документе подробно описано, как реализовать эти функции, и приведены пример кода для参考.
keywords: Aspose.Cells для Python via .NET, переносы строк, обертка текста, размещение текста
type: docs
weight: 60
url: /ru/python-net/line-breaks-and-text-wrapping/
---

{{% alert color="primary" %}}

Чтобы гарантировать, что текст в ячейке может быть прочитан, можно применить явные разрывы строк и перенос текста. Перенос текста превращает одну строку в несколько в ячейке, а явные разрывы строк устанавливаются точно там, где вы их хотите.

{{% /alert %}}

## **Перенос текста в ячейке**

Чтобы перенести текст в ячейке, используйте свойство [**Style.is_text_wrapped**](https://reference.aspose.com/cells/python-net/aspose.cells/style/is_text_wrapped).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-LineBreakTextWrapping-WrapText-1.py" >}}

## **Использование явных переносов строк**

Вы можете использовать '\n' в C# и 'vbLf' в VB.NET для вставки явных переносов строк в ячейку.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-LineBreakTextWrapping-UseExplicitLineBreaks-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
