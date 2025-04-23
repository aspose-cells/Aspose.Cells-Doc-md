---
title: なぜ Open XML SDK を使用しないのか
type: docs
weight: 90
url: /ja/net/why-not-open-xml-sdk/
---

{{% alert color="primary" %}}

このような質問を時々耳にします:

**無料の Open XML SDK ではなく、なぜ Aspose 製品を使用するべきなのか**

この質問に答えるのは簡単です：機能と機能性です。

{{% /alert %}}

## **Open XML SDK とは何ですか？**

[MSDN ライブラリ](https://docs.microsoft.com/en-us/office/open-xml/open-xml-sdk?redirectedfrom=MSDN) によると、Open XML SDK は次のように定義されています:

"Open XML SDK 2.5 は Open XML パッケージとパッケージ内の基礎となる Open XML スキーマ要素を操作するタスクを簡略化します。 Open XML SDK 2.5 は、開発者が Open XML パッケージで行う多くの一般的なタスクをカプセル化し、数行のコードで複雑な操作を行うことができます."

OOXML ドキュメントは基本的に圧縮された XML ファイルであり、Open XML SDK はこの OOXML ドキュメントのコンテンツを、強力に型付けされた方法で操作するためのクラスのコレクションです。これにより、ファイルを解凍して XML を抽出し、その XML を DOM ツリーに読み込んで直接 XML 要素と属性を扱う代わりに、Open XML SDK はそれらの操作を行うためのクラスを提供します。

## **Aspose.Cells とは何ですか？**

Aspose.Cells は、アプリケーションが次のようなスプレッドシート処理を実行できるようにするクラスライブラリです：

- PDF、HTML、TIFF への変換を含む、すべての一般的な Microsoft Excel フォーマット間の高品質な変換。
- ワークブック オブジェクトモデルでのプログラミング。
- スタイル付けやグラフィック、チャートなどのデータを自動的にマージし、フラグメントから単一または複数のドキュメントからドキュメントを構築する能力。
- 配列、ArrayList、DataTable / ResultSetなどの異なるデータソースからのデータのインポートなど、ハイレベルな機能。
- ほぼすべての標準および高度な Microsoft Excel 関数をサポートする強力な式計算エンジン。

## **Open XML SDK と Aspose.Cells の比較**

次の表は、Open XML SDK と Aspose.Cells の機能を比較しています。

|**機能または機能カテゴリ**|**Open XML SDK**|**Aspose.Cells**|
| :- | :- | :- |
|サポートされる Excel またはその他のフォーマット|XLSX|XLS、CSV、SpreadsheetML 2003、XLSX、HTML、Tab Delimited、ODS、Plain Text (TXT)、PDF、XPS|
|Excel フォーマット間の変換|いいえ|はい|
|ワークブック オブジェクトモデルでの高レベルなプログラミング:
- 検索および置換
- スプレッドシートのアセンブリ
- フラグメントやワークシートをワークブック間でコピー|いいえ|はい|
|文書オブジェクトモデルでの詳細なプログラミング、すべてのスプレッドシート要素の個別の要素や書式設定プロパティへのアクセス。|はい|はい|
|OOXML ドキュメントの関連識別子、リスト識別子などの基礎となる XML 要素や属性への低レベルで直接的なアクセス。|はい|いいえ|
|レポートの作成、データでドキュメントを埋める:
- DataTable / ResultSet へのデータのインポート／エクスポート
- スマートマーカー機能
- 行／列／範囲の挿入／削除
- カスタムデータソース|いいえ|はい|
|レンダリングおよび印刷:
- ワークシートページをラスターイメージ (TIFF、多ページTIFF、PNG、JPEG、BMP) にレンダリング
- スプレッドシートページをベクターイメージ (EMF) にレンダリング
- チャートをイメージに変換 (TIFF、多ページTIFF、PNG、JPEG、BMP、EMF など)
- 画像の解像度、品質、圧縮およびその他のオプションの指定
- .NET の印刷インフラストラクチャを使用したスプレッドシートの印刷。コンポーネントには Microsoft Excel のプリントプレビューで表示されるようにワークシートを印刷するための組み込みのプリントメソッドがあります。|いいえ|はい|
|式を動的に計算／再計算する|いいえ|はい|
| サポートされているプラットフォーム | Windows、.NET | Windows、Linux、Java、.NET、Mono |

OpenXMLとAspose.Cellsを比較するためには、OpenXMLと比較して異なるタスクがどのように行われるかを示したAspose.Cells for OpenXMLプロジェクトに慣れていただくことをお勧めします。このプロジェクトは、Aspose.Cells for .NET APIとOpenXMLを使用してさまざまなタスクを行う方法を示しています。また、Aspose.Cellsのみで利用可能なテキストドキュメントの操作機能もカバーしています。

このプロジェクトは、OpenXMLからAspose.Cellsへの移行を検討している開発者にも役立ちます。

{{% alert color="primary" %}}

[OpenXMLと比較した Aspose.Cells for .NET の機能を備えたプラグイン（ソースコードの例を含む）を探索してください](https://github.com/asposemarketplace/Aspose_for_OpenXML)。

このプラグインはAspose.Cellsの評価版を使用しています。評価版で満足できたら、[Asposeのウェブサイト](https://purchase.aspose.com/buy) からライセンスを購入できます。評価メッセージと機能の制限を削除するには、製品ライセンスを適用する必要があります。製品を購入すると、ライセンスファイルが提供されます。[「ライセンスとサブスクリプション」](/cells/ja/net/licensing/) の記事に記載された手順に従ってください。

{{% /alert %}}

**結論**: Open XML SDKとAspose.Cellsは直接競合していません。なぜなら、それらはかなり異なるニーズとユーザーに対応しているからです。

## **Open XML SDKを使わない理由**
Open XML SDKは、OOXML文書を強力な型指定の方法で操作するためのクラスライブラリです。Aspose.Cellsは、Microsoft Excelおよび他のファイル形式に対応した非常に便利なスプレッドシート処理ライブラリです。

XLSXドキュメントで行う必要があるのがかなり基本的なプログラミング操作だけなら、Open XML SDKが適した選択肢になるかもしれません。Open XML SDKを使用すると、シンプルなXLSXドキュメントの生成やコメントの削除、ヘッダー/フッターの削除、画像の抽出などの簡単なタスクを行うことにかなり快適になるでしょう。 
Open XML SDKで達成できるタスクもありますが、Aspose.Cellsでは達成できないことがあります。たとえば、OOXMLドキュメントのXML要素や属性に直接アクセスする必要がある場合は、Open XML SDKを使用する必要があります。

ただし、ドキュメントで次のようないくつかのタスクを実行する必要がある場合は、Aspose.Cellsを使用するのが最適な選択肢です:

- XLSXに加えて他のファイル形式のサポート。
- ワークブック間でフラグメントやワークシートをコピーしたり、オブジェクト、スタイル、その他の適切な方法でフォーマットを結合する。
- フォーマット済みまたはフォーマットされていないテキストの置換。
- 配列、ArrayList、DataTable / ResultSetなどの異なるデータソースからのデータのインポートなど、ハイレベルな機能。
- データソースから注文詳細などのビジネスドキュメントの生成。
- ドキュメントをMicrosoft Excelで変換した場合とまったく同じようにPDFまたはXPSに変換。
- .NETまたはJavaアプリケーションの開発。

{{< app/cells/assistant language="csharp" >}}
