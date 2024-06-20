---
title: Преобразование текста в столбцы с использованием Aspose.Cells
type: docs
weight: 30
url: /ru/python-net/convert-text-to-columns-using-aspose-cells/
description: Эта статья показывает, как преобразовать текст в столбцы с помощью Aspose.Cells для Python via .NET API.
keywords: Библиотека Python Excel, преобразование текста в столбцы в Python, преобразование текста в столбцы в Python.
---

## **Возможные сценарии использования**

Вы можете преобразовать ваш текст в столбцы с помощью Microsoft Excel. Эта функция доступна в разделе *Инструменты данных* на вкладке *Данные*. Чтобы разделить содержимое столбца на несколько столбцов, данные должны содержать определенный разделитель, такой как запятая (или любой другой символ), на основе которого Microsoft Excel разделяет содержимое ячейки на несколько ячеек. Aspose.Cells для Python via .NET также предоставляет эту функцию с помощью метода [**Worksheet.Cells.text_to_columns()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/text_to_columns/).

## **Преобразование текста в столбцы с использованием Aspose.Cells для библиотеки Python Excel**

В следующем образце кода объясняется использование метода [**Worksheet.Cells.text_to_columns()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/text_to_columns/). Код сначала добавляет имена людей в столбец A первого листа. Имя и фамилия разделены символом пробела. Затем он применяет метод [**Worksheet.Cells.text_to_columns()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/text_to_columns/) к столбцу A и сохраняет его как выходной файл Excel. Если вы откроете [выходной файл Excel](25395213.xlsx), вы увидите, что имена находятся в столбце A, а фамилии - в столбце B, как показано на этом скриншоте.

![todo:image_alt_text](convert-text-to-columns-using-aspose-cells_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-ConvertTextToColumns.py" >}}
