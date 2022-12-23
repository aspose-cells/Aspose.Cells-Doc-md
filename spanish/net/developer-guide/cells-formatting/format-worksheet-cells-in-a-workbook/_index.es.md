---
title: Dar formato a la hoja de trabajo Cells en un libro de trabajo
type: docs
weight: 2000
url: /es/net/format-worksheet-cells-in-a-workbook/
---
{{% alert color="primary" %}}

Este artículo muestra cómo:

1. Utilice estilos para dar formato rápidamente a los datos.
1. Formato de celdas en filas y columnas.
1. Use bordes y colores para enfatizar los datos.
1. Aplique formatos de números para enfatizar los datos.
1. Use fuentes y atributos para resaltar datos.
1. Da formato a los datos en un rango con nombre.
1. Cambiar la alineación y la orientación de los datos.
1. Establezca la altura de fila y el ancho de columna.

 El proyecto de ejemplo realiza todas estas tareas y brinda a los desarrolladores una descripción detallada de cómo crear un libro de trabajo, agregar datos y aplicar formato usando[Aspose.Cells](https://products.aspose.com/cells/net/).

{{% /alert %}}

## **Formateo de datos**

El formato se utiliza para distinguir entre diferentes tipos de información y para mostrar los datos con claridad.

Un formato representa un estilo y se define como un conjunto de características, como fuentes y tamaños de fuentes, formatos de números, bordes de celdas, sombreado de celdas, sangría, alineación y orientación del texto. Los bordes proporcionan más formas de resaltar información. Un borde es una línea dibujada alrededor de una celda o un grupo de celdas.

Los formatos numéricos también hacen que los datos sean más significativos. Al aplicar diferentes formatos de números, puede cambiar la apariencia de los números sin cambiar el número detrás de la apariencia.

Aspose.Cells le permite dibujar bordes alrededor de celdas y rangos fácilmente. También le permite aplicar fuentes y sombrear celdas. El componente es lo suficientemente eficiente como para dar formato a una fila o columna completa, establecer alineaciones, ajustar y rotar texto en celdas. Aspose.Cells admite además todos los formatos de números admitidos por Microsoft Excel.

Este artículo muestra cómo crear una aplicación de consola en Visual Studio.Net que genera un informe de ventas anual. El libro de trabajo se crea desde cero, luego se insertan los datos y se formatea la hoja de trabajo. Mostramos cómo crear una aplicación de consola simple que crea un libro de Excel (también puede usar un archivo de plantilla), inserta datos de ventas en la primera hoja de trabajo, formatea los datos y guarda un archivo de Excel.

### **Proceso**

A continuación se muestran los pasos necesarios para crear una hoja de cálculo y formatear diferentes celdas en diferentes filas y columnas de una hoja de trabajo.

1. Descargar e instalar Aspose.Cells:
   1. [Descargar](https://downloads.aspose.com/cells/net) Aspose.Cells for .NET.
 1. Instálelo en su computadora de desarrollo.
1. Cree un proyecto y agregue referencias:
 1. Inicie Visual Studio.Net.
 1. Cree una nueva aplicación de consola.
 1. Agregue una referencia a Aspose.Cells, por ejemplo...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll
1. Agregue el siguiente código al proyecto:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FormatWorksheetCells-1.cs" >}}
