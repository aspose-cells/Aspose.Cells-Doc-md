---
title: Spécifiez le chemin où GridWeb stocke les fichiers temporaires
type: docs
weight: 50
url: /fr/net/gridweb-cache-files/
keywords: cache,session,storage
---
###  à propos du cache de fichiers
{{% alert color="primary" %}} 

Lorsque le mode de session GridWeb est ViewState, il stocke ses fichiers de session temporaires dans le répertoire de base de l'application. Parfois, il n'est pas acceptable d'y stocker des fichiers de session temporaires, car le répertoire de base de l'application peut ne pas disposer d'autorisations d'écriture dessus. Dans de tels cas, GridWeb lève une telle exception

{{< highlight "java" >}}

 [UnauthorizedAccessException: Access to

the path 'D:\inetpub\wwwroot\AsposeExcelTest\gwb_tempGridWeb1' is denied.]

{{< /highlight >}}

La solution au problème ci-dessus consiste à donner un accès en écriture au répertoire de base de l'application ou à modifier le chemin des fichiers de session temporaires GridWeb ayant un accès en écriture à l'aide de la propriété GridWeb.SessionStorePath. Ce chemin doit être relatif au répertoire de base de l'application.

{{% /alert %}} 
####  **Spécifiez le chemin où GridWeb stocke les fichiers de session temporaires**
L'exemple de code suivant spécifie le chemin où GridWeb stocke les fichiers de session temporaires.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-SpecifySessionStorePath.aspx-SpecifySessionStorePath.cs" >}}

###  à propos du cache d'images

lorsqu'il y a des formes/images dans la feuille de calcul, GridWeb enregistre toutes les formes/images dans un chemin de cache

 le chemin du cache par défaut est***System.Web.HttpContext.Current.Server.MapPath("/acwcache")***

 nous pouvons aussi utiliser***GridWeb.PictureCachePathGridWeb.PictureCachePath*** pour définir ce chemin sur un chemin spécifique.

lorsque nous ouvrons une page, GridWeb résoudra l'URL de l'image de demande et obtiendra le flux d'image du cache par l'ID de l'URL.

 par exemple, si l'adresse de votre page est*http://ip/mygridwebapp/test.aspx*  

l'URL de demande d'image générée par GridWeb sera *http://ip/mygridwebapp/test.aspx/acw_image/imageid*.

####  parfois les formes/images ne sont pas chargées lorsque vous utilisez[URL amicale](https://weblogs.asp.net/psheriff/using-friendly-urls-in-web-forms).

vous devez vérifier la demande d'URL d'image.

 la demande d'image normale doit ressembler à :*http://ip/mygridwebapp/test.aspx/acw_image/imageid*

mais votre demande va comme ceci :*http://ip/mygridwebapp/test/acw_image/imageid*

si vous utilisez FriendlyUrl, vous devez filtrer la demande d'URL d'image pour GridWeb.

ainsi, le serveur de contrôle GridWeb peut obtenir et résoudre la demande et trouver le flux d'images à partir du chemin du cache.

par exemple, nous supposons que l'URL de votre page est la suivante :*http://ip/mygridwebapp/test.aspx*

alors le code ci-dessous est une solution de contournement pour résoudre ce problème.
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





