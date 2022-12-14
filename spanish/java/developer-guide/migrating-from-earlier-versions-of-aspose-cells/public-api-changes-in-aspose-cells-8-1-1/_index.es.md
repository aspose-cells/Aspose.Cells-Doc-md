---
title: Público API Cambios en Aspose.Cells 8.1.1
type: docs
weight: 60
url: /es/java/public-api-changes-in-aspose-cells-8-1-1/
---
{{% alert color="primary" %}} 

Este documento describe los cambios al Aspose.Cells API de la versión 8.1.0 a la 8.1.1, que pueden ser de interés para los desarrolladores de módulos y aplicaciones. Incluye no solo[métodos públicos nuevos y actualizados](/cells/es/java/public-api-changes-in-aspose-cells-8-1-1/) , sino también una descripción de cualquier[cambios en el comportamiento](/cells/es/java/public-api-changes-in-aspose-cells-8-1-1/) detrás de escena en Aspose.Cells.

{{% /alert %}} 
## **Propiedades y funciones añadidas**
### **Se agregó la propiedad HtmlSaveOptions.PresentationPreference**
La clase HtmlSaveOptions ha expuesto getter/setter para la propiedad PresentationPreference que se puede usar para representar los resultados con un mejor diseño al exportar hojas de cálculo a HTML o MHTML. El valor predeterminado es falso. mientras que si se establece en verdadero, el Aspose.Cells API exporta el contenido de la hoja de trabajo con una mejor presentación.

{{% alert color="primary" %}} 

 Consulte el artículo detallado sobre[Use la opción PresentationPreference para un mejor diseño](/cells/es/java/excel-to-html-use-presentationpreference-option-for-better-layout/)

{{% /alert %}} 
### **Soporte agregado para escenarios de hojas de trabajo**
Un escenario es un modelo hipotético que incluye celdas de entrada de variables unidas por una o más fórmulas. Aspose.Cells ha expuesto un getter y setter para la propiedad Worksheet.Scenarios junto con las siguientes clases para ayudar a los desarrolladores a crear, manipular y eliminar escenarios.

1. Escenario: Representa un escenario individual.
1. ScenarioCollection: Representa una colección de escenarios.
1. ScenarioInputCellCollection: representa una lista de celdas de entrada para un escenario particular.
1. ScenarioInputCell: Representa una celda de entrada de la colección de celdas de entrada para un escenario particular.

{{% alert color="primary" %}} 

 Consulte el artículo detallado sobre[Cómo crear, manipular o eliminar escenarios de las hojas de trabajo](/cells/es/java/create-manipulate-or-remove-scenarios-from-worksheets/).

{{% /alert %}}
## **Cambio en el comportamiento de CellsException**
Con versiones anteriores de Aspose.Cells for Java API, cuando se cargaba una hoja de cálculo posiblemente dañada en una instancia de Workbook, API tendía a mostrar un mensaje genérico sin mencionar dónde podría estar el problema. Hemos cambiado este comportamiento para 8.1.1 para que API arroje una excepción con un mensaje significativo que indique dónde (qué celda) y qué (expresión de fórmula) causa la excepción al leer el archivo de plantilla.
