---
title: Безопасный PDF Документы
type: docs
weight: 120
url: /ru/net/secure-pdf-documents/
---
{{% alert color="primary" %}}

Иногда разработчикам необходимо работать с зашифрованными файлами PDF. Например, им необходимо защитить документы с помощью паролей пользователя и владельца, чтобы никто не мог их открыть, или ограничить возможность печати или извлечения содержимого документа.

В этой статье объясняется, как передать параметры безопасности PDF при сохранении электронных таблиц в PDF.

{{% /alert %}}

 Aspose.Cells обеспечивает[**Aspose.Cells.Rendering.PdfSecurity**](https://reference.aspose.com/cells/net/aspose.cells.rendering.pdfsecurity) namespace для работы с безопасностью. Пример кода ниже описывает, как защитить PDF-файлы с помощью Aspose.Cells.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-SecurePDFDocuments-1.cs" >}}

{{% alert color="primary" %}}

 Если электронная таблица содержит формулы, лучше всего вызвать[**Рабочая книга.ВычислитьФормулу()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula)непосредственно перед рендерингом в PDF. Это гарантирует, что значения, зависящие от формулы, будут пересчитаны, а правильные значения будут отображены в PDF.

{{% /alert %}}
