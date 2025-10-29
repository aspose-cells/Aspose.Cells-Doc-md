---
title: Сохранение файла ODS в соответствии со спецификациями ODF 1.1, 1.2 и 1.3 с помощью Golang через C++
linktitle: Сохранить как ODF 1.1, 1.2 и 1.3
description: Преобразование Excel в стандарты ODF 1.1, 1.2 и 1.3 с помощью Aspose.Cells и C++.
type: docs
weight: 230
url: /ru/go-cpp/save-ods-file-in-odf-1-1-and-1-2-specifications/
---

{{% alert color="primary" %}}

Aspose.Cells поддерживает сохранение файла ODS (**OpenDocument Spreadsheet**) в спецификациях ODF (**OpenDocument Format**) 1.1, 1.2 и 1.3. В Aspose.Cells есть свойство [**OdsSaveOptions.GetOdfStrictVersion()**](https://reference.aspose.com/cells/go-cpp/odssaveoptions/getodfstrictversion/), которое указывает версию ODF для сохранения ODS файлов. Значение по умолчанию — [**OpenDocumentFormatVersionType.Odf12**](https://reference.aspose.com/cells/cpp/aspose.cells.ods/opendocumentformatversiontype/). Поэтому сохранение ODS файла без этого настройки использует спецификации 1.2.

{{% /alert %}}

Пример ниже создает объект рабочей книги, добавляет значение в ячейку A1 на первом листе и затем сохраняет файл ODS в спецификациях ODF 1.1, 1.2 и 1.3. По умолчанию файл ODS сохраняется в спецификации ODF 1.2.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveOdsFileInOdf11And12Specifications.go" >}}
