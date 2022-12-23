---
title: Найти ячейки с определенным стилем
type: docs
weight: 80
url: /ru/java/find-cells-with-specific-style/
description: В этой статье показано, как найти ячейки с определенным стилем с помощью MS Excel и Aspose.Cells for Java API.
keywords: find cells with specific style, find cells with specific style excel, find cells with specific style excel java, search cells with specific style, search cells with specific style excel, search cells with specific style excel java, how to find cells with specific style, how to find cells with specific style excel, how to find cells with specific style excel java
---
{{% alert color="primary" %}}

Иногда вам нужно найти ячейки с определенным стилем. В этой статье показано, как добиться этого с помощью Microsoft Excel, а также Aspose.Cells for Java API.

{{% /alert %}}

## Использование Microsoft Excel

Это шаги, необходимые для поиска ячеек с определенными стилями в MS Excel.

1.  Выбирать**Найти и выбрать** в**Вкладка «Главная»**.
1.  Выбирать**Находить**.
1.  Нажмите**Параметры**если дополнительные параметры не видны.
1.  Выбирать**Выберите формат из Cell...** от**Формат** падать.
1. Выберите ячейку со стилем, который вы хотите найти.
1.  Нажмите**Найти все** чтобы найти все ячейки со стилем, похожим на выбранную ячейку.

## Используя Aspose.Cells for Java

 Aspose.Cells for Java предоставляет функцию поиска ячеек на листе с определенным стилем. Для этого API предоставляет[**FindOptions.setStyle()**](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#Style) имущество.

### Образец кода

 Следующий фрагмент кода находит все ячейки, которые имеют тот же стиль, что и ячейка**А1** и изменяет текст внутри этих ячеек. Пожалуйста, посмотрите на скриншот исходного и выходного файлов, чтобы проанализировать вывод примера кода.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FindCellsWithSpecificStyle-FindCellsWithSpecificStyle.java" >}}

После выполнения кода все ячейки, имеющие тот же стиль, что и ячейка A1, будут иметь текст «Найдено».

### Скриншоты

![дело:изображение_альтернативный_текст](find-cells-with-specific-style_1.png)

**Фигура:** Исходный файл с ячейками, имеющими стили

 Вот выходной файл, сгенерированный следующим кодом. Вы можете увидеть все ячейки, которые имеют тот же стиль, что и ячейка**А1** есть текст "Найдено"

![дело:изображение_альтернативный_текст](find-cells-with-specific-style_2.png)

**Фигура:**Выходной файл с найденными ячейками после поиска по**А1** стиль
