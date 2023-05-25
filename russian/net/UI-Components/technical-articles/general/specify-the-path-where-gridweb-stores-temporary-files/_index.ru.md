---
title: Укажите путь, по которому GridWeb хранит временные файлы.
type: docs
weight: 50
url: /ru/net/gridweb-cache-files/
keywords: cache,session,storage
---
###  про файловый кеш
{{% alert color="primary" %}} 

Когда режим сеанса GridWeb — ViewState, он сохраняет свои временные файлы сеанса в базовом каталоге приложения. Иногда хранить там временные файлы сеансов недопустимо, поскольку базовый каталог приложений может не иметь прав на запись в него. В таких случаях GridWeb выдает такое исключение

{{< highlight "java" >}}

 [UnauthorizedAccessException: Access to

the path 'D:\inetpub\wwwroot\AsposeExcelTest\gwb_tempGridWeb1' is denied.]

{{< /highlight >}}

Решение вышеуказанной проблемы состоит в том, чтобы предоставить доступ на запись к базовому каталогу приложений или изменить путь к временным файлам сеанса GridWeb, имеющим доступ на запись, с помощью свойства GridWeb.SessionStorePath. Этот путь должен относиться к базовому каталогу приложений.

{{% /alert %}} 
####  **Укажите путь, по которому GridWeb хранит временные файлы сеансов.**
В следующем примере кода указывается путь, по которому GridWeb хранит временные файлы сеансов.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-SpecifySessionStorePath.aspx-SpecifySessionStorePath.cs" >}}

###  о кэше картинок

когда на листе есть фигуры/изображения, GridWeb сохранит все фигуры/изображения в пути кэша.

 путь к кешу по умолчанию***System.Web.HttpContext.Current.Server.MapPath("/acwcache")***

 также мы можем использовать***GridWeb.PictureCachePath*** чтобы установить этот путь на определенный путь.

когда мы открываем страницу, GridWeb разрешает URL-адрес изображения запроса и получает поток изображения из кеша по идентификатору URL-адреса.

 например, если адрес вашей страницы*http://ip/mygridwebapp/test.aspx*  

URL-адрес запроса изображения, сгенерированный GridWeb, будет *http://ip/mygridwebapp/test.aspx/acw_image/imageid*.

####  иногда формы/изображения не загружаются при использовании[Дружественный URL](https://weblogs.asp.net/psheriff/using-friendly-urls-in-web-forms).

вам нужно проверить запрос URL-адреса изображения.

 обычный запрос изображения должен выглядеть так:*http://ip/mygridwebapp/test.aspx/acw_image/imageid*

но ваш запрос выглядит так: *http://ip/mygridwebapp/test/acw_image/imageid*

если вы используете FriendlyUrl, вам необходимо отфильтровать запрос URL-адреса изображения для GridWeb.

таким образом, управляющий сервер GridWeb может получить и разрешить запрос, а также найти поток изображения из пути кэша.

например, мы предполагаем, что URL-адрес вашей страницы выглядит следующим образом: *http://ip/mygridwebapp/test.aspx*

тогда приведенный ниже код является обходным путем для решения этой проблемы.
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





