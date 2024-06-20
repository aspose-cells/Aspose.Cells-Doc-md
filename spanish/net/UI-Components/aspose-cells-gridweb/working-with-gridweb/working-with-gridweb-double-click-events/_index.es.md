---
title: Trabajar con eventos de doble clic de GridWeb
type: docs
weight: 80
url: /es/net/aspose-cells-gridweb/gridweb-double-click-event/
keywords: GridWeb,doble clic,evento de clic,evento
description: Este artículo describe cómo utilizar el evento de doble clic en GridWeb.
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb contiene tres tipos de eventos de doble clic:

- CellDoubleClick, se dispara cuando se hace doble clic en una celda.
- ColumnDoubleClick, se dispara cuando se hace doble clic en el encabezado de una columna.
- RowDoubleClick, se dispara cuando se hace doble clic en el encabezado de una fila.

Este tema discute cómo habilitar eventos de doble clic en Aspose.Cells.GridWeb. También se analiza la creación de controladores de eventos para estos eventos.

{{% /alert %}} 
## **Habilitar Eventos de Doble Clic**
Todos los tipos de eventos de doble clic se pueden habilitar del lado del cliente configurando la propiedad EnableDoubleClickEvent del control GridWeb en true.

{{% alert color="primary" %}} 

De forma predeterminada, la propiedad EnableDoubleClickEvent se establece en falso. Esto significa que los eventos de doble clic no están habilitados de forma predeterminada. Para implementar dichos eventos, primero habilite la función.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleDoubleClickEvents.aspx-EnableDoubleClickEvents.cs" >}}



Una vez habilitados los eventos de doble clic, es posible crear controladores de eventos para cualquier evento de doble clic. Estos controladores de eventos realizan tareas específicas cuando se dispara un evento de doble clic dado.
## **Manejo de eventos de doble clic**
Para crear un controlador de eventos en Visual Studio:

1. Haga doble clic en un evento en la lista de **Eventos** en el panel de propiedades.

Para este ejemplo, implementamos controladores de eventos para varios eventos de doble clic.
### **Doble clic en celda**
El controlador de eventos para el evento CellDoubleClick proporciona un argumento del tipo CellEventArgs, que proporciona la información completa de la celda que se ha hecho doble clic.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleDoubleClickEvents.aspx-CellDoubleClickEvent.cs" >}}
### **Doble clic en encabezado de columna**
El controlador de eventos para el evento ColumnDoubleClick proporciona un argumento del tipo RowColumnEventArgs que proporciona el número de índice de la columna para el encabezado que se ha hecho doble clic y otra información.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleDoubleClickEvents.aspx-ColumnDoubleClickEvent.cs" >}}
### **Doble clic en encabezado de fila**
El controlador de eventos para el evento RowDoubleClick proporciona un argumento del tipo RowColumnEventArgs que proporciona el número de índice de la fila para el encabezado que se ha hecho doble clic y otra información relacionada.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleDoubleClickEvents.aspx-RowDoubleClickEvent.cs" >}}
