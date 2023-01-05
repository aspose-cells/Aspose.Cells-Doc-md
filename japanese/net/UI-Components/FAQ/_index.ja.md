---
title: よくある質問
type: docs
weight: 400
url: /ja/net/grid-faq/
---
## **Aspose.Cells Grid Controls の評価版に制限はありますか?**
いいえ、Aspose.Cells Grid Controls の評価版には機能の制限はありません。評価版は、追加のワークシートを追加することを除いて、ライセンス版の全機能を提供します (**評価著作権に関する警告** ) を出力ファイルに追加します。
## **市場には非常に多くのグリッド コントロールがあります。なぜ Aspose.Cells Grid Controls を購入する必要があるのですか?**
 Aspose.Cells グリッド コントロールは、あらゆる種類のユーザーにとって手頃な価格で提供されています。非常にリーズナブルな価格で、Windows と Web アプリケーションで動作する 2 つのコントロールのスイートを提供します。さらに、それは単なるグリッドではなく、あなたの**スプレッドシート ビューアー、エディター、クリエーター**同時に。任意の種類のデータ ソース (通常のグリッド コントロールなど) にバインドできるだけでなく、Excel ファイルを作成および管理することもできます。また、強力でリッチな**式計算エンジン**組み込み関数 (Aspose.Cells グリッド コントロールでサポート) だけでなく、ユーザーが定義したカスタム式も計算できます。 Aspose.Cells Grid スイートには、ここでは説明しきれない機能が多数あります。詳細な機能リストについては、エディションの種類のページを参照してください。
## **最近、Aspose.Cells Grid Controls のライセンスを購入しました。 Aspose.Cells Grid Control を使用するアプリケーションでそのライセンスを使用するにはどうすればよいですか?**
を参照してください。[ライセンス](/cells/ja/net/licensing/) Aspose.Cells のページ グリッド コントロール。アプリケーションで Aspose.Cells Grid Controls のライセンスを使用する方法についての完全な詳細を提供します。
## **Aspose.Cells グリッド コントロールは Visual Studio.NET 2005 でサポートされていますか?**
はい、Aspose.Cells グリッド コントロールは、Visual Studio.NET 2005 以降のバージョンで完全にサポートされています。
## **Visual Studio.NET 2005 を使用して、Web サイトで Aspose.Cells.GridWeb コントロールを使用していますが、まったく機能していません。どうしたの？**
 Aspose.Cells.GridWeb は両方をサポート**ファイルシステム**と**HTTP**まだ混乱している場合は、Visual Studio.NET 2005 を使用して Aspose.Cells.GridWeb を操作するためのステップ バイ ステップ ガイドを参照してください。
## **Aspose.Cells.GridWeb ベースの Web プロジェクト/ソリューションをサーバーにデプロイするにはどうすればよいですか?**
GridWeb コントロールを持つ Web アプリケーションをデプロイする必要がある場合は、「acw_client" ディレクトリをプロジェクト フォルダーに追加してください。少なくとも、Web アプリケーション (サーバー上にデプロイされた) はそれを見つけることができませんでした。次のコード行を構成セクションに追加することで、スクリプト パスをいつでも指定できます (たとえば、 VS.NET プロジェクト) "acw_client」はファイルを含むフォルダーで、Aspose.Cells.GridWeb はこのフォルダーを使用して内部構成を管理します。スクリプト ファイル、画像ファイル、および GridWeb の動作を指定し、他の操作を設定するその他のファイルがあります。構成ファイルは、コントロールがいくつかのケース/シナリオで役立つ埋め込みクライアント リソース (画像、スクリプトなど) を使用します。

**XML**

{{< highlight "csharp" >}}

 <appSettings>

  <add key="aspose.cells.gridweb.acw_client_path" value="/grid/acw_client/"/>

  <add key="aspose.cells.gridweb.force_script_path" value="true"/>

  <add key="aspose.cells.gridweb.forcepath" value="true"/>

 </appSettings>

{{< /highlight >}}

{{% alert color="primary" %}} 

パスは常にプロジェクトのディレクトリに関連しています。プロジェクトのディレクトリ以外のディレクトリは使用しないでください。そのため、「acw_client」ディレクトリ (@GridWeb インストール フォルダー) をプロジェクトのディレクトリにコピーする必要があります。

{{% /alert %}} 
## **Internet Explorer 10 または 11 で Aspose.Cell.GridWeb を実行する**
現在、Aspose.Cells.GridWeb は Internet Explorer 10 または 11 ではうまく動作しないため、IE8/9 の互換モードを使用して IE10/11 ブラウザ タイプで動作させる必要があります。次の行を追加する必要があります**<メタ>**のヘッダーセクションのタグ**.aspx**ページ：



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-KnowledgeBase-FAQ-RunGridWebInIE-RunGridWebIE.aspx" >}}

