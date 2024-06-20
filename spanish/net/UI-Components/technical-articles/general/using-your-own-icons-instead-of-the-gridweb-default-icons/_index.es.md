---
title: Usar sus propios iconos en lugar de los iconos predeterminados de GridWeb
type: docs
weight: 10
url: /es/net/aspose-cells-gridweb/use-your-own-icons-instead-of-the-default-icons/
keywords: GridWeb, icono, iconos
description: Este artículo describe cómo usar iconos en GridWeb.
---

{{% alert color="primary" %}} 

A veces, es posible que desee utilizar sus propios iconos (imágenes) en lugar de los iconos predeterminados del control Aspose.Cells.GridWeb. Este artículo explica cómo hacerlo.

{{% /alert %}} 

Los iconos predeterminados del control se encuentran en la ruta URL "/acw_client/". La ruta del archivo por defecto puede ser: "C:\Program Files\Aspose\Aspose.Cells for .NET\acw_client". Encuentras archivos como submit.gif, save.gif, etc. en esa carpeta. Si deseas reemplazar estas imágenes con las tuyas, agrega una sección de configuración al archivo web.config de tu aplicación web.

**XML**

{{< highlight csharp >}}

 <appSettings>

 <add key="Aspose.Cells.GridWeb.acw_client_path" value="/acw_client/" />

</appSettings>



{{< /highlight >}}

Puede que hayas notado que esta configuración solo afecta la ruta de las imágenes del control y no afecta la ruta de los scripts de cliente del control. Por ejemplo, si ejecutas tu página con el control GridWeb y revisas el archivo fuente en el navegador, podrías encontrar que la propiedad de la ruta acw_client del elemento DIV del grid sigue diciendo: “/tuApp/webform1.aspx/”. En algunos casos, es posible que necesites redefinir la ruta del script de cliente. Para forzar al control a usar la ruta de imagen redefinida como la ruta del script de cliente, agrega otro ajuste de configuración en la sección appSettings.
**XML**

{{< highlight csharp >}}

 <add key="Aspose.Cells.GridWeb.force_script_path" value="true" />



{{< /highlight >}}

{{% alert color="primary" %}} 

Esta configuración solo tendrá efecto con el control licenciado.

{{% /alert %}}
