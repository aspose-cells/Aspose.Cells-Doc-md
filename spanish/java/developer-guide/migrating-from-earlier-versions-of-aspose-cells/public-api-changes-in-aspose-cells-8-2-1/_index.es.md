---
title: Público API Cambios en Aspose.Cells 8.2.1
type: docs
weight: 90
url: /es/java/public-api-changes-in-aspose-cells-8-2-1/
---
{{% alert color="primary" %}} 

Este documento describe los cambios al Aspose.Cells API de la versión 8.2.0 a la 8.2.1, que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo métodos públicos nuevos y actualizados, sino también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.Cells.

{{% /alert %}} 
## **Se agregó el método getValidation () para la clase Cell**
La validación de datos es una de las funciones que utilizan los diseñadores de hojas de cálculo para evitar que los usuarios inserten valores no válidos en una celda en particular. Con Aspose.Cells for Java 8.2.1, el API ha expuesto un mecanismo simple que identifica si se ha aplicado la validación de datos en una celda. Utilice el método getValidation de la clase Cell para adquirir cualquier validación aplicada. Si no hay validación, el método devuelve nulo. De manera similar, puede usar el método getValidationInCell de la clase ValidationCollection para adquirir la validación aplicada en cualquier celda proporcionando sus índices de fila y columna.

{{% alert color="primary" %}} 

 Consulte el artículo detallado sobre[Obtenga la validación aplicada en un Cell](https://docs.aspose.com/cells/java/get-validation-applied-on-a-cell/) para más información.

{{% /alert %}}
## **Se agregó el método getValidationValue() para la clase Cell**
Además de determinar si se ha aplicado la validación, también puede verificar si un valor dado cumple con las reglas de validación de datos para una celda en particular. Esta característica es útil en escenarios en los que desea verificar si el valor ingresado en la celda cumple con las reglas de validación de datos sobre la marcha. El Aspose.Cells API ha expuesto el método getValidationValue para la clase Cell. Si el valor ingresado en una celda no cumple con las reglas de validación de datos, el método getValidationValue para la clase Cell devuelve falso.

{{% alert color="primary" %}} 

 Consulte el artículo detallado sobre[Verifique que el valor Cell cumpla con las reglas de validación de datos](/cells/es/java/verify-that-cell-value-satisfies-data-validation-rules/).

{{% /alert %}}
## **Se agregó sobrecarga al método Printer(PrinterSettings printerSettings) para la clase WorkbookRender**
Puede usar el método sobrecargado para representar el libro de trabajo en la impresora a través de PrinterSettings.
