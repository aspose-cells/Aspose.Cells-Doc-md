---
title: Aspose.Cells テンプレートおよびスマートマーカー
type: docs
weight: 30
url: /ja/reportingservices/aspose-cells-template-and-smart-markers/
---

{{% alert color="primary" %}} 

Aspose.Cellsテンプレートは、Smart Markersを含むMicrosoft Excelワークブックです。Smart Markersは、レポートアイテムのデータプレースホルダーとして機能し、レンダリング時に対応するデータで置換されます。以下に示す5種類のスマートマーカーがあります。すべてのマーカーは、Aspose.Cells.Report.Designerによってテンプレートに挿入することができます。また、手動で編集することもできます。 

{{% /alert %}} 
### **スマートマーカー**
#### **データマーカー**
**データマーカー**のフォーマットは、&=DataSetName.FieldNameです。例: &=SalesDetail.sales where SalesDetailはデータセットまたはクエリの名前であり、salesはそのフィールドの名前です。データマーカーは、レンダリング時にReporting Servicesが提供するデータセットの値で置換されます。
#### **Reporting Servicesフォーミュラマーカー**
Reporting Servicesの**フォーミュラマーカー**のフォーマットは、&=expressionです。例: &=sum(SalesDetail.sales)/100. 式には、関数、データセットのフィールド、演算子などが含まれます。レンダリング時に、Reporting Servicesフォーミュラマーカーは計算された値で置換されます。
#### **Reporting Servicesグローバル変数マーカー**
Reporting Servicesの**グローバル変数マーカー**のフォーマットは、&=Globals! Variable Nameです。例: &=Globals!ExecutionTime where ExecutionTimeはグローバル変数の名前です。レンダリング時に、グローバル変数マーカーはグローバル変数の値で置換されます。
#### **Reporting Servicesパラメータマーカー**
レポートパラメータには、値とラベルの2つの属性があります。したがって、**パラメータマーカー**には、次の2つのフォーマットがあります: &= Parameters! ParamName.Value および &=Parameters! ParamName.Label. これらは、それぞれパラメータの名前とラベルを示します。レンダリング時に、パラメータマーカーはユーザーが入力したパラメータの値で置換されます。
#### **動的な式**
挿入された行で計算を行うためには、ダイナミックフォーミュラを使用します。**ダイナミックフォーミュラ**を使用すると、エクスポートプロセス中に挿入される行を参照する式でも、Microsoft Excelの式をセルに挿入することができます。それらは、各挿入された行に繰り返すこともできますし、データマーカーが配置されているセルでのみ使用することもできます。

ダイナミックフォーミュラのフォーマットは &=&=RepeatDynamicFormulaです。

ダイナミックフォーミュラでは、次の追加オプションが利用可能です:

- {r} – 現在の行番号。
- {2}, {-1} – 現在の行番号からのオフセット。

**繰り返しダイナミックフォーミュラと結果のExcelワークシート** 

![todo:image_alt_text](aspose-cells-template-and-smart-markers_1.png)
