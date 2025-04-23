---
title: Establecer formatos condicionales de archivos Excel y ODS.
linktitle: Formatos condicionales
type: docs
weight: 60
url: /es/python-net/conditional-formatting/
description: Cómo aplicar formatos condicionales a archivos Excel y ODS en Python.
keywords: aplicar formatos condicionales 
---

## **Introducción**

El formato condicional es una característica avanzada de Microsoft Excel que te permite aplicar formatos a una celda o rango de celdas y que ese formato cambie dependiendo del valor de la celda o del valor de una fórmula. Por ejemplo, puedes hacer que una celda aparezca en negrita solo cuando el valor de la celda sea mayor que 500. Cuando el valor de la celda cumple la condición, se aplica el formato especificado a la celda. Si el valor de la celda no cumple la condición del formato, se utiliza el formato predeterminado de la celda. En Microsoft Excel, selecciona **Formato**, luego **Formato condicional** para abrir el cuadro de diálogo Formato condicional.

Aspose.Cells para Python via .NET soporta aplicar formato condicional a celdas en tiempo de ejecución. Este artículo explica cómo. También explica cómo calcular el color que Excel usa para formatos condicionales con escala de colores.

## **Aplicar formato condicional**

Aspose.Cells para Python via .NET soporta el formato condicional de varias maneras:

- Usando una hoja de cálculo de diseñador
- Usando el método de copia.
- Creando formato condicional en tiempo de ejecución.

### **Usar la Hoja de Cálculo de Diseñador**

Los desarrolladores pueden crear una hoja de cálculo de diseño que contenga formato condicional en Microsoft Excel y luego abrir esa hoja con Aspose.Cells para Python via .NET. Aspose.Cells para Python via .NET carga y guarda la hoja de diseño, conservando cualquier configuración de formato condicional.

### **Usando el Método de Copia**

Aspose.Cells para Python via .NET permite a los desarrolladores copiar configuraciones de formato condicional de una celda a otra en la hoja de cálculo llamando al método [**Range.copy()**](https://reference.aspose.com/cells/python-net/aspose.cells/range/copy).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-UsingCopyMethod-1.py" >}}

## **Aplicar formato condicional en tiempo de ejecución**

Aspose.Cells para Python via .NET permite agregar y eliminar formato condicional en tiempo de ejecución. Los ejemplos de código a continuación muestran cómo configurar formato condicional:

1. Instanciar un libro de trabajo.
1. Agregar un formato condicional vacío.
1. Establecer el rango al que debe aplicarse el formato.
1. Definir las condiciones de formato.
1. Guarde el archivo.

Después de este ejemplo vienen varios ejemplos más pequeños que muestran cómo aplicar configuraciones de fuente, configuraciones de bordes y patrones.

Microsoft Excel 2007 agregó un formato condicional más avanzado que Aspose.Cells para Python via .NET también soporta. Los ejemplos aquí ilustran cómo usar formatos simples; los ejemplos de Microsoft Excel 2007 muestran cómo aplicar formatos condicionales más avanzados.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ConditionalFormattingatRuntime-1.py" >}}

### **Establecer fuente**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SettingFontStyle-1.py" >}}

{{% alert color="primary" %}}

Solo puedes cambiar el estilo de la fuente, el color del texto, el subrayado y la tachadura.

{{% /alert %}}

### **Establecer borde**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SetBorder-1.py" >}}

{{% alert color="primary" %}}

Solo puedes utilizar estilos de líneas delgadas para el borde del contorno. No se permiten líneas diagonales.

{{% /alert %}}

### **Establecer patrón**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SetPattern-1.py" >}}

## **Temas avanzados**
- [Agregar escalas de colores de 2 colores y 3 colores con formato condicional](/cells/es/python-net/adding-2-color-scale-and-3-color-scale-conditional-formattings/)
- [Aplicar formato condicional en hojas de cálculo](/cells/es/python-net/apply-conditional-formatting-in-worksheets/)
- [Aplicar sombreado a filas y columnas alternas con formato condicional](/cells/es/python-net/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/)
- [Generar imágenes de barras de datos de formato condicional](/cells/es/python-net/generate-conditional-formatting-databars-images/)
- [Obtener conjuntos de iconos, barras de datos o escalas de colores utilizados en el formato condicional](/cells/es/python-net/get-icon-sets-data-bars-or-color-scales-objects-used-in-conditional-formatting/)

{{< app/cells/assistant language="csharp" >}}
