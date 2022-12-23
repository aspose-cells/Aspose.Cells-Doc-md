---
title: 先例と扶養家族
type: docs
weight: 230
url: /ja/net/precedents-and-dependents/
---
{{% alert color="primary" %}} 

複雑な財務ワークシート、特に共同で開発されたものは、最も厄介なエラーを隠すことができます。数式が参照元セルと従属セルを使用している場合、数式の正確性をチェックし、エラーの原因を見つけることが難しい場合があります。

{{% /alert %}} 
## **序章**
- **先行細胞**別の Cell の数式によって参照されるセルです。たとえば、セル D10 に数式 =B5 が含まれている場合、セル B5 はセル D10 の参照元です。
- **依存セル**他のセルを参照する数式が含まれています。たとえば、セル D10 に式 =B5 が含まれている場合、セル D10 はセル B5 に従属しています。

スプレッドシートを読みやすくするために、スプレッドシートのどのセルが数式で使用されているかを明確に示したい場合があります。同様に、他のセルの依存セルを抽出することもできます。

Aspose.Cells を使用すると、セルをトレースして、リンクされているセルを見つけることができます。
## **先例と依存関係のトレース Cells: Microsoft Excel**
式は、クライアントによって行われた変更に基づいて変更される場合があります。たとえば、セル C1 が式を含む C3 および C4 に依存しており、C1 が変更された場合 (式がオーバーライドされる)、ビジネス ルールに基づいてスプレッドシートのバランスを取るために C3 および C4、または他のセルを変更する必要があります。

同様に、C1 に式 "=(B1*22)/(M2*N32)". C1 が依存しているセル、つまり先行セル B1、M2、および N32 を見つけたいと考えています。

特定のセルの他のセルへの依存関係を追跡する必要がある場合があります。ビジネスルールが数式に埋め込まれている場合、依存関係を見つけて、それに基づいていくつかのルールを実行したいと考えています。同様に、特定のセルの値が変更された場合、ワークシート内のどのセルがその変更の影響を受けるでしょうか?

Microsoft Excel では、ユーザーは先例と依存関係を追跡できます。

1. 上で**ビュー ツールバー**、 選択する**フォーミュラ監査**. [式の監査] ダイアログが表示されます。
1. トレースの前例:
1. 参照元セルを検索する数式を含むセルを選択します。
 1. アクティブ セルにデータを直接提供する各セルへのトレーサー矢印を表示するには、**前例をトレース**上で**フォーミュラ監査**ツールバー。
1. 特定のセル (依存セル) を参照する数式をトレースする
1. 依存セルを識別したいセルを選択します。
 1. アクティブなセルに依存する各セルへのトレーサ矢印を表示するには、[式の監査] ツールバーの [依存関係のトレース] をクリックします。
## **先例と従属をトレース Cells: Aspose.Cells**
### **前例をたどる**
Aspose.Cells を使用すると、先行セルを簡単に取得できます。単純な数式の参照元にデータを提供するセルを取得できるだけでなく、名前付き範囲を持つ複雑な数式の参照元にデータを提供するセルも検索できます。

以下の例では、テンプレートの Excel ファイル Book1.xls が使用されています。スプレッドシートには、最初のワークシートにデータと数式があります。

 Aspose.Cells は[Cell](https://reference.aspose.com/cells/net/aspose.cells/cell)クラス'[GetPrecedents](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getprecedents)細胞の前例を追跡するために使用される方法。それは[ReferredAreaCollection](https://reference.aspose.com/cells/net/aspose.cells/referredareacollection).上記のように、Book1.xls のセル B7 には数式「=SUM(A1:A3)」が含まれています。したがって、セル A1:A3 はセル B7 の先行セルです。次の例は、テンプレート ファイル Book1.xls を使用した参照元のトレース機能を示しています。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-TracingPrecedents-1.cs" >}}
### **依存関係のトレース**
Aspose.Cells を使用すると、スプレッドシートで依存セルを取得できます。 Aspose.Cells は、単純な数式に関するデータを提供するセルを取得できるだけでなく、名前付き範囲を持つ複雑な数式の依存関係にデータを提供するセルを検索することもできます。

Aspose.Cells は[Cell](https://reference.aspose.com/cells/net/aspose.cells/cell)クラス'[GetDependents](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getdependents)セルの依存関係を追跡するために使用されるメソッド。たとえば、Book1.xlsx では、B2 セルと C2 セルにそれぞれ "=A1+20" と "=A1+30" という数式があります。次の例は、テンプレート ファイル Book1.xlsx を使用して A1 セルの依存関係をトレースする方法を示しています。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-TracingDependents-1.cs" >}}
### **計算チェーンに従って先行セルと依存セルをトレースする**
先例と依存関係をトレースする上記の API は、式の式自体に従います。それらは、ユーザーがいくつかの式の相互依存関係を追跡するための便利な方法を提供するだけです。ワークブックに大量の数式があり、ユーザーがすべてのセルの参照元と依存関係をトレースする必要がある場合、パフォーマンスが低下します。このような状況では、ユーザーは使用を検討する必要があります[GetPrecedentsInCalculation](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getprecedentsincalculation/)と[GetDependentsInCalculation](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getdependentsincalculation/)メソッド。これら 2 つのメソッドは、計算チェーンに従って依存関係をトレースします。したがって、それらを使用するには、まず計算チェーンを有効にする必要があります[Workbook.Settings.FormulaSettings.EnableCalculationChain](https://reference.aspose.com/cells/net/aspose.cells/formulasettings/enablecalculationchain/) .次に、ワークブックの完全な計算を実行する必要があります[Workbook.CalculateFormula()](https://reference.aspose.com/cells/net/aspose.cells.workbook/calculateformula/methods/1).その後、必要なすべてのセルの前例または依存関係を追跡できます。

一部の数式では、結果の参照元が GetPrecedents と GetPrecedentsInCalculation で異なる場合があり、結果の従属が GetDependents と GetDependentsInCalculation で異なる場合があります。たとえば、セル A1 の数式が "=IF(TRUE,B2,C3)" の場合、GetPrecedents は A1 の参照元として B2 と C3 を提供します。したがって、GetDependents でチェックすると、B2 と C3 は両方とも従属 A1 を持っています。ただし、この式の計算では、B2 のみが計算結果に影響を与える可能性があることは明らかです。したがって、GetPrecedentsInCalculation は A1 に対して C3 を提供せず、GetDependentsInCalculation は C3 に対して A1 を提供しません。ワークブックの現在のデータに基づいて数式の計算結果に実際に影響を与える相互依存関係をトレースする必要がある場合は、GetDependents/GetPrecedents の代わりに GetDependentsInCalculation/GetPrecedentsInCalculation を使用する必要があります。

次の例は、セルの計算チェーンに従って参照元と従属をトレースする方法を示しています。


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-TracingDependenciesInCalculation.cs" >}}
