---
title: Uso de la función ICustomFunction
description: Este artículo describe cómo crear una función personalizada en Microsoft Excel usando la función ICustomFunction en la biblioteca Aspose.Cells. Al cargar un archivo de Excel existente o crear un nuevo archivo de Excel, podemos usar los métodos proporcionados por Aspose.Cells para definir y registrar funciones personalizadas y obtener los resultados. Finalmente, guardamos el archivo Excel modificado en el disco.
keywords: Aspose.Cells, Excel, ICustomFunction features, custom functions
type: docs
weight: 30
url: /es/net/using-icustomfunction-feature/
---
{{% alert color="primary" %}} 

Este artículo proporciona una comprensión detallada de cómo utilizar la característica ICustomFunction para implementar funciones personalizadas con las API Aspose.Cells.

La interfaz ICustomFunction permite agregar funciones de cálculo de fórmulas personalizadas para ampliar el motor de cálculo principal Aspose.Cells para cumplir con ciertos requisitos. Esta característica es útil para definir funciones personalizadas (definidas por el usuario) en un archivo de plantilla o en código donde la función personalizada se puede implementar y evaluar utilizando Aspose.Cells API como cualquier otra función predeterminada de Excel Microsoft.

 Tenga en cuenta que esta interfaz ha sido reemplazada por[ResumenCálculoMotor](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine/) y será eliminado en el futuro. Algunos artículos técnicos/ejemplos sobre el nuevo API:[aquí](/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/) y[aquí](/net/returning-a-range-of-values-using-abstractcalculationengine/)

{{% /alert %}} 
##  **Crear y evaluar una función definida por el usuario**
 Este artículo demuestra la implementación de la interfaz ICustomFunction para escribir una función personalizada y usarla en la hoja de cálculo para obtener los resultados. Definiremos una función personalizada por nombre.**MiFunc** que aceptará 2 parámetros con los siguientes detalles.

- El primer parámetro se refiere a una sola celda.
- El segundo parámetro se refiere a un rango de celdas.

La función personalizada agregará todos los valores del rango de celdas especificado como segundo parámetro y dividirá el resultado con el valor en el primer parámetro.

Así es como hemos implementado el método CalculateCustomFunction.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-UsingICustomFunctionfeature-ICustomFunction.cs" >}}


A continuación se explica cómo utilizar la función recién definida en una hoja de cálculo.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-UsingICustomFunctionfeature-UsingICustomFunctionFeature.cs" >}}
##  **Descripción general**
Las API Aspose.Cells simplemente colocan el objeto ReferedArea en "paramsList" cuando el parámetro correspondiente es una referencia o su resultado calculado es una referencia. Si necesita la referencia en sí, puede utilizar ReferedArea directamente. Si necesita obtener el valor de una sola celda de la referencia correspondiente a la posición de la fórmula, puede usar el método ReferedArea.GetValue(rowOffset, int colOffset). Si necesita una matriz de valores de celda para toda el área, puede usar el método ReferedArea.GetValues.

Como las API Aspose.Cells proporcionan el área referida en "paramsList", la colección ReferredAreaCollection en "contextObjects" ya no será necesaria (en versiones anteriores no era posible proporcionar siempre un mapa uno a uno a los parámetros de la función personalizada), por lo que se ha eliminado de los "contextObjects".

{{< highlight "java" >}}

 public object CalculateCustomFunction(string functionName, ArrayList paramsList, ArrayList contextObjects)

{

    ...

    object o = paramsList[i];

    if(o is ReferredArea) //fetch data from reference

    {

        ReferredArea ra = (ReferredArea)o;

        if(ra.IsArea)

        {

            o = ra.GetValues();

        }

        else

        {

            o = ra.GetValue(0, 0);

        }

    }

    if (o is Array)

    {

        ...

    }

    else if...

    ...

}

{{< /highlight >}}
