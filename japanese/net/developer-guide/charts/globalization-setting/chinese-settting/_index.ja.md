---
title: 中国地域のチャートをイメージに変換する
description: Aspose.Cells for .NETを使用して、中国構成のチャートを作成する方法を学習してください。当ガイドでは、フォント、サイズ、テキストの方向など、中国文字と書式をサポートするためのチャートの構成方法を実証します。
keywords: Aspose.Cells for .NET、チャート、中国構成、フォント、フォントサイズ、テキストの方向、サポート。
linktitle: 中国地域を設定する
type: docs
weight: 9
url: /ja/net/convert-chart-to-image-for-chinese-region/
alias: [/net/set-chinese-configuration-for-chart/]
---

{{% alert color="primary" %}}

このトピックでは、チャートの中国地域を設定する方法を示します。

{{% /alert %}}

## **継承クラスを定義する**

最初のステップとして、「[**ChartGlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/)」から継承するクラス"ChartChineseSetttings"を定義する必要があります。 
その後、関連する関数を書き換えることで、チャート要素のテキストを独自の言語で設定できます。
コード例:
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "ChartChineseSetttings.cs" >}}

## **チャートの中国語設定を構成する**

このステップでは、前のステップで定義した"ChartChineseSetttings"クラスを使用します。
コード例:

```
	Workbook wb = new Workbook("Chinese.xls");
	wb.Settings.GlobalizationSettings.ChartSettings = new ChartChineseSetttings();
	Chart chart0 = wb.Worksheets[0].Charts[0];
	chart0.ToImage("Output.png");
```

その後、出力イメージで効果を確認できます。チャートの要素は、設定に従ってレンダリングされます。

## **結論**

この例では、チャートに日本語の地域を設定しない場合、次のチャート要素はデフォルトの言語（英語など）でレンダリングされる場合があります。
上記の操作を行った後、日本語の地域を設定した出力チャート画像を取得できます。

|**サポートされる要素**|**この例の値**|**英語環境のデフォルト値**|
| :- | :- | :- |
| 軸タイトル名 | 坐標軸タイトル | 軸タイトル |
|軸単位名|百,千...|Hundreds, Thousands...|
| チャートタイトル名 | グラフタイトル | Chart Title |
| 凡例の増加名 | 増加 | Increase |
| 凡例の減少名 | 減少 | Decrease |
| 凡例の合計名 | 汇总 | Total |
| その他の名前 | その他 | Other |
| 系列名 | 系列 | Series |
