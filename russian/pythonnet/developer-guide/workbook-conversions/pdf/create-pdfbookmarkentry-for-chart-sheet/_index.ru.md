---
title: Создать PdfBookmarkEntry для листа диаграммы
type: docs
weight: 50
url: /ru/python-net/create-pdfbookmarkentry-for-chart-sheet/
description: Узнайте, как создать PdfBookmarkEntry для листа диаграммы с помощью Aspose.Cells for Python via .NET API.
keywords: Python Create PdfBookmarkEntry for Chart Sheet, Add PdfBookmarkEntry for Chart Sheet using Python, Python Insert PdfBookmarkEntry for Chart Sheet, PdfBookmarkEntry for Chart Sheet in Python
---
##  **Возможные сценарии использования**

Раньше Aspose.Cells for Python via .NET создавало бы[**PDFЗакладкаЗапись**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/pdfbookmarkentry/) за обычный лист. Но теперь Aspose.Cells for Python via .NET тоже может создавать[**PDFЗакладкаЗапись**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/pdfbookmarkentry/) для листа диаграммы. Поскольку на листе диаграммы нет другой ячейки, кроме ячейки A1, будет создано[**PDFЗакладкаЗапись**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/pdfbookmarkentry/) только для ячейки A1.

##  **Создать PdfBookmarkEntry для листа диаграммы**

 Следующий пример кода загружает[образец файла Excel](61767756.xlsx) который имеет четыре листа. Два из них — обычные листы, а два других — листы диаграмм. Он создает четыре записи закладок следующим образом:

- Закладка-I
- Закладка-II-Диаграмма1
- Закладка-III
- Закладка-IV-Диаграмма2

 На следующем снимке экрана показано[вывод PDF](61767757.pdf) созданный примером кода для справки.

![задача: image_alt_text](create-pdfbookmarkentry-for-chart-sheet_1.png)

##  **Образец кода**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-CreatePdfBookmarkEntryForChartSheet.py" >}}
