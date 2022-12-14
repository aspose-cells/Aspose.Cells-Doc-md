---
title: Uso de marcadores de imagen al agrupar datos en marcadores inteligentes
type: docs
weight: 630
url: /es/java/using-image-markers-while-grouping-data-in-smart-markers/
---
{{% alert color="primary" %}} 

Este artículo presenta un ejemplo que ilustra el uso de marcadores de imagen al agrupar datos en marcadores inteligentes.

{{% /alert %}} 
## **Uso de marcadores de imagen al agrupar datos en marcadores inteligentes**
El siguiente código de ejemplo crea un libro de trabajo y luego agrega las siguientes etiquetas de marcador inteligente en las celdas D2, E2 y F2 respectivamente.

{{< highlight "java" >}}

 &=Person.Name(group:normal,skip:1)

&=Person.City

&=Person.Photo(Picture:FitToCell)

{{< /highlight >}}

 Luego llena la fuente de datos con datos y llama al[WorkbookDesigner.Proceso()](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#process\(\) ) método para procesar etiquetas de marcadores inteligentes. El código utiliza estas imágenes, es decir[luna.png](5472549.png) y[luna2.png](5472548.png) pero puedes usar cualquier imagen. La siguiente captura de pantalla muestra el resultado de este código de ejemplo. Como puede ver, los datos de la columna E y F están agrupados con respecto a los datos de la columna D.

![todo:imagen_alternativa_texto](using-image-markers-while-grouping-data-in-smart-markers_1.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Technical-Articles-SmartMarkerGroupingImage.java" >}}
