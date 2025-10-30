---  
title: 中国地域向けにチャートを画像に変換するNode.js経由でC++を使用  
description: Aspose.Cells for Node.js via C++を使用して中国語の文字やフォーマット、フォント、サイズ、テキストの方向などを設定する方法を学びます。  
keywords: Aspose.Cells for Node.js、チャート、中国語設定、フォント、フォントサイズ、テキスト方向、サポート。  
linktitle: 中国地域を設定する  
type: docs  
weight: 9  
url: /ja/nodejs-cpp/convert-chart-to-image-for-chinese-region/  
alias: [/nodejs-cpp/set-chinese-configuration-for-chart/]  
---  

{{% alert color="primary" %}}  
このトピックでは、チャートの中国地域を設定する方法を示します。  
{{% /alert %}}  

## **継承クラスを定義する**  

最初のステップでは、[**ChartGlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/)から継承する"ChartChineseSetttings"クラスを定義する必要があります。  
その後、関連する関数を書き換えることで、チャート要素のテキストを独自の言語で設定できます。  
コード例:  
```javascript
const AsposeCells = require("aspose.cells.node");

class ChartChineseSettings extends AsposeCells.ChartGlobalizationSettings {
getAxisTitleName() {
return "坐标轴标题";
}

getAxisUnitName(type) {
switch (type) {
case AsposeCells.DisplayUnitType.None:
return '';
case AsposeCells.DisplayUnitType.Hundreds:
return '百';
case AsposeCells.DisplayUnitType.Thousands:
return '千';
case AsposeCells.DisplayUnitType.TenThousands:
return '万';
case AsposeCells.DisplayUnitType.HundredThousands:
return '十万';
case AsposeCells.DisplayUnitType.Millions:
return '百万';
case AsposeCells.DisplayUnitType.TenMillions:
return '千万';
case AsposeCells.DisplayUnitType.HundredMillions:
return '亿';
case AsposeCells.DisplayUnitType.Billions:
return '十亿';
case AsposeCells.DisplayUnitType.Trillions:
return '兆';
default:
return '';
}
}

getChartTitleName() {
return "图表标题";
}

getLegendDecreaseName() {
return "减少";
}

getLegendIncreaseName() {
return "增加";
}

getLegendTotalName() {
return "汇总";
}

getOtherName() {
return "其他";
}

getSeriesName() {
return "系列";
}
}
```  

## **チャートの中国語設定を構成する**  

このステップでは、前のステップで定義した"ChartChineseSetttings"クラスを使用します。  
コード例:  

```javascript  
const Workbook = require('aspose.cells');  
const wb = new Workbook("Chinese.xls");  
wb.settings.globalizationSettings.chartSettings = new ChartChineseSetttings();  
const chart0 = wb.worksheets[0].charts[0];  
chart0.toImage("Output.png");  
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

{{< app/cells/assistant language="nodejs-cpp" >}}
