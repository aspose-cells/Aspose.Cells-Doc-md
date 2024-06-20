---
title: Обнаружение объединенных ячеек на листе
type: docs
weight: 3000
url: /ru/java/detect-merged-cells-in-a-worksheet/
---

{{% alert color="primary" %}}

В Microsoft Excel несколько ячеек можно объединить в одну. Это часто используется для создания сложных таблиц или для создания ячейки, содержащей заголовок, который охватывает несколько столбцов.

Aspose.Cells позволяет определить объединенные области ячеек на листе. Вы также можете их разъединить. В этой статье приведены простейшие строки кода для выполнения этой задачи с использованием Aspose.Cells.

Эта статья дает краткие инструкции о том, как найти и затем разъединить объединенные ячейки на листе.

{{% /alert %}}

## **Демонстрация**

В этом примере используется шаблонный файл Microsoft Excel под названием **MergeTrial**. В нем есть несколько объединенных областей ячеек на листе также называемого Merge Trial.

**Файл шаблона**

![todo:image_alt_text](detect-merged-cells-in-a-worksheet_1.png)

Aspose.Cells предоставляет метод [**Cells.getMergedCells**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MergedCells), который используется для получения ArrayList объединенных областей ячеек.

Когда выполняется приведенный ниже код, он очищает содержимое листа и разъединяет все области ячеек перед повторным сохранением файла.

**Выходной файл**

![todo:image_alt_text](detect-merged-cells-in-a-worksheet_2.png)

## **Пример кода**

Пожалуйста, ознакомьтесь с приведенным ниже образцом кода, чтобы узнать, как определить объединенные области ячеек на листе и разъединить их.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DetectMergedCells-DetectMergedCells.java" >}}

## **Связанные статьи**

- [Объединение и разбиение ячеек](/cells/ru/java/merging-and-unmerging-cells/).
