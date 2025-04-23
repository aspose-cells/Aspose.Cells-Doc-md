---
title: Uso de Marcadores de Imagen al Agrupar Datos en Marcadores Inteligentes
type: docs
weight: 30
url: /es/net/using-image-markers-while-grouping-data-in-smart-markers/
---

## **Usar Marcadores de Imagen mientras se agrupan datos en Marcadores Inteligentes**
El siguiente ejemplo crea un libro de trabajo y luego agrega las siguientes etiquetas de Smart Markers en las celdas D2, E2 y F2 respectivamente.

{{< highlight java >}}

 &=Person.Name(group:normal,skip:1)

&=Person.City

&=Person.Photo(Picture:FitToCell)

{{< /highlight >}}

Luego llena la fuente de datos con datos y llama al método [WorkbookDesigner.Process()](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner/methods/process) para procesar las etiquetas de smart marker. El código utiliza estas imágenes, es decir [moon.png](5115492.png) y [moon2.png](5115491.png) pero puedes usar cualquier imagen.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageMarkersWhileGroupingDataInSmartMarkers-UsingImageMarkersWhileGroupingDataInSmartMarkers.cs" >}}
{{< app/cells/assistant language="csharp" >}}
