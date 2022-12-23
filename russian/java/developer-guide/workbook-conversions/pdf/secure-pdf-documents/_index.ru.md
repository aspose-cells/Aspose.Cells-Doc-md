---
title: Безопасный PDF Документы
type: docs
weight: 260
url: /ru/java/secure-pdf-documents/
description: Защитите файлы PDF при преобразовании из файлов Excel. В этой статье показано создание безопасного файла PDF из Excel с Aspose.Cells for Java API.
keywords: secure pdf documents java, secure pdf documents, excel to secure pdf, excel to secure pdf java, convert excel to secure pdf, convert excel to secure pdf java, convert excel to password protected pdf, convert excel to password protected pdf java, excel to password protected pdf java, excel to password protected pdf
---
{{% alert color="primary" %}}

Иногда разработчикам необходимо работать с зашифрованными файлами PDF. Например, им необходимо защитить документы с помощью паролей пользователя и владельца, чтобы никто не мог их открыть, или ограничить возможность печати или извлечения содержимого документа.

В этой статье объясняется, как передать параметры безопасности PDF при сохранении электронных таблиц в PDF.

{{% /alert %}} 

 Aspose.Cells API предоставляют[**PdfSecurityOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSecurityOptions)класс для работы с защитой файла формата PDF. Пример кода ниже описывает, как создать защищенные файлы PDF с Aspose.Cells for Java API.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SecurePDFDocuments-SecurePDFDocuments.java" >}}

{{% alert color="primary" %}}

 Если электронная таблица содержит формулы, лучше всего вызвать[**Рабочая книга.calculateFormula()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula()) непосредственно перед его визуализацией в PDF. Это гарантирует, что значения, зависящие от формулы, пересчитываются, и правильные значения отображаются в PDF.

{{% /alert %}}
