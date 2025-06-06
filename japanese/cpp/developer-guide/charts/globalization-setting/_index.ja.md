---
title: C++でローカライズされた画像にチャートを変換
description: Aspose.Cells for C++を使用してチャートのグローバル化設定を行う方法を学びます。ガイドでは、多言語や地域別の形式をサポートするようにチャートを設定し、テキスト、日付、および数字をさまざまな言語で正しく表示できるようにします。
keywords: Aspose.Cells for C++、チャート、グローバル化設定、多言語、地域別フォーマット、表示、テキスト、日付、数字
linktitle: ローカライズされた地域を設定する
type: docs
weight: 50
url: /ja/cpp/convert-chart-to-localized-image/
alias: [/cpp/how-to-set-globalization-configuration-for-chart/]
---

{{% alert color="primary" %}}

このトピックでは、チャートをローカル化されたイメージに変換する方法を示し、チャートに対してローカライズされた地域を設定する方法を学びます。

{{% /alert %}}

## **シナリオ**

チャートにローカライズされた地域設定を行う必要があるシナリオは何ですか？

Excelでチャートを含むxlsxファイルを開くとき、例としてスペインの地域設定で開いた場合、チャートエリア内の要素（チャートタイトルや凡例など）がスペイン語に翻訳されて表示されます。しかし、Aspose.Cellsでこのチャートを画像として保存すると、次のような問題が発生することがあります。 

**! [グローバル・イシュー](GlobalIssue.png)**

このシナリオでは、出力画像内のチャート凡例はExcelと異なり、デフォルトでは英語のまま表示され続けます。この問題は、チャートのローカライズされた地域設定を行うことで解決できます。正しい設定を行うと、以下の要素がローカライズ設定に従ってレンダリングされます。

## **サポートされている要素**

チャート内の以下の要素は、ローカリゼーション設定に応じてレンダリングされます。

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

次の例では、設定方法を詳しく示し、希望の効果を得るためのローカライズ地域の設定例を説明します。

- [チャートの中国地域を設定する方法](/cells/ja/cpp/convert-chart-to-image-for-chinese-region/)
- [チャートの日本地域を設定する方法](/cells/ja/cpp/convert-chart-to-image-for-japanese-region/)

