---
title: Cargar libro de trabajo con el tamaño de papel de impresora especificado
type: docs
weight: 790
url: /es/java/load-workbook-with-specified-printer-paper-size/
---
{{% alert color="primary" %}} 

 Puede especificar el tamaño de papel de la impresora de su elección mientras carga su libro de trabajo usando el[LoadOptions.setPaperSize()](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#setPaperSize\(int\)) método. Tenga en cuenta que si crea un nuevo archivo en MS Excel, encontrará que el tamaño del papel es el mismo que el de la configuración predeterminada de la impresora en su máquina.

{{% /alert %}} 
## **Cargar libro de trabajo con el tamaño de papel de impresora especificado**
 El siguiente código de ejemplo ilustra el uso de[LoadOptions.setPaperSize()](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#setPaperSize\(int\) método. Primero crea un libro de trabajo, luego lo guarda en un flujo de matriz de bytes en formato XLSX. Luego lo carga con papel tamaño A5 y lo guarda en formato PDF. Luego lo vuelve a cargar con papel tamaño A3 y lo vuelve a guardar en formato PDF. Si abre los PDF de salida y comprueba el tamaño del papel, verá que son diferentes. Uno es A5 y el otro es A3. Por favor descarga el[Salida A5 PDF](5473435.pdf) y[Salida A3 PDF](5473436.pdf) generado por el código para su referencia.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LoadWorkbook-LoadWorkbook.java" >}}
