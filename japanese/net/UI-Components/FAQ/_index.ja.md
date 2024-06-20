---
title: よくある質問
type: docs
weight: 400
url: /ja/net/grid-faq/
---

## **Aspose.Cells Gridコントロールの評価版に制限はありますか？**
いいえ、評価版は出力ファイルに**評価著作権警告**を追加する以外は、ライセンス版の全機能を提供します。

評価版は、追加のワークシート（**評価著作権警告**を含む）を出力ファイルに追加する以外は、ライセンス版の全機能を提供します。


## **市場には多くのグリッドコントロールがあります。なぜAspose.Cells Gridコントロールを購入すべきですか？**
Aspose.Cells Gridコントロールは非常に手頃な価格設定であり、あらゆる種類のユーザーに手頃な価格で提供されています。

それは単なる単純なグリッドにとどまらず、「**スプレッドシートビューア、エディタ＆クリエータ**」でもあります。 

また、通常のグリッドコントロールのように任意のデータソースにバインドするだけでなく、Excelファイルを作成および管理することもできます。また、組み込みの関数だけでなく、ユーザーが定義したカスタム式も計算する強力で豊富な**数式計算エンジン**を提供します。Aspose.Cells Gridスイートのその他の機能については、詳細な機能リストについてはエディションタイプページを参照してください。 

通常のグリッドコントロールと同様に任意のデータソースにバインドできるだけでなく、Excelファイルを作成および管理することもできます。また、Aspose.Cellsグリッドコントロールがサポートする組み込み関数だけでなく、ユーザーが定義したカスタム式も計算する強力で豊富な**数式計算エンジン**も提供します。Aspose.Cells Gridスイートのその他の機能についてはここでは網羅できませんが、より詳細な機能リストについてはEdition Typesページを参照してください。

## **最近Aspose.Cells Gridコントロールのライセンスを購入しました。Aspose.Cells Gridコントロールでそのライセンスをどのように使用できますか？**
Aspose.Cells Grid Controlsの[Licensing](/cells/ja/net/licensing/)ページを参照してください。 

アプリケーションでAspose.Cells Gridコントロールのライセンスを使用する方法についての詳細が記載されています。



## **Aspose.Cells.GridWebベースのWebプロジェクト/ソリューションをサーバーに展開する方法は？**
Webアプリケーションを展開する必要がある場合、GridWebコントロールを持つWebアプリケーションのプロジェクトフォルダーに"acw_client"ディレクトリをコピーします。

構成セクションに次のコードを追加することで、常にスクリプトパスを指定できます（たとえば、VS.NETプロジェクトのweb.configファイルなど）。"acw_client"は、内部構成を管理するためにAspose.Cells.GridWebが使用するフォルダであり、このフォルダにはスクリプトファイル、画像ファイル、およびその他のファイルが含まれており、GridWebの動作を指定し、その他の操作を設定するために使用されます。構成ファイルは埋め込まれたクライアントリソース（画像、スクリプトなど）の使用を防ぐために使用されます。

**XML**

{{< highlight csharp >}}

 <appSettings>

  <add key="aspose.cells.gridweb.acw_client_path" value="/grid/acw_client/"/>

  <add key="aspose.cells.gridweb.force_script_path" value="true"/>

  <add key="aspose.cells.gridweb.forcepath" value="true"/>

 </appSettings>

{{< /highlight >}}

{{% alert color="primary" %}} 

パスは常にプロジェクトディレクトリに関連しています。プロジェクトディレクトリ外のディレクトリを使用してはいけません。したがって、プロジェクトディレクトリに"acw_client"ディレクトリ（@GridWebインストールフォルダ）をコピーする必要があります。

{{% /alert %}} 
## **Internet ExplorerでAspose.Cell.GridWebを実行する**
現在、Aspose.Cells.GridWebはInternet Explorerをサポートしていません。古すぎるブラウザです。 
Chrome、Edge、Firefox、Safari、Operaをサポートしています



