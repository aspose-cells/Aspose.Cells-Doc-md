---
title: Применение итоговой строки и изменение направления итоговых строк справа от детальной
type: docs
weight: 100
url: /ru/java/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/
---

{{% alert color="primary" %}}

Эта статья объяснит, как применить итоговую строку к данным и изменить направление итоговых строк ниже детали.

Вы можете применить итоговую строку к данным, используя метод [**Worksheet.Cells.subtotal()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#subtotal(com.aspose.cells.CellArea,%20int,%20int,%20int[])). Он принимает следующие параметры.

- **CellArea** - Диапазон, на котором применяется промежуточный итог
- **GroupBy** - Поле для группировки по нулевому индексу
- **Function** - Функция промежуточного итога
- **TotalList** - Массив смещений нулевого индекса, указывающий на поля, к которым добавляются итоги
- **Replace** - Указывает, нужно ли заменить текущие промежуточные итоги
- **PageBreaks** - Указывает, нужно ли добавить разрыв страницы между группами
- **SummaryBelowData** - Указывает, нужно ли добавить итоги ниже данных

Также вы можете управлять направлением строк сводной информации **ниже деталей** с помощью свойства [**Worksheet.getOutline().SummaryRowBelow**](https://reference.aspose.com/cells/java/com.aspose.cells/outline#SummaryRowBelow), как показано на следующем скриншоте. Вы можете открыть эту настройку в Microsoft Excel, используя **Данные > Сводка > Настройки**

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_1.png)

{{% /alert %}}

## Пример

### Сравнение скриншотов исходных и выходных файлов

На следующем скриншоте показан исходный файл Excel, используемый в приведенном ниже образцовом коде, содержащий некоторые данные в столбцах A и B.

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_2.png)

На следующем скриншоте показан созданный примером кода файл Excel. Как видно, промежуточный итог применен к диапазону **A2:B11**, и направление сводной информации подробно описано.

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_3.png)

### Код на Java для применения промежуточного итога и изменения направления сводной информации ниже деталей

Вот пример кода для достижения указанного выше результата.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ApplyingSubtotal-1.java" >}}
