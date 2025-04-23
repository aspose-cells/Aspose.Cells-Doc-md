---  
title: 数字の設定
linktitle: 数字の設定  
description: Aspose.Cellsは、多くのセルの数値設定をサポートするスプレッドシート操作用Node.jsライブラリです。この記事では、Aspose.Cellsライブラリを使ったセルの数値設定の管理と数値形式の調整方法を紹介します。  
keywords: Aspose.Cells、Node.jsライブラリ、電子スプレッドシート、セルの数値設定、フォーマット、管理、数値と日付のフォーマット  
type: docs  
weight: 10  
url: /ja/nodejs-cpp/cells-number-settings/  
---  

## **数字と日付の表示形式を設定する方法**  

Microsoft Excelの非常に優れた特徴の一つは、数値と日付の表示形式を設定できることです。数値データは、十進法、通貨、パーセンテージ、分数、簿記値など、さまざまな値を表すために使用できます。これら全ての数値は、その値が表す情報の種類に応じて異なるフォーマットで表示されます。同様に、日付や時間も多くの表示形式があります。  
Aspose.Cellsはこの機能をサポートし、開発者が数値や日付の表示形式を設定できるようにします。  

### **Microsoft Excelで表示形式を設定する方法**  

Microsoft Excelで表示形式を設定するには：  

1. 任意のセルを右クリックします。  
2. **セルの書式設定**を選択します。ダイアログが表示され、あらゆる種類の値の表示フォーマットを設定できます。  

ダイアログの左側には、**標準**、**数値**、**通貨**、**会計**、**日付**、**時刻**、**パーセンテージ**など多くのカテゴリがあります。Aspose.Cellsはこれらすべての表示フォーマットをサポートしています。  

Aspose.Cellsは、Excelファイルを表すモジュール[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)を提供しています。[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)モジュールには、Excelファイル内の各ワークシートにアクセスできる[**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--)コレクションがあります。ワークシートは[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)モジュールによって表されます。[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)モジュールは[**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--)コレクションを提供し、その中の各アイテムは[**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell)クラスのオブジェクトを示します。  

Aspose.Cellsは、[**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell)モジュールのセルのフォーマット設定と取得に関する[**getStyle()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getstyle--)と[**setStyle(Style)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-)メソッドを提供します。これらのメソッドを使ってセルの書式設定を操作します。[**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)モジュールは、数値と日付の表示フォーマットを扱うための便利なプロパティも提供しています。  

### **組み込みの数値形式の使用方法**  

Aspose.Cells は、数値と日時の表示形式を設定するためのいくつかの組み込み番号形式を提供します。これらの組み込み番号形式は、[**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) オブジェクトの [**setNumber(number)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setNumber-number-) メソッドを使用して適用できます。すべての組み込み番号形式には、固有の数値値が割り当てられています。開発者は、[**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) オブジェクトの [**setNumber(number)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setNumber-number-) メソッドに任意の数値を割り当てて表示形式を適用できます。このアプローチは高速です。Aspose.Cells がサポートする組み込み番号形式は以下の通りです。  

|**値**|**タイプ**|**フォーマット文字列**|  
| :- | :- | :- |  
|0|General|General|  
|1|Decimal|0|  
|2|Decimal|0.00|  
|3|Decimal|#,##0|  
|4|Decimal|#,##0.00|  
|5|Currency|$#,##0;$-#,##0|  
|6|Currency|$#,##0;[Red]$-#,##0|  
|7|Currency|$#,##0.00;$-#,##0.00|  
|8|Currency|$#,##0.00;[Red]$-#,##0.00|  
|9|Percentage|0%|  
|10|Percentage|0.00%|  
|11|Scientific|0.00E+00|  
|12|Fraction|# ?/?|  
|13|Fraction|# */*|  
|14|Date|m/d/yyyy|  
|15|Date|d-mmm-yy|  
|16|Date|d-mmm|  
|17|Date|mmm-yy|  
|18|Time|h:mm AM/PM|  
|19|Time|h:mm:ss AM/PM|  
|20|Time|h:mm|  
|21|Time|h:mm:ss|  
|22|Time|m/d/yy h:mm|  
|37|Currency|#,##0;-#,##0|  
|38|Currency|#,##0;[Red]-#,##0|  
|39|Currency|#,##0.00;-#,##0.00|  
|40|Currency|#,##0.00;[Red]-#,##0.00|  
|41|Accounting|_ * #,##0_ ;_ * "_ ;_ @_|  
|42|Accounting|_ $* #,##0_ ;_ $* "_ ;_ @_|  
|43|Accounting|_ * #,##0.00_ ;_ * "??_ ;_ @_|  
|44|Accounting|_ $* #,##0.00_ ;_ $* "??_ ;_ @_|  
|45|Time|mm:ss|  
|46|Time|h:mm:ss|  
|47|Time|mm:ss.0|  
|48|Scientific|##0.0E+00|  
|49|Text|@|  


{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-NumberSetting-HowToUseBuiltInNumberFormats.js" >}}


### **カスタム数値形式の使用方法**  

表示形式のカスタム形式文字列を定義するには、[**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) オブジェクトの [**setCustom(string)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setCustom-string-) メソッドを使用します。この方法は事前設定された形式を使用するよりも遅いですが、より柔軟です。  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-NumberSetting-HowToUseBuiltInNumberFormats.js" >}}


{{% alert color="primary" %}}  

番号形式を設定するために [**setCustom(string)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setCustom-string-) メソッドを使用すると、以前 `[**setNumber(number)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setNumber-number-)` メソッドで設定された形式は上書きされます。逆も同様です。  

{{% /alert %}}  

## **高度なトピック**  
- [Style.Customプロパティを設定する際のカスタム数値形式を確認する](/cells/ja/nodejs-cpp/check-custom-number-format-when-setting-style-custom-property/)  
- [サポートされている数値形式のリスト](/cells/ja/nodejs-cpp/list-of-supported-number-formats/)  
- [カスタム日付形式パターン g および ge mm dd の表現](/cells/ja/nodejs-cpp/render-custom-date-format-pattern-g-and-ge-mm-dd/)  
- [ブックでのカスタム数値小数点およびグループの区切りの指定](/cells/ja/nodejs-cpp/specify-custom-number-decimal-and-group-separators-for-workbook/)  
- [DBNumカスタムパターンの書式設定の指定](/cells/ja/nodejs-cpp/specifying-dbnum-custom-pattern-formatting/)  
