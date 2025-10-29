---
title: Получить список используемых шрифтов в таблице или рабочей книге с помощью Golang через C++
linktitle: Получить список шрифтов
description: Aspose.Cells — это библиотека C++ для работы с файлами таблиц. Она поддерживает получение списка шрифтов, используемых в таблице или рабочей книге, позволяя пользователям получать информацию о шрифтах в документе. Эта статья покажет, как использовать Aspose.Cells для получения списка шрифтов.
keywords: Aspose.Cells, Электронная таблица, Книга, Шрифт, Список
type: docs
weight: 20
url: /ru/go-cpp/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/
---

## **Возможные сценарии использования**

Часто необходимо знать, какие шрифты используются в вашей книге для целей рендеринга. При преобразовании книги в PDF или изображение, Aspose.Cells требует, чтобы все необходимые шрифты были установлены на вашей системе или находились в вашем **каталоге шрифтов**. Если Aspose.Cells не может найти необходимый шрифт, он пытается заменить его на другой подходящий шрифт, который присутствует на вашей системе или в вашем каталоге шрифтов и может заменить ваш фактический шрифт. Это приводит не только к нежелательному рендерингу PDF или изображений, но и занимает время на поиск подходящих шрифтов.

Чтобы справиться с такими случаями, вам следует знать, какие шрифты используются в вашей книге, а затем установить их на вашей системе в случае окружения Windows или поместить их в ваш каталог шрифтов в случае окружения Windows или Linux.

Aspose.Cells предоставляет метод [**Workbook.GetFonts**](https://reference.aspose.com/cells/go-cpp/workbook/getfonts/), который возвращает список всех шрифтов, используемых в вашей книге или электронной таблице.

## **Получение списка используемых шрифтов в электронной таблице или книге**

Приведенный ниже образец кода загружает исходный файл Excel и извлекает список шрифтов, используемых в нем. В нем есть один фиктивный рабочий лист, в котором для иллюстрационных целей добавлены некоторые фиктивные шрифты. Когда код выводит все шрифты в рабочей книге, он также выводит эти фиктивные шрифты. Ниже показан снимок экрана [образца файла Excel](25395211.xlsx) и то, как отображаются фиктивные шрифты.

![todo:image_alt_text](get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetAListOfFontsUsedInASpreadsheetOrWorkbook.go" >}}
## **Вывод в консоль**

Вот консольный вывод вышеприведенного образца кода при выполнении с данным [образцом файла Excel](25395211.xlsx).

{{< highlight java >}}

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
