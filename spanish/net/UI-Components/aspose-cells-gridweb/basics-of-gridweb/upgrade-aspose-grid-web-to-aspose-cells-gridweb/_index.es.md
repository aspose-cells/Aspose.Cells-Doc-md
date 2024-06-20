---
title: Actualizar Aspose.Grid.Web a Aspose.Cells.GridWeb
type: docs
weight: 30
url: /es/net/aspose-cells-gridweb/upgrade-aspose-grid-web-to-aspose-cells-gridweb/
keywords: GridWeb 
description: Este artículo presenta cómo realizar la actualización en GridWeb.
---

{{% alert color="primary" %}}

Para facilitar la actualización, mantenemos un documento que describe información crítica para los usuarios existentes, especialmente aquellos que han utilizado la versión anterior de Aspose.Grid.Web y necesitan actualizar a Aspose.Cells.GridWeb.

Estas notas están destinadas a ser breves, y debería poder encontrar más información consultando las secciones de la [Guía del desarrollador](/cells/es/net/aspose-cells-gridweb/developer-guide/).

{{% /alert %}}

## **Actualizar a Aspose.Cells.GridWeb**

Los usuarios de Aspose.Grid.Web podrían encontrar problemas al utilizar el nuevo Aspose.Cells.GridWeb al actualizar a él. Cabe destacar que Aspose.Grid.Web ha sido renombrado y ahora forma parte de Aspose.Cells, por lo que no continuaremos o haremos modificaciones a las versiones anteriores del control. 

No es difícil actualizar al último componente Aspose.Cells.GridWeb.

{{% alert color="primary" %}}

Hay algunos cambios en la API, ya que las clases con los miembros, estructuras, enumeraciones, etc. permanecen iguales. La mayoría de los cambios se han realizado en los espacios de nombres del control y en otras etiquetas o atributos.

{{% /alert %}}

A continuación se muestra la lista de espacios de nombres y otros atributos/etiquetas que han cambiado:

1. El espacio de nombres Aspose.Grid.Web ha sido renombrado a Aspose.Cells.GridWeb.
1. El espacio de nombres Aspose.Grid.Web.Data ha sido renombrado a Aspose.Cells.GridWeb.Data.
1. El espacio de nombres Aspose.Grid.Web.Design ha sido renombrado a Aspose.Cells.GridWeb.Design.
1. El espacio de nombres Aspose.Grid.Formula fue renombrado a Aspose.Cells.GridFormula, y con las versiones recientes del componente, dicho espacio de nombres fue completamente eliminado de la API pública.
1. La etiqueta agw:GridWeb ha cambiado a acw:GridWeb en el formulario aspx.
1. La ruta del cliente de la antigua Aspose.Grid.Web, agw_client, ha cambiado a acw_client para Aspose.Cells.GridWeb.
1. La configuración de la ruta del cliente en el archivo web.config, por ejemplo: 

{{< highlight java >}}

 <appSettings> 

    <add key="aspose.grid.web.agw_client_path" value="/agw_client/" />

    <add key="aspose.grid.web.force_script_path" value="true" />

</appSettings>



{{< /highlight >}}

ha cambiado a 

{{< highlight java >}}

 <appSettings>

    <add key="aspose.cells.gridweb.acw_client_path" value="/acw_client/" />

    <add key="aspose.cells.gridweb.force_script_path" value="true" />

</appSettings>



{{< /highlight >}}
