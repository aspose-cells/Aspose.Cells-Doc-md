---  
title: Establecer formatos condicionales de archivos Excel y ODS
linktitle: Formatos condicionales  
type: docs  
weight: 60  
url: /es/nodejs-cpp/conditional-formatting/  
description: Cómo aplicar formatos condicionales en archivos Excel y ODS en Node.js vía C++.  
keywords: aplicar formatos condicionales en Node.js vía C++  
---  

## **Introducción**

El formato condicional es una característica avanzada que permite aplicar formatos a una celda o rango de celdas y que ese formato cambie dependiendo del valor de la celda o del valor de una fórmula. Por ejemplo, puedes hacer que una celda aparezca en negrita solo cuando el valor de la celda sea mayor a 500. Cuando el valor de la celda cumple la condición, se aplica el formato especificado a la celda. Si el valor de la celda no cumple la condición, se usa el formato predeterminado de la celda. En Microsoft Excel, selecciona **Formato**, luego **Formato condicional** para abrir el cuadro de diálogo de Formato condicional.

Aspose.Cells admite aplicar formato condicional a las celdas en tiempo de ejecución. Este artículo explica cómo. También explica cómo calcular el color utilizado por Excel para el formato condicional de escala de color.

## **Aplicar formato condicional**

Aspose.Cells admite el formato condicional de varias maneras:

- Usando una hoja de cálculo de diseñador
- Usando el método de copia.
- Creando formato condicional en tiempo de ejecución.

### **Usar la Hoja de Cálculo de Diseñador**

Los desarrolladores pueden crear una hoja de cálculo de diseñador que contenga formato condicional en Microsoft Excel y luego abrir esa hoja de cálculo con Aspose.Cells. Aspose.Cells carga y guarda la hoja de cálculo de diseñador, conservando cualquier configuración de formato condicional.

### **Usando el Método de Copia**

Aspose.Cells permite a los desarrolladores copiar la configuración de formato condicional de una celda a otra en la hoja de cálculo llamando al método [**Range.copy()**](https://reference.aspose.com/cells/nodejs-cpp/range/#copy-range-).

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ConditionalFormatting-CopyConditionalFormattsByCopyRange.js" >}}


## **Aplicar formato condicional en tiempo de ejecución**

Aspose.Cells te permite tanto agregar como eliminar formato condicional en tiempo de ejecución. Los ejemplos de código a continuación muestran cómo establecer el formato condicional:

1. Instanciar un libro de trabajo.
1. Agregar un formato condicional vacío.
1. Establecer el rango al que debe aplicarse el formato.
1. Definir las condiciones de formato.
1. Guarde el archivo.

Después de este ejemplo vienen varios ejemplos más pequeños que muestran cómo aplicar configuraciones de fuente, configuraciones de bordes y patrones.

Microsoft Excel 2007 agregó un formato condicional más avanzado que también soporta Aspose.Cells. Los ejemplos aquí muestran cómo usar un formato sencillo, mientras que los ejemplos de Microsoft Excel 2007 muestran cómo aplicar un formato condicional más avanzado.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ConditionalFormatting-ApplyingConditionalFormattingAtRuntime.js" >}}


### **Establecer fuente**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ConditionalFormatting-SetFont.js" >}}



{{% alert color="primary" %}}

Solo puedes cambiar el estilo de la fuente, el color del texto, el subrayado y la tachadura.

{{% /alert %}}

### **Establecer borde**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ConditionalFormatting-SetBorder.js" >}}


{{% alert color="primary" %}}

Solo puedes usar estilos de línea delgados para el borde del contorno. No se permiten líneas diagonales.

{{% /alert %}}

### **Establecer patrón**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ConditionalFormatting-SetPattern.js" >}}



## **Temas avanzados**  
- [Agregar escalas de colores de 2 colores y 3 colores con formato condicional](/cells/es/nodejs-cpp/adding-2-color-scale-and-3-color-scale-conditional-formattings/)  
- [Aplicar formato condicional en hojas de cálculo](/cells/es/nodejs-cpp/apply-conditional-formatting-in-worksheets/)  
- [Aplicar sombreado a filas y columnas alternas con formato condicional](/cells/es/nodejs-cpp/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/)  
- [Generar imágenes de barras de datos de formato condicional](/cells/es/nodejs-cpp/generate-conditional-formatting-databars-images/)  
- [Obtener conjuntos de iconos, barras de datos o escalas de colores utilizados en el formato condicional](/cells/es/nodejs-cpp/get-icon-sets-data-bars-or-color-scales-objects-used-in-conditional-formatting/)  


{{< app/cells/assistant language="nodejs-cpp" >}}
