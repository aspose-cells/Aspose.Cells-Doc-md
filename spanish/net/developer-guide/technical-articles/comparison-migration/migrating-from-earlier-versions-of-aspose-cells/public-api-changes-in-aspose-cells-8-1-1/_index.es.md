---
title: Público API Cambios en Aspose.Cells 8.1.1
type: docs
weight: 50
url: /es/net/public-api-changes-in-aspose-cells-8-1-1/
---
{{% alert color="primary" %}} 

Este documento describe los cambios al Aspose.Cells API de la versión 8.1.0 a la 8.1.1, que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo métodos públicos nuevos y actualizados, sino también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.Cells.

{{% /alert %}} 
## **Se agregó la propiedad HtmlSaveOptions.PresentationPreference**
La clase HtmlSaveOptions ha expuesto la propiedad PresentationPreference que se puede usar para representar los resultados con un mejor diseño al exportar hojas de cálculo a HTML o MHTML. El valor predeterminado es falso. mientras que si se establece en verdadero, el Aspose.Cells API exportará el contenido de la hoja de trabajo con una mejor presentación.

{{% alert color="primary" %}} 

 Consulte el artículo detallado sobre[Use la opción PresentationPreference para un mejor diseño](/cells/es/net/excel-to-html-use-presentationpreference-option-for-better-layout/)

{{% /alert %}}
## **Soporte agregado para escenarios de hojas de trabajo**
 Un escenario se denomina modelo hipotético e incluye celdas de entrada de variables unidas entre sí por una o más fórmulas según corresponda. Aspose.Cells API ha expuesto la propiedad Worksheet.Scenarios junto con las siguientes clases para facilitar a los usuarios la creación, manipulación y eliminación de escenarios de las hojas de trabajo,

1. Escenario: Representa un escenario individual.
1. ScenarioCollection: Representa una colección de escenarios.
1. ScenarioInputCellCollection: representa una lista de celdas de entrada para un escenario en particular.
1. ScenarioInputCell: Representa una celda de entrada de la colección de celdas de entrada para un escenario particular.

{{% alert color="primary" %}} 

 Consulte el artículo detallado sobre[Cómo crear, manipular o eliminar escenarios de las hojas de trabajo](/cells/es/net/create-manipulate-or-remove-scenarios-from-worksheets/).

{{% /alert %}}
