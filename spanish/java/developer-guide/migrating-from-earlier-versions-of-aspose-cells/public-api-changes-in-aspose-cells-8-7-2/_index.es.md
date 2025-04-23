---
title: Cambios en la API pública en Aspose.Cells 8.7.2
type: docs
weight: 260
url: /es/java/public-api-changes-in-aspose-cells-8-7-2/
---

{{% alert color="primary" %}} 

Este documento describe los cambios en la API de Aspose.Cells desde la versión 8.7.1 hasta la 8.7.2 que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo nuevos y actualizados métodos públicos, clases agregadas y eliminadas, etc., sino también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.Cells.

{{% /alert %}} 
## **APIs Añadidas**
### **Extendido el Motor de Cálculo Predeterminado**
Las APIs de Aspose.Cells tienen un potente motor de cálculo que puede calcular casi todas las funciones de Microsoft Excel. Además, las APIs de Aspose.Cells ahora permiten extender el motor de cálculo predeterminado para satisfacer los requisitos de cálculo personalizados de cualquier aplicación.

Las siguientes APIs se han agregado con el lanzamiento de Aspose.Cells for Java 8.7.2.

1. Clase AbstractCalculationEngine
1. Clase CalculationData
1. Propiedad CalculationOptions.CustomEngine

{{% alert color="primary" %}} 

Las APIs mencionadas anteriormente permiten implementar un motor de cálculo personalizado para todas las funciones (incluidas las funciones nativas de Excel) con más flexibilidad.

{{% /alert %}} {{% alert color="primary" %}} 

Para obtener más detalles sobre esta función, por favor revise el artículo detallado sobre [Implementar Motor de Cálculo Personalizado](/cells/es/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}} 

A continuación se muestra un escenario de uso simple.

**Java**

{{< highlight csharp >}}

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
### **Añadido Indexador Sobrecargado para TextBoxCollection**
Aspose.Cells for Java 8.7.2 ha expuesto el indexador sobrecargado para la clase TextBoxCollection para acceder a la instancia de TextBox utilizando su nombre como String.

{{% alert color="primary" %}} 

Para obtener más detalles sobre esta función, por favor revise el artículo detallado sobre [Acceder al TextBox por su Nombre](/cells/es/java/access-the-text-box-by-the-name/)

{{% /alert %}} 

Un escenario de uso simple se ve como sigue. 

**Java**

{{< highlight csharp >}}

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
{{< app/cells/assistant language="java" >}}
