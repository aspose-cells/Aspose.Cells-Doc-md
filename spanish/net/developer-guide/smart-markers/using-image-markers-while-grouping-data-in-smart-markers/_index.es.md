---
title: Uso de marcadores de imagen al agrupar datos en marcadores inteligentes
type: docs
weight: 30
url: /es/net/using-image-markers-while-grouping-data-in-smart-markers/
---
## **Uso de marcadores de imagen al agrupar datos en marcadores inteligentes**
El siguiente ejemplo crea un libro de trabajo y luego agrega las siguientes etiquetas de marcador inteligente en las celdas D2, E2 y F2 respectivamente.

{{< highlight "java" >}}

 &=Person.Name(group:normal,skip:1)

&=Person.City

&=Person.Photo(Picture:FitToCell)

{{< /highlight >}}

 Luego llena la fuente de datos con datos y llama al[WorkbookDesigner.Proceso()](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner/methods/process) método para procesar etiquetas de marcadores inteligentes. El código utiliza estas imágenes, es decir[luna.png](5115492.png) y[luna2.png](5115491.png) pero puedes usar cualquier imagen.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageMarkersWhileGroupingDataInSmartMarkers-UsingImageMarkersWhileGroupingDataInSmartMarkers.cs" >}}
