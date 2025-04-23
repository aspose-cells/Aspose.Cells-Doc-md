---
title: Применение итоговой строки и изменение направления итоговых строк справа от детальной
type: docs
weight: 100
url: /ru/net/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/
description: Узнать, как применить итог и изменить направление строк аутлайна суммари снизу от детализации с помощью API Aspose.Cells for .NET.
keywords: Применить итог, добавить итог, изменить направление строк аутлайна суммари снизу от детализации, изменить направление столбцов аутлайна суммари справа от детализации, создать итог и изменить направление строк аутлайна суммари снизу от детализации
---

{{% alert color="primary" %}}

Эта статья объяснит, как применить итоговую строку к данным и изменить направление итоговых строк ниже детали.

Вы можете применить итоговую строку к данным, используя метод [**Worksheet.Cells.Subtotal()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/subtotal/index). Он принимает следующие параметры.

- **CellArea** - Диапазон, на котором применяется промежуточный итог
- **GroupBy** - Поле для группировки по нулевому индексу
- **Function** - Функция промежуточного итога
- **TotalList** - Массив смещений нулевого индекса, указывающий на поля, к которым добавляются итоги
- **Replace** - Указывает, нужно ли заменить текущие промежуточные итоги
- **Разрывы страниц** - Указывает, добавлять ли разрыв страницы между группами
- **SummaryBelowData** - Указывает, нужно ли добавить итоги ниже данных

Также можно управлять направлением сводных строк **Ниже строки деталей** , как показано на следующем скриншоте, используя свойство Worksheet.Outline.SummaryRowBelow. Вы можете открыть этот параметр в Microsoft Excel, используя **Данные > Контур > Настройки**

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_1.png)

{{% /alert %}}

## Изображения исходных и выходных файлов

На следующем скриншоте показан исходный файл Excel, используемый в приведенном ниже образцовом коде, содержащий некоторые данные в столбцах A и B.

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_2.png)

На следующем скриншоте показан выходной файл Excel, созданный образцовым кодом. Как видно, к диапазону A2:B11 было применено итого, и направление контура - сводные строки ниже деталей.

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_3.png)

## Код C#, применяющий итог и изменяющий направление строк аутлайна-суммари

Вот пример кода для достижения указанного выше результата.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-ApplyingSubtotalChangeSummaryDirection-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
