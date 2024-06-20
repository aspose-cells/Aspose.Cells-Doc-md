---
title: Конвертировать Excel в Word
type: docs
weight: 300
url: /ru/python-java/convert-excel-to-word/
description: Конвертировать файл Excel в Word с помощью Python.
keywords: Экспорт рабочей книги в Word без офиса 2013, офиса 2016, офиса 2019 и офиса 365
---

{{% alert color="primary" %}}

Aspose.Cells для Python via Java поддерживает преобразование Excel (.xls, xlsx, .xlsb, xlsm), CSV и OpenOffice (.ods) файлов в файл Word.

{{% /alert %}}

## **Преобразовать рабочую книгу Excel в Word**

Нет необходимости думать, как преобразовать книгу Excel в формат Word, потому что библиотека Aspose.Cells для Python via Java предлагает лучшее решение. API Aspose.Cells для Python via Java поддерживает преобразование электронных таблиц в формат Word. Чтобы экспортировать книгу в формат Word, передайте [**SaveFormat.DOCX**](https://reference.aspose.com/cells/python-java/asposecells.api/saveformat) в качестве второго параметра метода [**Workbook.save**](https://reference.aspose.com/cells/python-java/asposecells.api/workbook#save\(java.lang.String,%20int\)). Вы также можете использовать класс [**DocxSaveOptions**](https://reference.aspose.com/cells/python-java/asposecells.api/DocxSaveOptions) для указания дополнительных настроек экспорта листа в файл .docx.

В следующем примере кода демонстрируется экспорт рабочей книги Excel в Word. Пожалуйста, посмотрите код для преобразования [исходного файла](sample.xlsx) в генерируемый кодом файл Word для справки.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Convert-Excel-to-Word.py" >}}


