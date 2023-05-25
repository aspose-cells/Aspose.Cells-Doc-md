---
title: 指定 GridWeb 存放临时文件的路径
type: docs
weight: 50
url: /zh/net/gridweb-cache-files/
keywords: cache,session,storage
---
### 关于文件缓存
{{% alert color="primary" %}} 

当 GridWeb 会话模式为 ViewState 时，它将其临时会话文件存储在应用程序基目录中。有时，将临时会话文件存储在那里是不可行的，因为应用程序基目录可能没有对其的写权限。在这种情况下，GridWeb 会抛出这样的异常

{{< highlight "java" >}}

 [UnauthorizedAccessException: Access to

the path 'D:\inetpub\wwwroot\AsposeExcelTest\gwb_tempGridWeb1' is denied.]

{{< /highlight >}}

上述问题的解决方案是使用 GridWeb.SessionStorePath 属性授予对应用程序基本目录的写入权限或更改具有写入权限的 GridWeb 临时会话文件路径。此路径应相对于应用程序基目录。

{{% /alert %}} 
####  **指定 GridWeb 存放临时会话文件的路径**
以下示例代码指定了 GridWeb 存储临时会话文件的路径。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-SpecifySessionStorePath.aspx-SpecifySessionStorePath.cs" >}}

### 关于图片缓存

当工作表中有形状/图片时，GridWeb会将所有的形状/图片保存到一个缓存路径

默认缓存路径是***System.Web.HttpContext.Current.Server.MapPath("/acwcache")***

我们也可以使用***GridWeb.图片缓存路径***将此路径设置为特定路径。

当我们打开一个页面时，GridWeb 会解析请求的图片 url，并通过 url id 从缓存中获取图片流。

例如，如果您的页面地址是*http://ip/mygridwebapp/test.aspx*  

GridWeb 生成的图像请求 url 将是 *http://ip/mygridwebapp/test.aspx/acw_image/imageid*。

#### 有时使用时未加载形状/图片[友好网址](https://weblogs.asp.net/psheriff/using-friendly-urls-in-web-forms).

您需要检查图片网址请求。

正常的图片请求应该是这样的：*http://ip/mygridwebapp/test.aspx/acw_image/imageid*

但是你的请求是这样的：*http://ip/mygridwebapp/test/acw_image/imageid*

如果您使用 FriendlyUrl，则需要过滤掉 GridWeb 的图像 url 请求。

这样 GridWeb 控制服务器就可以获取并解析请求，并从缓存路径中找到图像流。

例如，我们假定您的页面 url 如下：*http://ip/mygridwebapp/test.aspx*

那么下面的代码是解决此类问题的解决方法。
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





