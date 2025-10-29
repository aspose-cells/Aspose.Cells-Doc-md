---
title: Автонастройка строк для визуализации
type: docs
weight: 130
url: /ru/python-net/autofit-rows-for-rendering/
description: Узнайте, как автоматически настраивать строки для отображения через Aspose.Cells для Python via .NET API.
keywords: Библиотека Excel для Python, автонастройка строк для визуализации Python, автоматически подстраивает высоту строки при открытии файла Excel. 
---

Обычно, когда вы хотите отобразить весь текст в ячейке, вы можете автоматически подстроить строку в обычном виде с масштабом 100% в Microsoft Excel. Это позволяет тексту полностью отображаться в обычном виде, даже при печати или сохранении файла в формате PDF, текст будет отображаться правильно.

Однако в некоторых случаях автоматическая подгонка строки работает хорошо в обычном виде, но при переходе в вид для печати или сохранении файла в формате PDF текст обрезается. Пожалуйста, проверьте исходный файл [Book1.xlsx](Book1.xlsx) и скриншоты.

![текст обрезан в виде для печати](text_clipped_in_printview.png)

Если вы хотите предотвратить обрезание текста в сохраненном файле PDF, вы можете автоматически подстроить строку с помощью опции [AutoFitterOptions.for_rendering](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions/for_rendering/).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-AutofitRowsForRendering.py" >}}

Теперь текст не обрезается в сохраненном файле PDF.

![текст не обрезается в сохраненном pdf](text_not_clipped_in_saved_pdf.png)
{{< app/cells/assistant language="python-net" >}}
