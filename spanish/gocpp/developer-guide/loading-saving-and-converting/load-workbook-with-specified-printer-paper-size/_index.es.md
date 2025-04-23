---
title: Cargar libro de trabajo con tamaño de papel de impresora especificado
type: docs
weight: 430
url: /es/go-cpp/load-workbook-with-specified-printer-paper-size/
---

{{% alert color="primary" %}}

Puedes especificar el tamaño de papel de la impresora de tu elección al cargar tu libro usando el método [**LoadOptions.SetPaperSize()**](https://reference.aspose.com/cells/go-cpp/loadoptions/setpapersize/). Ten en cuenta que si creas un archivo nuevo en MS Excel, verás que el tamaño del papel es el mismo que la configuración de la impresora predeterminada en tu máquina.

{{% /alert %}}

El siguiente código de ejemplo ilustra el uso del método [**LoadOptions.SetPaperSize()**](https://reference.aspose.com/cells/go-cpp/loadoptions/setpapersize/). Primero crea un libro y luego lo guarda en un stream de memoria en formato XLSX. Luego lo carga con tamaño de papel A5 y lo guarda en formato PDF. Luego lo carga nuevamente con tamaño de papel A3 y lo guarda de nuevo en formato PDF. Si abres los PDFs de salida y verificas su tamaño de papel, verás que son diferentes. Uno es A5 y el otro es A3. Por favor, descarga el [PDF de salida A5](PrinterSize-a5_out.pdf) y el [PDF de salida A3](PrinterSize-a3_out.pdf) generados por el código para tu referencia.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-LoadWorkbookWithPrinterSize.go" >}}
