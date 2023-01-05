---
title: Создайте PdfBookmarkEntry для листа диаграммы
type: docs
weight: 50
url: /ru/java/create-pdfbookmarkentry-for-chart-sheet/
---
## **Возможные сценарии использования**

Раньше Aspose.Cells создавал[**PdfЗакладкаЗапись**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfBookmarkEntry) для обычного листа. Но теперь Aspose.Cells также может создавать[**PdfЗакладкаЗапись**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfBookmarkEntry) для диаграммного листа. Поскольку на листе диаграммы нет другой ячейки, кроме ячейки A1, она создаст[**PdfЗакладкаЗапись**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfBookmarkEntry)только для ячейки A1.

## **Создайте PdfBookmarkEntry для листа диаграммы**

Следующий пример кода загружает[образец файла Excel](61767772.xlsx)в котором четыре листа. Два из них — обычные листы, а два других — листы с диаграммами. Он создает четыре записи закладки следующим образом

- Закладка-I
- Закладка-II-Диаграмма1
- Закладка-III
- Закладка-IV-Chart2

На следующем снимке экрана показано[вывод PDF](61767771.pdf)сгенерированный образцом кода для справки.

![дело:изображение_альтернативный_текст](create-pdfbookmarkentry-for-chart-sheet_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Rendering-CreatePdfBookmarkEntryForChartSheet.java" >}}
