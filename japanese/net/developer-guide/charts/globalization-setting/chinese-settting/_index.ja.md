---
title: 中国地域のチャートを画像に変換
linktitle: 中国地域の設定
type: docs
weight: 9
url: /ja/net/convert-chart-to-image-for-chinese-region/
alias: [/net/set-chinese-configuration-for-chart/]
---
{{% alert color="primary" %}}

このトピックでは、グラフに中国地域を設定する方法を説明します。

{{% /alert %}}

##  **継承クラスを定義します**

最初のステップとして、以下を継承するクラス「Chart ChineseSettings」を定義する必要があります。[**チャートグローバリゼーション設定**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/). 
次に、関連する関数を書き直すことで、グラフ要素のテキストを独自の言語で設定できます。
コード例:
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "ChartChineseSetttings.cs" >}}

##  **チャートの中国語設定を構成する**

このステップでは、前のステップで定義したクラス「Chart ChineseSettings」を使用します。
コード例:

```
	Workbook wb = new Workbook("Chinese.xls");
	wb.Settings.GlobalizationSettings.ChartSettings = new ChartChineseSetttings();
	Chart chart0 = wb.Worksheets[0].Charts[0];
	chart0.ToImage("Output.png");
```

出力画像で効果を確認できます。グラフ内の要素は設定に従ってレンダリングされます。

##  **結論**

この例では、グラフに中国地域を設定しない場合、次のグラフ要素は英語などのデフォルト言語で表示される可能性があります。
上記の操作の後、中国地域を含む出力チャート画像を取得できます。

|**サポートされている要素**|**この例の値**|**英語環境のデフォルト値**|
| :- | :- | :- |
|軸タイトル名|坐标轴标题|軸タイトル|
|軸ユニット名|百,千...|何百、何千...|
|チャートのタイトル名|图表标题|チャートのタイトル|
|レジェンド増加名|增加|増加|
|凡例の名前の減少|减少|下降|
|凡例の合計名|汇总|合計|
|ほかの名前|其他|他の|
|シリーズ名|系列|シリーズ|
