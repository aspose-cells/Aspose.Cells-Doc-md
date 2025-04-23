---
title: Получение списка используемых шрифтов в электронной таблице или книге
type: docs
weight: 20
url: /ru/java/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/
---

## **Возможные сценарии использования**

Часто необходимо знать, какие шрифты используются в вашей книге для целей визуализации. Когда вы конвертируете свою книгу в PDF или изображение, то Aspose.Cells требует, чтобы все необходимые шрифты были установлены на вашей системе или находились в вашем каталоге шрифтов. Если Aspose.Cells не может найти необходимый шрифт, он пытается заменить его на какой-то другой подходящий шрифт, который присутствует на вашей системе или в вашем каталоге шрифтов и может заменить ваш фактический шрифт. Это не только приводит к нежелательному визуализации PDF или изображений, но и занимает время для поиска подходящих шрифтов.

Чтобы иметь дело с такими случаями, вам следует знать, какие шрифты используются в вашей книге, затем установить их на вашей системе в случае среды Windows или поместить их в каталог шрифтов в случае среды Windows или Linux.

Aspose.Cells предоставляет метод [Workbook.getFonts()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#getFonts--), который возвращает список всех используемых шрифтов в вашей книге или электронной таблице.

## **Получение списка используемых шрифтов в электронной таблице или книге**

Приведенный ниже образец кода загружает исходный файл Excel и извлекает список используемых в нем шрифтов. В нем есть один фиктивный лист, на котором добавлены некоторые фиктивные шрифты для иллюстрации. Когда код выводит все шрифты в книге, он также выводит эти фиктивные шрифты. На следующем скриншоте показан [образец файла Excel](sampleGetFonts.xlsx) и то, как перечислены фиктивные шрифты.

![todo:image_alt_text](get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetFontsUsedinWorkbook-GetFontsUsedinWorkbook.java" >}}

## **Вывод в консоль**

Вот консольный вывод приведенного выше образца кода при выполнении с данным [образцом файла Excel](sampleGetFonts.xlsx).

{{< highlight java >}}

Aspose.Cells.Font [ Calibri; 11.0; Regular; com.aspose.cells.Color@ff000000 ]

Aspose.Cells.Font [ Arial; 10.0; Regular; com.aspose.cells.Color@ff000000 ]

Aspose.Cells.Font [ Calibri; 10.0; Bold; com.aspose.cells.Color@ff000000 ]

Aspose.Cells.Font [ Calibri; 10.0; Regular; com.aspose.cells.Color@ff808080 ]

Aspose.Cells.Font [ Calibri; 10.0; Regular; com.aspose.cells.Color@ff376268 ]

Aspose.Cells.Font [ Calibri; 16.0; Bold; com.aspose.cells.Color@ffffffff ]

Aspose.Cells.Font [ Calibri; 36.0; Regular; com.aspose.cells.Color@ff376268 ]

Aspose.Cells.Font [ Calibri; 20.0; Bold; com.aspose.cells.Color@ff376268 ]

Aspose.Cells.Font [ Calibri; 16.0; Regular; com.aspose.cells.Color@ff376268 ]

Aspose.Cells.Font [ Calibri; 11.0; Regular; com.aspose.cells.Color@ff376268 ]

Aspose.Cells.Font [ Calibri; 11.0; Bold; com.aspose.cells.Color@ff376268 ]

Aspose.Cells.Font [ Calibri; 11.0; Bold; com.aspose.cells.Color@ffffffff ]

Aspose.Cells.Font [ Calibri; 11.0; Italic; com.aspose.cells.Color@ff376268 ]

Aspose.Cells.Font [ Calibri; 16.0; Regular; com.aspose.cells.Color@ff376268 ]

Aspose.Cells.Font [ Calibri; 16.0; Bold; com.aspose.cells.Color@ff376268 ]

Aspose.Cells.Font [ Calibri; 16.0; Regular; com.aspose.cells.Color@ff000000 ]

Aspose.Cells.Font [ Calibri; 16.0; Regular; com.aspose.cells.Color@ff294a4e ]

Aspose.Cells.Font [ Calibri; 16.0; Regular; com.aspose.cells.Color@ff294a4e ]

Aspose.Cells.Font [ Calibri; 12.0; Regular; com.aspose.cells.Color@ff294a4e ]

Aspose.Cells.Font [ Calibri; 11.0; Regular; com.aspose.cells.Color@ff294a4e ]

Aspose.Cells.Font [ Calibri; 11.0; Bold; com.aspose.cells.Color@ffffffff ]

Aspose.Cells.Font [ Dummy-Arial-X; 11.0; Regular; com.aspose.cells.Color@ff000000 ]

Aspose.Cells.Font [ Dummy-Arial-Y; 11.0; Regular; com.aspose.cells.Color@ff000000 ]

Aspose.Cells.Font [ Dummy-Arial-Z; 11.0; Regular; com.aspose.cells.Color@ff000000 ]

Aspose.Cells.Font [ Dummy-Times-I; 11.0; Regular; com.aspose.cells.Color@ff000000 ]

Aspose.Cells.Font [ Dummy-Times-II; 11.0; Regular; com.aspose.cells.Color@ff000000 ]

Aspose.Cells.Font [ Dummy-Times-III; 11.0; Regular; com.aspose.cells.Color@ff000000 ]

Aspose.Cells.Font [ Calibri; 10.5; Regular; com.aspose.cells.Color@ff376268 ]

Aspose.Cells.Font [ Calibri; 20.0; Regular; com.aspose.cells.Color@ff376268 ]

Aspose.Cells.Font [ Calibri; 11.0; Regular; com.aspose.cells.Color@ff376268 ]

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
