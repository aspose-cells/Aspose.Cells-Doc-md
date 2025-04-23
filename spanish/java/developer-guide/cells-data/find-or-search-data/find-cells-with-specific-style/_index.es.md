---
title: Encontrar celdas con un estilo específico
type: docs
weight: 80
url: /es/java/find-cells-with-specific-style/
description: Este artículo demuestra cómo encontrar celdas con un estilo específico utilizando MS Excel y la API Aspose.Cells for Java.
keywords: encontrar celdas con estilo específico, encontrar celdas con estilo específico excel, encontrar celdas con estilo específico excel java, buscar celdas con estilo específico, buscar celdas con estilo específico excel, buscar celdas con estilo específico excel java, cómo encontrar celdas con estilo específico, cómo encontrar celdas con estilo específico excel, cómo encontrar celdas con estilo específico excel java
---

{{% alert color="primary" %}}

A veces, necesitas encontrar las celdas con un estilo particular. Este artículo demuestra cómo lograrlo utilizando Microsoft Excel y la API Aspose.Cells for Java.

{{% /alert %}}

## Usando Microsoft Excel

Estos son los pasos necesarios para buscar celdas con estilos específicos en MS Excel.

1. Selecciona **Buscar y Seleccionar** en la pestaña **Inicio**.
1. Selecciona **Buscar**.
1. Haz clic en **Opciones** si las opciones avanzadas no son visibles.
1. Selecciona **Elegir formato de celda...** en el menú desplegable **Formato**.
1. Selecciona la celda con el estilo que deseas buscar.
1. Haz clic en **Buscar todo** para encontrar todas las celdas con un estilo similar al de la celda seleccionada.

## Usando Aspose.Cells for Java

Aspose.Cells for Java proporciona la función de encontrar celdas en la hoja de cálculo con un estilo específico. Para esto, la API proporciona la propiedad [**FindOptions.setStyle()**](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#Style).

### Código de Ejemplo

El siguiente fragmento de código encuentra todas las celdas que tienen el mismo estilo que la celda **A1** y cambia el texto dentro de esas celdas. Por favor, consulta la captura de pantalla de los archivos de origen y de salida para analizar la salida del código de ejemplo.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FindCellsWithSpecificStyle-FindCellsWithSpecificStyle.java" >}}

Después de la ejecución del código, todas las celdas que tienen el mismo estilo que la de la celda A1 tendrán el texto "Encontrado".

### Capturas de Pantalla

![todo:image_alt_text](find-cells-with-specific-style_1.png)

**Figura:** Archivo fuente con celdas con estilos

Aquí está el archivo de salida generado por el siguiente código. Puede ver que todas las celdas que tienen el mismo estilo que la celda **A1** tienen el texto "Encontrado".

![todo:image_alt_text](find-cells-with-specific-style_2.png)

**Figura:** Archivo de salida con celdas encontradas después de buscar por el estilo de **A1**
{{< app/cells/assistant language="java" >}}
