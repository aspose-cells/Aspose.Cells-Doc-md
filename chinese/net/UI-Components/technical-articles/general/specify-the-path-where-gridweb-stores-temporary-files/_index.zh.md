---
title: 指定GridWeb存储临时文件的路径
type: docs
weight: 50
url: /zh/net/aspose-cells-gridweb/gridweb-cache-files/
keywords: GridWeb，缓存，会话，存储
description: 本文介绍了GridWeb中的存储。
---
### 关于文件缓存
{{% alert color="primary" %}} 

当GridWeb会话模式为ViewState时，它将其临时会话文件存储在应用程序基本目录中。有时，在应用程序基本目录上可能没有写入权限，所以无法在那里存储临时会话文件。在这种情况下，GridWeb会抛出此类异常

{{< highlight java >}}

 [UnauthorizedAccessException: Access to

the path 'D:\inetpub\wwwroot\AsposeExcelTest\gwb_tempGridWeb1' is denied.]

{{< /highlight >}}

解决上述问题的方法是在应用程序基本目录中授予写入访问权限或使用GridWeb.SessionStorePath属性更改GridWeb临时会话文件的路径。此路径应相对于应用程序基本目录。

{{% /alert %}} 
#### **指定GridWeb存储临时会话文件的路径**
以下示例代码指定了GridWeb存储临时会话文件的路径。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-SpecifySessionStorePath.aspx-SpecifySessionStorePath.cs" >}}

### 关于图片缓存

当工作表中存在形状/图片时，GridWeb将所有形状/图片保存到缓存路径

默认的缓存路径为***System.Web.HttpContext.Current.Server.MapPath("/acwcache")***

也可以使用***GridWeb.PictureCachePath***将此路径设置为特定路径。

当我们打开页面时，GridWeb会解析请求图片的URL，并通过ID从缓存中获取图像流。

例如，如果您的页面地址是*http://ip/mygridwebapp/test.aspx*  

GridWeb生成的图像请求URL将是*http://ip/mygridwebapp/test.aspx/acw_image/imageid*。

#### 使用[Friendly Url](https://weblogs.asp.net/psheriff/using-friendly-urls-in-web-forms)时，有时形状/图片没有加载。

您需要检查图像URL请求。

正常的图像请求应该是这样的：*http://ip/mygridwebapp/test.aspx/acw_image/imageid*

但您的请求是这样的：*http://ip/mygridwebapp/test/acw_image/imageid*

如果您使用FriendlyUrl，您需要过滤掉GridWeb的图片URL请求。

这样，GridWeb控件服务器可以获取和解析请求，并从缓存路径中找到图像流。

例如，我们假设您的页面URL为：*http://ip/mygridwebapp/test.aspx*

然后下面的代码是一个解决这个问题的解决方法。
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





