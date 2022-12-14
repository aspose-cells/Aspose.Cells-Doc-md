---
title: Разрывы строк и перенос текста
type: docs
weight: 10
url: /ru/java/line-breaks-and-text-wrapping/
---
{{% alert color="primary" %}}

Чтобы гарантировать, что текст в ячейке может быть прочитан, можно применить явные разрывы строк и перенос текста. Обтекание текстом превращает одну строку в несколько в ячейке, при этом явные разрывы строк помещаются именно там, где вы хотите.

{{% /alert %}}

## **Чтобы обернуть текст в Cell**

 Чтобы перенести текст в ячейку, используйте[**Aspose.Cells.Style.setTextWrapped**](https://reference.aspose.com/cells/java/com.aspose.cells/style#IsTextWrapped)имущество.

В следующем примере кода показано, как использовать перенос текста и явные разрывы строк в ячейке.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-WrapTextinCell-1.java" >}}

## **Использование явных разрывов строк**

Вы можете использовать '\n' в Java, чтобы вставить явные разрывы строк в ячейке.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UseExplicitLineBreaks-UseExplicitLineBreaks.java" >}}
