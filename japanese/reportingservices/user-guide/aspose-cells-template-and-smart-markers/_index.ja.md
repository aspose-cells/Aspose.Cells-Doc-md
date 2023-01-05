---
title: Aspose.Cells テンプレートとスマートマーカー
type: docs
weight: 30
url: /ja/reportingservices/aspose-cells-template-and-smart-markers/
---
{{% alert color="primary" %}} 

Aspose.Cells テンプレートは、スマート マーカーを含む Microsoft Excel ワークブックです。スマート マーカーは、レポート アイテムのデータ プレースホルダーとして機能し、レンダリング時に対応するデータに置き換えられます。スマート マーカーには、次の 5 種類があります。すべてのマーカーは、Aspose.Cells.Report.Designer によってテンプレートに挿入できます。手動で編集することもできます。

{{% /alert %}} 
### **スマートマーカー**
#### **データ マーカー**
のフォーマット**データ マーカー**&=DataSetName.FieldName です。例: &=SalesDetail.sales ここで、SalesDetail はデータ セットまたはクエリの名前であり、sales はそのフィールドの 1 つの名前です。レンダリング時に、データ マーカーは Reporting Services によって提供されるデータセットの値に置き換えられます。
#### **Reporting Services 数式マーカー**
Reporting Services のフォーマット**数式マーカー**&=式です。例: &=sum(SalesDetail.sales)/100。式は、関数、データセット フィールド、演算子などで構成されます。レンダリング時。 Reporting Services の数式マーカーは、計算された値に置き換えられます。
#### **Reporting Services グローバル変数マーカー**
Reporting Services のフォーマット**グローバル変数マーカー**&=グローバルです!変数名。例: &=Globals!ExecutionTime ここで、ExecutionTime はグローバル変数の名前です。グローバル変数マーカーは、レンダリング時にグローバル変数値に置き換えられます。
#### **Reporting Services パラメータ マーカー**
レポート パラメータには、値とラベルの 2 つの属性があります。その結果、**パラメータ マーカー**&= パラメータの 2 つの形式があります。 ParamName.Value と &=Parameters!パラメータ名.ラベル。それぞれパラメータの名前とラベルを示します。レンダリング時に、パラメーター マーカーはユーザーが入力したパラメーター値に置き換えられます。
#### **動的数式**
挿入された行で計算を行うには、動的数式を使用します。**動的数式**Microsoft 数式がエクスポート プロセス中に挿入される行を参照している場合でも、Excel の数式をセルに挿入できます。挿入された行ごとに繰り返すことも、データ マーカーが配置されているセルでのみ使用することもできます。

動的数式の形式は &=&=RepeatDynamicFormula です。

動的数式では、次の追加オプションを使用できます。

- {r} – 現在の行番号。
- {2}、{-1} – 現在の行番号へのオフセット。

**繰り返し動的数式と結果の Excel ワークシート** 

![todo:画像_代替_文章](aspose-cells-template-and-smart-markers_1.png)
