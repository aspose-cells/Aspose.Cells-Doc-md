---
title: Cambios en la API Pública en Aspose.Cells 8.1.1
type: docs
weight: 60
url: /es/java/public-api-changes-in-aspose-cells-8-1-1/
---

{{% alert color="primary" %}} 

Este documento describe los cambios en la API de Aspose.Cells desde la versión 8.1.0 hasta la 8.1.1, que pueden ser de interés para los desarrolladores de módulos y aplicaciones. Incluye no solo [nuevos y actualizados métodos públicos](/cells/es/java/public-api-changes-in-aspose-cells-8-1-1/), sino también una descripción de cualquier [cambio en el comportamiento](/cells/es/java/public-api-changes-en-aspose-cells-8-1-1/) detrás de escena en Aspose.Cells.

{{% /alert %}} 
## **Propiedades y Características Agregadas**
### **Agregada la Propiedad HtmlSaveOptions.PresentationPreference**
La clase HtmlSaveOptions ha expuesto getter/setter para la propiedad PresentationPreference la cual puede ser utilizada para renderizar los resultados con un mejor diseño al exportar hojas de cálculo a HTML o MHTML. El valor predeterminado es false. mientras que si se establece en true, la API de Aspose.Cells exporta el contenido de la hoja de cálculo con una mejor presentación.

{{% alert color="primary" %}} 

Por favor consulte el artículo detallado sobre [Utilizar la Opción PresentationPreference para un Mejor Diseño](/cells/es/java/excel-to-html-use-presentationpreference-option-for-better-layout/)

{{% /alert %}} 
### **Soporte Agregado para Escenarios de Hoja de Cálculo**
Un escenario es un modelo de suposición que incluye celdas de entrada variables vinculadas por una o más fórmulas. Aspose.Cells ha expuesto un getter y setter para la propiedad Worksheet.Scenarios junto con las siguientes clases para ayudar a los desarrolladores a crear, manipular y eliminar escenarios.

1. Escenario: Representa un escenario individual.
1. Colección de escenarios: Representa una colección de escenarios.
1. Colección de celdas de entrada de escenarios: Representa una lista de celdas de entrada para un escenario particular.
1. Celda de entrada de escenario: Representa una celda de entrada de la colección de celdas de entrada para un escenario particular.

{{% alert color="primary" %}} 

Consulte el artículo detallado sobre [Cómo crear, manipular o eliminar escenarios de hojas de cálculo](/cells/es/java/create-manipulate-or-remove-scenarios-from-worksheets/).

{{% /alert %}}
## **Cambios en el comportamiento para CellsException**
Con versiones anteriores de la API Aspose.Cells for Java, cuando se cargaba una hoja de cálculo posiblemente dañada en una instancia de Workbook, la API solía lanzar un mensaje genérico sin mencionar dónde podría estar el problema. Hemos cambiado este comportamiento para 8.1.1 para que la API lance una excepción con un mensaje significativo que señala dónde (qué celda) y qué (expresión de fórmula) causa la excepción al leer el archivo de plantilla.
