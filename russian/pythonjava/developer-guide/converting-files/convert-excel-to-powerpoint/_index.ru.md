---
title: Преобразование Excel в PowerPoint
type: docs
weight: 300
url: /ru/python-java/convert-excel-to-powerpoint/
description: Преобразовать файл Excel в PPT с использованием Python.
keywords: Экспорт рабочей книги на слайд без офиса 2013, офиса 2016, офиса 2019 и офиса 365
---

{{% alert color="primary" %}}

Aspose.Cells для Python via Java поддерживает преобразование файлов Excel (.xls, xlsx, .xlsb, xlsm), CSV и OpenOffice (.ods) в файл PowerPoint.

{{% /alert %}}

## **Преобразовать рабочую книгу Excel в PPT**

Нет необходимости думать, как преобразовать книгу Excel в формат PowerPoint, потому что библиотека Aspose.Cells для Python via Java предлагает лучшее решение. API Aspose.Cells для Python via Java поддерживает преобразование электронных таблиц в формат PowerPoint. Чтобы экспортировать книгу в формат PowerPoint, передайте [**SaveFormat.PPTX**](https://reference.aspose.com/cells/python-java/asposecells.api/saveformat) в качестве второго параметра метода [**Workbook.save**](https://reference.aspose.com/cells/python-java/asposecells.api/workbook#save\(java.lang.String,%20int\)). Вы также можете использовать класс [**PptxSaveOptions**](https://reference.aspose.com/cells/python-java/asposecells.api/PptxSaveOptions) для указания дополнительных настроек экспорта листа в файл .pptx.

В следующем примере кода демонстрируется экспорт рабочей книги Excel в PPT. Пожалуйста, посмотрите код для преобразования [исходного файла](sample.xlsx) в генерируемый кодом файл Word для справки.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Convert-Excel-to-Pptx.py" >}}


