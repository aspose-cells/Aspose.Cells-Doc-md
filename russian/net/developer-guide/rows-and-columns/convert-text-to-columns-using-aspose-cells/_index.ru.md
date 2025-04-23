---
title: Преобразование текста в столбцы с использованием Aspose.Cells
type: docs
weight: 30
url: /ru/net/convert-text-to-columns-using-aspose-cells/
---

## **Возможные сценарии использования**

Вы можете преобразовать ваш текст в столбцы с использованием Microsoft Excel. Эта функция доступна в разделе *Инструменты данных* на вкладке *Данные*. Для разделения содержимого столбца на несколько столбцов данные должны содержать определенный разделитель, такой как запятая (или любой другой символ), на основе которого Microsoft Excel разделяет содержимое ячейки на несколько ячеек. Aspose.Cells также предоставляет эту функцию с помощью метода [**Worksheet.Cells.TextToColumns()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/texttocolumns).

## **Преобразование текста в столбцы с использованием Aspose.Cells**

В следующем образце кода объясняется использование метода [**Worksheet.Cells.TextToColumns()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/texttocolumns). Код сначала добавляет имена людей в столбец A первого листа. Имя и фамилия разделены символом пробела. Затем он применяет метод [**Worksheet.Cells.TextToColumns()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/texttocolumns) к столбцу A и сохраняет его как выходной файл Excel. Если вы откроете [выходной файл Excel](25395213.xlsx), вы увидите, что имена находятся в столбце A, а фамилии - в столбце B, как показано на этом скриншоте.

![todo:image_alt_text](convert-text-to-columns-using-aspose-cells_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-ConvertTextToColumns.cs" >}}
{{< app/cells/assistant language="csharp" >}}
