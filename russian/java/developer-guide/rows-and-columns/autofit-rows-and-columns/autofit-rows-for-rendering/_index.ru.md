---
title: Автоподбор строк для рендеринга
type: docs
weight: 130
url: /ru/java/autofit-rows-for-rendering/
---
Обычно, если вы хотите отобразить весь текст в ячейке, вы можете автоматически подогнать строку в обычном представлении с масштабом 100% в Microsoft Excel. Это позволяет тексту быть полностью видимым в обычном режиме, и даже если вы распечатаете или сохраните файл как PDF, текст будет отображаться правильно.

 Однако в некоторых случаях автоподбор строк работает нормально в обычном режиме, но когда вы переключаетесь в режим печати или сохраняете файл как PDF, текст обрезается. Пожалуйста, проверьте исходный файл[Книга1.xlsx](Book1.xlsx) и скриншоты.

![текст обрезан в printview](text_clipped_in_printview.png)

Если вы хотите предотвратить обрезание текста в сохраненном файле PDF, вы можете автоматически подогнать строку с помощью[AutoFitterOptions.ForRendering](https://reference.aspose.com/cells/java/com.aspose.cells/autofitteroptions/#setForRendering-boolean-) вариант.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Autofit-AutofitRowsForRendering.java" >}}

Теперь текст в выходном файле PDF не обрезается.

![текст не обрезается в сохраненном PDF-файле](text_not_clipped_in_saved_pdf.png)