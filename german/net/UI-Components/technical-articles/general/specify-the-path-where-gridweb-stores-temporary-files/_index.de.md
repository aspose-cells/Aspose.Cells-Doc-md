---
title: Geben Sie den Pfad an, in dem GridWeb temporäre Dateien speichert
type: docs
weight: 50
url: /de/net/gridweb-cache-files/
keywords: cache,session,storage
---
###  über den Datei-Cache
{{% alert color="primary" %}} 

Wenn der GridWeb-Sitzungsmodus ViewState ist, speichert es seine temporären Sitzungsdateien im Anwendungsbasisverzeichnis. Manchmal ist es nicht in Ordnung, temporäre Sitzungsdateien dort zu speichern, da das Anwendungsbasisverzeichnis möglicherweise keine Schreibberechtigungen dafür hat. In solchen Fällen löst GridWeb eine solche Ausnahme aus

{{< highlight "java" >}}

 [UnauthorizedAccessException: Access to

the path 'D:\inetpub\wwwroot\AsposeExcelTest\gwb_tempGridWeb1' is denied.]

{{< /highlight >}}

Die Lösung des oben genannten Problems besteht darin, Schreibzugriff auf das Anwendungsbasisverzeichnis zu gewähren oder den Pfad der temporären GridWeb-Sitzungsdateien mit Schreibzugriff mithilfe der Eigenschaft GridWeb.SessionStorePath zu ändern. Dieser Pfad sollte relativ zum Anwendungsbasisverzeichnis sein.

{{% /alert %}} 
####  **Geben Sie den Pfad an, in dem GridWeb temporäre Sitzungsdateien speichert**
Der folgende Beispielcode gibt den Pfad an, in dem GridWeb temporäre Sitzungsdateien speichert.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-SpecifySessionStorePath.aspx-SpecifySessionStorePath.cs" >}}

###  über den Bildcache

Wenn das Arbeitsblatt Formen/Bilder enthält, speichert GridWeb alle Formen/Bilder in einem Cache-Pfad

 Der Standard-Cache-Pfad lautet***System.Web.HttpContext.Current.Server.MapPath("/acwcache")***

 auch wir können verwenden***GridWeb.PictureCachePath*** um diesen Pfad auf einen bestimmten Pfad festzulegen.

Wenn wir eine Seite öffnen, löst GridWeb die angeforderte Bild-URL auf und ruft den Bildstream anhand der URL-ID aus dem Cache ab.

 zum Beispiel, wenn Ihre Seitenadresse ist*http://ip/mygridwebapp/test.aspx*  

Die von GridWeb generierte Bildanforderungs-URL lautet *http://ip/mygridwebapp/test.aspx/acw_image/imageid*.

####  Manchmal werden die Formen/Bilder bei der Verwendung nicht geladen[Freundliche URL](https://weblogs.asp.net/psheriff/using-friendly-urls-in-web-forms).

Sie müssen die Bild-URL-Anfrage überprüfen.

 Die normale Bildanfrage sieht wie folgt aus:*http://ip/mygridwebapp/test.aspx/acw_image/imageid*

aber Ihre Anfrage sieht so aus:*http://ip/mygridwebapp/test/acw_image/imageid*

Wenn Sie FriendlyUrl verwenden, müssen Sie die Bild-URL-Anfrage für GridWeb herausfiltern.

Somit kann der GridWeb-Steuerungsserver die Anfrage abrufen und auflösen und den Bildstream aus dem Cache-Pfad finden.

Beispielsweise gehen wir davon aus, dass Ihre Seiten-URL wie folgt aussieht:*http://ip/mygridwebapp/test.aspx*

Dann ist der folgende Code eine Problemumgehung, um dieses Problem zu beheben.
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





