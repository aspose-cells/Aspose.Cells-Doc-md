---
title: Создание PdfBookmarkEntry для листа с диаграммой
type: docs
weight: 50
url: /ru/java/create-pdfbookmarkentry-for-chart-sheet/
---

## **Возможные сценарии использования**

Раньше Aspose.Cells создавала [**PdfBookmarkEntry**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfBookmarkEntry) для обычного листа. Но теперь Aspose.Cells также может создавать [**PdfBookmarkEntry**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfBookmarkEntry) для листа с диаграммой. Поскольку лист с диаграммой не имеет других ячеек, кроме ячейки A1, то он создаст [**PdfBookmarkEntry**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfBookmarkEntry) только для ячейки A1.

## **Создание PdfBookmarkEntry для листа с диаграммой**

Следующий образец кода загружает [образец Excel-файла](61767772.xlsx), в котором четыре листа. Два из них - обычные листы, а два других - листы с диаграммами. Он создает четыре объекта закладки следующим образом

- Закладка-I
- Закладка-II-Chart1
- Закладка-III
- Закладка-IV-Chart2

На следующем скриншоте показан [PDF-файл](61767771.pdf), созданный образцовым кодом для справки.

![todo:image_alt_text](create-pdfbookmarkentry-for-chart-sheet_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Rendering-CreatePdfBookmarkEntryForChartSheet.java" >}}
