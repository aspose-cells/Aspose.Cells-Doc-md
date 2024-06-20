---
title: Укажите путь, где GridWeb хранит временные файлы.
type: docs
weight: 50
url: /ru/net/aspose-cells-gridweb/gridweb-cache-files/
keywords: GridWeb,кеш,сессия,хранилище
description: Эта статья описывает хранение в GridWeb.
---
### о файловом кеше
{{% alert color="primary" %}} 

Когда режим сессии GridWeb установлен как ViewState, он хранит свои временные файлы сессии внутри каталога базового приложения. Иногда нельзя хранить временные файлы сессии там, поскольку каталог базового приложения может не иметь разрешений на запись. В таких случаях GridWeb генерирует такое исключение.

{{< highlight java >}}

 [UnauthorizedAccessException: Access to

the path 'D:\inetpub\wwwroot\AsposeExcelTest\gwb_tempGridWeb1' is denied.]

{{< /highlight >}}

Решение проблемы заключается в предоставлении прав на запись в каталог базового приложения или изменении пути временных файлов сессии GridWeb с правами на запись с помощью свойства GridWeb.SessionStorePath. Этот путь должен быть относительным к каталогу базового приложения.

{{% /alert %}} 
#### **Укажите путь, где GridWeb хранит временные файлы сессии.**
В следующем примере кода указывается путь, где GridWeb хранит временные файлы сессии.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-SpecifySessionStorePath.aspx-SpecifySessionStorePath.cs" >}}

### о кеше изображений

когда в рабочем листе есть фигуры/изображения, GridWeb сохранит все фигуры/изображения по пути кеша

путь кеша по умолчанию - ***System.Web.HttpContext.Current.Server.MapPath("/acwcache")***

также мы можем использовать ***GridWeb.PictureCachePath*** для установки этого пути в конкретный путь.

при открытии страницы GridWeb разрешит запрошенный URL изображения и получит поток изображения из кеша по идентификатору URL.

например, если адрес вашей страницы *http://ip/mygridwebapp/test.aspx*  

сгенерированный GridWeb URL запроса изображения будет *http://ip/mygridwebapp/test.aspx/acw_image/imageid*.

#### иногда фигуры/изображения не загружаются, когда используются [Friendly Url](https://weblogs.asp.net/psheriff/using-friendly-urls-in-web-forms).

вам нужно проверить URL-адрес запроса изображения.

нормальный запрос изображения должен выглядеть так: *http://ip/mygridwebapp/test.aspx/acw_image/imageid*

но ваш запрос выглядит так: *http://ip/mygridwebapp/test/acw_image/imageid*

если вы используете FriendlyUrl, вам нужно фильтровать запросы изображений для GridWeb.

таким образом, серверное управление GridWeb может получить и обработать запрос, а затем найти поток изображения из кеша.

например, допустим, что URL вашей страницы выглядит так: *http://ip/mygridwebapp/test.aspx*

тогда приведенный ниже код - это обходной путь для решения таких проблем.
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





