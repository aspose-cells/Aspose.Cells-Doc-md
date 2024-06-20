---
title: Создание PdfBookmarkEntry для листа с диаграммой
type: docs
weight: 50
url: /ru/python-net/create-pdfbookmarkentry-for-chart-sheet/
description: Узнайте, как создать PdfBookmarkEntry для Листа Диаграмм с использованием Aspose.Cells для Python via .NET API.
keywords: Python Создать PdfBookmarkEntry для Листа Диаграмм, Добавить PdfBookmarkEntry для Листа Диаграмм с помощью Python, Вставить PdfBookmarkEntry для Листа Диаграмм с помощью Python, PdfBookmarkEntry для Листа Диаграмм в Python
---

## **Возможные сценарии использования**

Ранее Aspose.Cells для Python via .NET создавал [**PdfBookmarkEntry**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/pdfbookmarkentry/) для обычного листа. Но теперь Aspose.Cells для Python via .NET также может создать [**PdfBookmarkEntry**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/pdfbookmarkentry/) для листа диаграмм. Поскольку лист диаграмм не имеет никаких других ячеек, кроме ячейки A1, он будет создавать [**PdfBookmarkEntry**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/pdfbookmarkentry/) только для ячейки A1.

## **Создание PdfBookmarkEntry для листа с диаграммой**

Приведенный ниже пример кода загружает [образец Excel-файла](61767756.xlsx), который содержит четыре листа. Два из них обычные листы, а остальные два - листы диаграмм. Он создает четыре закладки следующим образом

- Закладка-I
- Закладка-II-Chart1
- Закладка-III
- Закладка-IV-Chart2

На следующем скриншоте показан [выходной PDF-файл](61767757.pdf), сгенерированный примером кода для справки.

![todo:image_alt_text](create-pdfbookmarkentry-for-chart-sheet_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-CreatePdfBookmarkEntryForChartSheet.py" >}}
