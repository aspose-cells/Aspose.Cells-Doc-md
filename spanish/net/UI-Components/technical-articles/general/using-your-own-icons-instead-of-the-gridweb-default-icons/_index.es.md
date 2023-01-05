---
title: Uso de sus propios iconos en lugar de los iconos predeterminados de GridWeb
type: docs
weight: 10
url: /es/net/using-your-own-icons-instead-of-the-gridweb-default-icons/
---
{{% alert color="primary" %}} 

A veces es posible que desee utilizar sus propios iconos (imágenes) en lugar de los iconos predeterminados del control Aspose.Cells.GridWeb. Este artículo explica cómo hacer esto.

{{% /alert %}} 

Los iconos predeterminados del control se encuentran en la ruta URL "/acw_cliente/". La ruta del archivo puede ser: "C:\Program Files\Aspose\Aspose.Cells for .NET\acw_client" de forma predeterminada. Encontrará archivos como submit.gif, save.gif, etc. en esa carpeta. Si desea reemplazar estas imágenes con las suyas, agregue una sección de configuración al archivo web.config de su aplicación web.

**XML**

{{< highlight "csharp" >}}

 <appSettings>

 <add key="Aspose.Cells.GridWeb.acw_client_path" value="/acw_client/" />

</appSettings>



{{< /highlight >}}

Es posible que haya notado que esta configuración solo afecta la ruta de las imágenes de control y no afecta la ruta de los scripts de cliente del control. Por ejemplo, si ejecuta su página con el control GridWeb y verifica el archivo fuente en el navegador, puede encontrar que el acw_ cliente_la propiedad de ruta del elemento DIV de la cuadrícula todavía dice: "/yourApp/webform1.aspx/". En algunos casos, es posible que deba redefinir la ruta del script del cliente. Para obligar al control a usar la ruta de la imagen redefinida como la ruta del script del cliente, agregue otra configuración en la sección de configuración de la aplicación
**XML**

{{< highlight "csharp" >}}

 <add key="Aspose.Cells.GridWeb.force_script_path" value="true" />



{{< /highlight >}}

{{% alert color="primary" %}} 

Esta configuración solo tendrá efecto con el control con licencia.

{{% /alert %}}
