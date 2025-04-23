---
title: Cargar libro de trabajo con tamaño de papel de impresora especificado
type: docs
weight: 790
url: /es/java/load-workbook-with-specified-printer-paper-size/
---

{{% alert color="primary" %}} 

Puede especificar el tamaño de papel de impresora de su elección al cargar su libro de trabajo usando el método [LoadOptions.setPaperSize()](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#setPaperSize-int-). Tenga en cuenta que, si crea un nuevo archivo en MS Excel, encontrará que el tamaño del papel es el mismo que la configuración del impresor predeterminado en su máquina.

{{% /alert %}} 
## **Cargar libro de trabajo con tamaño de papel de impresora especificado**
El siguiente código de ejemplo ilustra el uso del método [LoadOptions.setPaperSize()](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#setPaperSize-int-). Primero crea un libro de trabajo, luego lo guarda en un flujo de matriz de bytes en formato XLSX. Luego lo carga con tamaño de papel A5 y lo guarda en formato PDF. Luego lo carga nuevamente con tamaño de papel A3 y lo guarda otra vez en PDF. Si abre los PDF de salida y verifica su tamaño de papel, verá que son diferentes. Uno es A5 y el otro es A3. Descargue el [PDF de salida A5](5473435.pdf) y el [PDF de salida A3](5473436.pdf) generados por el código para su referencia.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LoadWorkbook-LoadWorkbook.java" >}}
{{< app/cells/assistant language="java" >}}
