---
title: Преобразование Excel в PDF
type: docs
weight: 50
url: /ru/python-java/convert-excel-to-pdf/
description: Как преобразовать Excel в PDF с помощью Python. В этой статье демонстрируется преобразование файлов Excel в PDF с использованием простого в использовании API Aspose.Cells для Python via Java.
keywords: excel to pdf python, python convert excel to pdf, python excel to pdf, convert excel to pdf python, convert excel to pdf in python, convert excel to pdf using python, excel to pdf in python, excel to pdf using python, aspose excel to pdf, aspose convert excel to pdf
---

## **Преобразовать Excel в PDF**

PDF-документы широко используются в качестве стандартного формата для обмена документами между организациями, государственными секторами и частными лицами. Разработчикам программного обеспечения часто предлагается разработать удобный способ преобразования файлов Microsoft Excel в документы PDF. API Aspose.Cells для Python via Java обеспечивает возможность преобразования файлов Excel в документы PDF (включая PDF/A). Aspose.Cells преобразует электронные таблицы в PDF с высокой точностью и достоверностью.

### **Прямое преобразование**

Чтобы сохранить файл Excel непосредственно в формате PDF, вы можете использовать метод [**Workbook.save**](https://reference.aspose.com/cells/python/asposecells.api/workbook#save(java.lang.String,%20com.aspose.cells.SaveOptions)) и передать [**SaveFormat.PDF**](https://reference.aspose.com/cells/python/asposecells.api/saveformat#PDF) в качестве второго параметра.

Приведенный ниже фрагмент кода демонстрирует использование метода [**SaveFormat.PDF**](https://reference.aspose.com/cells/python/asposecells.api/saveformat#PDF) и метода [**Workbook.save**](https://reference.aspose.com/cells/python/asposecells.api/workbook#save(java.lang.String,%20com.aspose.cells.SaveOptions)) для преобразования Excel в формат PDF.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-ConvertingToPDFFiles.py" >}}

### **Расширенное преобразование**

Чтобы иметь больше контроля над преобразованием в PDF, API предоставляет класс [**PdfSaveOptions**](https://reference.aspose.com/cells/python/asposecells.api/PdfSaveOptions). Класс [**PdfSaveOptions**](https://reference.aspose.com/cells/python/asposecells.api/PdfSaveOptions) может быть использован для установки различных атрибутов для преобразования. Установка различных свойств класса [**PdfSaveOptions**](https://reference.aspose.com/cells/python/asposecells.api/PdfSaveOptions) дает вам контроль над настройками печати, шрифтов, безопасности и сжатия для результирующего файла PDF. Наиболее заметным свойством является [**Compliance**](https://reference.aspose.com/cells/python/asposecells.api/pdfsaveoptions#Compliance), позволяющее сохранить файлы Excel в соответствующие стандартам PDF/A файлы PDF.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-AdvancedConversiontoPdf.py" >}}

{{% alert color="primary" %}}

если ваша электронная таблица содержит формулы, вызовите метод [**Workbook.calculateFormula**](https://reference.aspose.com/cells/python-java/asposecells.api/workbook#calculateFormula()) непосредственно перед рендерингом электронной таблицы в PDF. Это гарантирует, что зависимые от формул значения будут пересчитаны, и в PDF будут отображены правильные значения.

{{% /alert %}}
