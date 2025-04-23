---
title: 日本語地域のチャートを画像に変換
description: Aspose.Cells for .NETの使用方法を学習して、日本語設定でチャートを設定する方法をデモンストレーションします。フォント、サイズ、文字方向など、日本語文字および書式設定をサポートするチャートの構成方法を説明します。
keywords: Aspose.Cells for .NET、チャート、日本語設定、フォント、フォントサイズ、文字方向、サポート。
linktitle: 日本語地域の設定
type: docs
weight: 10
url: /ja/net/convert-chart-to-image-for-japanese-region/
alias: [/net/set-japanese-configuration-for-chart/]
---

{{% alert color="primary" %}}

このトピックでは、チャートの日本語地域を設定する方法を説明します。

{{% /alert %}}

## **継承クラスを定義する**

最初に、[**ChartGlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/)から継承する"ChartJapaneseSetttings"クラスを定義する必要があります。 
その後、関連する関数を書き換えることで、チャート要素のテキストを独自の言語で設定できます。
コード例:
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "ChartJapaneseSetttings.cs" >}}

## **チャートの日本語設定を構成する**

このステップでは、前のステップで定義した"ChartJapaneseSetttings"クラスを使用します。
コード例:

```
	Workbook wb = new Workbook("Japanese.xls");
	wb.Settings.GlobalizationSettings.ChartSettings = new ChartJapaneseSetttings();
	Chart chart0 = wb.Worksheets[0].Charts[0];
	chart0.ToImage("Output.png");
```

その後、出力イメージで効果を確認できます。チャートの要素は、設定に従ってレンダリングされます。

## **結論**

この例では、チャートに日本の地域を設定しないと、次のチャート要素がデフォルト言語(英語など)でレンダリングされる可能性があります。
上記の操作の後、日本の地域で出力されたチャート画像を取得できます。

|**サポートされる要素**|**この例の値**|**英語環境のデフォルト値**|
| :- | :- | :- |
|軸タイトル名|軸タイトル|Axis Title|
|軸単位名|百,千...|Hundreds, Thousands...|
|グラフタイトル名|グラフ タイトル|Chart Title|
|凡例増加名|ぞうか|Increase|
|凡例減少名|削減|Decrease|
|凡例全体名|すべての|Total|
|その他の名前|その他|Other|
|系列名|シリーズ|Series|
{{< app/cells/assistant language="csharp" >}}
