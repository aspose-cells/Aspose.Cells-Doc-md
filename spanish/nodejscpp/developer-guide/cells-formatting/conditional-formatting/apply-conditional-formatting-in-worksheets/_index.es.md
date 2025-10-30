---
title: Aplicar formato condicional en hojas de cálculo
linktitle: Aplicar formato condicional en hojas de cálculo
description: Cómo usar la biblioteca Aspose.Cells en Node.js vía C++ para aplicar formato condicional en hojas de cálculo para mayor control del aspecto de las celdas.
keywords: Aspose.Cells, formato condicional, Node.js vía C++, hoja de cálculo, formateo
type: docs
weight: 130
url: /es/nodejs-cpp/apply-conditional-formatting-in-worksheets/
---

{{% alert color="primary" %}}

Este artículo está diseñado para proporcionar una comprensión detallada de cómo agregar formato condicional a un rango de celdas en una hoja de cálculo.

El formato condicional es una función avanzada en Microsoft Excel que le permite aplicar formatos a un rango de celdas, y tener ese formato cambie dependiendo del valor de la celda o el valor de una fórmula. Por ejemplo, el fondo de una celda puede ser rojo para resaltar un valor negativo, o el color del texto podría ser verde para un valor positivo. Cuando el valor de la celda cumple con la condición del formato, se aplica el formato. Si el valor de la celda no cumple con la condición de formato, se utiliza el formato predeterminado de la celda.

Es posible aplicar formato condicional con la Automatización de Office de Microsoft, pero eso tiene sus desventajas. Hay varias razones y problemas involucrados, como la seguridad, la estabilidad, la escalabilidad y la velocidad. La razón principal para encontrar otra solución es que Microsoft en sí mismo recomienda fuertemente en contra de la Automatización de Office para soluciones de software.

Este artículo muestra cómo crear una aplicación de consola, agregar formato condicional a las celdas con algunas líneas de código más simples utilizando la API de Aspose.Cells.

{{% /alert %}}

## **Usar Aspose.Cells para Aplicar Formato Condicional Basado en el Valor de la Celda**

1. **Descargar e Instalar Aspose.Cells**.
   1. Descargue la versión Aspose.Cells for Node.js via C++.
1. Instálelo en su equipo de desarrollo.
   Todos los componentes de Aspose, al instalarse, funcionan en modo de evaluación. El modo de evaluación no tiene límite de tiempo y solo inserta marcas de agua en los documentos producidos.
1. **Crear un proyecto**.
    Inicie su proyecto Node.js inicializándolo. Este ejemplo crea una aplicación de consola Node.js.
1. **Agregar referencias**.
    Agregue una referencia a Aspose.Cells en su proyecto, por ejemplo requiriendo el paquete de la siguiente manera:
   ```javascript
   const AsposeCells = require("aspose.cells.node");
   ```
1. **Aplicar formato condicional basado en el valor de la celda**.
   A continuación se presenta el código usado para realizar la tarea. Aplica formato condicional en una celda.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ConditionalFormatting-ApplyToCellValue.js" >}}


Cuando se ejecuta el código anterior, se aplica formato condicional a la celda "A1" en la primera hoja del archivo de salida (output.xls). El formato condicional aplicado a A1 depende del valor de la celda. Si el valor de A1 está entre 50 y 100, el color de fondo será rojo debido al formato condicional aplicado.

## **Usar Aspose.Cells para Aplicar Formato Condicional Basado en Fórmula**

1. Aplicando formato condicional dependiendo de la fórmula (Fragmento de código)
   A continuación se muestra el código para lograr la tarea. Aplica formato condicional en B3.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ConditionalFormatting-ApplyToFormula.js" >}}

Cuando se ejecuta el código anterior, se aplica formato condicional a la celda "B3" en la primera hoja del archivo de salida (output.xls). El formato condicional aplicado depende de la fórmula que calcula el valor de "B3" como la suma de B1 y B2.
{{< app/cells/assistant language="nodejs-cpp" >}}
