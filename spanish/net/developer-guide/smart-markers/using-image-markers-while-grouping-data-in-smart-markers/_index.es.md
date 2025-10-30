---
title: Cómo Usar Marcadores de Imagen en Smart Markers
type: docs
weight: 30
url: /es/net/how-to-use-image-markers-in-smart-markers/
alias: [/net/using-image-markers-while-grouping-data-in-smart-markers/]
---

## **Escenarios de uso posibles**
Los marcadores de imagen son marcadores de posición especializados en sistemas de plantillas (como FoxPro, Handlebars, o frameworks de UI modernos) que inyectan dinámicamente imágenes o activos visuales en las plantillas. A veces, necesitas insertar imágenes usando smart markers. Aspose.Cells permite agregar imágenes a smart markers.

## **Parámetros de Imagen en Smart Markers**
Parámetros de marcadores inteligentes para gestionar imágenes.

- **Imagen:AjustarACelda** - Ajusta automáticamente la imagen a la altura de la fila y al ancho de la columna de la celda.
- **Imagen:EscalarN** - Escala la altura y el ancho al N por ciento.
- **Imagen:Ancho:NyAltura:N** - Renderiza la imagen de N pulgadas de alto y N pulgadas de ancho. También se pueden especificar posiciones Izquierda y Arriba (en puntos).

## **Cómo usar marcadores de imagen en Marcadores inteligentes**
Por favor, vea el siguiente ejemplo de código que muestra cómo insertar imágenes usando marcadores inteligentes.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-ImageMarkers-1.cs" >}}

## **Cómo usar marcadores de imagen al agrupar datos en marcadores inteligentes**
El siguiente ejemplo crea un libro de trabajo y luego agrega las siguientes etiquetas de Smart Markers en las celdas D2, E2 y F2 respectivamente.

{{< highlight java >}}

&=Person.Name(group:normal,skip:1)

&=Person.City

&=Person.Photo(Picture:FitToCell)

{{< /highlight >}}

Luego llena la fuente de datos con datos y llama al método [WorkbookDesigner.Process()](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner/methods/process) para procesar las etiquetas de smart marker. El código utiliza estas imágenes, es decir [moon.png](5115492.png) y [moon2.png](5115491.png) pero puedes usar cualquier imagen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageMarkersWhileGroupingDataInSmartMarkers-UsingImageMarkersWhileGroupingDataInSmartMarkers.cs" >}}

{{< app/cells/assistant language="csharp" >}}
