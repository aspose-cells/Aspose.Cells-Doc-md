---  
title: 日本地域向けにチャートを画像に変換するNode.js経由でC++を使用  
description: Aspose.Cells for Node.js via C++を使用して日本語の設定をチャートに適用する方法を学びます。ガイドでは、フォント、サイズ、テキストの方向など、日本語の文字とフォーマットをサポートするようにチャートを設定する方法を示します。  
keywords: Aspose.Cells for Node.js via C++、チャート、日本語設定、フォント、フォントサイズ、テキスト方向、サポート。  
linktitle: 日本語地域の設定  
type: docs  
weight: 10  
url: /ja/nodejs-cpp/convert-chart-to-image-for-japanese-region/  
alias: [/nodejs-cpp/set-japanese-configuration-for-chart/]  
---  

{{% alert color="primary" %}}  
このトピックでは、チャートの日本語地域を設定する方法を説明します。  
{{% /alert %}}  

## **継承クラスを定義する**  

最初のステップでは、[**ChartGlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/)から継承する"ChartJapaneseSettings"クラスを定義する必要があります。  
その後、関連する関数を書き換えることで、チャート要素のテキストを独自の言語で設定できます。  
コード例:  
```javascript
const AsposeCells = require("aspose.cells.node");

class ChartJapaneseSettings extends AsposeCells.ChartGlobalizationSettings {
getAxisTitleName() {
return "軸タイトル";
}

getAxisUnitName(type) {
switch (type) {
case AsposeCells.DisplayUnitType.None:
return '';
case AsposeCells.DisplayUnitType.Hundreds:
return "百";
case AsposeCells.DisplayUnitType.Thousands:
return "千";
case AsposeCells.DisplayUnitType.TenThousands:
return "万";
case AsposeCells.DisplayUnitType.HundredThousands:
return "10万";
case AsposeCells.DisplayUnitType.Millions:
return "百万";
case AsposeCells.DisplayUnitType.TenMillions:
return "千万";
case AsposeCells.DisplayUnitType.HundredMillions:
return "億";
case AsposeCells.DisplayUnitType.Billions:
return "10億";
case AsposeCells.DisplayUnitType.Trillions:
return "兆";
default:
return '';
}
}

getChartTitleName() {
return "グラフ タイトル";
}

getLegendDecreaseName() {
return "削減";
}

getLegendIncreaseName() {
return "ぞうか";
}

getLegendTotalName() {
return "すべての";
}

getOtherName() {
return "その他";
}

getSeriesName() {
return "シリーズ";
}
}
```  

## **チャートの日本語設定を構成する**  

このステップでは、前のステップで定義した"ChartJapaneseSettings"クラスを使用します。  
コード例:  

```javascript  
const { Workbook } = require('aspose.cells');

let wb = new Workbook("Japanese.xls");
wb.settings.globalizationSettings.chartSettings = new ChartJapaneseSettings();
let chart0 = wb.worksheets[0].charts[0];
chart0.toImage("Output.png");
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

