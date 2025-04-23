---
title: Uso de Marcadores de Imagen al Agrupar Datos en Marcadores Inteligentes
type: docs
weight: 630
url: /es/java/using-image-markers-while-grouping-data-in-smart-markers/
---

{{% alert color="primary" %}} 

Este artículo presenta un ejemplo que ilustra el uso de marcadores de imagen al agrupar datos en marcadores inteligentes.

{{% /alert %}} 
## **Usar Marcadores de Imagen mientras se agrupan datos en Marcadores Inteligentes**
El siguiente código de ejemplo crea un libro y luego agrega las siguientes etiquetas de Marcador Inteligente en las celdas D2, E2 y F2 respectivamente.

{{< highlight java >}}

 &=Person.Name(group:normal,skip:1)

&=Person.City

&=Person.Photo(Picture:FitToCell)

{{< /highlight >}}

Luego llena la fuente de datos con datos y llama al método [WorkbookDesigner.Process()](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#process--) para procesar las etiquetas de marcadores inteligentes. El código usa estas imágenes, es decir, [moon.png](5472549.png) y [moon2.png](5472548.png), pero puedes usar cualquier imagen. La siguiente captura de pantalla muestra la salida de este código de ejemplo. Como puedes ver, los datos en la columna E y F están agrupados con respecto a los datos en la columna D.

![todo:image_alt_text](using-image-markers-while-grouping-data-in-smart-markers_1.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Technical-Articles-SmartMarkerGroupingImage.java" >}}
{{< app/cells/assistant language="java" >}}
