---
title: Преобразование текста в столбцы с помощью Aspose.Cells
type: docs
weight: 70
url: /ru/java/convert-text-to-columns-using-aspose-cells/
---
## **Возможные сценарии использования**
Вы можете преобразовать текст в столбцы, используя Microsoft Excel. Эта функция доступна из*Инструменты данных* под*Данные* вкладка Чтобы разделить содержимое столбца на несколько столбцов, данные должны содержать определенный разделитель, например запятую (или любой другой символ), на основе которого Microsoft Excel разделяет содержимое ячейки на несколько ячеек. Aspose.Cells также предоставляет эту функцию через[тексттоколоннс](https://reference.aspose.com/cells/java/com.aspose.cells/cells#textToColumns\(int,%20int,%20int,%20com.aspose.cells.TxtLoadOptions\)) метод.
## **Преобразование текста в столбцы с помощью Aspose.Cells**
Следующий пример кода объясняет использование[тексттоколоннс](https://reference.aspose.com/cells/java/com.aspose.cells/cells#textToColumns\(int,%20int,%20int,%20com.aspose.cells.TxtLoadOptions\)) метод. Код сначала добавляет имена некоторых людей в столбец A первого рабочего листа. Имя и фамилия разделены пробелом. Затем он применяет[тексттоколоннс](https://reference.aspose.com/cells/java/com.aspose.cells/cells#textToColumns\(int,%20int,%20int,%20com.aspose.cells.TxtLoadOptions\) ) для столбца A и сохраняет его как выходной файл Excel. Если вы откроете[выходной файл excel](25395230.xlsx), вы увидите, что имена находятся в столбце A, а фамилии — в столбце B, как показано на этом снимке экрана.

![дело:изображение_альтернативный_текст](convert-text-to-columns-using-aspose-cells_1.png)
## **Образец кода**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-ConvertTexttoCols-ConvertTexttoCols.java" >}}
