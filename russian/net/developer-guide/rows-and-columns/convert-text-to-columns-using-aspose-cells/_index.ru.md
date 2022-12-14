---
title: Преобразование текста в столбцы с помощью Aspose.Cells
type: docs
weight: 30
url: /ru/net/convert-text-to-columns-using-aspose-cells/
---
## **Возможные сценарии использования**

Вы можете преобразовать текст в столбцы, используя Microsoft Excel. Эта функция доступна из*Инструменты данных* под*Данные* вкладка Чтобы разделить содержимое столбца на несколько столбцов, данные должны содержать определенный разделитель, например запятую (или любой другой символ), на основе которого Microsoft Excel разделяет содержимое ячейки на несколько ячеек. Aspose.Cells также предоставляет эту функцию через[**Рабочий лист.Cells.TextToColumns()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/texttocolumns)метод.

## **Преобразование текста в столбцы с помощью Aspose.Cells**

 В следующем примере кода объясняется использование[**Рабочий лист.Cells.TextToColumns()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/texttocolumns) метод. Код сначала добавляет имена некоторых людей в столбец A первого рабочего листа. Имя и фамилия разделены пробелом. Затем применяется[**Рабочий лист.Cells.TextToColumns()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/texttocolumns) метод в столбце A и сохраните его как выходной файл Excel. Если вы откроете[выходной файл excel](25395213.xlsx), вы увидите, что имена находятся в столбце A, а фамилии — в столбце B, как показано на этом снимке экрана.

![дело:изображение_альтернативный_текст](convert-text-to-columns-using-aspose-cells_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-ConvertTextToColumns.cs" >}}
