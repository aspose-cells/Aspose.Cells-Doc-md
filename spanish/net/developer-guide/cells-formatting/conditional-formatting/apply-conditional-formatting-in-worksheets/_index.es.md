---
title: Aplicar formato condicional en hojas de trabajo
description: Cómo utilizar la biblioteca Aspose.Cells en C# para aplicar formato condicional en hojas de trabajo. Al ajustar estos criterios, tiene más control sobre el aspecto y la apariencia de las células.
keywords: Aspose.Cells, Conditional Formatting, C#, Worksheet, Formatting
type: docs
weight: 130
url: /es/net/apply-conditional-formatting-in-worksheets/
---
{{% alert color="primary" %}}

Este artículo está diseñado para proporcionar una comprensión detallada de cómo agregar formato condicional a un rango de celdas en una hoja de trabajo.

El formato condicional es una característica avanzada en Microsoft Excel que le permite aplicar formatos a un rango de celdas y hacer que ese formato cambie según el valor de la celda o el valor de una fórmula. Por ejemplo, el fondo de una celda puede ser rojo para resaltar un valor negativo, o el color del texto puede ser verde para un valor positivo. Cuando el valor de la celda cumple con la condición de formato, se aplica el formato. Si el valor de la celda no cumple con la condición de formato, se utiliza el formato predeterminado de la celda.

Es posible aplicar formato condicional con Microsoft Office Automation, pero eso tiene sus inconvenientes. Hay varias razones y cuestiones involucradas: por ejemplo, seguridad, estabilidad, escalabilidad y velocidad. La razón principal para encontrar otra solución es que el propio Microsoft recomienda encarecidamente no utilizar Office Automation para soluciones de software.

Este artículo muestra cómo crear una aplicación de consola y agregar formato condicional en celdas con unas pocas líneas de código simples usando Aspose.Cells API.

{{% /alert %}}

##  **Uso de Aspose.Cells para aplicar formato condicional según el valor Cell**

1. *Descargue e instale Aspose.Cells**.
 1. Descargar Aspose.Cells for .NET.
1. Instálelo en su computadora de desarrollo.
 Todos los componentes Aspose, cuando están instalados, funcionan en modo de evaluación. El modo de evaluación no tiene límite de tiempo y sólo inyecta marcas de agua en los documentos producidos.
1. *Crear un proyecto**.
 Inicie Visual Studio.NET y cree una nueva aplicación de consola. Este ejemplo crea una aplicación de consola C#, pero también puedes usar VB.NET.
1. *Agregar referencias**.
 Agregue una referencia a Aspose.Cells a su proyecto, por ejemplo agregue una referencia a….\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll
1. *Aplicar formato condicional según el valor de la celda.
 continuación se muestra el código utilizado para realizar la tarea. Aplico formato condicional en una celda.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ApplyConditionalFormatting-ApplyConditionalFormattingCellValue-1.cs" >}}

Cuando se ejecuta el código anterior, se aplica el formato condicional a la celda "A1" en la primera hoja de trabajo del archivo de salida (output.xls). El formato condicional aplicado a A1 depende del valor de la celda. Si el valor de la celda A1 está entre 50 y 100, el color de fondo es rojo debido al formato condicional aplicado.

##  **Uso de Aspose.Cells para aplicar formato condicional según la fórmula**

1. Aplicar formato condicional según la fórmula (fragmento de código)
 A continuación se muestra el código para realizar la tarea. Aplica formato condicional en B3.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ApplyConditionalFormatting-ApplyConditionalFormattingFormula-1.cs" >}}

Cuando se ejecuta el código anterior, se aplica formato condicional a la celda "B3" en la primera hoja de trabajo del archivo de salida (output.xls). El formato condicional aplicado depende de la fórmula que calcula el valor de "B3" como suma de B1 y B2.
