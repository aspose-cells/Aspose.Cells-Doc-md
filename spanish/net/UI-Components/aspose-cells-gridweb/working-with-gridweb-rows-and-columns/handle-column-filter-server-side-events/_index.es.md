---
title: Manejar Eventos del Servidor de Filtro de Columnas
type: docs
weight: 90
url: /es/net/aspose-cells-gridweb/handle-column-filter-server-side-events/
keywords: GridWeb,filter,OnBeforeColumnFilter,OnAfterColumnFilter
description: Este artículo presenta cómo manejar el evento de filtro de columna en GridWeb.
---

{{% alert color="primary" %}} 

El filtrado de datos es probablemente la característica de Excel más utilizada que le permite filtrar los datos en función de un criterio específico. Los datos filtrados muestran solo las filas que cumplen la condición al ocultar las filas que no cumplen el criterio.
El componente Aspose.Cells.GridWeb proporciona la capacidad de realizar el filtrado de datos utilizando su interfaz. Para ampliar sus capacidades, el componente Aspose.Cells.GridWeb también proporciona dos eventos que pueden servir como devolución de llamada al mecanismo de filtrado realizado a través de la interfaz de GridWeb.

{{% /alert %}} 
## **Manejo de Evento del Lado del Servidor al Aplicar el Filtro de Columna**
Hay dos eventos principales detallados a continuación.

1. OnBeforeColumnFilter: Se dispara antes de que se aplique el filtro en una columna.
1. OnAfterColumnFilter: Se dispara después de que se ha aplicado el filtro en una columna.

Aquí está el script ASPX del componente Aspose.Cells.GridWeb para agregar y asignar los eventos mencionados anteriormente.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-HandleColumnFilterEvents-HandleColumnFilterEvents.aspx" >}}



Estos eventos pueden usarse para obtener información útil sobre el proceso de filtrado, como el índice de la columna y el valor en el que se debe aplicar el filtro. A continuación se muestra el fragmento que demuestra el uso del evento OnBeforeColumnFilter para recuperar el índice de la columna y el valor que el usuario ha seleccionado en la interfaz de GridWeb para el filtrado.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-HandleColumnFilterEvents.aspx-BeforeColumnFilter.cs" >}}


Por otro lado, si el requisito es obtener el número de filas filtradas después de que se ha aplicado el filtro, entonces puede usar el evento OnAfterColumnFilter como se muestra a continuación.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-HandleColumnFilterEvents.aspx-AfterColumnFilter.cs" >}}

{{% alert color="primary" %}} 

Consulte la introducción a todos los [Eventos de GridWeb](/cells/es/net/aspose-cells-gridweb/working-with-gridweb-events/) junto con algunos detalles sobre cómo manejar estos eventos.

{{% /alert %}}
