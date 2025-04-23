---
title: ローカライズされたイメージにチャートを変換
description: Aspose.Cells for .NETを使用してチャートのグローバリゼーション設定を行う方法を学んでください。当社のガイドでは、チャートを複数の言語と地域の書式に対応させ、異なる言語でテキスト、日付、および数値を正しく表示するために、チャートの構成方法を説明します。
keywords: Aspose.Cells for .NET、チャート、グローバリゼーション設定、複数言語、地域の書式、表示、テキスト、日付、数値。
linktitle: ローカライズされた地域を設定する
type: docs
weight: 50
url: /ja/net/convert-chart-to-localized-image/
alias: [/net/how-to-set-globalization-configuration-for-chart/]
---

{{% alert color="primary" %}}

このトピックでは、チャートをローカル化されたイメージに変換する方法を示し、チャートに対してローカライズされた地域を設定する方法を学びます。

{{% /alert %}}

## **シナリオ**

チャートにローカライズされた地域を設定する必要があるシナリオは？ 

Excelでグラフが含まれるxlsxファイルを開くと、この場合、Excelでスペインの地域設定で開くと、グラフエリア内の要素（チャートタイトル、凡例など）がスペイン語に翻訳されたものが表示されます。しかし、Aspose.Cellsでこのチャートを画像として保存すると、次の問題が発生する可能性があります。 

**! [グローバル・イシュー](GlobalIssue.png)**

この場合、出力画像のチャートの凡例はExcelと同じではなく、デフォルトで英語で表示されたままです。これを解決するために、チャートにローカライズされた地域を設定します。正しい設定では、次の要素がローカライズ設定に従ってレンダリングされます。

## **サポートされている要素**

チャート内の次の要素は、ローカライズ設定に従ってレンダリングされます。

|**サポートされている要素**|**英語環境のデフォルト値**|
| :- | :- |
|軸タイトル名|Axis Title|
|軸単位名|Hundreds, Thousands...|
|チャートタイトル名|Chart Title|
|凡例増加名|Increase|
|凡例減少名|Decrease|
|凡例合計名|Total|
|その他名|Other|
|系列名|Series|

## **操作手順**

次の例は、望んだ効果を達成するためにローカライズされた地域を設定する方法を詳しく示します。

- [チャートの中国地域を設定する方法](/cells/ja/net/convert-chart-to-image-for-chinese-region/)
- [チャートの日本地域を設定する方法](/cells/ja/net/convert-chart-to-image-for-japanese-region/)

{{< app/cells/assistant language="csharp" >}}
