---
title: GridWeb が一時セッション ファイルを保存するパスを指定します
type: docs
weight: 50
url: /ja/net/specify-the-path-where-gridweb-stores-temporary-session-files/
---
{{% alert color="primary" %}} 

GridWeb セッション モードが ViewState の場合、一時セッション ファイルはアプリケーション ベース ディレクトリ内に格納されます。 Application Base Directory に書き込み権限がない可能性があるため、一時セッション ファイルをそこに保存しても問題ない場合があります。そのような場合、GridWeb はそのような例外をスローします。

{{< highlight "java" >}}

 [UnauthorizedAccessException: Access to

the path 'D:\inetpub\wwwroot\AsposeExcelTest\gwb_tempGridWeb1' is denied.]{{< /highlight >}}

上記の問題の解決策は、Application Base Directory への書き込みアクセス権を付与するか、GridWeb.SessionStorePath プロパティを使用して書き込みアクセス権を持つ GridWeb 一時セッション ファイル パスを変更することです。このパスは、アプリケーション ベース ディレクトリからの相対パスである必要があります。

{{% /alert %}} 
## **GridWeb が一時セッション ファイルを保存するパスを指定します**
次のサンプル コードは、GridWeb が一時セッション ファイルを格納するパスを指定します。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-SpecifySessionStorePath.aspx-SpecifySessionStorePath.cs" >}}
