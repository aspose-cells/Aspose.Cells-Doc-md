---
title: Получите список шрифтов, используемых в электронной таблице или книге.
description: Aspose.Cells — это библиотека .NET для работы с файлами электронных таблиц. Он поддерживает получение списка шрифтов, используемых в электронной таблице или книге, что позволяет пользователям получать информацию о шрифтах, используемых в документе. В этой статье показано, как использовать библиотеку Aspose.Cells для получения списка шрифтов.
keywords: Aspose.Cells, Spreadsheet, Workbook, Font, List
type: docs
weight: 20
url: /ru/net/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/
---
##  **Возможные сценарии использования**

Часто бывает необходимо знать, какие шрифты используются в вашей книге для целей рендеринга. Когда вы конвертируете свою книгу в PDF или изображение, для Aspose.Cells требуется, чтобы все необходимые шрифты были установлены в вашей системе или присутствовали в вашем *каталоге шрифтов**. Если Aspose.Cells не может найти нужный шрифт, он пытается заменить его другим подходящим шрифтом, который присутствует в вашей системе или в вашем каталоге шрифтов и может заменить ваш фактический шрифт. Это не только приводит к нежелательному рендерингу PDF или изображений, но также требует времени на поиск подходящих шрифтов.

Чтобы справиться с такими случаями, вы должны знать, какие шрифты используются в вашей книге, а затем либо установить эти шрифты в своей системе в случае среды Windows, либо поместить их в каталог шрифтов в случае среды Windows или Linux.

 Aspose.Cells обеспечивает**[Workbook.GetFonts](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/getfonts)**метод, который возвращает список всех шрифтов, используемых в вашей книге или электронной таблице.

##  **Получите список шрифтов, используемых в электронной таблице или книге.**

 Следующий пример кода загружает исходный файл Excel и получает список используемых в нем шрифтов. В нем есть один фиктивный рабочий лист, на который для иллюстрации добавлены несколько фиктивных шрифтов. Когда код печатает все шрифты внутри книги, он также печатает эти фиктивные шрифты. На следующем снимке экрана показано[образец файла Excel](25395211.xlsx) и как перечислены фиктивные шрифты.

![задача: image_alt_text](get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook_1.png)

##  **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Fonts-GetListOfFontsUsedInSpreadsheetOrWorkbook.cs" >}}

##  **Консольный вывод**

 Вот консольный вывод приведенного выше примера кода при выполнении с заданным[образец файла Excel](25395211.xlsx).

{{< highlight "java" >}}

Aspose.Cells.Font [ Calibri; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Arial; 10; Regular; Color [A=255, R=0, G=0, B=0] ]

Aspose.Cells.Font [ Calibri; 10; Bold; Color [Black] ]

Aspose.Cells.Font [ Calibri; 10; Regular; Color [A=255, R=128, G=128, B=128] ]

Aspose.Cells.Font [ Calibri; 10; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 16; Bold; Color [A=255, R=255, G=255, B=255] ]

Aspose.Cells.Font [ Calibri; 36; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 20; Bold; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 11; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 11; Bold; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 11; Bold; Color [A=255, R=255, G=255, B=255] ]

Aspose.Cells.Font [ Calibri; 11; Italic; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 16; Bold; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [Black] ]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [A=255, R=41, G=74, B=78] ]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [A=255, R=41, G=74, B=78] ]

Aspose.Cells.Font [ Calibri; 12; Regular; Color [A=255, R=41, G=74, B=78] ]

Aspose.Cells.Font [ Calibri; 11; Regular; Color [A=255, R=41, G=74, B=78] ]

Aspose.Cells.Font [ Calibri; 11; Bold; Color [A=255, R=255, G=255, B=255] ]

Aspose.Cells.Font [ Dummy-Arial-X; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Dummy-Arial-Y; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Dummy-Arial-Z; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Dummy-Times-I; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Dummy-Times-II; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Dummy-Times-III; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Calibri; 10.5; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 20; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 11; Regular; Color [A=255, R=55, G=98, B=104] ]

{{< /highlight >}}
