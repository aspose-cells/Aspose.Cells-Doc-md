---
title: Cambios en la API pública en Aspose.Cells 8.2.1
type: docs
weight: 80
url: /es/net/public-api-changes-in-aspose-cells-8-2-1/
---

{{% alert color="primary" %}} 

Este documento describe los cambios en la API de Aspose.Cells desde la versión 8.2.0 hasta la 8.2.1, que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo métodos públicos nuevos y actualizados, sino también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.Cells.

{{% /alert %}} 
## **Se agregó el método GetValidation() para la clase Cell**
La validación de datos es una de las características que los diseñadores de hojas de cálculo utilizan para evitar que los usuarios inserten valores no válidos en una celda específica. Con Aspose.Cells for .NET 8.2.1, la API ha expuesto un mecanismo simple que identifica si se ha aplicado validación de datos a una celda. Utilice el método GetValidation de la clase Cell para adquirir cualquier validación aplicada. Si no hay validación, el método devuelve null. Del mismo modo, puede utilizar el método GetValidationInCell de la clase ValidationCollection para adquirir la validación aplicada en cualquier celda proporcionando sus índices de fila y columna.

{{% alert color="primary" %}} 

Consulte el artículo detallado sobre [Obtener Validación Aplicada en una Celda](/cells/es/net/get-validation-applied-on-a-cell/) para obtener más información.

{{% /alert %}}
## **Se agregó el método GetValidationValue() para la clase Cell**
Además de determinar si se ha aplicado validación, también se puede verificar si un valor dado cumple con las reglas de validación de datos para una celda específica. Esta función es útil en escenarios en los que se desea verificar si el valor introducido en la celda cumple con las reglas de validación de datos sobre la marcha. La API Aspose.Cells ha expuesto el método GetValidationValue para la clase Cell. Si el valor introducido en una celda no cumple con las reglas de validación de datos, el método GetValidationValue para la clase Cell devuelve false.

{{% alert color="primary" %}} 

Consulte el artículo detallado sobre [Verificar que el Valor de la Celda Cumple con las Reglas de Validación de Datos](/cells/es/net/verify-that-cell-value-satisfies-data-validation-rules/).

{{% /alert %}}
## **Se agregó el método de sobrecarga ToPrinter(PrinterSettings printerSettings) para la clase WorkbookRender**
Puede utilizar el método sobrecargado para renderizar el libro de trabajo a una impresora a través de PrinterSettings.
