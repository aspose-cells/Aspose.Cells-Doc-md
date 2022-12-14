---
title: Especifique la ruta donde GridWeb almacena los archivos de sesión temporales
type: docs
weight: 50
url: /es/net/specify-the-path-where-gridweb-stores-temporary-session-files/
---
{{% alert color="primary" %}} 

Cuando el modo de sesión de GridWeb es ViewState, almacena sus archivos de sesión temporales dentro del directorio base de la aplicación. A veces, no está bien almacenar archivos de sesión temporales allí porque es posible que el Directorio base de la aplicación no tenga permisos de escritura. En tales casos, GridWeb lanza tal excepción

{{< highlight "java" >}}

 [UnauthorizedAccessException: Access to

the path 'D:\inetpub\wwwroot\AsposeExcelTest\gwb_tempGridWeb1' is denied.]{{< /highlight >}}

La solución al problema anterior es otorgar acceso de escritura al directorio base de la aplicación o cambiar la ruta de los archivos de sesión temporales de GridWeb que tienen acceso de escritura mediante la propiedad GridWeb.SessionStorePath. Esta ruta debe ser relativa al directorio base de la aplicación.

{{% /alert %}} 
## **Especifique la ruta donde GridWeb almacena los archivos de sesión temporales**
El siguiente código de ejemplo especifica la ruta donde GridWeb almacena los archivos de sesión temporales.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-SpecifySessionStorePath.aspx-SpecifySessionStorePath.cs" >}}
