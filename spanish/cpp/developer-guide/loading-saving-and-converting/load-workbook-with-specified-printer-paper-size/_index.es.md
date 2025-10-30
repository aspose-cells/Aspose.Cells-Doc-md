---
title: Cargar libro de trabajo con tamaño de papel de impresora especificado
type: docs
weight: 430
url: /es/cpp/load-workbook-with-specified-printer-paper-size/
---

{{% alert color="primary" %}}

Puede especificar el tamaño de papel de la impresora de su elección al cargar su libro usando el método [**LoadOptions.SetPaperSize()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/setpapersize/). Tenga en cuenta, si crea un archivo nuevo en MS Excel, verá que el tamaño de papel es el mismo que el ajuste de la impresora predeterminada en su máquina.

{{% /alert %}}

El siguiente código de ejemplo ilustra el uso del método [**LoadOptions.SetPaperSize()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/setpapersize/). Primero crea un libro de trabajo, luego lo guarda en un flujo de memoria en formato XLSX. Luego, lo carga con tamaño de papel A5 y lo guarda en formato PDF. Después, lo carga nuevamente con tamaño de papel A3 y lo guarda otra vez en PDF. Si abre los PDFs de salida y verifica su tamaño de papel, verá que son diferentes. Uno es A5 y el otro es A3. Descargue los [PDF de salida en A5](PrinterSize-a5_out.pdf) y [PDF de salida en A3](PrinterSize-a3_out.pdf) generados por el código para su referencia.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadWorkbookWithPrinterSize-1.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
