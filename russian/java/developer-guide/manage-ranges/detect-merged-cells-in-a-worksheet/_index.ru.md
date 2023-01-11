﻿---
title: Обнаружение слияния Cells на рабочем листе
type: docs
weight: 3000
url: /ru/java/detect-merged-cells-in-a-worksheet/
---
{{% alert color="primary" %}}

В Microsoft Excel несколько ячеек можно объединить в одну. Это часто используется для создания сложных таблиц или для создания ячейки с заголовком, охватывающим несколько столбцов.

Aspose.Cells позволяет идентифицировать объединенные области ячеек на листе. Вы также можете разъединить их. В этой статье приведены самые простые строки кода для выполнения задачи с использованием Aspose.Cells.

В этой статье приведены краткие инструкции о том, как найти и разъединить объединенные ячейки на листе.

{{% /alert %}}

## **Демонстрация**

 В этом примере используется файл шаблона Microsoft Excel с именем**Объединить пробную версию**. У него есть несколько объединенных областей ячеек на листе, также называемом пробным слиянием.

**Файл шаблона**

![дело:изображение_альтернативный_текст](detect-merged-cells-in-a-worksheet_1.png)

 Aspose.Cells обеспечивает[**Cells.getMergedCells**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MergedCells)метод, который используется для получения ArrayList объединенных областей ячеек.

Когда приведенный ниже код выполняется, он очищает содержимое листа и разъединяет все области ячеек перед повторным сохранением файла.

**Выходной файл**

![дело:изображение_альтернативный_текст](detect-merged-cells-in-a-worksheet_2.png)

## **Пример кода**

См. следующий пример кода, чтобы узнать, как идентифицировать объединенные области ячеек на листе и разъединить их.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DetectMergedCells-DetectMergedCells.java" >}}

## **Статьи по Теме**

- [Объединение и разделение ячеек](/cells/ru/java/merging-and-unmerging-cells/).