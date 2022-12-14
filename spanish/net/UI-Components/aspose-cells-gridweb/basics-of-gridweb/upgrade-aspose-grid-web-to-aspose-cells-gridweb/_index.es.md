---
title: Actualice Aspose.Grid.Web a Aspose.Cells.GridWeb
type: docs
weight: 30
url: /es/net/upgrade-aspose-grid-web-to-aspose-cells-gridweb/
---
{{% alert color="primary" %}}

Para facilitar la actualización, mantenemos un documento que describe información crítica para los usuarios existentes, especialmente aquellos que han usado el Aspose.Grid.Web anterior y necesitan actualizar al Aspose.Cells.GridWeb fusionado.

 Estas son notas breves y debería poder encontrar más información consultando las secciones del[Guía del desarrollador](/cells/es/net/developer-guide/).

{{% /alert %}}

## **Actualizando a Aspose.Cells.GridWeb**

 Los usuarios de Aspose.Grid.Web pueden encontrar problemas al usar el nuevo Aspose.Cells.GridWeb cuando lo actualicen. Cabe señalar que Aspose.Grid.Web ha cambiado de nombre y se ha convertido en parte de Aspose.Cells, por lo que no continuaremos ni realizaremos modificaciones en versiones anteriores del control.

No es difícil actualizar al último componente Aspose.Cells.GridWeb.

{{% alert color="primary" %}}

Hay algunos cambios en el API ya que las clases con los miembros, estructuras, enumeraciones, etc. siguen siendo las mismas. La mayoría de los cambios se han realizado en los espacios de nombres del control y otras etiquetas o atributos.

{{% /alert %}}

La siguiente es la lista de espacios de nombres y otros atributos/etiquetas que se cambian ahora:

1. El espacio de nombres Aspose.Grid.Web ha cambiado de nombre a Aspose.Cells.GridWeb.
1. El espacio de nombres Aspose.Grid.Web.Data ha cambiado de nombre a Aspose.Cells.GridWeb.Data.
1. El espacio de nombres Aspose.Grid.Web.Design ha cambiado de nombre a Aspose.Cells.GridWeb.Design.
1. El espacio de nombres Aspose.Grid.Formula pasó a llamarse Aspose.Cells.GridFormula y, con los lanzamientos recientes del componente, dicho espacio de nombres se eliminó por completo del público API.
1. La etiqueta agw:GridWeb ha cambiado a acw:GridWeb en el formulario aspx.
1. La antigua ruta del cliente Aspose.Grid.Web, agw_cliente, ha cambiado a acw_cliente para Aspose.Cells.GridWeb.
1.  La configuración de la ruta del cliente en el archivo web.config, por ejemplo:

{{< highlight "java" >}}

 <appSettings> 

    <add key="aspose.grid.web.agw_client_path" value="/agw_client/" />

    <add key="aspose.grid.web.force_script_path" value="true" />

</appSettings>



{{< /highlight >}}

 ha cambiado a

{{< highlight "java" >}}

 <appSettings>

    <add key="aspose.cells.gridweb.acw_client_path" value="/acw_client/" />

    <add key="aspose.cells.gridweb.force_script_path" value="true" />

</appSettings>



{{< /highlight >}}
