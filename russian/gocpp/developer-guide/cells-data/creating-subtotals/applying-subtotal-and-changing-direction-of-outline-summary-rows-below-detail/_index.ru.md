---
title: Применение промежуточных итогов и изменение направления строк сводки по шаблону Golang через C++
linktitle: Применение итоговой строки и изменение направления итоговых строк справа от детальной
type: docs
weight: 100
url: /ru/go-cpp/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/
description: Узнайте, как применять subtotal и менять направление строк сводки ниже деталей, используя API Aspose.Cells for C++.
keywords: Применить итог, добавить итог, изменить направление строк аутлайна суммари снизу от детализации, изменить направление столбцов аутлайна суммари справа от детализации, создать итог и изменить направление строк аутлайна суммари снизу от детализации
---

{{% alert color="primary" %}}

 В этой статье описано, как применять Subtotal к данным и менять направление строк сводки ниже деталей.

Вы можете применить Subtotal к данным методом [**Worksheet.Cells.Subtotal()**](https://reference.aspose.com/cells/go-cpp/cells/subtotal_cellarea_int_consolidationfunction_int32array/). Он принимает следующие параметры:

- **CellArea** - Диапазон, на котором применяется промежуточный итог
- **GroupBy** - Поле для группировки по нулевому индексу
- **Function** - Функция промежуточного итога
- **TotalList** - Массив смещений нулевого индекса, указывающий на поля, к которым добавляются итоги
- **Заменить** - указывает, следует ли заменять текущие подсуммы
- **Разрывы страниц** - указывает, нужно ли добавлять разрыв страницы между группами
- **Итоги ниже данных** - указывает, нужно ли добавлять итог под данными.

Также, вы можете контролировать направление строк сводки **подробных данных** с помощью свойства `Worksheet.Outline.SummaryRowBelow`, как показано на следующем скриншоте. Настройку можно открыть в Microsoft Excel через **Данные > Группировка > Настройки**.

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_1.png)

{{% /alert %}}

## Изображения исходных и выходных файлов

На следующем скриншоте показан исходный файл Excel, используемый в приведенном ниже образцовом коде, содержащий некоторые данные в столбцах A и B.

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_2.png)

На следующем скриншоте показан выходной файл Excel, созданный образцовым кодом. Как видно, к диапазону A2:B11 было применено итого, и направление контура - сводные строки ниже деталей.

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_3.png)

## Код на C++, для применения subtotal и изменения направления строк сводки

Вот пример кода для достижения указанного выше результата.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ApplyingSubtotalAndChangingDirectionOfOutlineSummaryRowsBelowDetail.go" >}}
