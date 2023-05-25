---
title: GridWeb'in geçici dosyaları depoladığı yolu belirtin
type: docs
weight: 50
url: /tr/net/gridweb-cache-files/
keywords: cache,session,storage
---
###  dosya önbelleği hakkında
{{% alert color="primary" %}} 

GridWeb oturum modu ViewState olduğunda, geçici oturum dosyalarını Uygulama Temel Dizininde depolar. Bazen, Uygulama Temel Dizini üzerinde yazma izinleri olmayabileceğinden, geçici oturum dosyalarını burada depolamak uygun değildir. Bu gibi durumlarda, GridWeb böyle bir istisna atar.

{{< highlight "java" >}}

 [UnauthorizedAccessException: Access to

the path 'D:\inetpub\wwwroot\AsposeExcelTest\gwb_tempGridWeb1' is denied.]

{{< /highlight >}}

Yukarıdaki sorunun çözümü, Uygulama Temel Dizinine yazma erişimi vermek veya GridWeb.SessionStorePath özelliğini kullanarak yazma erişimi olan GridWeb geçici oturum dosyalarının yolunu değiştirmektir. Bu yol, Uygulama Temel Dizinine göre olmalıdır.

{{% /alert %}} 
####  **GridWeb'in geçici oturum dosyalarını depoladığı yolu belirtin**
Aşağıdaki örnek kod, GridWeb'in geçici oturum dosyalarını depoladığı yolu belirtir.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-SpecifySessionStorePath.aspx-SpecifySessionStorePath.cs" >}}

###  resim önbelleği hakkında

çalışma sayfasında şekiller/resimler olduğunda, GridWeb tüm şekli/resimleri bir önbellek yoluna kaydeder

 varsayılan önbellek yolu***System.Web.HttpContext.Current.Server.MapPath("/acwcache")***

 ayrıca kullanabiliriz***GridWeb.PictureCachePath*** bu yolu belirli bir yola ayarlamak için.

Bir sayfa açtığımızda, GridWeb istek görüntü url'sini çözecek ve görüntü akışını önbellekten url kimliği ile alacaktır.

 örneğin, sayfa adresiniz*http://ip/mygridwebapp/test.aspx*  

GridWeb tarafından oluşturulan görüntü isteği url'si *http://ip/mygridwebapp/test.aspx/acw_image/imageid* olacaktır.

####  kullandığınızda bazen şekiller/resimler yüklenmez[Dost URL'si](https://weblogs.asp.net/psheriff/using-friendly-urls-in-web-forms).

resim url isteğini kontrol etmeniz gerekiyor.

 normal resim isteği şöyle olacaktır:*http://ip/mygridwebapp/test.aspx/acw_image/imageid*

ancak isteğiniz şöyle: *http://ip/mygridwebapp/test/acw_image/imageid*

FriendlyUrl kullanıyorsanız, GridWeb için resim url isteğini filtrelemeniz gerekir.

böylece GridWeb kontrol sunucusu, isteği alıp çözebilir ve önbellek yolundan görüntü akışını bulabilir.

örneğin, sayfanızın url'sini şu şekilde varsayıyoruz:*http://ip/mygridwebapp/test.aspx*

o zaman aşağıdaki kod, bu sorunu çözmek için bir geçici çözümdür.
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





