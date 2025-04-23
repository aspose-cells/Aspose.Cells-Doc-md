---
title: Сохранить файл ODS в спецификациях ODF 1.1, 1.2 и 1.3
type: docs
weight: 170
url: /ru/java/save-ods-file-in-odf-1-1-and-1-2-specifications/
---

{{% alert color="primary" %}}

Aspose.Cells поддерживает сохранение файла ODS (OpenDocument Spreadsheet) в формате ODF 1.1, 1.2 и 1.3. В Aspose.Cells добавлено свойство [**OdsSaveOptions.setOdfStrictVersion()**](https://reference.aspose.com/cells/java/com.aspose.cells/odssaveoptions/#setOdfStrictVersion-int-) для указания версии ODF при сохранении ODS. Значение по умолчанию этого свойства — [**OpenDocumentFormatVersionType.ODF_12**](https://reference.aspose.com/cells/java/com.aspose.cells/opendocumentformatversiontype/#ODF-12). Поэтому ODS-файл, сохраняемый без этой настройки, будет использовать спецификацию 1.2.

{{% /alert %}}

Приведенный ниже образец кода создает объект книги, добавляет некоторое значение в ячейку A1 первого листа и затем сохраняет файл ODS в спецификациях ODF 1.1 и 1.2. По умолчанию файл ODS сохраняется в спецификации ODF 1.2.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SaveODSfile-SaveODSfile.java" >}}
{{< app/cells/assistant language="java" >}}
