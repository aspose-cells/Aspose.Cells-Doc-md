---
title: Cargar libro de trabajo con el tamaño de papel de impresora especificado
type: docs
weight: 430
url: /es/net/load-workbook-with-specified-printer-paper-size/
---
{{% alert color="primary" %}}

 Puede especificar el tamaño de papel de la impresora de su elección mientras carga su libro de trabajo usando el[**LoadOptions.SetPaperSize()**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/methods/setpapersize) método. Tenga en cuenta que si crea un nuevo archivo en MS Excel, encontrará que el tamaño del papel es el mismo que el de la configuración predeterminada de la impresora en su máquina.

{{% /alert %}}

 El siguiente código de ejemplo ilustra el uso de[**LoadOptions.SetPaperSize()**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/methods/setpapersize) método. Primero crea un libro de trabajo, luego lo guarda en el flujo de memoria en formato XLSX. Luego lo carga con papel tamaño A5 y lo guarda en formato PDF. Luego lo vuelve a cargar con papel tamaño A3 y lo vuelve a guardar en formato PDF. Si abre los PDF de salida y comprueba el tamaño del papel, verá que son diferentes. Uno es A5 y el otro es A3. Por favor descarga el[PDF de salida A5](5115234.pdf) y[PDF de salida A3](5115233.pdf) generado por el código para su referencia.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LoadWorkbookWithPrinterSize-1.cs" >}}
