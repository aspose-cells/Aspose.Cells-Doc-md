---
title: Создать PdfBookmarkEntry для листа диаграмм с помощью Golang через C++
linktitle: Создание PdfBookmarkEntry для листа с диаграммой
type: docs
weight: 50
url: /ru/go-cpp/create-pdfbookmarkentry-for-chart-sheet/
description: Узнайте, как создавать PdfBookmarkEntry для листов с графиками, используя Aspose.Cells for C++.
---

## **Возможные сценарии использования**

Ранее Aspose.Cells создавала [**PdfBookmarkEntry**](https://reference.aspose.com/cells/go-cpp/pdfbookmarkentry/) для обычного листа. Но теперь Aspose.Cells также может создавать [**PdfBookmarkEntry**](https://reference.aspose.com/cells/go-cpp/pdfbookmarkentry/) для листа диаграммы. Поскольку лист диаграммы не содержит никаких других ячеек, кроме ячейки A1, то она создаст [**PdfBookmarkEntry**](https://reference.aspose.com/cells/go-cpp/pdfbookmarkentry/) только для ячейки A1.

## **Создание PdfBookmarkEntry для листа с диаграммой**

Следующий пример кода загружает [пробный файл Excel](61767756.xlsx), содержащий четыре листа. Два из них — обычные листы и еще два — графические листы. Он создает четыре пункта закладок следующим образом:

- Закладка-I
- Закладка-II-Chart1
- Закладка-III
- Закладка-IV-Chart2

На следующем скриншоте показан [выходной PDF-файл](61767757.pdf), сгенерированный примером кода для справки.

![todo:image_alt_text](create-pdfbookmarkentry-for-chart-sheet_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CreatePdfbookmarkentryForChartSheet.go" >}}
