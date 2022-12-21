---
title: Cell 数式を追加
type: docs
weight: 30
url: /ja/net/add-cell-formulas/
---
{{% alert color="primary" %}} 

Aspose.Cells.GridWeb が提供する最も価値のある機能は、数式または関数のサポートです。 Aspose.Cells.GridWeb には、ワークシートの数式を計算する独自の数式エンジンがあります。 Aspose.Cells.GridWeb は、組み込み関数とユーザー定義関数または数式の両方をサポートしています。このトピックでは、Aspose.Cells.GridWeb API を使用してセルに数式を追加する方法について詳しく説明します。

{{% /alert %}} 
## **数式を Cells に追加する**
### **数式を追加して計算する方法は?**
セルの Formula プロパティを使用して、セル内の数式を追加、アクセス、および変更することができます。 Aspose.Cells.GridWeb は、単純なものから複雑なものまで、ユーザー定義の数式をサポートしています。ただし、多数の組み込み関数または数式 (Microsoft Excel に類似) も Aspose.Cells.GridWeb で提供されます。組み込み関数の完全なリストを表示するには、これを参照してください。[サポートされている関数のリスト。](/cells/ja/net/list-of-supported-functions/)

{{% alert color="primary" %}} 

式の構文は、Microsoft Excel 構文と互換性がある必要があります。たとえば、すべての式は等号 (=) で始まる必要があります。

式を動的に追加するには、**=** 記号を使用しなくても Aspose.Cells.GridWeb はそれを式として認識しますが、エンド ユーザーが GUI で作業している場合は、「=」記号を使用する必要があります。

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddFormulas.aspx-AddFormulas.cs" >}}



**数式が B3 セルに追加されましたが、GridWeb によって計算されませんでした** 

![todo:画像_代替_文章](add-cell-formulas_1.png)

上のスクリーンショットでは、式が B3 に追加されていますが、まだ計算されていないことがわかります。すべての数式を計算するには、以下に示すようにワークシートに数式を追加した後、GridWeb コントロールの GridWorksheetCollection の CalculateFormula メソッドを呼び出します。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddFormulas.aspx-CalculateFormulas.cs" >}}

{{% alert color="primary" %}} 

をクリックして数式を計算することもできます。**送信**.

**GridWebのSubmitボタンをクリック** 

![todo:画像_代替_文章](add-cell-formulas_2.png)

**重要** ユーザーが**セーブ**また**元に戻す**ボタン、またはシート タブ、すべての式は GridWeb によって自動的に計算されます。

**計算後の数式結果** 

![todo:画像_代替_文章](add-cell-formulas_3.png)

{{% /alert %}} 
### **他のワークシートから Cells を参照する**
Aspose.Cells.GridWeb を使用すると、異なるワークシートに保存されている値を数式で参照して、複雑な数式を作成できます。

別のワークシートからセル値を参照するための構文は、SheetName!CellName です。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddFormulas.aspx-AddComplexFormulas.cs" >}}
