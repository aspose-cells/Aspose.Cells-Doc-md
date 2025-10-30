---
title: Cargar libro de trabajo con tamaño de papel de impresora especificado
type: docs
weight: 430
url: /es/python-net/load-workbook-with-specified-printer-paper-size/
---

{{% alert color="primary" %}}

Puede especificar el tamaño de papel de la impresora de su elección al cargar su libro usando el método [**LoadOptions.set_paper_size()**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/set_paper_size). Tenga en cuenta, si crea un archivo nuevo en MS Excel, verá que el tamaño de papel es el mismo que el ajuste de la impresora predeterminada en su máquina.

{{% /alert %}}

El siguiente código de ejemplo ilustra el uso del método [**LoadOptions.set_paper_size()**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/set_paper_size). Primero crea un libro, luego lo guarda en la memoria en formato XLSX. Luego lo carga con tamaño de papel A5 y lo guarda en formato PDF. Luego lo carga nuevamente con tamaño de papel A3 y lo guarda de nuevo en formato PDF. Si abre los PDF de salida y verifica su tamaño de papel, verá que son diferentes. Uno es A5 y el otro es A3. Descargue el [PDF de salida A5](5115234.pdf) y el [PDF de salida A3](5115233.pdf) generados por el código como referencia.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-LoadWorkbookWithPrinterSize-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
