---
title: Specificare il percorso in cui GridWeb memorizza i file temporanei
type: docs
weight: 50
url: /it/net/aspose-cells-gridweb/gridweb-cache-files/
keywords: GridWeb, cache, sessione, storage
description: Questo articolo descrive lo storage in GridWeb.
---
### riguardo alla cache file
{{% alert color="primary" %}} 

Quando la modalità sessione di GridWeb è ViewState, memorizza i file di sessione temporanei all'interno della directory di base dell'applicazione. A volte, non è corretto memorizzare i file di sessione temporanei lì perché la directory di base dell'applicazione potrebbe non avere le autorizzazioni di scrittura. In tali casi, GridWeb genera un'eccezione del genere.

{{< highlight java >}}

 [UnauthorizedAccessException: Access to

the path 'D:\inetpub\wwwroot\AsposeExcelTest\gwb_tempGridWeb1' is denied.]

{{< /highlight >}}

La soluzione al problema sopra è concedere l'accesso in scrittura alla directory di base dell'applicazione o modificare il percorso dei file di sessione temporanei di GridWeb che hanno accesso in scrittura utilizzando la proprietà GridWeb.SessionStorePath. Questo percorso dovrebbe essere relativo alla directory di base dell'applicazione.

{{% /alert %}} 
#### **Specificare il percorso in cui GridWeb memorizza i file di sessione temporanei**
Il codice di esempio seguente specifica il percorso in cui GridWeb memorizza i file di sessione temporanei.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-SpecifySessionStorePath.aspx-SpecifySessionStorePath.cs" >}}

### riguardo alla cache immagini

quando ci sono forme/immagini nel foglio di lavoro, GridWeb salverà tutte le forme/immagini in un percorso di cache

il percorso di cache predefinito è ***System.Web.HttpContext.Current.Server.MapPath("/acwcache")***

possiamo anche usare ***GridWeb.PictureCachePath*** per impostare questo percorso su un percorso specifico.

quando apriamo una pagina GridWeb risolverà l'URL dell'immagine richiesta e otterrà lo stream dell'immagine dalla cache tramite l'ID dell'URL.

ad esempio, se l'indirizzo della tua pagina è *http://ip/mygridwebapp/test.aspx*  

l'URL della richiesta dell'immagine generato da GridWeb sarà *http://ip/mygridwebapp/test.aspx/acw_image/imageid*.

#### a volte le forme/immagini non vengono caricate quando si utilizza [URL amichevole](https://weblogs.asp.net/psheriff/using-friendly-urls-in-web-forms).

è necessario controllare l'URL della richiesta dell'immagine.

la richiesta normale dell'immagine dovrebbe essere simile a: *http://ip/mygridwebapp/test.aspx/acw_image/imageid*

ma la tua richiesta sarà simile a questa: *http://ip/mygridwebapp/test/acw_image/imageid*

se utilizzi FriendlyUrl è necessario filtrare la richiesta dell'URL dell'immagine per GridWeb.

così il server di controllo GridWeb può ottenere e risolvere la richiesta e trovare lo stream dell'immagine dal percorso della cache.

ad esempio assumiamo che l'URL della tua pagina sia simile a: *http://ip/mygridwebapp/test.aspx*

allora il codice qui sotto è un workaround per risolvere tale problema.
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





