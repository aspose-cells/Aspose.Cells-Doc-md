---
title: 先行および従属
type: docs
weight: 230
url: /ja/java/precedents-and-dependents/
---

{{% alert color="primary" %}} 

特に共同で開発された複雑な財務ワークシートは、最も恥ずかしいエラーを隠すことがあります。式の正確さをチェックし、エラーの原因を特定することは、先行セルおよび従属セルを使用する式をチェックする際に困難になるかもしれません。

{{% /alert %}} 
## **紹介**
- **先行セル** は、他のセルの数式で参照されているセルです。たとえば、セル D10 が数式 =B5 を含む場合、セル B5 はセル D10 の先行セルです。
- **従属セル** は、他のセルを参照する式を含んでいます。たとえば、セル D10 に式 =B5 が含まれている場合、セル D10 はセル B5 の従属セルです。

スプレッドシートをわかりやすくするために、スプレッドシートに含まれるセルが式で使用されているかを明確に表示することがあります。同様に、他のセルの従属セルを抽出することがあります。

Aspose.Cells を使用すると、セルをトレースしてリンクされているセルを特定することができます。
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
## **先行および従属セルをトレース： Aspose.Cells**
### **先行をトレース**
Aspose.Cells を使用すると、先行セルを取得することが容易になります。シンプルな式の先行セルに提供されているセルだけでなく、名前付き範囲で複雑な式の先行セルに提供されているセルを見つけることもできます。

以下の例では、テンプレートの Excel ファイルである Book1.xls を使用しています。スプレッドシートには最初のワークシートにデータと数式が含まれています。

Aspose.Cellsは、[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/Cell)クラスの[GetPrecedents](https://reference.aspose.com/cells/java/com.aspose.cells/Cell#getPrecedents--)メソッドを提供しており、これを使用してセルの直前のセルを追跡できます。これにより、[ReferredAreaCollection](https://reference.aspose.com/cells/java/com.aspose.cells/ReferredAreaCollection)が返されます。上記の例では、Book1.xlsにおいて、セルB7に式"=SUM(A1:A3)"が含まれています。したがって、セルA1:A3はセルB7の直前のセルです。次の例は、テンプレートファイルBook1.xlsを使用して、直前のセルの追跡機能を実証しています。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-TracingPrecedents.java" >}}
### **従属をトレース**
Aspose.Cellsを使用すると、スプレッドシート内の依存セルを取得できます。Aspose.Cellsは、単純な式に関連するデータを提供するセルだけでなく、名前付き範囲からのデータを提供する複雑な式の依存セルも検索できます。

Aspose.Cellsは、[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/Cell)クラスの[GetDependents](https://reference.aspose.com/cells/java/com.aspose.cells/Cell#getDependents(boolean))メソッドを提供しており、これを使用してセルの依存セルを追跡できます。たとえば、Book1.xlsxにはセルB2およびC2に式"=A1+20"および"=A1+30"が含まれています。次の例は、テンプレートファイルBook1.xlsxを使用して、A1セルの依存セルを追跡する方法を示しています。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-TracingDependents.java" >}}
### **計算チェーンに従って直前および依存セルを追跡する**
追跡先行および依存関係の上記のAPIは、式自体に従います。これらは、数式の相互依存関係を追跡するための便利な方法を提供します。ワークブックに多数の数式があり、ユーザーがすべてのセルの追跡先行および依存関係を追跡する必要がある場合、パフォーマンスが低下します。そのような状況では、[GetPrecedentsInCalculation](https://reference.aspose.com/cells/java/com.aspose.cells/Cell#getPrecedentsInCalculation--)および[GetDependentsInCalculation](https://reference.aspose.com/cells/java/com.aspose.cells/Cell#getDependentsInCalculation(boolean)/)メソッドを使用することを検討すべきです。これらの2つのメソッドは、計算チェーンに従って依存関係を追跡します。したがってこれらを使用するためには、まず[Workbook.Settings.FormulaSettings.EnableCalculationChain](https://reference.aspose.com/cells/java/com.aspose.cells/FormulaSettings#EnableCalculationChain)で計算チェーンを有効にする必要があります。その後、[Workbook.CalculateFormula()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula(com.aspose.cells.CalculationOptions))でワークブックの完全な計算を行う必要があります。その後、追跡先行または依存関係を必要とするすべてのセルのためにこれを行うことができます。

一部の数式では、GetPrecedentsとGetPrecedentsInCalculationの結果の先行は異なる場合がありますし、GetDependentsとGetDependentsInCalculationの結果の依存関係も異なる場合があります。たとえば、セルA1の数式が"=IF(TRUE,B2,C3)"である場合、GetPrecedentsはA1の先行としてB2とC3を提供します。したがって、GetDependentsを確認すると、B2とC3の両方が依存関係A1を持っています。しかし、この数式の計算では、計算結果に影響するのは明らかにB2だけです。そのため、GetPrecedentsInCalculationはA1にC3を提供しませんし、GetDependentsInCalculationはC3にA1を提供しません。時には、ユーザーは現在のワークブックのデータに基づいて実際に計算結果に影響するそれらの相互依存関係を追跡する必要がある場合があります。その場合は、GetDependentsInCalculation/GetPrecedentsInCalculationを使用する必要があります。

以下のサンプルコードは、セルに対する計算チェーンに従って先行および依存関係を追跡する方法を示しています。


{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-TracingDependenciesInCalculation.java" >}}
