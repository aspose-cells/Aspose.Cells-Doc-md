---
title: Geben Sie den Pfad an, an dem GridWeb temporäre Dateien speichert
type: docs
weight: 50
url: /de/net/aspose-cells-gridweb/gridweb-cache-files/
keywords: GridWeb,cache,Sitzung,Speicher
description: Dieser Artikel beschreibt den Speicher in GridWeb.
---
### zum Datei-Cache
{{% alert color="primary" %}} 

Wenn der GridWeb-Sitzungsmodus ViewState ist, speichert er seine temporären Sitzungsdateien im Anwendungs-Basisverzeichnis. Manchmal ist es nicht in Ordnung, temporäre Sitzungsdateien dort zu speichern, da das Anwendungs-Basisverzeichnis möglicherweise keine Schreibberechtigungen hat. In solchen Fällen wirft GridWeb eine solche Ausnahme

{{< highlight java >}}

 [UnauthorizedAccessException: Access to

the path 'D:\inetpub\wwwroot\AsposeExcelTest\gwb_tempGridWeb1' is denied.]

{{< /highlight >}}

Die Lösung für das obige Problem besteht darin, dem Anwendungs-Basisverzeichnis Schreibzugriff zu gewähren oder den Pfad für temporäre Sitzungsdateien von GridWeb zu ändern und Schreibzugriff zu haben, indem die Eigenschaft GridWeb.SessionStorePath verwendet wird. Dieser Pfad sollte relativ zum Anwendungs-Basisverzeichnis sein.

{{% /alert %}} 
#### **Geben Sie den Pfad an, an dem GridWeb temporäre Sitzungsdateien speichert**
Der folgende Beispielcode gibt den Pfad an, an dem GridWeb temporäre Sitzungsdateien speichert.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-SpecifySessionStorePath.aspx-SpecifySessionStorePath.cs" >}}

### zum Bild-Cache

Wenn es Formen/Bilder im Arbeitsblatt gibt, speichert GridWeb alle Formen/Bilder in einem Cache-Pfad

Der Standard-Cache-Pfad ist ***System.Web.HttpContext.Current.Server.MapPath("/acwcache")***

Auch können wir ***GridWeb.PictureCachePath*** verwenden, um diesen Pfad auf einen bestimmten Pfad festzulegen.

Wenn wir eine Seite öffnen, wird GridWeb die angeforderte Bild-URL auflösen und den Bild-Stream aus dem Cache anhand der URL-ID abrufen.

Beispielsweise, wenn Ihre Seitenadresse *http://ip/meinegridwebanwendung/test.aspx* lautet  

Die von GridWeb generierte Bildanforderungs-URL wird *http://ip/meinegridwebanwendung/test.aspx/acw_image/imageid* lauten.

#### Manchmal werden Formen/Bilder nicht geladen, wenn Sie [Freundliche URLs](https://weblogs.asp.net/psheriff/using-friendly-urls-in-web-forms) verwenden.

Sie müssen die Bild-URL-Anfrage überprüfen.

Die normale Bildanforderung sollte so aussehen: *http://ip/mygridwebapp/test.aspx/acw_image/imageid*

Aber Ihre Anforderung sieht so aus: *http://ip/mygridwebapp/test/acw_image/imageid*

Wenn Sie FriendlyUrl verwenden, müssen Sie die Bild-URL-Anforderung für GridWeb filtern.

Daher kann die GridWeb-Steuerungsserver die Anforderung erhalten und auflösen und den Bildstream aus dem Cache-Pfad finden.

Beispiel: Wir nehmen an, dass die URL Ihrer Seite so aussieht: *http://ip/mygridwebapp/test.aspx*

Dann ist der folgende Code ein Workaround, um ein solches Problem zu beheben.
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





