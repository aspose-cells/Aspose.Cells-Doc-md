---
title: Filtrado de datos
type: docs
weight: 100
url: /es/net/filtering-data/
---
{{% alert color="primary" %}} 

**Aspose.Cells.GridDesktop** proporciona funciones de filtro automático y filtro de datos personalizado para los usuarios. Con estas funciones, puede encontrar una manera de seleccionar solo los elementos de la hoja de trabajo que desea mostrar en una lista. Además, puede filtrar elementos en una lista de acuerdo con un criterio establecido. Puede filtrar texto, números o fechas con la función Filtro automático/Filtro de datos personalizado.

 Puedes usar**Habilitar autofiltro** Atributo booleano de**AjustesFiltroFila** class para habilitar la función de filtro automático para el control GridDesktop. Hay algunas otras propiedades de la clase que puede usar, por ejemplo**Fila de encabezado** , **fila de inicio** y**EndRow**para especificar los índices de encabezado, fila inicial y final. los**Criterios** La propiedad se utiliza para establecer los criterios de filtrado personalizados. La clase también tiene un método llamado**FilterRows** para obtener las filas filtradas según los criterios dados.

 GridDesktop también admite el atributo de búsqueda de tipo "contiene" (que no distingue entre mayúsculas y minúsculas) en RowFilter. Puedes utilizar**Ignorar caso** propiedad de**CuadrículaColumna** class para especificar el atributo de distinción entre mayúsculas y minúsculas para su necesidad. También puede usar una propiedad llamada**EsInicioConCriterios** de**CuadrículaColumna** class para indicar si RowFilter usa los criterios StartWith en una columna; el valor predeterminado de la propiedad se establece en falso.

{{% /alert %}} 
## **Filtrado de datos**
En este ejemplo, implementamos las funciones de filtro automático y filtro de datos personalizado. Completamos una lista de datos en GridDesktop, habilitamos la función de filtro automático y luego buscamos filas filtradas según algunos criterios.
### **Filtro automático**


{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-FilteringData-AutoFilter.cs" >}}
### **Filtro de datos personalizado**


{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-FilteringData-CustomFilter.cs" >}}
