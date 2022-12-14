---
title: Получить список шрифтов, используемых в электронной таблице или книге
type: docs
weight: 20
url: /ru/java/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/
---
## **Возможные сценарии использования**

 Часто бывает необходимо знать шрифты, используемые в вашей книге для целей рендеринга. Когда вы конвертируете свою книгу в PDF или изображение, Aspose.Cells требует, чтобы все необходимые шрифты были установлены в вашей системе или присутствовали в вашем**каталог шрифтов**Если Aspose.Cells не может найти нужный шрифт, он пытается заменить его другим подходящим шрифтом, который присутствует в вашей системе или в вашем каталоге шрифтов и может заменить ваш реальный шрифт. Это не только приводит к нежелательному отображению PDF или изображений, но и требует времени на поиск подходящих шрифтов.

Чтобы иметь дело с такими случаями, вы должны знать, какие шрифты используются в вашей книге, а затем либо установить эти шрифты в своей системе в случае среды Windows, либо поместить их в каталог шрифтов в случае среды Windows или Linux.

 Aspose.Cells обеспечивает[Рабочая книга.getFonts()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#getFonts()), который возвращает список всех шрифтов, используемых в вашей книге или электронной таблице.

## **Получить список шрифтов, используемых в электронной таблице или книге**

 Следующий пример кода загружает исходный файл Excel и извлекает список используемых внутри него шрифтов. У него есть один фиктивный рабочий лист, на который для иллюстрации добавлены несколько фиктивных шрифтов. Когда код печатает все шрифты внутри книги, он также печатает эти фиктивные шрифты. На следующем снимке экрана показано[образец эксель файла](sampleGetFonts.xlsx)и как перечислены фиктивные шрифты.

![дело:изображение_альтернативный_текст](get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetFontsUsedinWorkbook-GetFontsUsedinWorkbook.java" >}}

## **Консольный вывод**

 Вот вывод консоли приведенного выше примера кода при выполнении с заданным[образец эксель файла](sampleGetFonts.xlsx).

{{< highlight "java" >}}

Aspose.Cells.Font [ Calibri; 11.0; Regular; com.aspose.cells.Color@ff000000 ]Aspose.Cells.Font [ Arial; 10.0; Regular; com.aspose.cells.Color@ff000000 ]Aspose.Cells.Font [ Calibri; 10.0; Bold; com.aspose.cells.Color@ff000000 ]Aspose.Cells.Font [ Calibri; 10.0; Regular; com.aspose.cells.Color@ff808080 ]Aspose.Cells.Font [ Calibri; 10.0; Regular; com.aspose.cells.Color@ff376268 ]Aspose.Cells.Font [ Calibri; 16.0; Bold; com.aspose.cells.Color@ffffffff ]Aspose.Cells.Font [ Calibri; 36.0; Regular; com.aspose.cells.Color@ff376268 ]Aspose.Cells.Font [ Calibri; 20.0; Bold; com.aspose.cells.Color@ff376268 ]Aspose.Cells.Font [ Calibri; 16.0; Regular; com.aspose.cells.Color@ff376268 ]Aspose.Cells.Font [ Calibri; 11.0; Regular; com.aspose.cells.Color@ff376268 ]Aspose.Cells.Font [ Calibri; 11.0; Bold; com.aspose.cells.Color@ff376268 ]Aspose.Cells.Font [ Calibri; 11.0; Bold; com.aspose.cells.Color@ffffffff ]Aspose.Cells.Font [ Calibri; 11.0; Italic; com.aspose.cells.Color@ff376268 ]Aspose.Cells.Font [ Calibri; 16.0; Regular; com.aspose.cells.Color@ff376268 ]Aspose.Cells.Font [ Calibri; 16.0; Bold; com.aspose.cells.Color@ff376268 ]Aspose.Cells.Font [ Calibri; 16.0; Regular; com.aspose.cells.Color@ff000000 ]Aspose.Cells.Font [ Calibri; 16.0; Regular; com.aspose.cells.Color@ff294a4e ]Aspose.Cells.Font [ Calibri; 16.0; Regular; com.aspose.cells.Color@ff294a4e ]Aspose.Cells.Font [ Calibri; 12.0; Regular; com.aspose.cells.Color@ff294a4e ]Aspose.Cells.Font [ Calibri; 11.0; Regular; com.aspose.cells.Color@ff294a4e ]Aspose.Cells.Font [ Calibri; 11.0; Bold; com.aspose.cells.Color@ffffffff ]Aspose.Cells.Font [ Dummy-Arial-X; 11.0; Regular; com.aspose.cells.Color@ff000000 ]Aspose.Cells.Font [ Dummy-Arial-Y; 11.0; Regular; com.aspose.cells.Color@ff000000 ]Aspose.Cells.Font [ Dummy-Arial-Z; 11.0; Regular; com.aspose.cells.Color@ff000000 ]Aspose.Cells.Font [ Dummy-Times-I; 11.0; Regular; com.aspose.cells.Color@ff000000 ]Aspose.Cells.Font [ Dummy-Times-II; 11.0; Regular; com.aspose.cells.Color@ff000000 ]Aspose.Cells.Font [ Dummy-Times-III; 11.0; Regular; com.aspose.cells.Color@ff000000 ]Aspose.Cells.Font [ Calibri; 10.5; Regular; com.aspose.cells.Color@ff376268 ]Aspose.Cells.Font [ Calibri; 20.0; Regular; com.aspose.cells.Color@ff376268 ]Aspose.Cells.Font [ Calibri; 11.0; Regular; com.aspose.cells.Color@ff376268 ]{{< /highlight >}}
