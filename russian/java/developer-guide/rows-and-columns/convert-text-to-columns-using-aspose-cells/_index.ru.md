---
title: Преобразование текста в столбцы с использованием Aspose.Cells
type: docs
weight: 70
url: /ru/java/convert-text-to-columns-using-aspose-cells/
---

## **Возможные сценарии использования**
Вы можете преобразовать ваш Текст в Столбцы с помощью Microsoft Excel. Эта функция доступна во вкладке *Данные* в разделе *Инструменты данных*. Для разделения содержимого столбца на несколько столбцов данные должны содержать определитель, например запятую (или другой символ), по которому Microsoft Excel разделяет содержимое ячейки. Aspose.Cells также предоставляет эту функцию через метод [TextToColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#textToColumns-int-int-int-com.aspose.cells.TxtLoadOptions-).
## **Преобразование текста в столбцы с использованием Aspose.Cells**
Следующий пример кода демонстрирует использование метода [TextToColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#textToColumns-int-int-int-com.aspose.cells.TxtLoadOptions-). Сначала он добавляет имена людей в столбец А первого листа. Имя и фамилия разделены пробелом. Потом применяется метод [TextToColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#textToColumns-int-int-int-com.aspose.cells.TxtLoadOptions-) к столбцу А и сохраняется как итоговый файл Excel. Открыв [выходной файл Excel](25395230.xlsx), вы увидите, что имена расположены в столбце А, а фамилии — в столбце В, как показано на скриншоте.

![todo:image_alt_text](convert-text-to-columns-using-aspose-cells_1.png)
## **Образец кода**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-ConvertTexttoCols-ConvertTexttoCols.java" >}}
{{< app/cells/assistant language="java" >}}
