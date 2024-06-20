---
title: Автонастройка строк для визуализации
type: docs
weight: 130
url: /ru/java/autofit-rows-for-rendering/
---

Обычно, когда вы хотите отобразить весь текст в ячейке, вы можете автоматически подстроить строку в обычном виде с масштабом 100% в Microsoft Excel. Это позволяет тексту полностью отображаться в обычном виде, даже при печати или сохранении файла в формате PDF, текст будет отображаться правильно.

Однако в некоторых случаях автоматическая подгонка строки работает хорошо в обычном виде, но при переходе в вид для печати или сохранении файла в формате PDF текст обрезается. Пожалуйста, проверьте исходный файл [Book1.xlsx](Book1.xlsx) и скриншоты.

![текст обрезан в виде для печати](text_clipped_in_printview.png)

Если вы хотите предотвратить обрезание текста в сохраненном файле PDF, вы можете автоматически подгонять строку с помощью опции [AutoFitterOptions.ForRendering](https://reference.aspose.com/cells/java/com.aspose.cells/autofitteroptions/#setForRendering-boolean-).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Autofit-AutofitRowsForRendering.java" >}}

Теперь текст не обрезается в сохраненном файле PDF.

![текст не обрезается в сохраненном pdf](text_not_clipped_in_saved_pdf.png)
