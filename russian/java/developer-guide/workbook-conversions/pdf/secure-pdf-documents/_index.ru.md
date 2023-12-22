---
title: Безопасные PDF Документы
type: docs
weight: 260
url: /ru/java/secure-pdf-documents/
description: Защитите файлы PDF при конвертации из файлов Excel. В этой статье показано создание безопасного файла PDF из Excel с помощью Aspose.Cells for Java API.
keywords: secure pdf documents java, secure pdf documents, excel to secure pdf, excel to secure pdf java, convert excel to secure pdf, convert excel to secure pdf java, convert excel to password protected pdf, convert excel to password protected pdf java, excel to password protected pdf java, excel to password protected pdf
---
{{% alert color="primary" %}}

Иногда разработчикам приходится работать с зашифрованными файлами PDF. Например:

- Защитите документы паролями владельца и пользователя, чтобы никто не мог их открыть.
- Установите ограничения или разрешения для документа после его открытия. например, ограничить возможность распечатки или извлечения содержимого документа.

В этой статье объясняется, как передать параметры безопасности PDF при сохранении электронных таблиц в PDF.

{{% /alert %}}

 Aspose.Cells обеспечивает[**PDFSecurityOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsecurityoptions/)для работы с охраной. Вы можете установить пароли владельца и пользователя при сохранении в PDF. Пароль владельца или пароль пользователя потребуется, чтобы открыть зашифрованный документ PDF для просмотра.

- Пароль пользователя может быть нулевым или пустой строкой, в этом случае пароль от пользователя не будет требоваться при открытии документа PDF.
- Открытие документа PDF с правильным паролем владельца обеспечивает полный доступ (без каких-либо ограничений доступа) к документу.
- Открытие документа PDF с правильным паролем пользователя (или открытие документа, у которого нет пароля пользователя) обеспечивает ограниченный доступ в соответствии с указанными разрешениями.

В приведенном ниже примере кода показано, как создать защищенные файлы PDF с помощью Aspose.Cells for Java API.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SecurePDFDocuments-SecurePDFDocuments.java" >}}

{{% alert color="primary" %}}

 Если электронная таблица содержит формулы, лучше всего вызвать[**Рабочая книга.calculateFormula()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula()непосредственно перед его рендерингом в PDF. Это гарантирует, что значения, зависящие от формулы, будут пересчитаны, а правильные значения будут отображены в PDF.

{{% /alert %}}
