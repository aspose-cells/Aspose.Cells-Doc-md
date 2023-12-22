---
title: Применение промежуточного итога и изменение направления строк итоговой структуры под подробностями
type: docs
weight: 100
url: /ru/net/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/
description: Узнайте, как применить промежуточный итог и изменить направление строк сводной информации под подробностями, используя Aspose.Cells for .NET API.
keywords: Apply subtotal, Add subtotal, change direction of outline summary Rows below Detail, change direction of outline summary Columns to right of Detail, Create subtotal and change direction of outline summary Rows below Detail
---
{{% alert color="primary" %}}

В этой статье объясняется, как применить промежуточный итог к данным и изменить направление строк сводной информации под подробностями.

 Вы можете применить промежуточный итог к данным, используя[**Рабочий лист.Cells.Промежуточный итог()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/subtotal/index) метод. Он принимает следующие параметры.

- **CellArea** - Диапазон применения промежуточного итога.
- **Группа по** - Поле для группировки, как целочисленное смещение, отсчитываемое от нуля.
- **Функция** - Функция промежуточного итога.
- **Тоталлист**— Массив смещений полей, отсчитываемых от нуля, указывающий поля, к которым добавляются промежуточные итоги.
- **Заменять** - Указывает, заменить ли текущие промежуточные итоги
- **Разрывы страниц** - Указывает, добавлять ли разрыв страницы между группами.
- **Сводные данные ниже** - Указывает, следует ли добавлять сводку ниже данных.

 Кроме того, вы можете контролировать направление контура.**Строки сводки под подробностями** как показано на следующем снимке экрана с использованием свойства Worksheet.Outline.SummaryRowBelow. Вы можете открыть этот параметр в Microsoft Excel, используя**Данные > Структура > Настройки**

![задача: image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_1.png)

{{% /alert %}}

##  Изображения исходных и выходных файлов

На следующем снимке экрана показан исходный файл Excel, используемый в приведенном ниже примере кода, который содержит некоторые данные в столбцах A и B.

![задача: image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_2.png)

На следующем снимке экрана показан выходной файл Excel, созданный с помощью примера кода. Как видите, к диапазону A2:B11 был применен промежуточный итог, а направление контура — это сводные строки под деталями.

![задача: image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_3.png)

## Код C# для применения промежуточного итога и изменения направления строк сводной информации

Вот пример кода для достижения результата, показанного выше.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-ApplyingSubtotalChangeSummaryDirection-1.cs" >}}
