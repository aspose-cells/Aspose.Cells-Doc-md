---
title: Encuentra celdas con un estilo específico
type: docs
weight: 80
url: /es/java/find-cells-with-specific-style/
description: Este artículo muestra cómo encontrar celdas con un estilo específico usando MS Excel y Aspose.Cells for Java API.
keywords: find cells with specific style, find cells with specific style excel, find cells with specific style excel java, search cells with specific style, search cells with specific style excel, search cells with specific style excel java, how to find cells with specific style, how to find cells with specific style excel, how to find cells with specific style excel java
---
{{% alert color="primary" %}}

A veces, necesitas encontrar las celdas con algún estilo particular. Este artículo demuestra cómo lograr esto utilizando Microsoft Excel y Aspose.Cells for Java API.

{{% /alert %}}

## Usando Microsoft Excel

Estos son los pasos necesarios para buscar celdas con estilos específicos en MS Excel.

1.  Seleccione**Buscar y seleccionar** en el**Pestaña Inicio**.
1.  Seleccione**Encontrar**.
1.  Hacer clic**Opciones**si las opciones avanzadas no están visibles.
1.  Seleccione**Elija el formato de Cell...** desde el**Formato** desplegable.
1. Seleccione la celda con el estilo que desea buscar.
1.  Hacer clic**Encuentra todos** para encontrar todas las celdas con estilo similar a su celda seleccionada.

## Usando Aspose.Cells for Java

 Aspose.Cells for Java proporciona la función para encontrar celdas en la hoja de trabajo con algún estilo específico. Para esto, el API proporciona[**BuscarOpciones.setStyle()**](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#Style) propiedad.

### Código de muestra

 El siguiente fragmento de código encuentra todas las celdas que tienen el mismo estilo que el de celda**A1** y cambia el texto dentro de esas celdas. Consulte la captura de pantalla de los archivos fuente y de salida para analizar la salida del código de muestra.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FindCellsWithSpecificStyle-FindCellsWithSpecificStyle.java" >}}

Después de la ejecución del código, todas las celdas que tengan el mismo estilo que la celda A1 tendrán el texto "Encontrado".

### capturas de pantalla

![todo:imagen_alternativa_texto](find-cells-with-specific-style_1.png)

**Figura:** Archivo de origen con celdas que tienen estilos

 Aquí está el archivo de salida generado por el siguiente código. Puedes ver todas las celdas que tienen el mismo estilo que de celda**A1** tiene un texto "Encontrado"

![todo:imagen_alternativa_texto](find-cells-with-specific-style_2.png)

**Figura:**Archivo de salida con celdas encontradas después de buscar por**A1** estilo
