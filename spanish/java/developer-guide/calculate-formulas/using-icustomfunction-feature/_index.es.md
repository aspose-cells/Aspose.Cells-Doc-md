---
title: Usando la función ICustomFunction
type: docs
weight: 890
url: /es/java/using-icustomfunction-feature/
---

{{% alert color="primary" %}} 

Este artículo proporciona una comprensión detallada de cómo usar la función ICustomFunction para implementar funciones personalizadas con las API de Aspose.Cells.

La interfaz ICustomFunction permite agregar funciones de cálculo de fórmulas personalizadas para extender el motor de cálculo básico de Aspose.Cells para satisfacer ciertos requisitos. Esta función es útil para definir funciones personalizadas en un archivo de plantilla o en código, donde la función personalizada puede ser implementada y evaluada utilizando las API de Aspose.Cells como cualquier otra función predeterminada de Microsoft Excel.

Ten en cuenta que esta interfaz ha sido reemplazada por [AbstractCalculationEngine](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine) y será eliminada en el futuro. Algunos artículos/ejemplos técnicos sobre la nueva API: [aquí](/cells/es/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/) y [aquí](/cells/es/java/returning-a-range-of-values-using-abstractcalculationengine/).

{{% /alert %}} {{% alert color="primary" %}} 

Si eres nuevo en las APIs Aspose.Cells for Java, por favor verifica [este](https://docs.aspose.com/cells/java/installation/) artículo para saber cómo puedes adquirir y hacer referencia a las Aspose.Cells for Java en tu proyecto.

{{% /alert %}} 
## **Creación y evaluación de una función definida por el usuario**
Este artículo demuestra la implementación de la interfaz ICustomFunction para escribir una función personalizada y usarla en la hoja de cálculo para obtener los resultados. Definiremos una función personalizada llamada **MyFunc** que aceptará 2 parámetros con los detalles siguientes.

- El primer parámetro se refiere a una sola celda
- El segundo parámetro se refiere a un rango de celdas

La función personalizada sumará todos los valores del rango de celdas especificado como segundo parámetro y dividirá el resultado por el valor del primer parámetro.

Aquí está cómo hemos implementado el método calculateCustomFunction.

**Java**

{{< highlight csharp >}}

 public class CustomFunction implements ICustomFunction

{

    @Override

    public Object calculateCustomFunction(String functionName, java.util.ArrayList paramsList, java.util.ArrayList contextObjects)

    {

        double result = 0f;

        double sum = 0;

        //Get the value of 1st parameter

        Object firstParamB1 = paramsList.get(0);

        if (firstParamB1 instanceof ReferredArea)

        {

            ReferredArea ra = (ReferredArea)firstParamB1;

            firstParamB1 = ra.getValue(0, 0);

        }

        //Get values of 2nd parameter

        Object secondParamC1C5 = paramsList.get(1);

        if (secondParamC1C5 instanceof ReferredArea)

        {

            ReferredArea ra = (ReferredArea)secondParamC1C5;

            for (int i = ra.getStartRow(); i <= ra.getEndRow(); i++)

            {

                //Add all values

                sum += (double)ra.getValue(i, 0);

            }

        }

        result = sum / (double)firstParamB1;

        // Return result of the function

        return result;

    }

}

{{< /highlight >}}

Así es como se utiliza la función recién definida en una hoja de cálculo

**Java**

{{< highlight csharp >}}

 //Open the workbook

Workbook workbook = new Workbook();

//Obtaining the reference of the first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Adding a sample value to "A1" cell

worksheet.getCells().get("B1").putValue(5);

//Adding a sample value to "A2" cell

worksheet.getCells().get("C1").putValue(100);

//Adding a sample value to "A3" cell

worksheet.getCells().get("C2").putValue(150);

//Adding a sample value to "B1" cell

worksheet.getCells().get("C3").putValue(60);

//Adding a sample value to "B2" cell

worksheet.getCells().get("C4").putValue(32);

//Adding a sample value to "B2" cell

worksheet.getCells().get("C5").putValue(62);

//Adding custom formula to Cell A1

worksheet.getCells().get("A1").setFormula("=MyFunc(B1,C1:C5)");

//Calcualating Formulas

workbook.calculateFormula(false, new CustomFunction());

//Assign resultant value to Cell A1

worksheet.getCells().get("A1").putValue(worksheet.getCells().get("A1").getValue());

//Save the file

workbook.save(dir + "UsingICustomFunction.xls");

{{< /highlight >}}
## **Visión general**
Las API de Aspose.Cells simplemente colocan el objeto ReferredArea en la "paramsList" cuando el parámetro correspondiente es una referencia o su resultado calculado es una referencia. Si necesita la referencia en sí, puede usar directamente ReferredArea. Si necesita obtener el valor de una sola celda de la referencia correspondiente a la posición de la fórmula, puede usar el método ReferredArea.getValue(rowOffset, colOffset). Si necesita un array de valores de celdas para toda la área, puede usar el método ReferredArea.getValues.

Como las API de Aspose.Cells dan ReferredArea en "paramsList", la ReferredAreaCollection en "contextObjects" ya no será necesaria (en las versiones antiguas no siempre podía dar un mapeo uno a uno a los parámetros de la función personalizada) por lo tanto se ha eliminado de los "contextObjects".

{{< highlight java >}}

 public Object calculateCustomFunction(String functionName, ArrayList paramsList, ArrayList contextObjects)

{

    ...

    Object o = paramsList.get(i);

    if(o is ReferredArea) //fetch data from reference

    {

        ReferredArea ra = (ReferredArea)o;

        if(ra.isArea())

        {

            o = ra.getValues();

        }

        else

        {

            o = ra.getValue(0, 0);

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
