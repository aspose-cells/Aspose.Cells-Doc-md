---
title: 先行および従属
type: docs
weight: 230
url: /ja/python-net/precedents-and-dependents/
---

{{% alert color="primary" %}} 

特に共同で開発された複雑な財務ワークシートは、最も恥ずかしいエラーを隠すことがあります。式の正確さをチェックし、エラーの原因を特定することは、先行セルおよび従属セルを使用する式をチェックする際に困難になるかもしれません。

{{% /alert %}} 
## **紹介**
- **先行セル** は、他のセルの数式で参照されているセルです。たとえば、セル D10 が数式 =B5 を含む場合、セル B5 はセル D10 の先行セルです。
- **従属セル** は、他のセルを参照する式を含んでいます。たとえば、セル D10 に式 =B5 が含まれている場合、セル D10 はセル B5 の従属セルです。

スプレッドシートをわかりやすくするために、スプレッドシートに含まれるセルが式で使用されているかを明確に表示することがあります。同様に、他のセルの従属セルを抽出することがあります。

Aspose.Cells for Python via .NETはセルをトレースし、リンクされているセルを見つけ出すことができます。
## **先行および従属セルのトレース： Microsoft Excel**
例えば、セル C1 が式を含む C3 および C4 に依存しており、C1 が変更される場合（つまり式が上書きされる場合）、C3 および C4 などの他のセルは、ビジネスルールに基づいてスプレッドシートをバランスさせるために変更する必要があります。

同様に、C1 に式 "=(B1*22)/(M2*N32)" を含むとします。C1 が依存しているセルである先行セル B1、M2、N32 を見つけたいとします。

特定のセルの依存関係を他のセルにトレースする必要があるかもしれません。ビジネスルールが式に埋め込まれている場合、依存関係を見つけ、それに基づいていくつかのルールを実行したいと思うかもしれません。同様に、特定のセルの値が変更される場合、その変更に影響を受けるワークシート内のセルを見つけたいと思うかもしれません。

Microsoft Excel を使用すると、先行および従属をトレースすることができます。

1. **表示ツールバー**から**数式監査**を選択します。数式監査ダイアログが表示されます。
1. 先行をトレース：
   1. 先行セルを特定したい式を含むセルを選択します。
   1. 直接データを提供する各セルにトレーサーアローを表示するには、 **式監査** ツールバーの **先行をトレース** をクリックします。
1. 特定のセルを参照する式をトレースする（従属）
   1. 従属セルを特定したいセルを選択します。
   1. アクティブセルに依存している各セルにトレーサーアローを表示するには、 **式監査** ツールバーの **従属をトレース** をクリックします。
## **前提セルと従属セルのトレース：Aspose.Cells for Python via .NET**
### **先行をトレース**
Aspose.Cells for Python via .NETは前提セルを簡単に取得できます。単純な式の前提となるセルだけでなく、名前付き範囲の複雑な式の前提を提供するセルも見つけることができます。

以下の例では、テンプレートの Excel ファイルである Book1.xls を使用しています。スプレッドシートには最初のワークシートにデータと数式が含まれています。

Aspose.Cells for Python via .NETは、[**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell)クラスの[**get_precedents**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_precedents/#)メソッドを使用してセルの前提セルを追跡します。これは[**ReferredAreaCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/referredareacollection)を返します。上記の例では、Book1.xlsのセルB7は“=SUM(A1:A3)”という式を含んでいます。したがって、A1:A3はセルB7の前提セルです。この追跡プリセデント機能の例をテンプレートファイルBook1.xlsで示します。



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-TracingPrecedents-1.py" >}}
### **従属をトレース**
Aspose.Cells for Python via .NETは、スプレッドシート内の従属セルを取得することも可能です。これらのセルは、単純な式のデータ提供だけでなく、名前付き範囲の複雑な式においてもデータを提供するセルを見つけ出すことができます。

Aspose.Cells for Python via .NETは、[**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell)クラスの[**get_dependents**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_dependents/#bool)メソッドを用いてセルの従属セルを追跡します。例えば、Book1.xlsxのセルB2とC2にはそれぞれ“=A1+20”と“=A1+30”という式があります。これらのセルの従属セルを追跡する方法を例示します。



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-TracingDependents-1.py" >}}

### **計算チェーンに従って直前および依存セルを追跡する**
前述の前提セルと従属セルの追跡APIは、式式そのものに基づいています。これらは、少数の式の相互依存関係を追跡する便利な方法を提供します。もしも、多くの式が含まれるワークブック内で、すべてのセルの前提と従属を追跡したい場合、パフォーマンスが低下します。その場合、[**get_precedents_in_calculation**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_precedents_in_calculation/#)と[**get_dependents_in_calculation**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_dependents_in_calculation/#bool)メソッドの使用を検討してください。これらのメソッドは計算チェーンに沿って依存関係を追跡します。まず、[**Workbook.settings.formula_settings.enable_calculation_chain**](https://reference.aspose.com/cells/python-net/aspose.cells/formulasettings/enable_calculation_chain/)を使って計算チェーンを有効にし、その後、[**Workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#)を使ってワークブック全体の再計算を行います。それから、必要なセルの前提や従属を追跡できます。

一部の数式では、GetPrecedentsとGetPrecedentsInCalculationの結果の先行は異なる場合がありますし、GetDependentsとGetDependentsInCalculationの結果の依存関係も異なる場合があります。たとえば、セルA1の数式が"=IF(TRUE,B2,C3)"である場合、GetPrecedentsはA1の先行としてB2とC3を提供します。したがって、GetDependentsを確認すると、B2とC3の両方が依存関係A1を持っています。しかし、この数式の計算では、計算結果に影響するのは明らかにB2だけです。そのため、GetPrecedentsInCalculationはA1にC3を提供しませんし、GetDependentsInCalculationはC3にA1を提供しません。時には、ユーザーは現在のワークブックのデータに基づいて実際に計算結果に影響するそれらの相互依存関係を追跡する必要がある場合があります。その場合は、GetDependentsInCalculation/GetPrecedentsInCalculationを使用する必要があります。

以下のサンプルコードは、セルに対する計算チェーンに従って先行および依存関係を追跡する方法を示しています。


{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-TracingDependenciesInCalculation.py" >}}

{{< app/cells/assistant language="python-net" >}}
