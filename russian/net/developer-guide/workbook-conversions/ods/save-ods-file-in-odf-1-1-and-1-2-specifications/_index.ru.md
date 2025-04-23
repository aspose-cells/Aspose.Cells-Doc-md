---
title: Сохранение файла ODS в соответствии со стандартами ODF 1.1, 1.2 и 1.3
linktitle: Сохранить как ODF 1.1, 1.2 и 1.3
description: Конвертация Excel в стандарты ODF 1.1, 1.2 и 1.3 с помощью Aspose.Cells.
type: docs
weight: 230
url: /ru/net/save-ods-file-in-odf-1-1-and-1-2-specifications/
---

{{% alert color="primary" %}}

Aspose.Cells поддерживает сохранение файла ODS (**OpenDocument Spreadsheet**) в спецификациях ODF (**OpenDocument Format**) 1.1, 1.2 и 1.3. В Aspose.Cells есть свойство [**OdsSaveOptions.OdfStrictVersion**](https://reference.aspose.com/cells/net/aspose.cells/odssaveoptions/odfstrictversion/), которое указывает версию ODF для сохранения ODS файлов. Значение по умолчанию — [**OpenDocumentFormatVersionType.Odf12**](https://reference.aspose.com/cells/net/aspose.cells.ods/opendocumentformatversiontype/). Поэтому сохранение ODS файла без этого настройки использует спецификации 1.2.

{{% /alert %}}

Пример ниже создает объект рабочей книги, добавляет значение в ячейку A1 на первом листе и затем сохраняет файл ODS в спецификациях ODF 1.1, 1.2 и 1.3. По умолчанию файл ODS сохраняется в спецификации ODF 1.2.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-OdsFileSaveOptions-SaveODSFileinODF11and12Specifications.cs" >}}
{{< app/cells/assistant language="csharp" >}}
