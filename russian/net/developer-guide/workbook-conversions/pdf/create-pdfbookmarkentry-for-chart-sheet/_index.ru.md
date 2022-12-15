---
title: Создайте PdfBookmarkEntry для листа диаграммы
type: docs
weight: 50
url: /ru/net/create-pdfbookmarkentry-for-chart-sheet/
---
## **Возможные сценарии использования**

Раньше Aspose.Cells создавал[**PdfЗакладкаЗапись**](https://reference.aspose.com/cells/net/aspose.cells.rendering/pdfbookmarkentry) для обычного листа. Но теперь Aspose.Cells также может создавать[**PdfЗакладкаЗапись**](https://reference.aspose.com/cells/net/aspose.cells.rendering/pdfbookmarkentry) для диаграммного листа. Поскольку на листе диаграммы нет другой ячейки, кроме ячейки A1, она создаст[**PdfЗакладкаЗапись**](https://reference.aspose.com/cells/net/aspose.cells.rendering/pdfbookmarkentry) только для ячейки A1.

## **Создайте PdfBookmarkEntry для листа диаграммы**

 Следующий пример кода загружает[образец файла Excel](61767756.xlsx) в котором четыре листа. Два из них — обычные листы, а два других — листы с диаграммами. Он создает четыре записи закладки следующим образом

- Закладка-I
- Закладка-II-Диаграмма1
- Закладка-III
- Закладка-IV-Chart2

На следующем снимке экрана показано[вывод PDF](61767757.pdf) сгенерированный образцом кода для справки.

![дело:изображение_альтернативный_текст](create-pdfbookmarkentry-for-chart-sheet_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Rendering-CreatePdfBookmarkEntryForChartSheet.cs" >}}
