---
title: Geçici dosyaların depolandığı yolunu belirleyin
type: docs
weight: 50
url: /tr/net/aspose-cells-gridweb/gridweb-cache-files/
keywords: GridWeb,önbellek,oturum,depolama
description: Bu makale, GridWeb de depolamayı açıklar.
---
### dosya önbelleği hakkında
{{% alert color="primary" %}} 

GridWeb oturum modu ViewState olduğunda, geçici oturum dosyalarını Uygulama Taban Dizininde saklar. Bazen, bu tür geçici oturum dosyalarını saklamak uygun olmayabilir çünkü Uygulama Taban Dizinine yazma izni olmayabilir. Bu durumlarda, GridWeb bu tür bir istisna fırlatır.

{{< highlight java >}}

 [UnauthorizedAccessException: Access to

the path 'D:\inetpub\wwwroot\AsposeExcelTest\gwb_tempGridWeb1' is denied.]

{{< /highlight >}}

Yukarıdaki problemi çözmenin çözümü, Uygulama Taban Dizinine yazma erişimi vermek veya GridWeb.SessionStorePath özelliğini kullanarak yazma erişimi olan GridWeb geçici oturum dosyalarının yolunu değiştirmektir. Bu yol, Uygulama Taban Dizinine göre göreli olmalıdır.

{{% /alert %}} 
#### **Geçici oturum dosyalarını sakladığı yolunu belirtin**
Aşağıdaki örnek kod, GridWeb'in geçici oturum dosyalarını depoladığı yolu belirtir.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-SpecifySessionStorePath.aspx-SpecifySessionStorePath.cs" >}}

### resim önbelleği hakkında

Çalışma sayfasında şekil/resim bulunduğunda, GridWeb tüm şekil/resimleri bir önbellek yolu belirtir.

Varsayılan önbellek yolu ***System.Web.HttpContext.Current.Server.MapPath("/acwcache")***'dir.

Ayrıca, bu yolu belirlemek için ***GridWeb.PictureCachePath*** kullanabiliriz.

Bir sayfa açtığımızda, GridWeb isteğe bağlı resim URL'sini çözecek ve URL kimliğine göre önbellekten resim akışını alacaktır.

Örneğin, sayfa adresiniz *http://ip/mygridwebapp/test.aspx* ise  

GridWeb tarafından oluşturulan resim isteği URL'si *http://ip/mygridwebapp/test.aspx/acw_image/imageid* olacaktır.

#### bazen [Dostça URL](https://weblogs.asp.net/psheriff/using-friendly-urls-in-web-forms) kullanırken şekil/resimler yüklenmez.

Resim URL isteğini kontrol etmeniz gerekir.

Normal resim isteği şöyle olmalıdır: *http://ip/mygridwebapp/test.aspx/acw_image/imageid*

Ancak isteğiniz şöyle olmalıdır: *http://ip/mygridwebapp/test/acw_image/imageid*

Dostça URL kullanıyorsanız, GridWeb için resim URL isteğini filtrelemeniz gerekir.

Böylece GridWeb kontrol sunucusu isteği çözebilir ve önbellek yolundan resim akışını bulabilir.

Örneğin, sayfa URL'niz şöyle varsayalım: *http://ip/mygridwebapp/test.aspx*

Sonra aşağıdaki kod, bu tür bir sorunu düzeltmek için bir çözüm yolu sağlar.
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





