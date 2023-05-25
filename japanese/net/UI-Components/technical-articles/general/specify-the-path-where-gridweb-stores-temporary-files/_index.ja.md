---
title: GridWebが一時ファイルを保存するパスを指定します
type: docs
weight: 50
url: /ja/net/gridweb-cache-files/
keywords: cache,session,storage
---
### ファイルキャッシュについて
{{% alert color="primary" %}} 

GridWeb セッション モードが ViewState の場合、一時セッション ファイルはアプリケーション ベース ディレクトリ内に保存されます。場合によっては、アプリケーション ベース ディレクトリに書き込み権限がない可能性があるため、一時セッション ファイルをそこに保存することが適切ではないことがあります。このような場合、GridWeb はそのような例外をスローします

{{< highlight "java" >}}

 [UnauthorizedAccessException: Access to

the path 'D:\inetpub\wwwroot\AsposeExcelTest\gwb_tempGridWeb1' is denied.]

{{< /highlight >}}

上記の問題の解決策は、アプリケーション ベース ディレクトリへの書き込みアクセスを付与するか、GridWeb.SessionStorePath プロパティを使用して書き込みアクセスを持つ GridWeb 一時セッション ファイルのパスを変更することです。このパスは、アプリケーション ベース ディレクトリに対する相対パスである必要があります。

{{% /alert %}} 
####  **GridWebが一時セッションファイルを保存するパスを指定します**
次のサンプル コードでは、GridWeb が一時セッション ファイルを保存するパスを指定します。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-SpecifySessionStorePath.aspx-SpecifySessionStorePath.cs" >}}

### 画像キャッシュについて

ワークシートに図形/画像がある場合、GridWeb はすべての図形/画像をキャッシュ パスに保存します

デフォルトのキャッシュパスは***System.Web.HttpContext.Current.Server.MapPath("/acwcache")***

私たちも使うことができます***GridWeb.PictureCachePath***このパスを特定のパスに設定します。

ページを開くと、GridWeb はリクエストの画像 URL を解決し、URL ID によってキャッシュから画像ストリームを取得します。

たとえば、ページアドレスが次の場合、*http://ip/mygridwebapp/test.aspx*  

GridWeb によって生成される画像リクエストの URL は *http://ip/mygridwebapp/test.aspx/acw_image/imageid* になります。

#### を使用すると、図形や画像が読み込まれない場合があります。[フレンドリー URL](https://weblogs.asp.net/psheriff/using-friendly-urls-in-web-forms).

画像 URL リクエストを確認する必要があります。

通常の画像リクエストは次のようになります。*http://ip/mygridwebapp/test.aspx/acw_image/imageid*

しかし、あなたのリクエストは次のようになります:*http://ip/mygridwebapp/test/acw_image/imageid*

FriendlyUrl を使用する場合は、GridWeb の画像 URL リクエストをフィルターで除外する必要があります。

したがって、GridWeb コントロール サーバーはリクエストを取得して解決し、キャッシュ パスからイメージ ストリームを見つけることができます。

たとえば、ページの URL は次のように仮定します:*http://ip/mygridwebapp/test.aspx*

以下のコードは、そのような問題を解決するための回避策です。
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





