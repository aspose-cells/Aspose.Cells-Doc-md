---
title: Перенос строк и перенос текста
type: docs
weight: 10
url: /ru/java/line-breaks-and-text-wrapping/
---

{{% alert color="primary" %}}

Чтобы гарантировать, что текст в ячейке может быть прочитан, можно применить явные разрывы строк и перенос текста. Перенос текста превращает одну строку в несколько в ячейке, а явные разрывы строк устанавливаются точно там, где вы их хотите.

{{% /alert %}}

## **Перенос текста в ячейке**

Чтобы перенести текст в ячейке, используйте свойство [**Aspose.Cells.Style.setTextWrapped**](https://reference.aspose.com/cells/java/com.aspose.cells/style#IsTextWrapped).

В следующем образце кода показано, как использовать перенос текста и явные переносы строк в ячейке.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-WrapTextinCell-1.java" >}}

## **Использование явных переносов строк**

Вы можете использовать '\n' в Java для вставки явных переносов строк в ячейку.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UseExplicitLineBreaks-UseExplicitLineBreaks.java" >}}
