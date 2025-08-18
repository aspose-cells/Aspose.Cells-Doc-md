---
title: なぜ Open XML SDK を使用しないのか
type: docs
weight: 20
url: /ja/java/why-not-open-xml-sdk/
---

{{% alert color="primary" %}} 

このような質問を時々耳にします:

**無料の Open XML SDK ではなく、なぜ Aspose 製品を使用するべきなのか**

この質問は簡単に答えられます：**機能と機能**。

{{% /alert %}} 
## **Open XML SDKとは何ですか？**
MSDNライブラリによると、Open XML SDKは次のように定義されています：Open XML SDK 2.0は、Open XMLパッケージおよびパッケージ内の基本的なOpen XMLスキーマ要素を操作するタスクを簡素化します。Open XML SDK 2.0は、開発者がOpen XMLパッケージで実行する一般的なタスクをカプセル化しており、わずか数行のコードで複雑な操作を実行できるようにしています。OOXMLドキュメントは基本的には圧縮されたXMLファイルであり、Open XML SDKは、OOXMLドキュメントの内容を強力に型付けされた方法で操作できるようにするクラスのコレクションです。これにより、ファイルを解凍してXMLを抽出し、そのXMLをDOMツリーにロードしてXML要素や属性を直接操作する代わりに、Open XML SDKはそれを行うためのクラスを提供します。
## **Aspose.Cellsとは何ですか？**
Aspose.Cellsは、アプリケーションが次のスプレッドシート処理タスクを実行できるクラスライブラリです：すべての主要なExcel形式間の高品質の変換、PDF、HTML、TIFFへの変換および印刷。ブックモデルを使用したプログラミング。断片からドキュメントの構築、一つまたは複数のドキュメントから、自動的にデータをマージし、スタイル付けされた書式、チャート、グラフィックを組み合わせる機能。Array、ArrayList、DataTable / ResultSetなど、さまざまなデータソースからデータのインポート機能。ほぼすべての標準および高度なMicrosoft Excel関数をサポートする堅牢な式計算エンジン。


## **Open XML SDKとAspose.Cellsを比較する**
次の表はOpen XML SDKとAspose.Cellsの機能を比較しています。

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
|<p>レポートを生成し、文書にデータを埋め込む:</p><p>- *DataTable /* ResultSet へのデータのインポート/エクスポート。</p><p>- スマートマーカー機能。</p><p>- 行/列/範囲の挿入/削除。</p><p>- カスタムデータソース。</p>|いいえ|はい|
|<p>レンダリングと印刷:* ワークシートページをラスターイメージ（TIFF、マルチページTIFF、PNG、JPEG、BMP）にレンダリングします。* スプレッドシートページをベクターイメージ（EMF）にレンダリングします。* チャートをイメージ（TIFF、マルチページTIFF、PNG、JPEG、BMP、EMFなど）に変換します</p><p>- イメージの解像度、品質、圧縮などのオプションを指定します。</p><p>- .NETの印刷インフラストラクチャを使用してスプレッドシートを印刷します。コンポーネントにはワークシートを印刷するためのビルトインの印刷メソッドがあり、MS Excelの印刷プレビューに表示されるワークシートを印刷することができます。</p>|いいえ|はい|
|数式を動的に計算/再計算する |いいえ |はい |
| サポートされているプラットフォーム | Windows、.NET | Windows、Linux、Java、.NET、Mono |
## **結論**
  {{% alert color="primary" %}}Open XML SDK and Aspose.Cells do not compete head to head because they address quite different needs and audiences. Open XML SDK is a class library to provide a strong-typed way to work with OOXML documents. Aspose.Cells is a very useful spreadsheet processing library that provides great support for all Microsoft Excel and other file formats. If all you need to do is a fairly basic programming operation on a XLSX document, then Open XML SDK might be a suitable choice. With Open XML SDK you will be fairly comfortable doing simple tasks like generating a simple XLSX document or removing comments, headers/footers, extracting images or others. Some tasks can be achieved with Open XML SDK, but cannot be achieved with Aspose.Cells. For example, if you need to directly access the XML elements and attributes of an OOXML document, then you should use Open XML SDK.However, if you need to perform complex operations on documents, such as some of the following tasks, then using Aspose.Cells is your best option: Support other file formats in addition to XLSX. Copy fragments and worksheets between workbooks or join workbooks in a way that combines objects, styles and other formatting in an appropriate manner. Replace formatted or unformatted text. High-level functions, such as, import data from different data sources including Array, ArrayList, DataTable / ResultSet. Generate a business document, such as an order with order details from a data source. Convert a document to PDF or XPS so it appears exactly like Microsoft Excel would have converted it. Develop a .NET or Java application. {{% /alert %}}
{{< app/cells/assistant language="java" >}}
