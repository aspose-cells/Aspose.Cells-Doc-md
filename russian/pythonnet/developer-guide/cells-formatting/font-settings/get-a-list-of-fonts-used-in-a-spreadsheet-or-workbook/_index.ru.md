---
title: Получение списка используемых шрифтов в электронной таблице или книге
description: Aspose.Cells — это библиотека на Python для работы с файлами таблиц. Она поддерживает получение списка используемых в таблице шрифтов, что позволяет пользователям получать информацию о шрифтах, использованных в документе. В этой статье показано, как использовать библиотеку Aspose.Cells для Python via .NET для получения списка шрифтов.
keywords: Aspose.Cells для Python via .NET, Таблицы, Книга, Шрифт, Список
type: docs
weight: 20
url: /ru/python-net/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/
---

## **Возможные сценарии использования**

Часто необходимо знать, какие шрифты используются в вашей рабочей книге, для целей отображения. При конвертации книги в PDF или изображение, Aspose.Cells для Python via .NET требует, чтобы все необходимые шрифты были установлены на вашем компьютере или находились в вашей **директории шрифтов**. Если Aspose.Cells для Python via .NET не сможет найти нужный шрифт, он попытается заменить его подходящим шрифтом, который есть на вашем устройстве или в директории шрифтов, и способен заменить ваш текущий шрифт. Это приводит к нежелательному отображению итогового PDF или изображений и увеличивает время обработки.

Чтобы справиться с такими случаями, вам следует знать, какие шрифты используются в вашей книге, а затем установить их на вашей системе в случае окружения Windows или поместить их в ваш каталог шрифтов в случае окружения Windows или Linux.

Aspose.Cells для Python via .NET предоставляет метод [**Workbook.get_fonts**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/get_fonts), который возвращает список всех шрифтов, используемых в вашей рабочей книге или таблице.

## **Получение списка используемых шрифтов в электронной таблице или книге**

Приведенный ниже образец кода загружает исходный файл Excel и извлекает список шрифтов, используемых в нем. В нем есть один фиктивный рабочий лист, в котором для иллюстрационных целей добавлены некоторые фиктивные шрифты. Когда код выводит все шрифты в рабочей книге, он также выводит эти фиктивные шрифты. Ниже показан снимок экрана [образца файла Excel](25395211.xlsx) и то, как отображаются фиктивные шрифты.

![todo:image_alt_text](get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-GetListOfFontsUsedInSpreadsheetOrWorkbook.py" >}}

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

{{< app/cells/assistant language="python-net" >}}
