---
title: GolangからC++でチャートを画像に変換し、中国地域用に最適化する
linktitle: 中国地域を設定する
description: Aspose.Cells for C++を使用して中国向けのチャート設定を行う方法を学びます。フォント、サイズ、テキスト方向などを設定し、中国文字やフォーマットのサポートを行います。
keywords: Aspose.Cells for C++、チャート、中国設定、フォント、フォントサイズ、テキスト方向、サポート。
type: docs
weight: 9
url: /ja/go-cpp/convert-chart-to-image-for-chinese-region/
alias: [/cpp/set-chinese-configuration-for-chart/]
---

{{% alert color="primary" %}}

このトピックでは、チャートの中国地域を設定する方法を示します。

{{% /alert %}}

## **継承クラスを定義する**

最初のステップでは、[**ChartGlobalizationSettings**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/)から継承する"ChartChineseSetttings"クラスを定義する必要があります。 
次に、関連する関数をオーバーライドして、チャート要素のテキストを自分の言語に設定できます。

コード例:
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChineseSettting.go" >}}
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
