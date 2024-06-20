---
title: GridWebが一時ファイルを保存するパスを指定する
type: docs
weight: 50
url: /ja/net/aspose-cells-gridweb/gridweb-cache-files/
keywords: GridWeb,キャッシュ,セッション,ストレージ
description: この記事では、GridWebのストレージについて説明します。
---
### ファイルキャッシュについて
{{% alert color="primary" %}} 

GridWebセッションモードがViewStateの場合、一時セッションファイルはアプリケーションベースディレクトリ内に保存されます。アプリケーションベースディレクトリには書き込み権限がない場合があり、そのような場合、GridWebはそのような例外をスローします。

{{< highlight java >}}

 [UnauthorizedAccessException: Access to

the path 'D:\inetpub\wwwroot\AsposeExcelTest\gwb_tempGridWeb1' is denied.]

{{< /highlight >}}

上記の問題への解決策は、アプリケーションベースディレクトリに書き込みアクセスを与えるか、GridWeb.SessionStorePathプロパティを使用して書き込みアクセスのあるGridWeb一時セッションファイルのパスを変更することです。このパスは、アプリケーションベースディレクトリに対する相対パスである必要があります。

{{% /alert %}} 
#### **GridWebが一時セッションファイルを保存するパスを指定する**
以下のサンプルコードは、GridWebが一時セッションファイルを保存するパスを指定しています。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-SpecifySessionStorePath.aspx-SpecifySessionStorePath.cs" >}}

### 画像キャッシュについて

ワークシートに図形/画像がある場合、GridWebはすべての図形/画像をキャッシュパスに保存します

デフォルトのキャッシュパスは***System.Web.HttpContext.Current.Server.MapPath("/acwcache")***

また、***GridWeb.PictureCachePath***を使用して、このパスを特定のパスに設定することもできます。

ページを開くと、GridWebはリクエスト画像URLを解決し、URL IDによってキャッシュから画像ストリームを取得します。

たとえば、ページのアドレスが*http://ip/mygridwebapp/test.aspx*の場合  

GridWebによって生成された画像リクエストURLは*http://ip/mygridwebapp/test.aspx/acw_image/imageid*になります。

#### 時には、[Friendly Url](https://weblogs.asp.net/psheriff/using-friendly-urls-in-web-forms)を使用すると、図形/画像が読み込まれないことがあります。

画像URLのリクエストを確認する必要があります。

通常の画像リクエストは次のようになります:*http://ip/mygridwebapp/test.aspx/acw_image/imageid*

ただし、リクエストが次のようになる場合:*http://ip/mygridwebapp/test/acw_image/imageid*

FriendlyUrlを使用する場合、GridWebの画像URLのリクエストをフィルタリングする必要があります。

したがって、GridWebコントロールサーバーはリクエストを取得し、解決し、キャッシュパスから画像ストリームを見つけることができます。

たとえば、ページのURLが次のような場合:*http://ip/mygridwebapp/test.aspx*

次に、以下のコードはそのような問題を修正するための回避策です。
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





