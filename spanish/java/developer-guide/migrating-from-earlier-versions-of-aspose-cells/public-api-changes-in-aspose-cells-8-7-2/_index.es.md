---
title: Público API Cambios en Aspose.Cells 8.7.2
type: docs
weight: 260
url: /es/java/public-api-changes-in-aspose-cells-8-7-2/
---
{{% alert color="primary" %}} 

Este documento describe los cambios al Aspose.Cells API de la versión 8.7.1 a la 8.7.2 que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo métodos públicos nuevos y actualizados, clases agregadas y eliminadas, etc., sino también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.Cells.

{{% /alert %}} 
## **API añadidas**
### **Extendió el motor de cálculo predeterminado**
Las API Aspose.Cells tienen un potente motor de cálculo que puede calcular casi todas las funciones Microsoft de Excel. Además, las API Aspose.Cells ahora permiten ampliar el motor de cálculo predeterminado para cumplir con los requisitos de cálculo personalizados de cualquier aplicación.

Se agregaron las siguientes API con el lanzamiento de Aspose.Cells for Java 8.7.2.

1. Clase AbstractCalculationEngine
1. Clase de datos de cálculo
1. Propiedad CalculationOptions.CustomEngine

{{% alert color="primary" %}} 

Las API mencionadas anteriormente permiten implementar un motor de cálculo personalizado para todas las funciones (incluidas las funciones nativas de Excel) con más flexibilidad.

{{% /alert %}} {{% alert color="primary" %}} 

 Para obtener más detalles sobre esta función, consulte el artículo detallado sobre[Implementación del motor de cálculo personalizado](/cells/es/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}} 

El siguiente es el escenario de uso simple.

**Java**

{{< highlight "csharp" >}}

 public class CustomEngine extends AbstractCalculationEngine

{

	public void calculate(CalculationData data)

        {

		if(data.getFunctionName().toUpperCase().equals("SUM")==true)

                {

                    double val = (double)data.getCalculatedValue();

                    val = val + 30;

                    data.setCalculatedValue(val);

                }

        }

}

{{< /highlight >}}
### **Indizador sobrecargado agregado para TextBoxCollection**
Aspose.Cells for Java 8.7.2 ha expuesto el indexador sobrecargado para la clase TextBoxCollection para acceder a la instancia de TextBox usando su nombre como String.

{{% alert color="primary" %}} 

 Para obtener más detalles sobre esta función, consulte el artículo detallado sobre[Acceder al cuadro de texto a través de su nombre](/cells/es/java/access-the-text-box-by-the-name/)

{{% /alert %}} 

 El escenario de uso simple se ve de la siguiente manera.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

Workbook workbook = new Workbook();

//Access the first Worksheet from the collection

Worksheet sheet = workbook.getWorksheets().get(0);

//Add a TextBox to the collection

int idx = sheet.getTextBoxes().add(10, 10, 10, 10);

//Access the TextBox using its index

TextBox box = sheet.getTextBoxes().get(idx);

//Set the name for the TextBox

box.setName("MyTextBox");

//Access the same TextBox via its name

box = sheet.getTextBoxes().get("MyTextBox");

{{< /highlight >}}
