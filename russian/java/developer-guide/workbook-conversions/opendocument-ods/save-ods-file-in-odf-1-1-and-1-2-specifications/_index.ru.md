﻿---
title: Сохраните файл ODS в спецификациях ODF 1.1 и 1.2.
type: docs
weight: 170
url: /ru/java/save-ods-file-in-odf-1-1-and-1-2-specifications/
---
{{% alert color="primary" %}}

Aspose.Cells поддерживает сохранение (**Электронная таблица OpenDocument**) ODS файл в (**Формат OpenDocument** ) Спецификации ODF 1.1 и ODF 1.2. Aspose.Cells добавил[**OdsSaveOptions.setStrictSchema11()**](https://reference.aspose.com/cells/java/com.aspose.cells/odssaveoptions#IsStrictSchema11) свойство использовать спецификацию ODF 1.1 для сохранения файлов ODS. Значение по умолчанию для этого свойства**ЛОЖЬ**поэтому файл ODS, сохраненный без этих специальных настроек, будет использовать спецификацию 1.2.

{{% /alert %}}

Пример кода ниже создает объект рабочей книги, добавляет некоторое значение в ячейку A1 первого рабочего листа, а затем сохраняет файл ODS в спецификациях ODF 1.1 и 1.2. По умолчанию файл ODS сохраняется в спецификации ODF 1.2.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SaveODSfile-SaveODSfile.java" >}}
