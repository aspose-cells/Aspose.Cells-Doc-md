---
title: Конвертировать Excel в PDF
type: docs
weight: 50
url: /ru/python-java/convert-excel-to-pdf/
description: Как конвертировать Excel в PDF с помощью Python. В этой статье показано преобразование файлов Excel в PDF с помощью Python и простой в использовании Aspose.Cells for Python via Java API.
keywords: excel to pdf python, python convert excel to pdf, python excel to pdf, convert excel to pdf python, convert excel to pdf in python, convert excel to pdf using python, excel to pdf in python, excel to pdf using python, aspose excel to pdf, aspose convert excel to pdf
---
## **Конвертировать Excel в PDF**

Документы в формате PDF широко используются в качестве стандартного формата обмена документами между организациями, государственными секторами и отдельными лицами. Разработчиков программного обеспечения часто просят разработать способ простого преобразования файлов Excel Microsoft в документы PDF. Aspose.Cells for Python via Java API предоставляет возможность конвертировать файлы Excel в документы PDF (включая PDF/A). Aspose.Cell конвертирует электронные таблицы в PDF с высокой степенью точности и достоверности.

### **Прямое преобразование**

Чтобы сохранить файл Excel непосредственно в PDF, вы можете использовать[**Книга.сохранить**](https://reference.aspose.com/cells/python/asposecells.api/workbook#save(java.lang.String,%20com.aspose.cells.SaveOptions)) метод и проход[**СохранитьФормат.PDF**](https://reference.aspose.com/cells/python/asposecells.api/saveformat#PDF) как второй параметр.

Следующий фрагмент кода демонстрирует использование[**СохранитьФормат.PDF**](https://reference.aspose.com/cells/python/asposecells.api/saveformat#PDF)и[**Книга.сохранить**](https://reference.aspose.com/cells/python/asposecells.api/workbook#save(java.lang.String,%20com.aspose.cells.SaveOptions)) метод преобразования Excel в формат PDF.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-ConvertingToPDFFiles.py" >}}

### **Расширенное преобразование**

Чтобы иметь больший контроль над преобразованием в PDF, API предоставляет[**PdfSaveOptions**](https://reference.aspose.com/cells/python/asposecells.api/PdfSaveOptions)учебный класс.[**PdfSaveOptions**](https://reference.aspose.com/cells/python/asposecells.api/PdfSaveOptions)можно использовать для установки различных атрибутов преобразования. Установка различных свойств[**PdfSaveOptions**](https://reference.aspose.com/cells/python/asposecells.api/PdfSaveOptions)class даст вам контроль над настройками печати, шрифта, безопасности и сжатия для результирующего файла PDF. Наиболее примечательным свойством является[**Согласие**](https://reference.aspose.com/cells/python/asposecells.api/pdfsaveoptions#Compliance)который позволяет сохранять файлы Excel в файлы PDF, совместимые с форматом PDF/A.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-AdvancedConversiontoPdf.py" >}}

{{% alert color="primary" %}}

 если ваша электронная таблица содержит формулы, вызовите[**Рабочая книга.calculateFormula**](https://reference.aspose.com/cells/python/asposecells.api/workbook#calculateFormula()) непосредственно перед преобразованием электронной таблицы в PDF. Это гарантирует, что значения, зависящие от формулы, будут пересчитаны, а в PDF-файле отобразятся правильные значения.

{{% /alert %}}
