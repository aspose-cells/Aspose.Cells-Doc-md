---
title: Cambios en la API Pública en Aspose.Cells 8.1.1
type: docs
weight: 50
url: /es/net/public-api-changes-in-aspose-cells-8-1-1/
---

{{% alert color="primary" %}} 

Este documento describe los cambios en la API de Aspose.Cells desde la versión 8.1.0 hasta la 8.1.1, que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo métodos públicos nuevos y actualizados, sino también una descripción de cualquier cambio en el comportamiento entre bastidores en Aspose.Cells.

{{% /alert %}} 
## **Añadida la propiedad PresentationPreference de HtmlSaveOptions**
La clase HtmlSaveOptions ha expuesto la propiedad PresentationPreference, que se puede utilizar para renderizar los resultados con un diseño mejor al exportar hojas de cálculo a HTML o MHTML. El valor predeterminado es falso. Mientras que si se establece en verdadero, la API de Aspose.Cells exportará el contenido de la hoja de cálculo con una mejor presentación.

{{% alert color="primary" %}} 

Consulte el artículo detallado sobre [Usar la opción PresentationPreference para obtener un mejor diseño](/cells/es/net/excel-to-html-use-presentationpreference-option-for-better-layout/)

{{% /alert %}}
## **Soporte Agregado para Escenarios de Hoja de Cálculo**
Un escenario es un modelo de supuestos que incluye celdas de entrada variables vinculadas por una o más fórmulas, según corresponda. La API de Aspose.Cells ha expuesto la propiedad Worksheet.Scenarios junto con las siguientes clases para facilitar a los usuarios la creación, manipulación y eliminación de escenarios de hojas de cálculo, 

1. Escenario: Representa un escenario individual.
1. Colección de escenarios: Representa una colección de escenarios.
1. ScenarioInputCellCollection: Representa una lista de celdas de entrada para un escenario particular.
1. ScenarioInputCell: Representa una celda de entrada de la colección de celdas de entrada para un escenario particular.

{{% alert color="primary" %}} 

Consulte el artículo detallado sobre [Cómo crear, manipular o eliminar escenarios de hojas de cálculo](/cells/es/net/create-manipulate-or-remove-scenarios-from-worksheets/)

{{% /alert %}}
