---
title: 日本地域のチャートを画像に変換
description: Aspose.Cells の使用方法を学ぶ for .NET はチャートの日本語構成を設定します。このガイドでは、日本語の文字と書式設定 (フォント、サイズ、テキストの方向など) をサポートするようにグラフを構成する方法を説明します。
keywords: Aspose.Cells for .NET, Charts, Japanese configuration, font, font size, text direction, support.
linktitle: 日本の地域を設定する
type: docs
weight: 10
url: /ja/net/convert-chart-to-image-for-japanese-region/
alias: [/net/set-japanese-configuration-for-chart/]
---
{{% alert color="primary" %}}

このトピックでは、チャートに日本のリージョンを設定する方法を説明します。

{{% /alert %}}

##  **継承クラスを定義します**

最初のステップとして、以下を継承するクラス「ChartJapaneseSettings」を定義する必要があります。[**チャートグローバリゼーション設定**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/). 
次に、関連する関数を書き直すことで、グラフ要素のテキストを独自の言語で設定できます。
コード例:
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "ChartJapaneseSetttings.cs" >}}

##  **チャートの日本語設定を構成する**

このステップでは、前のステップで定義したクラス「ChartJapaneseSettings」を使用します。
コード例:

```
	Workbook wb = new Workbook("Japanese.xls");
	wb.Settings.GlobalizationSettings.ChartSettings = new ChartJapaneseSetttings();
	Chart chart0 = wb.Worksheets[0].Charts[0];
	chart0.ToImage("Output.png");
```

出力画像で効果を確認できます。グラフ内の要素は設定に従ってレンダリングされます。

##  **結論**

この例では、チャートに日本の地域を設定しない場合、次のチャート要素は英語などのデフォルト言語で表示される可能性があります。
上記の操作により、日本のリージョンを含む出力チャート画像を取得できます。

|**サポートされている要素**|**この例の値**|**英語環境のデフォルト値**|
| :- | :- | :- |
|軸タイトル名|軸タイトル|軸タイトル|
|軸ユニット名|百,千...|何百、何千...|
|チャートのタイトル名|グラフ タイトル|チャートのタイトル|
|レジェンド増加名|ぞうか|増加|
|凡例の名前の減少|削減|減少|
|凡例の合計名|すべての|合計|
|ほかの名前|その他|他の|
|シリーズ名|シリーズ|シリーズ|
