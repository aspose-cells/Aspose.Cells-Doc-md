---
title: Aplicar formato condicional en hojas de trabajo
type: docs
weight: 130
url: /es/net/apply-conditional-formatting-in-worksheets/
---
{{% alert color="primary" %}}

Este artículo está diseñado para proporcionar una comprensión detallada de cómo agregar formato condicional a un rango de celdas en una hoja de trabajo.

El formato condicional es una función avanzada en Microsoft Excel que le permite aplicar formatos a un rango de celdas y hacer que ese formato cambie según el valor de la celda o el valor de una fórmula. Por ejemplo, el fondo de una celda puede ser rojo para resaltar un valor negativo o el color del texto puede ser verde para un valor positivo. Cuando el valor de la celda cumple la condición de formato, se aplica el formato. Si el valor de la celda no cumple con la condición de formato, se utiliza el formato predeterminado de la celda.

Es posible aplicar formato condicional con Microsoft Office Automation pero eso tiene sus inconvenientes. Hay varias razones y problemas involucrados: por ejemplo, seguridad, estabilidad, escalabilidad y velocidad. La razón principal para encontrar otra solución es que Microsoft recomienda encarecidamente que no se utilice la automatización de oficinas para las soluciones de software.

Este artículo muestra cómo crear una aplicación de consola, agregar formato condicional en celdas con unas pocas líneas de código simples usando Aspose.Cells API.

{{% /alert %}}

## **Uso de Aspose.Cells para aplicar formato condicional basado en el valor Cell**

1. **Descargar e Instalar Aspose.Cells**.
 1. Descargar Aspose.Cells for .NET.
1. Instálalo en tu computadora de desarrollo.
Todos los componentes Aspose, cuando están instalados, funcionan en modo de evaluación. El modo de evaluación no tiene límite de tiempo y solo inyecta marcas de agua en los documentos producidos.
1. **crear un proyecto**.
 Inicie Visual Studio.NET y cree una nueva aplicación de consola. Este ejemplo crea una aplicación de consola C#, pero también puede usar VB.NET.
1. **Agregar referencias**.
 Agregue una referencia a Aspose.Cells a su proyecto, por ejemplo, agregue una referencia a ….\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll
1. * Aplicar formato condicional basado en el valor de la celda.
 A continuación se muestra el código utilizado para realizar la tarea. Aplico formato condicional en una celda.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ApplyConditionalFormatting-ApplyConditionalFormattingCellValue-1.cs" >}}

Cuando se ejecuta el código anterior, se aplica formato condicional a la celda "A1" en la primera hoja de trabajo del archivo de salida (output.xls). El formato condicional aplicado a A1 depende del valor de la celda. Si el valor de la celda de A1 está entre 50 y 100, el color de fondo es rojo debido al formato condicional aplicado.

## **Uso de Aspose.Cells para aplicar formato condicional basado en fórmula**

1. Aplicar formato condicional según la fórmula (fragmento de código)
 A continuación se muestra el código para realizar la tarea. Aplica formato condicional en B3.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ApplyConditionalFormatting-ApplyConditionalFormattingFormula-1.cs" >}}

Cuando se ejecuta el código anterior, se aplica formato condicional a la celda "B3" en la primera hoja de trabajo del archivo de salida (output.xls). El formato condicional aplicado depende de la fórmula que calcula el valor de "B3" como la suma de B1 y B2.
