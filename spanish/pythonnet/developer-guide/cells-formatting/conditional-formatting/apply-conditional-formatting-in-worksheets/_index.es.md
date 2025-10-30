---
title: Aplicar formato condicional en hojas de cálculo
description: Cómo usar la biblioteca Aspose.Cells para Python via .NET para aplicar formato condicional en hojas de cálculo. Ajustando estos criterios, tienes mayor control sobre cómo se ven y aparecen las celdas.
keywords: Aspose.Cells, Formato condicional, Python, Hoja de cálculo, Formato
type: docs
weight: 130
url: /es/python-net/apply-conditional-formatting-in-worksheets/
---

{{% alert color="primary" %}}

Este artículo está diseñado para proporcionar una comprensión detallada de cómo agregar formato condicional a un rango de celdas en una hoja de cálculo.

El formato condicional es una función avanzada en Microsoft Excel que le permite aplicar formatos a un rango de celdas, y tener ese formato cambie dependiendo del valor de la celda o el valor de una fórmula. Por ejemplo, el fondo de una celda puede ser rojo para resaltar un valor negativo, o el color del texto podría ser verde para un valor positivo. Cuando el valor de la celda cumple con la condición del formato, se aplica el formato. Si el valor de la celda no cumple con la condición de formato, se utiliza el formato predeterminado de la celda.

Es posible aplicar formato condicional con la Automatización de Office de Microsoft, pero eso tiene sus desventajas. Hay varias razones y problemas involucrados, como la seguridad, la estabilidad, la escalabilidad y la velocidad. La razón principal para encontrar otra solución es que Microsoft en sí mismo recomienda fuertemente en contra de la Automatización de Office para soluciones de software.

Este artículo muestra cómo crear una aplicación de consola, agregar formato condicional a las celdas con algunas líneas de código más simples utilizando la API de Aspose.Cells.

{{% /alert %}}

## **Usar Aspose.Cells para Aplicar Formato Condicional Basado en el Valor de la Celda**

1. **Descargar e Instalar Aspose.Cells**.
   1. Descarga Aspose.Cells para Python via .NET.
1. Instálelo en su equipo de desarrollo.
   Todos los componentes de Aspose, al instalarse, funcionan en modo de evaluación. El modo de evaluación no tiene límite de tiempo y solo inserta marcas de agua en los documentos producidos.
1. **Crear un proyecto**.
   Inicia Visual Studio.NET y crea una nueva aplicación de consola. Este ejemplo crea una aplicación de consola en Python, pero también puedes usar VB.NET.
1. **Agregar referencias**.
   Agrega una referencia a Aspose.Cells a tu proyecto.
1. *Aplicar formato condicional basado en el valor de la celda.
   A continuación se muestra el código utilizado para llevar a cabo la tarea. Aplica formato condicional a una celda.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ApplyConditionalFormattingCellValue-1.py" >}}

Cuando se ejecuta el código anterior, se aplica formato condicional a la celda 'A1' en la primera hoja de cálculo del archivo de salida (output.xls). El formato condicional aplicado a A1 depende del valor de la celda. Si el valor de la celda A1 está entre 50 y 100, el color de fondo es rojo debido al formato condicional aplicado.

## **Usar Aspose.Cells para Aplicar Formato Condicional Basado en Fórmula**

1. Aplicando formato condicional dependiendo de la fórmula (Fragmento de código)
   A continuación se muestra el código para lograr la tarea. Aplica formato condicional en B3.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ApplyConditionalFormattingFormula-1.py" >}}

Cuando se ejecuta el código anterior, se aplica formato condicional a la celda “B3” en la primera hoja de cálculo del archivo de salida (output.xls). El formato condicional aplicado depende de la fórmula que calcula el valor de “B3” como la suma de B1 y B2.

{{< app/cells/assistant language="python-net" >}}
