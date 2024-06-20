---
title: Создание PdfBookmarkEntry для листа с диаграммой
type: docs
weight: 50
url: /ru/net/create-pdfbookmarkentry-for-chart-sheet/
---

## **Возможные сценарии использования**

Ранее Aspose.Cells создавала [**PdfBookmarkEntry**](https://reference.aspose.com/cells/net/aspose.cells.rendering/pdfbookmarkentry) для обычного листа. Но теперь Aspose.Cells также может создавать [**PdfBookmarkEntry**](https://reference.aspose.com/cells/net/aspose.cells.rendering/pdfbookmarkentry) для листа диаграммы. Поскольку лист диаграммы не содержит никаких других ячеек, кроме ячейки A1, то она создаст [**PdfBookmarkEntry**](https://reference.aspose.com/cells/net/aspose.cells.rendering/pdfbookmarkentry) только для ячейки A1.

## **Создание PdfBookmarkEntry для листа с диаграммой**

Приведенный ниже пример кода загружает [образец Excel-файла](61767756.xlsx), который содержит четыре листа. Два из них обычные листы, а остальные два - листы диаграмм. Он создает четыре закладки следующим образом

- Закладка-I
- Закладка-II-Chart1
- Закладка-III
- Закладка-IV-Chart2

На следующем скриншоте показан [выходной PDF-файл](61767757.pdf), сгенерированный примером кода для справки.

![todo:image_alt_text](create-pdfbookmarkentry-for-chart-sheet_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Rendering-CreatePdfBookmarkEntryForChartSheet.cs" >}}
