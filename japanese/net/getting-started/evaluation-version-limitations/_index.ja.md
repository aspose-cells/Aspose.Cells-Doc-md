---
title: 評価版の制限事項
type: docs
weight: 110
url: /ja/net/evaluation-version-limitations/
description: Aspose.Cells for .NET では、さまざまな購入プランが提供されるか、C# のライセンスおよびサブスクリプション ポリシーを使用した評価用の無料トライアルと 30 日間の一時ライセンスが提供されます。
keywords: Evaluation Version Limitations, Number of Opened Files in Evaluation Version, Evaluation Watermark using Evaluation Version.
---
##  **Aspose.Cells の評価版を入手する方法**

評価版をダウンロードできます**Aspose.Cells** NETから[そのダウンロードページ](https://repository.aspose.com/webapp/#/artifacts/browse/tree/General/repo/com/aspose/aspose-cells) Maven リポジトリ。評価版では、製品のライセンス版とまったく同じ機能が提供されます。さらに、評価版は、ライセンスを購入し、ライセンスを適用するコードを数行追加するだけでライセンスが付与されます。

 *Aspose.Cells** の評価に満足したら、次のことができます。[ライセンスを購入する](https://purchase.aspose.com)ウェブサイトAsposeで。提供されているさまざまなサブスクリプション タイプについてよく理解してください。ご不明な点がございましたら、お気軽にAspose営業チームまでお問い合わせください。

すべての Aspose ライセンスには、この期間中にリリースされる新しいバージョンまたは修正への無料アップグレードのための 1 年間のサブスクリプションが含まれています。テクニカル サポートは無料かつ無制限で、ライセンス ユーザーと評価ユーザーの両方に提供されます。

##  **評価版の制限なしで Aspose.Cells をテストする方法**

テストしたい場合は**Aspose.Cells**評価版の制限がない場合は、30 日間の一時ライセンスをリクエストしてください。を参照してください。[仮免許を取得するにはどうすればよいですか?](https://purchase.aspose.com/temporary-license)詳細については。


##  **評価版の制限事項**

の評価版**Aspose.Cells**製品 (ライセンスが指定されていない) は製品のすべての機能を提供しますが、1 つのプログラムで開くことができるファイルは 100 個と、評価ウォーターマーク付きの追加のワークシートに制限されています。

制限事項を以下に示します。

###  **第 1 の制限: 開いているファイルの数**

プログラムの実行時に開くことができる Excel ファイルは 100 個までです。アプリケーションがこの数を超えると、例外がスローされます。

###  **第 2 の制限: 評価ウォーターマークのあるワークシート**
このワークシートは常にアクティブなワークシートとして表示されます。ライセンス版のみ、アクティブなワークシートを他のワークシートに設定できます。
<br>
<image src="1.png" width="70%" />
<br>

###  **第3制限：評価情報を含むプレーンテキスト**
Aspose.Cells が出力したプレーンテキストファイルでは、文書の末尾に評価情報が追加されます。
<br>
<image src="2.png" width="70%" />
<br>

###  **4 番目の制限: PDF および評価ウォーターマーク付きの画像**
出力 PDF または Aspose.Cells による画像ファイルでは、評価のウォーターマークがドキュメント/画像の上部に貼り付けられます。GridWeb コントロールでも評価著作権警告 (追加のワークシート) を非表示にすることはできません。常に追加されます。 (ワークシートタブの最後) コントロール内。
<br>
<image src="3.png" width="70%" />
<br>

###  **5番目の制限事項: 構成ファイルの設定(Aspose.Cells.GridWeb)**
次のコード行を構成セクション (web.config ファイルなど) に追加しても、スクリプト パスを再指定することはできません。 acw_client はファイルが含まれるフォルダーで、Aspose.Cells.GridWeb はこのフォルダーを使用して内部構成を管理します。このフォルダーには、GridWeb の動作を指定し、その他の操作を設定するためのスクリプト ファイル、画像ファイル、その他のファイルがあります。構成ファイルは、コントロールが埋め込みクライアント リソース (画像、スクリプトなど) を使用しないようにするために使用され、場合によっては役立ちます。さらに、web.config ファイル内のこの構成設定は、コントロールのライセンス済みバージョンでのみ有効になります。

**XML**
{{< highlight "csharp" >}}
<appSettings>

<add key="aspose.cells.gridweb.acw_client_path" value="/acw_client/" />

<add key="aspose.cells.gridweb.force_script_path" value="true" />

</appSettings>

{{< /highlight >}}

{{% alert color="primary" %}}

ファイル システム Web サイトや MS Ajax 拡張機能などで Aspose.Cells.GridWeb コントロールを使用している場合、これらの設定は場合によっては必須になることがあります。

{{% /alert %}}