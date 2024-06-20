---
title: Filtrado de Datos
type: docs
weight: 100
url: /es/net/aspose-cells-griddesktop/filtering-data/
keywords: GridDesktop, filtrar, filtrar datos, AutoFiltro, Filtro de Filas
description: Este artículo presenta cómo filtrar datos en el Archivo de trabajo en GridDesktop.
---

{{% alert color="primary" %}} 

**Aspose.Cells.GridDesktop** proporciona funciones de Autofilrado y Filtro de Datos Personalizados para los usuarios. Utilizando estas funciones, puede encontrar una forma de seleccionar solo los elementos de la hoja de trabajo que desee mostrar en una lista. Además, se le permite filtrar elementos en una lista de acuerdo con un criterio establecido. Puede filtrar texto, números o fechas con la función de AutoFiltrado / Filtro de Datos Personalizado.

Puede utilizar el atributo booleano **EnableAutoFilter** de la clase **RowFilterSettings** para habilitar la función de AutoFiltrado para el control GridDesktop. Hay algunas otras propiedades de la clase que puede usar, como **HeaderRow**, **StartRow** y **EndRow** para especificar los índices de la fila de encabezado, inicio y fin. La propiedad **Criteria** se usa para establecer los criterios de filtrado personalizados. La clase también tiene un método llamado **FilterRows** para obtener las filas filtradas en base a los criterios dados.

El atributo de búsqueda tipo "contiene" (no distingue mayúsculas y minúsculas) en RowFilter también es compatible con GridDesktop. Puede usar la propiedad **IgnoreCase** de la clase **GridColumn** para especificar el atributo de sensibilidad a mayúsculas y minúsculas según su necesidad. También puede utilizar una propiedad llamada **IsStartWithCriteria** de la clase **GridColumn** para indicar si el RowFilter utiliza los criterios de Inicio con en una columna; el valor predeterminado de la propiedad se establece en falso.

{{% /alert %}} 
## **Filtrado de Datos**
Implementamos tanto las funciones de AutoFiltrado como de Filtro de Datos Personalizados en este ejemplo. Llenamos una lista de datos en el GridDesktop, habilitamos la función de AutoFiltrado y luego buscamos filas filtradas basadas en algunos criterios.
### **AutoFiltro**


{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-FilteringData-AutoFilter.cs" >}}
### **Filtro de Datos Personalizado**


{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-FilteringData-CustomFilter.cs" >}}
