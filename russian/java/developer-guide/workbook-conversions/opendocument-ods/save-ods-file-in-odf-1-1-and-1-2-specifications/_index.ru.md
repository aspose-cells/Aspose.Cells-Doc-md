---
title: Сохранить файл ODS в спецификациях ODF 1.1 и 1.2
type: docs
weight: 170
url: /ru/java/save-ods-file-in-odf-1-1-and-1-2-specifications/
---

{{% alert color="primary" %}}

Aspose.Cells поддерживает сохранение (**OpenDocument Spreadsheet**) файла ODS в спецификациях (**OpenDocument Format**) ODF 1.1 и ODF 1.2. Aspose.Cells добавил свойство [**OdsSaveOptions.setStrictSchema11()**](https://reference.aspose.com/cells/java/com.aspose.cells/odssaveoptions#IsStrictSchema11) для использования спецификации ODF 1.1 для сохранения файлов ODS. Значение по умолчанию этого свойства **false**, поэтому файл ODS, сохраненный без этого специального параметра, будет использовать спецификацию 1.2.

{{% /alert %}}

Приведенный ниже образец кода создает объект книги, добавляет некоторое значение в ячейку A1 первого листа и затем сохраняет файл ODS в спецификациях ODF 1.1 и 1.2. По умолчанию файл ODS сохраняется в спецификации ODF 1.2.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SaveODSfile-SaveODSfile.java" >}}
