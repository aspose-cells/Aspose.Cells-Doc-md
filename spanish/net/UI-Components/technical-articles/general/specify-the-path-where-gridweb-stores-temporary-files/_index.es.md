---
title: Especifique la ruta donde GridWeb almacena archivos temporales
type: docs
weight: 50
url: /es/net/aspose-cells-gridweb/gridweb-cache-files/
keywords: GridWeb, caché, sesión, almacenamiento
description: Este artículo describe el almacenamiento en GridWeb.
---
### sobre la caché de archivos
{{% alert color="primary" %}} 

Cuando el modo de sesión de GridWeb es ViewState, almacena sus archivos temporales de sesión dentro del Directorio Base de la Aplicación. A veces, no está bien almacenar archivos temporales de sesión allí porque es posible que el Directorio Base de la Aplicación no tenga permisos de escritura. En tales casos, GridWeb arroja tal excepción

{{< highlight java >}}

 [UnauthorizedAccessException: Access to

the path 'D:\inetpub\wwwroot\AsposeExcelTest\gwb_tempGridWeb1' is denied.]

{{< /highlight >}}

La solución al problema anterior es otorgar acceso de escritura al Directorio Base de la Aplicación o cambiar la ruta de los archivos temporales de sesión de GridWeb con acceso de escritura utilizando la propiedad GridWeb.SessionStorePath. Esta ruta debe ser relativa al Directorio Base de la Aplicación.

{{% /alert %}} 
#### **Especifique la ruta donde GridWeb almacena archivos temporales de sesión**
El siguiente código de ejemplo especifica la ruta donde GridWeb almacena archivos temporales de sesión.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-SpecifySessionStorePath.aspx-SpecifySessionStorePath.cs" >}}

### sobre la caché de imágenes

cuando hay formas/figuras en la hoja de cálculo, GridWeb guardará todas las formas/figuras en una ruta de caché

la ruta de caché predeterminada es ***System.Web.HttpContext.Current.Server.MapPath("/acwcache")***

también podemos usar ***GridWeb.PictureCachePath*** para establecer esta ruta en una ruta específica.

cuando abrimos una página, GridWeb resolverá la URL de la imagen solicitada y obtendrá el flujo de la imagen de la caché por el ID de la URL.

por ejemplo, si la dirección de su página es *http://ip/mygridwebapp/test.aspx*  

la URL de solicitud de imagen generada por GridWeb será *http://ip/mygridwebapp/test.aspx/acw_image/imageid*.

#### a veces las formas/imágenes no se cargan cuando se utiliza [Friendly Url](https://weblogs.asp.net/psheriff/using-friendly-urls-in-web-forms).

necesitas verificar la solicitud de URL de imagen.

la solicitud de imagen normal debería ser como: *http://ip/mygridwebapp/test.aspx/acw_image/imageid*

pero tu solicitud se ve así:*http://ip/mygridwebapp/test/acw_image/imageid*

si usas FriendlyUrl necesitas filtrar la solicitud de URL de imagen para GridWeb.

así la solicitud del servidor de control de GridWeb puede obtener y resolver la solicitud y encontrar el flujo de imagen desde la ruta de caché.

por ejemplo asumimos que la URL de tu página es como esta:*http://ip/mygridwebapp/test.aspx*

entonces el siguiente código es una solución temporal para arreglar dicho problema.
```csharp
//write your custom url resolver:MyWebFormsFriendlyUrlResolver
public class MyWebFormsFriendlyUrlResolver : WebFormsFriendlyUrlResolver
{
public MyWebFormsFriendlyUrlResolver() { }

    public override string ConvertToFriendlyUrl(string path)
    {
        if (!string.IsNullOrEmpty(path))
        {//filter your GridWeb related page,here we use 'mygridwebapp' to identify as we assume your page is:http://ip/mygridwebapp/test.aspx
            if (path.ToLower().Contains("mygridwebapp"))
            { // Here the filter code
                return path;
            }
        }
        return base.ConvertToFriendlyUrl(path);
    }
}
//in RoutConfig.cs set the custom url resolver:MyWebFormsFriendlyUrlResolver
public static class RouteConfig
{
    public static void RegisterRoutes(RouteCollection routes)
    {
        var settings = new FriendlyUrlSettings();
        settings.AutoRedirectMode = RedirectMode.Permanent;
        routes.EnableFriendlyUrls(settings, new IFriendlyUrlResolver[] {
                             new MyWebFormsFriendlyUrlResolver() });
    }
}
```





