---
title: Establecer formatos condicionales de archivos Excel y ODS.
linktitle: Formatos condicionales
type: docs
weight: 60
url: /es/net/conditional-formatting/
description: Cómo aplicar formatos condicionales a archivos Excel y ODS en CSharp.
keywords: apply conditional formats 
---
## **Introducción**

 El formato condicional es una función avanzada de Excel Microsoft que le permite aplicar formatos a una celda o rango de celdas y hacer que ese formato cambie según el valor de la celda o el valor de una fórmula. Por ejemplo, puede hacer que una celda aparezca en negrita solo cuando el valor de la celda es superior a 500. Cuando el valor de la celda cumple la condición, se aplica el formato especificado a la celda. Si el valor de la celda no cumple con la condición de formato, se utiliza el formato predeterminado de la celda. En Microsoft Excel, seleccione**Formato** , después**Formato condicional** para abrir el cuadro de diálogo Formato condicional.

Aspose.Cells admite la aplicación de formato condicional a las celdas en tiempo de ejecución. Este artículo explica cómo. También explica cómo calcular el color utilizado por Excel para el formato condicional de la escala de colores.

## **Aplicar formato condicional**

Aspose.Cells admite el formato condicional de varias formas:

- Usando la hoja de cálculo del diseñador
- Utilizando el método de copia.
- Creación de formato condicional en tiempo de ejecución.

### **Uso de la hoja de cálculo del diseñador**

Los desarrolladores pueden crear una hoja de cálculo de diseñador que contenga formato condicional en Microsoft Excel y luego abrir esa hoja de cálculo con Aspose.Cells. Aspose.Cells carga y guarda la hoja de cálculo de diseñador, manteniendo cualquier configuración de formato condicional.

### **Uso del método de copia**

 Aspose.Cells permite a los desarrolladores copiar configuraciones de formato condicional de una celda a otra en la hoja de trabajo llamando al[**Rango.Copiar()**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/copy/index) método.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-UsingCopyMethod-1.cs" >}}

## **Aplicar formato condicional en tiempo de ejecución**

Aspose.Cells le permite agregar y quitar formato condicional en tiempo de ejecución. Los ejemplos de código a continuación muestran cómo configurar el formato condicional:

1. Crear una instancia de un libro de trabajo.
1. Agregue un formato condicional vacío.
1. Establezca el rango al que se debe aplicar el formato.
1. Defina las condiciones de formato.
1. Guarda el archivo.

Después de este ejemplo, viene una serie de otros ejemplos más pequeños que muestran cómo aplicar configuraciones de fuentes, configuraciones de bordes y patrones.

Microsoft Excel 2007 agregó formato condicional más avanzado que Aspose.Cells también admite. Los ejemplos aquí ilustran cómo usar formato simple, los ejemplos Microsoft de Excel 2007 muestran cómo aplicar formato condicional más avanzado.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConditionalFormattingatRuntime-1.cs" >}}

### **Establecer fuente**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontStyle-1.cs" >}}

{{% alert color="primary" %}}

Solo puede cambiar el estilo de fuente, el color del texto, el estilo de subrayado y el estilo de tachado.

{{% /alert %}}

### **Establecer borde**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-SetBorder-1.cs" >}}

{{% alert color="primary" %}}

Solo puede usar estilos de línea fina en el borde del contorno. No se permiten líneas diagonales.

{{% /alert %}}

### **Establece un patron**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-SetPattern-1.cs" >}}

## **Temas avanzados**
- [Adición de formatos condicionales de escala de 2 colores y escala de 3 colores](/cells/es/net/adding-2-color-scale-and-3-color-scale-conditional-formattings/)
- [Aplicar formato condicional avanzado](/cells/es/net/apply-advanced-conditional-formatting/)
- [Aplicar formato condicional en hojas de trabajo](/cells/es/net/apply-conditional-formatting-in-worksheets/)
- [Aplicar sombreado a filas y columnas alternativas con formato condicional](/cells/es/net/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/)
- [Generar imágenes de barras de datos de formato condicional](/cells/es/net/generate-conditional-formatting-databars-images/)
- [Obtener conjuntos de iconos, barras de datos o objetos de escalas de color utilizados en el formato condicional](/cells/es/net/get-icon-sets-data-bars-or-color-scales-objects-used-in-conditional-formatting/)

