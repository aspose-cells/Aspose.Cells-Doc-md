---
title: Получить список шрифтов, используемых в электронной таблице или книге
type: docs
weight: 20
url: /ru/net/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/
---
## **Возможные сценарии использования**

Часто бывает необходимо знать шрифты, используемые в вашей книге для целей рендеринга. Когда вы конвертируете свою книгу в PDF или изображение, Aspose.Cells требует, чтобы все необходимые шрифты были установлены в вашей системе или присутствовали в вашем**каталог шрифтов**Если Aspose.Cells не может найти нужный шрифт, он пытается заменить его другим подходящим шрифтом, который присутствует в вашей системе или в вашем каталоге шрифтов и может заменить ваш реальный шрифт. Это не только приводит к нежелательному отображению PDF или изображений, но и требует времени на поиск подходящих шрифтов.

Чтобы иметь дело с такими случаями, вы должны знать, какие шрифты используются в вашей книге, а затем либо установить эти шрифты в своей системе в случае среды Windows, либо поместить их в каталог шрифтов в случае среды Windows или Linux.

 Aspose.Cells обеспечивает**[Workbook.GetFonts] (https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/getfonts)**метод, который возвращает список всех шрифтов, используемых в вашей книге или электронной таблице.

## **Получить список шрифтов, используемых в электронной таблице или книге**

 Следующий пример кода загружает исходный файл Excel и извлекает список используемых внутри него шрифтов. У него есть один фиктивный рабочий лист, на который добавлены фиктивные шрифты для иллюстраций. Когда код печатает все шрифты внутри книги, он также печатает эти фиктивные шрифты. На следующем снимке экрана показано[образец эксель файла](25395211.xlsx)и как перечислены фиктивные шрифты.

![дело:изображение_альтернативный_текст](get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Fonts-GetListOfFontsUsedInSpreadsheetOrWorkbook.cs" >}}

## **Консольный вывод**

 Вот вывод консоли приведенного выше примера кода при выполнении с заданным[образец эксель файла](25395211.xlsx).

{{< highlight "java" >}}

Aspose.Cells.Font [ Calibri; 11; Regular; Color [Black]]

Aspose.Cells.Font [ Arial; 10; Regular; Color [A=255, R=0, G=0, B=0]]

Aspose.Cells.Font [ Calibri; 10; Bold; Color [Black]]

Aspose.Cells.Font [ Calibri; 10; Regular; Color [A=255, R=128, G=128, B=128]]

Aspose.Cells.Font [ Calibri; 10; Regular; Color [A=255, R=55, G=98, B=104]]

Aspose.Cells.Font [ Calibri; 16; Bold; Color [A=255, R=255, G=255, B=255]]

Aspose.Cells.Font [ Calibri; 36; Regular; Color [A=255, R=55, G=98, B=104]]

Aspose.Cells.Font [ Calibri; 20; Bold; Color [A=255, R=55, G=98, B=104]]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [A=255, R=55, G=98, B=104]]

Aspose.Cells.Font [ Calibri; 11; Regular; Color [A=255, R=55, G=98, B=104]]

Aspose.Cells.Font [ Calibri; 11; Bold; Color [A=255, R=55, G=98, B=104]]

Aspose.Cells.Font [ Calibri; 11; Bold; Color [A=255, R=255, G=255, B=255]]

Aspose.Cells.Font [ Calibri; 11; Italic; Color [A=255, R=55, G=98, B=104]]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [A=255, R=55, G=98, B=104]]

Aspose.Cells.Font [ Calibri; 16; Bold; Color [A=255, R=55, G=98, B=104]]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [Black]]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [A=255, R=41, G=74, B=78]]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [A=255, R=41, G=74, B=78]]

Aspose.Cells.Font [ Calibri; 12; Regular; Color [A=255, R=41, G=74, B=78]]

Aspose.Cells.Font [ Calibri; 11; Regular; Color [A=255, R=41, G=74, B=78]]

Aspose.Cells.Font [ Calibri; 11; Bold; Color [A=255, R=255, G=255, B=255]]

Aspose.Cells.Font [ Dummy-Arial-X; 11; Regular; Color [Black]]

Aspose.Cells.Font [ Dummy-Arial-Y; 11; Regular; Color [Black]]

Aspose.Cells.Font [ Dummy-Arial-Z; 11; Regular; Color [Black]]

Aspose.Cells.Font [ Dummy-Times-I; 11; Regular; Color [Black]]

Aspose.Cells.Font [ Dummy-Times-II; 11; Regular; Color [Black]]

Aspose.Cells.Font [ Dummy-Times-III; 11; Regular; Color [Black]]

Aspose.Cells.Font [ Calibri; 10.5; Regular; Color [A=255, R=55, G=98, B=104]]

Aspose.Cells.Font [ Calibri; 20; Regular; Color [A=255, R=55, G=98, B=104]]

Aspose.Cells.Font [ Calibri; 11; Regular; Color [A=255, R=55, G=98, B=104]]

{{< /highlight >}}
