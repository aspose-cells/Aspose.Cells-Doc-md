---
title: JavaScriptを使ったローカライズされた画像へのチャート変換
description: Aspose.Cells for JavaScriptを使ったチャートのグローバリゼーション設定方法について学びます。複数の言語や地域のフォーマットに対応させて、テキスト、日付、数値を正しく表示させる設定例を紹介します。
keywords: Aspose.Cells for JavaScriptを経由したC++、チャート、グローバリゼーション設定、多言語、地域フォーマット、表示、テキスト、日付、数字。
linktitle: ローカライズされた地域を設定する
type: docs
weight: 50
url: /ja/javascript-cpp/convert-chart-to-localized-image/
alias: [/javascript-cpp/how-to-set-globalization-configuration-for-chart/]
---

{{% alert color="primary" %}}

このトピックでは、チャートをローカル化されたイメージに変換する方法を示し、チャートに対してローカライズされた地域を設定する方法を学びます。

{{% /alert %}}

## **シナリオ**

チャートにローカライズされた地域設定を行う必要があるシナリオは何ですか？ 

Excelでチャートを含むxlsxファイルを開くとき、例えばExcelのスペイン地域設定で開いた場合、チャートエリアの要素（タイトル、凡例など）がスペイン語に翻訳されて表示されます。しかし、Aspose.Cellsを使用してこのチャートを画像として保存すると、以下の問題に遭遇することがあります： 

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

- [チャートの中国地域を設定する方法](/cells/ja/javascript-cpp/convert-chart-to-image-for-chinese-region/)
- [チャートの日本地域を設定する方法](/cells/ja/javascript-cpp/convert-chart-to-image-for-japanese-region/)
