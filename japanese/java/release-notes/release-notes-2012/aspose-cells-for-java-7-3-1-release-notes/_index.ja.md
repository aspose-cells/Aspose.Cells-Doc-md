---
title: Aspose.Cells for Java 7.3.1 リリースノート
type: docs
weight: 40
url: /ja/java/aspose-cells-for-java-7-3-1-release-notes/
---
{{% alert color="primary" %}} 

このページには、[Aspose.Cells for Java 7.3.1](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-7.3.1/)

{{% /alert %}} 

私たちです
ユーザー向けに Aspose.Cells for Java v7.3.1 を発表できることをうれしく思います。

新機能

 -ページ設定のヘッダー/フッターのスクリプトを解析

- 条件付き書式 - DataBar タイプの不足しているフィールドを含める
- 条件付き書式 - IconSet タイプの欠損値を含める
- 条件付き書式 - サポート
- シート間の数式で条件付き書式ルールを読み取る
- Cells.MinDataColumn および Cells.MinDataRow プロパティをサポート
- 条件付き書式で Cell 背景色をサポート (MS Excel 2010)
- ピボットテーブルのデータ フィルターがサポートされています
- MS Excel 2010 の高度なデータ検証がサポートされています

（ノート：

上記チケット全て
.NET ユーザーに代わって最初に追加されました。私たちの Java バージョン以来
この製品は、(機能と拡張に関して) .NET と同等に一致します。
現在、Java バージョンにこれらの新機能/拡張機能を組み込みました。
製品の。
) 

機能強化

・PDF保存時に一時フォントファイルが複数作成される

 ヘッダー/フッターの日付がワークブックのロケール設定に合わせてフォーマットされていない

- 新しいオプションをサポート: Aspose.Cells.Disable=Open JDK の JVM クラッシュの java.awt.headless の代わりに SunFontManager

 - HTML ファイルのオートシェイプをエクスポート

例外

- 例外: PDF に保存するときの「Shape to Image エラー」

 -PDF に保存するときの形状から画像への問題

- Chart.calculate() メソッドの「NullPointerException」

 -XLS を PDF として保存すると例外が発生する

-XLS を PDF として保存すると例外 II が発生する

バグ

 PDF を保存する際のテキストのオーバーラップとグリッド線の欠落

-再保存時に余分な枠線が表示される問題を修正

テンプレート ファイルを XLS ファイルとして

 参照 "!$A$1" で名前を読むと例外が発生する

 特定のグラフのデータで PDF 生成に失敗した

-範囲を挿入した後の数式が正しくない

 Excel ワークブックから生成された PDF のページ数が多かった

-ワークシートをコピーすると、グラフのラベルがずれたり重なったりする
