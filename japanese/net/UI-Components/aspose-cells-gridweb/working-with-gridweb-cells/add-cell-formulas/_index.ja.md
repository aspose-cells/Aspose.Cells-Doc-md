---
title: セルに数式を追加する
type: docs
weight: 30
url: /ja/net/aspose-cells-gridweb/add-cell-formula/
keywords: GridWeb,数式
description: この記事では、GridWebでセルに数式を追加する方法について紹介します。
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWebが提供する最も価値のある機能は、数式や関数のサポートです。Aspose.Cells.GridWebには、ワークシート内の数式を計算するための独自の数式エンジンがあります。Aspose.Cells.GridWebは、組み込みの関数やユーザー定義の関数または数式の両方をサポートしています。このトピックでは、Aspose.Cells.GridWeb APIを使用してセルに数式を追加する方法について詳しく説明します。

{{% /alert %}} 
## **セルに数式を追加し、アクセスしたり変更したりすることができます。セルのFormulaプロパティを使用して、Aspose.Cells.GridWebはシンプルから複雑なユーザー定義の数式をサポートしています。ただし、Aspose.Cells.GridWebには多くの組み込み関数や数式（Microsoft Excelと同様）が提供されています。組み込みの関数の完全なリストについては、[サポートされる関数のリスト](/cells/ja/net/aspose-cells-gridweb/list-of-supported-functions/)を参照してください。**
### **数式の追加と計算方法**
Aspose.Cells.GridWebでは、セルのFormulaプロパティを使用してセルに数式を追加、アクセス、および変更することができます。Aspose.Cells.GridWebは、簡単なものから複雑なものまで、ユーザー定義の数式をサポートしています。ただし、Aspose.Cells.GridWebには多くの組み込み関数や数式（Microsoft Excelに類似）も提供されています。組み込み関数の完全なリストについては、この[サポートされている関数のリスト](/cells/ja/net/aspose-cells-gridweb/list-of-supported-functions/)を参照してください。

{{% alert color="primary" %}} 

数式の構文は、Microsoft Excelの構文と互換性がある必要があります。たとえば、すべての数式は等号（=）で始まらなければなりません。

動的に数式を追加する場合、Aspose.Cells.GridWebは、**=**記号を使用しなくても数式として認識します。ただし、GUIで作業するエンドユーザーが使用する場合は、"="記号を使用する必要があります。

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddFormulas.aspx-AddFormulas.cs" >}}



**B3セルに追加された数式をGridWebによって計算されていません** 

![todo:image_alt_text](add-cell-formulas_1.png)

上のスクリーンショットに示されているように、数式がB3に追加されていますが、まだ計算されていません。すべての数式を計算するには、ワークシートに数式を追加した後、GridWebコントロールのGridWorksheetCollectionのCalculateFormulaメソッドを呼び出します。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddFormulas.aspx-CalculateFormulas.cs" >}}

{{% alert color="primary" %}} 

ユーザーは**送信**をクリックして数式を計算することもできます。

**GridWebの送信ボタンをクリック** 

![todo:image_alt_text](add-cell-formulas_2.png)

**重要**: ユーザーが**保存**ボタン、**元に戻す**ボタン、またはシートタブをクリックすると、すべての数式が自動的にGridWebによって計算されます。

**計算後の数式の結果** 

![todo:image_alt_text](add-cell-formulas_3.png)

{{% /alert %}} 
### **他のワークシートからセルを参照する**
Aspose.Cells.GridWebを使用すると、異なるワークシートに格納されている値をその数式で参照して、複雑な数式を作成することが可能です。

異なるワークシートからセルの値を参照する構文はSheetName!CellNameです。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddFormulas.aspx-AddComplexFormulas.cs" >}}
