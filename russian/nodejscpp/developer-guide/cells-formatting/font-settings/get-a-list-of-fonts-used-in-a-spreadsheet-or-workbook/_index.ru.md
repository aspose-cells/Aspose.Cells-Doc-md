---
title: Получение списка используемых шрифтов в электронной таблице или книге
linktitle: Получение списка используемых шрифтов в электронной таблице или книге
description: Узнайте, как получить список используемых шрифтов в таблице или книге с помощью Aspose.Cells for Node.js via C++. В этой статье вы узнаете, как извлечь информацию о шрифтах из документа.
keywords: Aspose.Cells, Node.js через C++, Таблица, Книга, Шрифт, Список
type: docs
weight: 20
url: /ru/nodejs-cpp/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/
---

## **Возможные сценарии использования**

Часто необходимо знать, какие шрифты используются в вашей книге для целей рендеринга. При преобразовании книги в PDF или изображение, Aspose.Cells требует, чтобы все необходимые шрифты были установлены на вашей системе или находились в вашем **каталоге шрифтов**. Если Aspose.Cells не может найти необходимый шрифт, он пытается заменить его на другой подходящий шрифт, который присутствует на вашей системе или в вашем каталоге шрифтов и может заменить ваш фактический шрифт. Это приводит не только к нежелательному рендерингу PDF или изображений, но и занимает время на поиск подходящих шрифтов.

Чтобы работать с такими случаями, вам нужно знать, какие шрифты используются в вашей книге, затем либо установить эти шрифты на вашей системе в случае Windows, либо поместить их в каталог шрифтов в случае Windows или Linux.

 Aspose.Cells for Node.js via C++ предоставляет метод [**Workbook.getFonts**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getFonts--), который возвращает список всех шрифтов, используемых в вашей книге или таблице.

## **Получение списка используемых шрифтов в электронной таблице или книге**

Приведенный ниже образец кода загружает исходный файл Excel и извлекает список шрифтов, используемых в нем. В нем есть один фиктивный рабочий лист, в котором для иллюстрационных целей добавлены некоторые фиктивные шрифты. Когда код выводит все шрифты в рабочей книге, он также выводит эти фиктивные шрифты. Ниже показан снимок экрана [образца файла Excel](25395211.xlsx) и то, как отображаются фиктивные шрифты.

![todo:image_alt_text](get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-GetFontsListUsedInWorkbook.js" >}}


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
