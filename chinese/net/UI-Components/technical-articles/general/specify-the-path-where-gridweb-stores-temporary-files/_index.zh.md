---
title: 指定GridWeb存储临时文件的路径。
type: docs
weight: 50
url: /zh/net/aspose-cells-gridweb/gridweb-cache-files/
keywords: GridWeb,cache,session,storage
description: 本文描述了GridWeb的存储。
---
### 关于文件缓存
{{% alert color="primary" %}} 

当GridWeb会话模式是ViewState时，它将存储临时会话文件在应用基目录内。有时，在那里存储临时会话文件可能不允许，因为应用基目录可能没有写入权限。在这种情况下，GridWeb会抛出该异常。

{{< highlight java >}}

 [UnauthorizedAccessException: Access to

the path 'D:\inetpub\wwwroot\AsposeExcelTest\gwb_tempGridWeb1' is denied.]

{{< /highlight >}}

解决上述问题的办法是给予应用基目录写入权限，或者使用GridWeb.SessionStorePath属性改变GridWeb临时会话文件的路径。该路径应该是相对于应用基目录的。

{{% /alert %}} 
#### **指定GridWeb存储临时会话文件的路径。**
以下示例代码指定了GridWeb存储临时会话文件的路径。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-SpecifySessionStorePath.aspx-SpecifySessionStorePath.cs" >}}

### 关于图片缓存

当工作表中有形状/图片时，GridWeb会将所有形状/图片保存在缓存路径中。

默认的缓存路径是***System.Web.HttpContext.Current.Server.MapPath("/acwcache")***。

我们也可以使用***GridWeb.PictureCachePath***来将该路径设置为特定路径。

当我们打开一个页面时，GridWeb会解析请求的图像URL，并根据URL ID从缓存中获取图像流。

例如，如果您的页面地址是*http://ip/mygridwebapp/test.aspx*  

GridWeb生成的图像请求URL将会是*http://ip/mygridwebapp/test.aspx/acw_image/imageid*。

#### 有时，当您使用[Friendly Url](https://weblogs.asp.net/psheriff/using-friendly-urls-in-web-forms)时，形状/图片加载失败。

您需要检查图像URL请求。

正常的图像请求应该像这样：*http://ip/mygridwebapp/test.aspx/acw_image/imageid*。

但是您的请求可能是这样的：*http://ip/mygridwebapp/test/acw_image/imageid*。

如果您使用 FriendlyUrl，您需要过滤掉 GridWeb 请求中的图片 URL。

这样 GridWeb 控件服务器就可以获取和解析请求，并从缓存路径中找到图像流。

举个例子，假设您的页面 URL 如下：*http://ip/mygridwebapp/test.aspx*

那么下面的代码就是一种解决这种问题的方法。
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





