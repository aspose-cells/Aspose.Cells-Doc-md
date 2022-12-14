---
title: Creación de subtotales
type: docs
weight: 800
url: /es/net/creating-subtotals/
---
{{% alert color="primary" %}}

Puede crear automáticamente subtotales para cualquier valor repetido en una hoja de cálculo. Aspose.Cells proporciona funciones API que lo ayudan a agregar subtotales a las hojas de cálculo mediante programación.

{{% /alert %}}

## **Usando Microsoft Excel**

Para agregar subtotales en Microsoft Excel:

1. Cree una lista de datos simple en la primera hoja de trabajo del libro de trabajo (como se muestra en la figura a continuación) y guarde el archivo como Book1.xls.
1. Seleccione cualquier celda dentro de su lista.
1.  Desde el**Datos** menú, seleccione**subtotales**. Se mostrará el cuadro de diálogo Subtotales. Defina qué función utilizar y dónde colocar los subtotales.

## **Usando el Aspose.Cells API**

 Aspose.Cells proporciona una clase,[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , que representa un archivo de Excel Microsoft. los[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la clase contiene un[**Hojas de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)colección que permite el acceso a cada hoja de trabajo en el archivo de Excel.

 Una hoja de trabajo está representada por el[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) clase. La clase proporciona una amplia gama de propiedades y métodos para administrar hojas de trabajo y otros objetos. Cada hoja de trabajo consta de un[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) recopilación. Para agregar subtotales a una hoja de trabajo, use el[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) clase'[**Total parcial**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/subtotal/index)método. Proporcione valores de parámetros al método para especificar cómo se debe calcular y colocar el subtotal.

En los ejemplos a continuación, hemos agregado subtotales a la primera hoja de trabajo del archivo de plantilla (Book1.xls) usando Aspose.Cells API. Cuando se ejecuta el código, se crea una hoja de trabajo con subtotales.

Los fragmentos de código que siguen muestran cómo agregar subtotales a una hoja de trabajo con Aspose.Cells for .NET.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-CreatingSubtotals-1.cs" >}}

## **Temas avanzados**
- [Aplicar subtotal y cambiar la dirección de las filas de resumen del esquema debajo del detalle](/cells/es/net/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/)
