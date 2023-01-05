---
title: Manejar eventos secundarios del servidor de filtro de columnas
type: docs
weight: 90
url: /es/net/handle-column-filter-server-side-events/
---
{{% alert color="primary" %}} 

El filtrado de datos es probablemente la función de Excel más utilizada que le permite filtrar los datos según un criterio específico. Los datos filtrados muestran solo las filas que cumplen la condición al ocultar las filas que no cumplen los criterios.
Aspose.Cells. El componente GridWeb brinda la capacidad de realizar el filtrado de datos utilizando su interfaz. Para ampliar sus capacidades, el componente Aspose.Cells.GridWeb también proporciona dos eventos que pueden servir como devolución de llamada al mecanismo de filtrado realizado a través de la interfaz de usuario de GridWeb.

{{% /alert %}} 
## **Manejo del evento del lado del servidor al aplicar el filtro de columna**
Hay dos eventos principales como se detalla a continuación.

1. OnBeforeColumnFilter: se activa antes de que se aplique el filtro en una columna.
1. OnAfterColumnFilter: se activa después de que se haya aplicado el filtro en una columna.

Aquí está el script ASPX del componente Aspose.Cells.GridWeb para agregar y asignar los eventos antes mencionados.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-HandleColumnFilterEvents-HandleColumnFilterEvents.aspx" >}}



Estos eventos se pueden usar para obtener información útil sobre el proceso de filtrado, como el índice de columna y el valor en el que se debe aplicar el filtro. A continuación se muestra el fragmento que demuestra el uso del evento OnBeforeColumnFilter para recuperar el índice de la columna y el valor que el usuario seleccionó en la interfaz de usuario de GridWeb para el filtrado.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-HandleColumnFilterEvents.aspx-BeforeColumnFilter.cs" >}}


Por otro lado, si el requisito es obtener el número de filas filtradas después de aplicar el filtro, puede usar el evento OnAfterColumnFilter como se muestra a continuación.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-HandleColumnFilterEvents.aspx-AfterColumnFilter.cs" >}}

{{% alert color="primary" %}} 

 Ver introducción a todos[Trabajar con eventos de GridWeb](/cells/es/net/working-with-gridweb-events/) junto con algunos detalles sobre cómo manejar estos eventos.

{{% /alert %}}
