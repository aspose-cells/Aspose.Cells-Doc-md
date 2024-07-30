---
title: Cargar libro de trabajo con tamaño de papel de impresora especificado
type: docs
weight: 430
url: /es/cpp/load-workbook-with-specified-printer-paper-size/
---

{{% alert color="primary" %}}

Puede especificar el tamaño de papel de la impresora de su elección al cargar su libro usando el método [**LoadOptions.SetPaperSize()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/setpapersize/). Tenga en cuenta, si crea un archivo nuevo en MS Excel, verá que el tamaño de papel es el mismo que el ajuste de la impresora predeterminada en su máquina.

{{% /alert %}}

El siguiente código de muestra ilustra el uso del método [**LoadOptions.SetPaperSize()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/setpapersize/). Primero crea un libro de trabajo, luego lo guarda en una secuencia de memoria en formato XLSX. Luego lo carga con tamaño de papel A5 y lo guarda en formato PDF. Luego lo carga nuevamente con tamaño de papel A3 y lo guarda nuevamente en formato PDF. Si abres los PDF de salida y revisas su tamaño de papel, verás que son diferentes. Uno es A5 y el otro es A3. Por favor, descargue el [PDF de salida A5](PrinterSize-a5_out.pdf) y el [PDF de salida A3](PrinterSize-a3_out.pdf) generados por el código para su referencia.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadWorkbookWithPrinterSize-1.cpp" >}}
