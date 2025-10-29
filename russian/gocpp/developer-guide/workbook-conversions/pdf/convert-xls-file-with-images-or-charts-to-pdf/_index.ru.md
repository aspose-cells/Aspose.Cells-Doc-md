---
title: Преобразование файла XLS с изображениями или графиками в PDF с помощью Golang через C++
linktitle: Преобразование XLS файла с изображениями или диаграммами в PDF
type: docs
weight: 50
url: /ru/go-cpp/convert-xls-file-with-images-or-charts-to-pdf/
description: Преобразование XLS файлов с изображениями или графиками в документы PDF с помощью Aspose.Cells и Golang через C++.
---

{{% alert color="primary" %}} 

Aspose.Cells поддерживает преобразование XLS файлов, содержащих изображения и графики, в PDF-документы. Aspose.Cells for C++ может работать независимо для преобразования таблицы в PDF: для этого не требуется Aspose.PDF для C++. Процесс может выполняться в памяти, так как он не зависит от временных или промежуточных XML-файлов. Это означает, что крупные файлы Excel, например, содержащие изображения, графики и другие объекты рисования, могут быть быстро и эффективно преобразованы.

{{% /alert %}} 
## **Образец кода**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertXlsFileWithImagesOrChartsToPdf.go" >}}
{{% alert color="primary" %}} 

Если в таблице есть формулы, лучше всего вызвать метод [Calculate(CalculationData data)](https://reference.aspose.com/cells/go-cpp/abstractcalculationengine/calculate/) сразу перед отображением в PDF. Это гарантирует перерасчет значений, зависящих от формул, и правильное отображение в PDF.

{{% /alert %}}
