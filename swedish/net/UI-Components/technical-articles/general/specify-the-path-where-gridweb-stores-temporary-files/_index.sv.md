---
title: Ange sökvägen där GridWeb lagrar temporära filer
type: docs
weight: 50
url: /sv/net/gridweb-cache-files/
keywords: cache,session,storage
---
###  om filcache
{{% alert color="primary" %}} 

När GridWeb-sessionsläget är ViewState, lagrar det sina temporära sessionsfiler i Application Base Directory. Ibland är det inte OK att lagra temporära sessionsfiler där eftersom Application Base Directory kanske inte har skrivbehörighet på den. I sådana fall gör GridWeb ett sådant undantag

{{< highlight "java" >}}

 [UnauthorizedAccessException: Access to

the path 'D:\inetpub\wwwroot\AsposeExcelTest\gwb_tempGridWeb1' is denied.]

{{< /highlight >}}

Lösningen på ovanstående problem är att ge skrivåtkomst till Application Base Directory eller ändra sökvägen till GridWebs temporära sessionsfiler med skrivåtkomst med hjälp av egenskapen GridWeb.SessionStorePath. Den här sökvägen bör vara relativ till Application Base Directory.

{{% /alert %}} 
####  **Ange sökvägen där GridWeb lagrar temporära sessionsfiler**
Följande exempelkod anger sökvägen där GridWeb lagrar temporära sessionsfiler.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-SpecifySessionStorePath.aspx-SpecifySessionStorePath.cs" >}}

###  om bildcache

när det finns former/bilder i kalkylbladet kommer GridWeb att spara alla former/bilder till en cache-sökväg

 standardcache-sökvägen är***System.Web.HttpContext.Current.Server.MapPath("/acwcache")***

 vi kan också använda***GridWeb.PictureCachePath*** för att ställa in den här sökvägen till en specifik sökväg.

när vi öppnar en sida kommer GridWeb att lösa begäran om bild-url och hämta bildströmmen från cachen med url-id.

 till exempel om din sidadress är*http://ip/mygridwebapp/test.aspx*  

webbadressen för bildbegäran som genereras av GridWeb kommer att vara *http://ip/mygridwebapp/test.aspx/acw_image/imageid*.

####  ibland laddas inte formerna/bilderna när du använder[Vänlig URL](https://weblogs.asp.net/psheriff/using-friendly-urls-in-web-forms).

du måste kontrollera bildens webbadressbegäran.

 den normala bildbegäran ska vara så här:*http://ip/mygridwebapp/test.aspx/acw_image/imageid*

men din begäran ser ut så här:*http://ip/mygridwebapp/test/acw_image/imageid*

om du använder FriendlyUrl måste du filtrera bort webbadressbegäran för bilden för GridWeb.

sålunda kan GridWebs kontrollserver hämta och lösa begäran och hitta bildströmmen från cachesökvägen.

till exempel antar vi din sidas url så här:*http://ip/mygridwebapp/test.aspx*

koden nedan är en lösning för att lösa ett sådant problem.
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





