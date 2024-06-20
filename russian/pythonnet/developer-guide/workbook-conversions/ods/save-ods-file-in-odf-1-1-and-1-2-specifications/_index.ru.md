---
title: Сохранить файл ODS в спецификациях ODF 1.1 и 1.2
linktitle: Сохранить как ODF 1.1 и 1.2 
description: Конвертировать Excel в спецификации ODF 1.1 и 1.2 с помощью Aspose.Cells.
type: docs
weight: 230
url: /ru/python-net/save-ods-file-in-odf-1-1-and-1-2-specifications/
description: Как сохранить файл ODS в спецификации ODF 1.1 и 1.2 с использованием Aspose.Cells для Python via .NET API.
keywords: Python сохранить файл ODS в спецификации ODF 1.1 и 1.2, сохранить файл ODS в спецификации ODF 1.1 и 1.2, Python via NET.
---

{{% alert color="primary" %}}

Aspose.Cells для Python via .NET поддерживает сохранение файла ODS (**OpenDocument Spreadsheet**) в спецификациях ODF (**OpenDocument Format**) 1.1 и 1.2. Aspose.Cells для Python via .NET имеет свойство [**OdsSaveOptions.is_strict_schema11**](https://reference.aspose.com/cells/python-net/aspose.cells/odssaveoptions/is_strict_schema11/), которое определяет использование спецификации ODF 1.1 при сохранении файлов ODS. Значение по умолчанию этого свойства — **false**, поэтому файл ODS, сохраненный без этой настройки, использует спецификации 1.2.

{{% /alert %}}

Приведенный ниже образец кода создает объект книги, добавляет некоторое значение в ячейку A1 на первом листе, а затем сохраняет файл ODS в спецификациях ODF 1.1 и 1.2. По умолчанию файл ODS сохраняется в спецификации ODF 1.2.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-OdsFileSaveOptions-SaveODSFileinODF11and12Specifications.py" >}}
