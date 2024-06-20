---
title: Ange sökvägen där GridWeb lagrar temporära filer
type: docs
weight: 50
url: /sv/net/aspose-cells-gridweb/gridweb-cache-files/
keywords: GridWeb,cache,session,lagring
description: Denna artikel beskriver lagringen i GridWeb.
---
### om filcache
{{% alert color="primary" %}} 

När GridWeb-sessionläget är ViewState lagrar den sina temporära sessionfiler inuti Application Base Directory. Ibland är det inte OK att lagra temporära sessionfiler där eftersom Application Base Directory kanske inte har skrivbehörighet på den. I sådana fall kastar GridWeb ett sådant undantag

{{< highlight java >}}

 [UnauthorizedAccessException: Access to

the path 'D:\inetpub\wwwroot\AsposeExcelTest\gwb_tempGridWeb1' is denied.]

{{< /highlight >}}

Lösningen på ovanstående problem är att ge skrivåtkomst till Application Base Directory eller ändra sökvägen för GridWebs temporära sessionfiler med skrivåtkomst med hjälp av egenskapen GridWeb.SessionStorePath. Denna sökväg ska vara relativ till Application Base Directory.

{{% /alert %}} 
#### **Ange sökvägen där GridWeb lagrar temporära sessionfiler**
Följande kodexempel specificerar sökvägen där GridWeb lagrar temporära sessionfiler.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-SpecifySessionStorePath.aspx-SpecifySessionStorePath.cs" >}}

### om bildcache

när det finns former/bilder i kalkylarket, sparar GridWeb alla former/bilder till en cachad sökväg

standard-cach-sökvägen är ***System.Web.HttpContext.Current.Server.MapPath("/acwcache")***

vi kan också använda ***GridWeb.PictureCachePath*** för att ange denna sökväg till en specifik sökväg.

när vi öppnar en sida kommer GridWeb att lösa förfrågningsbildens URL och hämta bildströmmen från cachen via URL:en.

till exempel, om din sidadress är *http://ip/mygridwebapp/test.aspx*  

bildförfrågnings-URL:en som genereras av GridWeb kommer att vara *http://ip/mygridwebapp/test.aspx/acw_image/imageid*.

#### ibland laddas inte formerna/bilderna när du använder [Friendly Url](https://weblogs.asp.net/psheriff/using-friendly-urls-in-web-forms).

du måste kontrollera bildens URL-begäran.

den normala bildbegäran bör se ut så här: *http://ip/mygridwebapp/test.aspx/acw_image/imageid*

men din förfrågan går så här :*http://ip/mygridwebapp/test/acw_image/imageid*

om du använder FriendlyUrl måste du filtrera bort bildens URL-begäran för GridWeb.

så kan GridWeb kontrollserver hämta och lösa begäran och hitta bildströmmen från cachsökvägen.

till exempel antar vi att din sidadress ser ut så här:*http://ip/mygridwebapp/test.aspx*

nedan är koden ett workaround för att åtgärda ett sådant problem.
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





