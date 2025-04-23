---
title: Cambios en la API pública en Aspose.Cells 8.2.1
type: docs
weight: 90
url: /es/java/public-api-changes-in-aspose-cells-8-2-1/
---

{{% alert color="primary" %}} 

Este documento describe los cambios en la API de Aspose.Cells desde la versión 8.2.0 hasta la 8.2.1, que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo métodos públicos nuevos y actualizados, sino también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.Cells.

{{% /alert %}} 
## **Se agregó el método getValidation() para la clase Cell**
La validación de datos es una de las funciones que los diseñadores de hojas de cálculo utilizan para evitar que los usuarios inserten valores no válidos en una celda específica. Con Aspose.Cells for Java 8.2.1, la API ha expuesto un mecanismo simple que identifica si se ha aplicado una validación de datos a una celda. Utilice el método getValidation de la clase Cell para adquirir cualquier validación aplicada. Si no hay validación, el método devuelve null. De manera similar, puede usar el método getValidationInCell de la clase ValidationCollection para adquirir la validación aplicada a cualquier celda al proporcionar sus índices de fila y columna.

{{% alert color="primary" %}} 

Por favor, consulte el artículo detallado sobre [Obtener la validación aplicada a una celda](https://docs.aspose.com/cells/java/get-validation-applied-on-a-cell/) para obtener más información.

{{% /alert %}}
## **Se agregó el método getValidationValue() para la clase Cell**
Además de determinar si se ha aplicado una validación, también puede verificar si un valor dado satisface las reglas de validación de datos para una celda en particular. Esta función es útil en escenarios en los que desea verificar si el valor introducido en la celda satisface las reglas de validación de datos sobre la marcha. La API de Aspose.Cells ha expuesto el método getValidationValue para la clase Cell. Si el valor introducido en una celda no satisface las reglas de validación de datos, el método getValidationValue para la clase Cell devuelve falso.

{{% alert color="primary" %}} 

Por favor, consulte el artículo detallado sobre [Verificar que el valor de la celda satisface las reglas de validación de datos](/cells/es/java/verify-that-cell-value-satisfies-data-validation-rules/) para obtener más información.

{{% /alert %}}
## **Se agregó la sobrecarga del método toPrinter(PrinterSettings printerSettings) para la clase WorkbookRender**
Puede utilizar el método sobrecargado para renderizar el libro de trabajo a una impresora a través de PrinterSettings.
{{< app/cells/assistant language="java" >}}
