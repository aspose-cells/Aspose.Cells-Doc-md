---
title: GridWeb のデフォルト アイコンの代わりに独自のアイコンを使用する
type: docs
weight: 10
url: /ja/net/using-your-own-icons-instead-of-the-gridweb-default-icons/
---
{{% alert color="primary" %}} 

Aspose.Cells.GridWeb コントロールの既定のアイコンの代わりに、独自のアイコン (画像) を使用したい場合があります。この記事では、これを行う方法について説明します。

{{% /alert %}} 

コントロールのデフォルト アイコンは、URL パス "/acw" にあります。_client/". ファイル パスは、"C:\Program Files\Aspose\Aspose.Cells for .NET\acw_そのフォルダーには、submit.gif、save.gif などのファイルがあります。これらの画像を独自の画像に置き換えたい場合は、Web アプリケーションの web.config ファイルに config セクションを追加します。

**XML**

{{< highlight "csharp" >}}

 <appSettings>

 <add key="Aspose.Cells.GridWeb.acw_client_path" value="/acw_client/" />

</appSettings>



{{< /highlight >}}

この構成はコントロール イメージ パスにのみ影響し、コントロールのクライアント スクリプト パスには影響しないことに気付いたかもしれません。たとえば、GridWeb コントロールを使用してページを実行し、ブラウザでソース ファイルを確認すると、acw が_クライアント_グリッドの DIV 要素のパス プロパティには、まだ「/yourApp/webform1.aspx/」と表示されています。場合によっては、クライアント スクリプト パスの再定義が必要になることがあります。コントロールが再定義されたイメージ パスをクライアント スクリプト パスとして使用するように強制するには、appSettings セクションに別の構成設定を追加します。
**XML**

{{< highlight "csharp" >}}

 <add key="Aspose.Cells.GridWeb.force_script_path" value="true" />



{{< /highlight >}}

{{% alert color="primary" %}} 

この構成は、ライセンスされたコントロールでのみ有効になります。

{{% /alert %}}
