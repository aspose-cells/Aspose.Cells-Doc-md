---
title: Implementar un motor de cálculo personalizado para ampliar el motor de cálculo predeterminado de Aspose.Cells
description: Este artículo describe cómo ampliar el motor de cálculo predeterminado implementando un motor de cálculo personalizado utilizando la biblioteca Aspose.Cells. Al cargar un archivo de Excel existente o crear uno nuevo, podemos utilizar los métodos proporcionados por Aspose.Cells para implementar un motor de cálculo personalizado y obtener los resultados. Finalmente, guardamos el archivo Excel modificado en el disco.
keywords: Aspose.Cells, Excel, Custom Calculation Engine, extends the default calculation engine
type: docs
weight: 80
url: /es/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---
##  **Implementar motor de cálculo personalizado**

Aspose.Cells tiene un potente motor de cálculo que puede calcular casi todas las Microsoft fórmulas de Excel. A pesar de esto, también le permite ampliar el motor de cálculo predeterminado, lo que le proporciona mayor potencia y flexibilidad.

Las siguientes propiedades y clases se utilizan para implementar esta característica.

- **[CalculationOptions.CustomEngine](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/customengine)**
- **[AbstractCalculationEngine](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine)**
- **[Datos de cálculo](https://reference.aspose.com/cells/net/aspose.cells/calculationdata)**

El siguiente código implementa el motor de cálculo personalizado. Implementa la interfaz**[AbstractCalculationEngine](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine)** que tiene un**[Calcular (datos de CalculationData)] (https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine/methods/calculate)** método. Este método se aplica a todas sus fórmulas. Dentro de este método, capturamos el**TODAY** función y agregar un día a la fecha del sistema. Entonces, si la fecha actual es 27/07/2023, el motor personalizado calculará HOY() como 28/07/2023.

###  **Muestra de programación**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ImplementCustomCalculationEngine-ImplementCustomCalculationEngine.cs" >}}

###  **Resultado**

Verifique la salida de la consola del código de muestra anterior, el valor (fecha y hora) de A1 con motor personalizado debe ser un día posterior al resultado sin motor personalizado.

###  **Artículo relacionado**

{{% alert color="primary" %}}

[Cálculo directo de una función personalizada sin escribirla en una hoja de trabajo](/cells/es/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}
