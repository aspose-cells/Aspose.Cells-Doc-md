---
title: チャートをローカライズされた画像に変換
description: Aspose.Cells for .NET を使用してグラフのグローバリゼーション構成を設定する方法について説明します。このガイドでは、複数の言語と地域形式をサポートし、さまざまな言語でテキスト、日付、数値を正しく表示するようにグラフを構成する方法を説明します。
keywords: Aspose.Cells for .NET, Charts, Globalization Settings, Multiple Languages, Regional Formats, Display, Text, Dates, Numbers.
linktitle: ローカライズされた領域を設定する
type: docs
weight: 50
url: /ja/net/convert-chart-to-localized-image/
alias: [/net/how-to-set-globalization-configuration-for-chart/]
---
{{% alert color="primary" %}}

このトピックでは、チャートをローカライズされた画像に変換する方法を説明し、チャートのローカライズされた領域を設定する方法を学びます。

{{% /alert %}}

##  **シナリオ**

どのようなシナリオでチャートのローカライズされた領域を設定する必要がありますか?

Excel でグラフを含む xlsx ファイルを開くと (この場合、Excel でスペイン語の地域設定を使用してファイルを開いたとします)、グラフ領域内の要素 (グラフのタイトル、長さなど) がスペイン語に翻訳されて表示されます。ただし、このグラフを Aspose.Cells の画像として保存すると、次の問題が発生する可能性があります。

**![グローバル問題](GlobalIssue.png)**

このシナリオでは、出力画像のグラフの凡例は Excel のものと同じではなく、デフォルトで英語で表示されたままになります。チャートにローカライズされた領域を設定することで、この問題を解決できるようになりました。正しい設定を使用すると、次の要素がローカリゼーション設定に従ってレンダリングされます。

##  **サポートされている要素**

チャート内の次の要素は、ローカリゼーション設定に従ってレンダリングできます。

|**サポートされている要素**|**英語環境のデフォルト値**|
| :- | :- |
|軸タイトル名|軸タイトル|
|軸ユニット名|何百、何千...|
|チャートのタイトル名|チャートのタイトル|
|レジェンド増加名|増加|
|凡例の名前の減少|減少|
|凡例の合計名|合計|
|ほかの名前|他の|
|シリーズ名|シリーズ|

##  **操作手順**

次の例では、ローカライズされた領域を設定して必要な効果を実現する方法を詳しく示します。

- [グラフの中国地域を設定する方法](/cells/ja/net/convert-chart-to-image-for-chinese-region/)
- [チャートに日本の地域を設定する方法](/cells/ja/net/convert-chart-to-image-for-japanese-region/)

