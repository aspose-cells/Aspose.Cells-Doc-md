---
title: Specificare il percorso in cui GridWeb archivia i file temporanei
type: docs
weight: 50
url: /it/net/gridweb-cache-files/
keywords: cache,session,storage
---
###  sulla cache dei file
{{% alert color="primary" %}} 

Quando la modalità di sessione di GridWeb è ViewState, archivia i file di sessione temporanei all'interno della directory di base dell'applicazione. A volte, non è corretto archiviare lì i file di sessione temporanei perché la directory di base dell'applicazione potrebbe non disporre delle autorizzazioni di scrittura su di essa. In tali casi, GridWeb genera un'eccezione di questo tipo

{{< highlight "java" >}}

 [UnauthorizedAccessException: Access to

the path 'D:\inetpub\wwwroot\AsposeExcelTest\gwb_tempGridWeb1' is denied.]

{{< /highlight >}}

La soluzione al problema precedente è concedere l'accesso in scrittura alla directory di base dell'applicazione o modificare il percorso dei file della sessione temporanea di GridWeb con accesso in scrittura utilizzando la proprietà GridWeb.SessionStorePath. Questo percorso dovrebbe essere relativo alla directory di base dell'applicazione.

{{% /alert %}} 
####  **Specificare il percorso in cui GridWeb archivia i file di sessione temporanei**
Il codice di esempio seguente specifica il percorso in cui GridWeb archivia i file di sessione temporanei.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-SpecifySessionStorePath.aspx-SpecifySessionStorePath.cs" >}}

###  sulla cache delle immagini

quando ci sono forme/immagini nel foglio di lavoro, GridWeb salverà tutte le forme/immagini in un percorso della cache

 il percorso della cache predefinito è***System.Web.HttpContext.Current.Server.MapPath("/acwcache")***

 anche noi possiamo usare***GridWeb.PictureCachePath*** per impostare questo percorso su un percorso specifico.

quando apriamo una pagina, GridWeb risolverà l'URL dell'immagine della richiesta e otterrà il flusso dell'immagine dalla cache tramite l'ID dell'URL.

 ad esempio, se l'indirizzo della tua pagina è*http://ip/mygridwebapp/test.aspx*  

l'URL di richiesta dell'immagine generato da GridWeb sarà *http://ip/mygridwebapp/test.aspx/acw_image/imageid*.

####  a volte le forme/immagini non vengono caricate durante l'utilizzo[URL amichevole](https://weblogs.asp.net/psheriff/using-friendly-urls-in-web-forms).

è necessario controllare la richiesta dell'URL dell'immagine.

 la normale richiesta di immagine sarà come:*http://ip/mygridwebapp/test.aspx/acw_image/imageid*

ma la tua richiesta va così :*http://ip/mygridwebapp/test/acw_image/imageid*

se usi FriendlyUrl devi filtrare la richiesta dell'URL dell'immagine per GridWeb.

quindi il server di controllo GridWeb può ottenere e risolvere la richiesta e trovare il flusso di immagini dal percorso della cache.

ad esempio supponiamo che l'URL della tua pagina sia questo:*http://ip/mygridwebapp/test.aspx*

quindi il codice seguente è una soluzione alternativa per risolvere tale problema.
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





