---
title: Especifique la ruta donde GridWeb almacena los archivos temporales
type: docs
weight: 50
url: /es/net/gridweb-cache-files/
keywords: cache,session,storage
---
###  sobre caché de archivos
{{% alert color="primary" %}} 

Cuando el modo de sesión de GridWeb es ViewState, almacena sus archivos de sesión temporales dentro del directorio base de la aplicación. A veces, no está bien almacenar archivos de sesión temporales allí porque es posible que el Directorio base de la aplicación no tenga permisos de escritura. En tales casos, GridWeb lanza tal excepción

{{< highlight "java" >}}

 [UnauthorizedAccessException: Access to

the path 'D:\inetpub\wwwroot\AsposeExcelTest\gwb_tempGridWeb1' is denied.]

{{< /highlight >}}

La solución al problema anterior es otorgar acceso de escritura al directorio base de la aplicación o cambiar la ruta de los archivos de sesión temporales de GridWeb que tienen acceso de escritura mediante la propiedad GridWeb.SessionStorePath. Esta ruta debe ser relativa al directorio base de la aplicación.

{{% /alert %}} 
####  **Especifique la ruta donde GridWeb almacena los archivos de sesión temporales**
El siguiente código de ejemplo especifica la ruta donde GridWeb almacena los archivos de sesión temporales.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-SpecifySessionStorePath.aspx-SpecifySessionStorePath.cs" >}}

###  sobre el caché de imágenes

cuando hay formas/imágenes en la hoja de trabajo, GridWeb guardará todas las formas/imágenes en una ruta de caché

 la ruta de caché predeterminada es***Sistema.Web.HttpContext.Current.Server.MapPath("/acwcache")***

 también podemos usar***GridWeb.PictureCachePath*** para establecer esta ruta en una ruta específica.

cuando abrimos una página, GridWeb resolverá la URL de la imagen de solicitud y obtendrá la transmisión de la imagen del caché por la identificación de la URL.

 por ejemplo, si la dirección de su página es*http://ip/mygridwebapp/prueba.aspx*  

la URL de solicitud de imagen generada por GridWeb será *http://ip/mygridwebapp/test.aspx/acw_image/imageid*.

####  a veces las formas/imágenes no se cargan cuando usa[URL amigable](https://weblogs.asp.net/psheriff/using-friendly-urls-in-web-forms).

debe verificar la solicitud de URL de la imagen.

 la solicitud de imagen normal será como:*http://ip/mygridwebapp/test.aspx/acw_image/imageid*

pero su solicitud es así:*http://ip/mygridwebapp/test/acw_image/imageid*

si usa FriendlyUrl, debe filtrar la solicitud de URL de imagen para GridWeb.

por lo tanto, el servidor de control de GridWeb puede obtener y resolver la solicitud y encontrar el flujo de imágenes desde la ruta de caché.

por ejemplo, asumimos que la URL de su página es esta:*http://ip/mygridwebapp/test.aspx*

entonces el siguiente código es una solución para solucionar este problema.
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





