---
title: Establecer formatos condicionales de archivos Excel y ODS.
linktitle: Formatos condicionales
type: docs
weight: 60
url: /es/net/conditional-formatting/
description: Cómo aplicar formatos condicionales a archivos Excel y ODS en CSharp.
keywords: aplicar formatos condicionales 
---

## **Introducción**

El formato condicional es una característica avanzada de Microsoft Excel que te permite aplicar formatos a una celda o rango de celdas y que ese formato cambie dependiendo del valor de la celda o del valor de una fórmula. Por ejemplo, puedes hacer que una celda aparezca en negrita solo cuando el valor de la celda sea mayor que 500. Cuando el valor de la celda cumple la condición, se aplica el formato especificado a la celda. Si el valor de la celda no cumple la condición del formato, se utiliza el formato predeterminado de la celda. En Microsoft Excel, selecciona **Formato**, luego **Formato condicional** para abrir el cuadro de diálogo Formato condicional.

Aspose.Cells admite aplicar formato condicional a las celdas en tiempo de ejecución. Este artículo explica cómo. También explica cómo calcular el color utilizado por Excel para el formato condicional de escala de color.

## **Aplicar formato condicional**

Aspose.Cells admite el formato condicional de varias maneras:

- Usando una hoja de cálculo de diseñador
- Usando el método de copia.
- Creando formato condicional en tiempo de ejecución.

### **Usar la Hoja de Cálculo de Diseñador**

Los desarrolladores pueden crear una hoja de cálculo de diseñador que contenga formato condicional en Microsoft Excel y luego abrir esa hoja de cálculo con Aspose.Cells. Aspose.Cells carga y guarda la hoja de cálculo de diseñador, conservando cualquier configuración de formato condicional.

### **Usando el Método de Copia**

Aspose.Cells permite a los desarrolladores copiar la configuración de formato condicional de una celda a otra en la hoja de cálculo llamando al método [**Range.Copy()**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/copy/index).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-UsingCopyMethod-1.cs" >}}

## **Aplicar formato condicional en tiempo de ejecución**

Aspose.Cells te permite tanto agregar como eliminar formato condicional en tiempo de ejecución. Los ejemplos de código a continuación muestran cómo establecer el formato condicional:

1. Instanciar un libro de trabajo.
1. Agregar un formato condicional vacío.
1. Establecer el rango al que debe aplicarse el formato.
1. Definir las condiciones de formato.
1. Guarde el archivo.

Después de este ejemplo vienen varios ejemplos más pequeños que muestran cómo aplicar configuraciones de fuente, configuraciones de bordes y patrones.

Microsoft Excel 2007 agregó un formato condicional más avanzado que también es compatible con Aspose.Cells. Los ejemplos aquí ilustran cómo usar formatos simples. Los ejemplos de Microsoft Excel 2007 muestran cómo aplicar formatos condicionales más avanzados.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConditionalFormattingatRuntime-1.cs" >}}

### **Establecer fuente**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontStyle-1.cs" >}}

{{% alert color="primary" %}}

Solo puedes cambiar el estilo de la fuente, el color del texto, el subrayado y la tachadura.

{{% /alert %}}

### **Establecer borde**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-SetBorder-1.cs" >}}

{{% alert color="primary" %}}

Solo puedes utilizar estilos de líneas delgadas para el borde del contorno. No se permiten líneas diagonales.

{{% /alert %}}

### **Establecer patrón**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-SetPattern-1.cs" >}}

## **Temas avanzados**
- [Agregar escalas de colores de 2 colores y 3 colores con formato condicional](/cells/es/net/adding-2-color-scale-and-3-color-scale-conditional-formattings/)
- [Aplicar formato condicional avanzado](/cells/es/net/apply-advanced-conditional-formatting/)
- [Aplicar formato condicional en hojas de cálculo](/cells/es/net/apply-conditional-formatting-in-worksheets/)
- [Aplicar sombreado a filas y columnas alternas con formato condicional](/cells/es/net/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/)
- [Generar imágenes de barras de datos de formato condicional](/cells/es/net/generate-conditional-formatting-databars-images/)
- [Obtener conjuntos de iconos, barras de datos o escalas de colores utilizados en el formato condicional](/cells/es/net/get-icon-sets-data-bars-or-color-scales-objects-used-in-conditional-formatting/)

