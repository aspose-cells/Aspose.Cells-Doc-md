---
title: Usando la función ICustomFunction
description: Este artículo describe cómo crear una función personalizada en Microsoft Excel usando la función ICustomFunction en la librería Aspose.Cells. Al cargar un archivo de Excel existente o crear uno nuevo, podemos usar los métodos proporcionados por Aspose.Cells para definir y registrar funciones personalizadas y obtener los resultados. Finalmente, guardamos el archivo de Excel modificado en el disco.
keywords: Aspose.Cells, Excel, funciones personalizadas ICustomFunction
type: docs
weight: 30
url: /es/net/using-icustomfunction-feature/
---

{{% alert color="primary" %}} 

Este artículo proporciona una comprensión detallada de cómo usar la función ICustomFunction para implementar funciones personalizadas con las API de Aspose.Cells.

La interfaz ICustomFunction permite agregar funciones de cálculo de fórmulas personalizadas para extender el motor de cálculo básico de Aspose.Cells para satisfacer ciertos requisitos. Esta función es útil para definir funciones personalizadas en un archivo de plantilla o en código, donde la función personalizada puede ser implementada y evaluada utilizando las API de Aspose.Cells como cualquier otra función predeterminada de Microsoft Excel.

Ten en cuenta que esta interfaz ha sido reemplazada por [AbstractCalculationEngine](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine/) y será eliminada en el futuro. Algunos artículos/ejemplos técnicos sobre la nueva API: [aquí](/cells/es/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/) y [aquí](/cells/es/net/returning-a-range-of-values-using-abstractcalculationengine/)

{{% /alert %}} 
## **Creación y evaluación de una función definida por el usuario**
Este artículo demuestra la implementación de la interfaz ICustomFunction para escribir una función personalizada y usarla en la hoja de cálculo para obtener los resultados. Definiremos una función personalizada llamada **MyFunc** que aceptará 2 parámetros con los detalles siguientes.

- El primer parámetro se refiere a una sola celda
- El segundo parámetro se refiere a un rango de celdas

La función personalizada sumará todos los valores del rango de celdas especificado como segundo parámetro y dividirá el resultado por el valor del primer parámetro.

Así es como hemos implementado el método CalculateCustomFunction.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-UsingICustomFunctionfeature-ICustomFunction.cs" >}}


Así es como se utiliza la función recién definida en una hoja de cálculo



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-UsingICustomFunctionfeature-UsingICustomFunctionFeature.cs" >}}
## **Visión general**
Las API de Aspose.Cells simplemente colocan el objeto ReferredArea en la "paramsList" cuando el parámetro correspondiente es una referencia o su resultado calculado es una referencia. Si necesita la referencia en sí, puede usar directamente ReferredArea. Si necesita obtener el valor de una sola celda de la referencia correspondiente con la posición de la fórmula, puede usar el método ReferredArea.GetValue(filaOffset, int colOffset). Si necesita un array de valores de celda para toda el área, entonces puede usar ReferredArea.GetValues método.

Como las API de Aspose.Cells dan ReferredArea en "paramsList", la ReferredAreaCollection en "contextObjects" ya no será necesaria (en las versiones antiguas no siempre podía dar un mapeo uno a uno a los parámetros de la función personalizada) por lo tanto se ha eliminado de los "contextObjects".

{{< highlight java >}}

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
