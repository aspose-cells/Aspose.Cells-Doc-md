---
title: Público API Cambios en Aspose.Cells 8.7.2
type: docs
weight: 250
url: /es/net/public-api-changes-in-aspose-cells-8-7-2/
---
{{% alert color="primary" %}} 

Este documento describe los cambios al Aspose.Cells API de la versión 8.7.1 a la 8.7.2 que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo métodos públicos nuevos y actualizados, clases agregadas y eliminadas, etc., sino también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.Cells.

{{% /alert %}} 
## **API añadidas**
### **Extendió el motor de cálculo predeterminado**
Las API Aspose.Cells tienen un potente motor de cálculo que puede calcular casi todas las funciones Microsoft de Excel. Además, las API Aspose.Cells ahora permiten ampliar el motor de cálculo predeterminado para cumplir con los requisitos de cálculo personalizados de cualquier aplicación.

Se agregaron las siguientes API con el lanzamiento de Aspose.Cells for .NET 8.7.2.

1. Clase AbstractCalculationEngine
1. Clase de datos de cálculo
1. Propiedad CalculationOptions.CustomEngine

{{% alert color="primary" %}} 

Las API mencionadas anteriormente permiten implementar un motor de cálculo personalizado para todas las funciones (incluidas las funciones nativas de Excel) con más flexibilidad.

{{% /alert %}} {{% alert color="primary" %}} 

 Para obtener más detalles sobre esta función, consulte el artículo detallado sobre[Implementación del motor de cálculo personalizado](/cells/es/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}} 

El siguiente es el escenario de uso simple.

**C#**

{{< highlight "csharp" >}}

 public class MyEngine : AbstractCalculationEngine

{

    public override void Calculate(CalculationData data)

    {

        string funcName = data.FunctionName.ToUpper();

        if ("MYFUNC".Equals(funcName))

        {

            //do calculation for MYFUNC here

            int count = data.ParamCount;

            object res = null;

            for (int i = 0; i < count; i++)

            {

                object pv = data.GetParamValue(i);

                if (pv is ReferredArea)

                {

                    ReferredArea ra = (ReferredArea)pv;

                    pv = ra.GetValue(0, 0);

                }

                //process the parameter here

                //res = ...;

            }

            data.CalculatedValue = res;

        }

    }

}

{{< /highlight >}}


### **Indizador sobrecargado agregado para TextBoxCollection**
Aspose.Cells for .NET 8.7.2 ha expuesto el índice sobrecargado para la clase TextBoxCollection para acceder a la instancia de TextBox usando su nombre como cadena.

{{% alert color="primary" %}} 

 Para obtener más detalles sobre esta función, consulte el artículo detallado sobre[Acceder al cuadro de texto a través de su nombre](/cells/es/net/access-the-text-box-by-the-name/)

{{% /alert %}} 

El escenario de uso simple se ve de la siguiente manera.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

Workbook workbook = new Workbook();

//Access the first Worksheet from the collection

Worksheet sheet = workbook.Worksheets[0];

//Add a TextBox to the collection

int idx = sheet.TextBoxes.Add(10, 10, 10, 10);

//Access the TextBox using its index

TextBox box = sheet.TextBoxes[idx];

//Set the name for the TextBox

box.Name = "MyTextBox";

//Access the same TextBox via its name

box = sheet.TextBoxes["MyTextBox"];

{{< /highlight >}}


### **Se agregó el evento OnAfterColumnFilter para GridWeb**
Aspose.Cells.GridWeb for .NET 8.7.2 ha expuesto el evento OnAfterColumnFilter que sirve como devolución de llamada al mecanismo de filtrado realizado a través de la interfaz de usuario Aspose.Cells.GridWeb. Como sugiere el nombre, el evento se activa después de que se aplica el filtrado de columnas y se puede usar para obtener la información de filtrado, como el índice de columna en el que se aplicó el filtro y el valor de filtro seleccionado.

El escenario de uso simple se ve de la siguiente manera.

**C#**

{{< highlight "csharp" >}}

 protected void GridWeb1_AfterColumnFilter(object sender, Aspose.Cells.GridWeb.RowColumnEventArgs e)

{

    string msg = "Column index: " + (e.Num) + ", Filtered Value:" + e.Argument;

}

{{< /highlight >}}

{{% alert color="primary" %}} 

No olvide registrar el evento en el control GridWeb<acw:gridweb OnAfterColumnFilter="GridWeb1_AfterColumnFilter"/>

{{% /alert %}}
