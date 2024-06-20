---
title: Сохранить файл ODS в спецификациях ODF 1.1 и 1.2
linktitle: Сохранить как ODF 1.1 и 1.2 
description: Конвертировать Excel в спецификации ODF 1.1 и 1.2 с помощью Aspose.Cells.
type: docs
weight: 230
url: /ru/net/save-ods-file-in-odf-1-1-and-1-2-specifications/
---

{{% alert color="primary" %}}

Aspose.Cells поддерживает сохранение файла ODS (**OpenDocument Spreadsheet**) в спецификациях ODF (**OpenDocument Format**) 1.1 и 1.2. У Aspose.Cells есть свойство [**OdsSaveOptions.IsStrictSchema11**](https://reference.aspose.com/cells/net/aspose.cells/odssaveoptions/properties/isstrictschema11), которое указывает на использование спецификации ODF 1.1 для сохранения файлов ODS. Значение по умолчанию этого свойства - **false**, поэтому файл ODS, сохраненный без этой настройки, использует спецификации 1.2.

{{% /alert %}}

Приведенный ниже образец кода создает объект книги, добавляет некоторое значение в ячейку A1 на первом листе, а затем сохраняет файл ODS в спецификациях ODF 1.1 и 1.2. По умолчанию файл ODS сохраняется в спецификации ODF 1.2.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-OdsFileSaveOptions-SaveODSFileinODF11and12Specifications.cs" >}}
