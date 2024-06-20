---
title: Spécifiez le chemin où GridWeb stocke les fichiers temporaires.
type: docs
weight: 50
url: /fr/net/aspose-cells-gridweb/gridweb-cache-files/
keywords: GridWeb,cache,session,stockage
description: Cet article décrit le stockage dans GridWeb.
---
### à propos du cache de fichiers
{{% alert color="primary" %}} 

Lorsque le mode session de GridWeb est ViewState, il stocke ses fichiers de session temporaires à l'intérieur du répertoire de base de l'application. Parfois, il n'est pas correct de stocker des fichiers de session temporaires à cet endroit car le répertoire de base de l'application pourrait ne pas avoir les autorisations d'écriture nécessaires. Dans de tels cas, GridWeb génère une telle exception

{{< highlight java >}}

 [UnauthorizedAccessException: Access to

the path 'D:\inetpub\wwwroot\AsposeExcelTest\gwb_tempGridWeb1' is denied.]

{{< /highlight >}}

La solution à ce problème consiste à donner l'accès en écriture au répertoire de base de l'application ou à changer le chemin des fichiers de session temporaires de GridWeb ayant les autorisations d'écriture en utilisant la propriété GridWeb.SessionStorePath. Ce chemin doit être relatif au répertoire de base de l'application.

{{% /alert %}} 
#### **Spécifiez le chemin où GridWeb stocke les fichiers de session temporaires.**
Le code d'exemple suivant spécifie le chemin où GridWeb stocke les fichiers de session temporaires.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-SpecifySessionStorePath.aspx-SpecifySessionStorePath.cs" >}}

### à propos du cache d'images

lorsqu'il y a des formes/images dans la feuille de calcul, GridWeb enregistrera toutes les formes/images dans un chemin de cache

le chemin de cache par défaut est ***System.Web.HttpContext.Current.Server.MapPath("/acwcache")***

nous pouvons également utiliser ***GridWeb.PictureCachePath*** pour définir ce chemin vers un chemin spécifique.

lorsque nous ouvrons une page, GridWeb résoudra l'URL de l'image demandée et récupérera le flux d'image du cache en utilisant l'ID d'URL.

par exemple, si l'adresse de votre page est *http://ip/mygridwebapp/test.aspx*  

l'URL de requête d'image générée par GridWeb sera *http://ip/mygridwebapp/test.aspx/acw_image/imageid*.

#### parfois, les formes/images ne se chargent pas lorsque vous utilisez [Friendly Url](https://weblogs.asp.net/psheriff/using-friendly-urls-in-web-forms).

vous devez vérifier l'URL de la demande d'image.

la requête d'image normale doit ressembler à : *http://ip/mygridwebapp/test.aspx/acw_image/imageid*

mais votre demande ressemble à ceci : *http://ip/mygridwebapp/test/acw_image/imageid*

si vous utilisez FriendlyUrl, vous devez filtrer la requête d'url de l'image pour GridWeb.

ainsi, le serveur de contrôle GridWeb peut obtenir et résoudre la requête et trouver le flux d'image à partir du chemin du cache.

par exemple, nous supposons que l'url de votre page est comme ceci : *http://ip/mygridwebapp/test.aspx*

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





