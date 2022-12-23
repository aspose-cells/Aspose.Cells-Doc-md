---
title: Trabajar con eventos de doble clic de GridWeb
type: docs
weight: 80
url: /es/net/working-with-gridweb-double-click-events/
---
{{% alert color="primary" %}} 

Aspose.Cells.GridWeb contiene tres tipos de eventos de doble clic:

- CellDoubleClick, se activa cuando se hace doble clic en una celda.
- ColumnDoubleClick, se activa cuando se hace doble clic en el encabezado de una columna.
- RowDoubleClick, se activa cuando se hace doble clic en el encabezado de una fila.

Este tema trata sobre cómo habilitar eventos de doble clic en Aspose.Cells.GridWeb. También analiza la creación de controladores de eventos para estos eventos.

{{% /alert %}} 
## **Habilitación de eventos de doble clic**
Todos los tipos de eventos de doble clic se pueden habilitar en el lado del cliente estableciendo la propiedad EnableDoubleClickEvent del control GridWeb en verdadero.

{{% alert color="primary" %}} 

De forma predeterminada, la propiedad EnableDoubleClickEvent se establece en falso. Esto significa que los eventos de doble clic no están habilitados de forma predeterminada. Para implementar dichos eventos, primero habilite la función.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleDoubleClickEvents.aspx-EnableDoubleClickEvents.cs" >}}



Una vez que los eventos de doble clic están habilitados, es posible crear controladores de eventos para cualquier evento de doble clic. Estos controladores de eventos realizan tareas específicas cuando se activa un evento de doble clic determinado.
## **Gestión de eventos de doble clic**
Para crear un controlador de eventos en Visual Studio:

1.  Haga doble clic en un evento en el**Eventos** lista en el panel Propiedades.

Para este ejemplo, implementamos controladores de eventos para varios eventos de doble clic.
### **Doble clic Cell**
El controlador de eventos para el evento CellDoubleClick proporciona un argumento del tipo CellEventArgs, que proporciona la información completa de la celda en la que se hace doble clic.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleDoubleClickEvents.aspx-CellDoubleClickEvent.cs" >}}
### **Encabezado de columna de doble clic**
El controlador de eventos para el evento ColumnDoubleClick proporciona un argumento del tipo RowColumnEventArgs que proporciona el número de índice de la columna del encabezado en el que se hizo doble clic y otra información.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleDoubleClickEvents.aspx-ColumnDoubleClickEvent.cs" >}}
### **Encabezado de fila de doble clic**
El controlador de eventos para el evento RowDoubleClick proporciona un argumento del tipo RowColumnEventArgs que proporciona el número de índice de la fila del encabezado en el que se hizo doble clic y otra información relacionada.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleDoubleClickEvents.aspx-RowDoubleClickEvent.cs" >}}
