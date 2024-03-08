---
title: Uso de la función ICustomFunction
type: docs
weight: 890
url: /es/java/using-icustomfunction-feature/
---
{{% alert color="primary" %}} 

Este artículo proporciona una comprensión detallada de cómo utilizar la característica ICustomFunction para implementar funciones personalizadas con las API Aspose.Cells.

La interfaz ICustomFunction permite agregar funciones de cálculo de fórmulas personalizadas para ampliar el motor de cálculo principal Aspose.Cells para cumplir con ciertos requisitos. Esta característica es útil para definir funciones personalizadas (definidas por el usuario) en un archivo de plantilla o en código donde la función personalizada se puede implementar y evaluar utilizando Aspose.Cells API como cualquier otra función predeterminada de Excel Microsoft.

 Tenga en cuenta que esta interfaz ha sido reemplazada por[ResumenCálculoMotor](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine) será eliminado en el futuro. Algunos artículos/ejemplos técnicos sobre el nuevo API:[aquí](/cells/es/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/) y[aquí](/cells/es/java/returning-a-range-of-values-using-abstractcalculationengine/)

{{% /alert %}} {{% alert color="primary" %}} 

 Si es nuevo en las API Aspose.Cells for Java, verifique[este](https://docs.aspose.com/cells/java/installation/) artículo para saber cómo puedes adquirir y hacer referencia al Aspose.Cells for Java en tu proyecto.

{{% /alert %}} 
##  **Crear y evaluar una función definida por el usuario**
 Este artículo demuestra la implementación de la interfaz ICustomFunction para escribir una función personalizada y usarla en la hoja de cálculo para obtener los resultados. Definiremos una función personalizada por nombre.**MiFunc** que aceptará 2 parámetros con los siguientes detalles.

- El primer parámetro se refiere a una sola celda.
- El segundo parámetro se refiere a un rango de celdas.

La función personalizada agregará todos los valores del rango de celdas especificado como segundo parámetro y dividirá el resultado con el valor en el primer parámetro.

Así es como hemos implementado el método calcularCustomFunction.

**Java**

{{< highlight "csharp" >}}

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

A continuación se explica cómo utilizar la función recién definida en una hoja de cálculo.

**Java**

{{< highlight "csharp" >}}

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
##  **Descripción general**
Las API Aspose.Cells simplemente colocan el objeto ReferedArea en "paramsList" cuando el parámetro correspondiente es una referencia o su resultado calculado es una referencia. Si necesita la referencia en sí, puede utilizar ReferedArea directamente. Si necesita obtener el valor de una sola celda de la referencia correspondiente a la posición de la fórmula, puede usar el método ReferedArea.getValue(rowOffset, int colOffset). Si necesita una matriz de valores de celda para toda el área, puede usar el método ReferedArea.getValues.

Como las API Aspose.Cells proporcionan el área referida en "paramsList", la colección ReferredAreaCollection en "contextObjects" ya no será necesaria (en versiones anteriores no era posible proporcionar siempre un mapa uno a uno a los parámetros de la función personalizada), por lo que se ha eliminado de los "contextObjects".

{{< highlight "java" >}}

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
