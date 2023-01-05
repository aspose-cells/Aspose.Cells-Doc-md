---
title: Uso de la función ICustomFunction
type: docs
weight: 30
url: /es/net/using-icustomfunction-feature/
---
{{% alert color="primary" %}} 

Este artículo proporciona una comprensión detallada de cómo usar la función ICustomFunction para implementar funciones personalizadas con las API Aspose.Cells.

La interfaz ICustomFunction permite agregar funciones de cálculo de fórmulas personalizadas para ampliar el motor de cálculo central Aspose.Cells para cumplir con ciertos requisitos. Esta característica es útil para definir funciones personalizadas (definidas por el usuario) en un archivo de plantilla o en un código donde la función personalizada se puede implementar y evaluar utilizando las API Aspose.Cells como cualquier otra función de Excel predeterminada Microsoft.

{{% /alert %}} 
## **Crear y evaluar una función definida por el usuario**
Este artículo demuestra la implementación de la interfaz ICustomFunction para escribir una función personalizada y usarla en la hoja de cálculo para obtener los resultados. Definiremos una función personalizada por nombre**MiFunc** que aceptará 2 parámetros con los siguientes detalles.

- El primer parámetro se refiere a una sola celda.
- El segundo parámetro se refiere a un rango de celdas.

La función personalizada agregará todos los valores del rango de celdas especificado como segundo parámetro y dividirá el resultado con el valor en el primer parámetro.

Así es como hemos implementado el método CalculateCustomFunction.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-UsingICustomFunctionfeature-ICustomFunction.cs" >}}


Aquí se explica cómo usar la función recién definida en una hoja de cálculo



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-UsingICustomFunctionfeature-UsingICustomFunctionFeature.cs" >}}
## **Descripción general**
Las API Aspose.Cells simplemente colocan el objeto ReferedArea en "paramsList" cuando el parámetro correspondiente es una referencia o su resultado calculado es una referencia. Si necesita la referencia en sí, puede usar ReferedArea directamente. Si necesita obtener el valor de una sola celda de la referencia correspondiente a la posición de la fórmula, puede usar el método ReferedArea.GetValue(rowOffset, int colOffset). Si necesita una matriz de valores de celda para toda el área, puede usar el método ReferedArea.GetValues.

Como las API Aspose.Cells brindan el área referida en "paramsList", la colección ReferredAreaCollection en "contextObjects" ya no será necesaria (en versiones anteriores, no siempre podía proporcionar un mapa uno a uno a los parámetros de la función personalizada), por lo tanto, ha sido eliminado de los "contextObjects".

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
