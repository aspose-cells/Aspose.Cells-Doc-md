---
title: Cell 検証を追加
type: docs
weight: 70
url: /ja/net/add-cell-validations/
---
{{% alert color="primary" %}} 

Aspose.Cells.GridWeb の高度な機能の 1 つは、セルの入力検証規則を追加することです。開発者は、入力値を制御および検証するために、セルに対してさまざまな種類の検証ルールを作成できます。このトピックでは、サポートされている検証の種類とその作成方法について説明します。

{{% /alert %}} 
## **検証の種類**
Aspose.Cells.GridWeb を使用して、3 種類の検証を適用できます。

- リストの検証。
- ドロップダウン リストの検証。
- カスタム式の検証。

それぞれについて、以下で詳しく説明します。
### **リストの検証**
リストの検証により、ユーザーは値を入力するか、メニューから値を選択することにより、セル入力を提供できます。セルのリスト検証を作成するには:

1. Aspose.Cells.GridWeb コントロールを Web フォームに追加します。
1. ワークシートにアクセスします。
1. 検証を追加するセルにアクセスします。
1. セルの検証を作成し、検証タイプをリストとして指定します。
1. リスト検証の値を追加します。

サンプル コードは、C1 にリストの検証を追加します。ユーザーがセルをクリックすると、リストが表示されます。

**出力: リストから値を選択する** 

![todo:画像_代替_文章](add-cell-validations_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddListValidation.aspx-AddListValidation.cs" >}}
### **ドロップダウン リストの検証**
ドロップダウン リストの検証により、ユーザーは事前定義されたリストから値を選択してセルに入力できます。ドロップダウン リストの検証を作成するには:

1. Aspose.Cells.GridWeb コントロールを Web フォームに追加します。
1. ワークシートにアクセスします。
1. 検証を作成するセルにアクセスします。
1. セルの検証を作成し、タイプを DropDownList として指定します。
1. 検証用の値を追加します。

サンプル コードは、ドロップダウン リストの検証を C1 に追加します。ユーザーがセルをクリックすると、ドロップダウンが表示され、ユーザーはそこから値を選択できます。

**ドロップダウンからの値の選択** 

![todo:画像_代替_文章](add-cell-validations_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddDropdownListValidation.aspx-AddDropDownListValidation.cs" >}}
### **カスタム式の検証**
カスタム式の検証により、開発者は独自のカスタム正規表現を記述して入力値を検証できます。カスタム式検証を作成するには:

1. Aspose.Cells.GridWeb コントロールを Web フォームに追加します。
1. ワークシートにアクセスします。
1. 検証を作成するセルにアクセスします。
1. セルの検証を作成し、型を CustomExpression として指定します。
1. 検証の正規表現を設定します。

サンプル コードは、カスタム式の検証を C1 に追加します。ユーザーは、正規表現で指定された形式に従ってのみセルに日付を追加できます。

**正規表現に従って C1 に日付値を追加する** 

![todo:画像_代替_文章](add-cell-validations_3.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddCustomValidation.aspx-AddCustomValidation.cs" >}}
### **検証の強制**
Aspose.Cells.GridWeb を使用すると、ユーザーは入力データをサーバーに送信できます。異なるセルに検証規則があり、GridWeb コントロールの ForceValidation プロパティが true に設定されていない場合でも、間違った入力データもサーバーに送信され、検証は強制されません。 GridWeb の ForceValidation プロパティは、デフォルトで常に true に設定されています。

 ForceValidation プロパティが true の場合、すべてのセルの入力値が有効になるまで、コントロールは Web サーバーにデータをポストしません。たとえば、誰かがセルに無効な入力値を入力した場合、または値を入力しなかった場合、クライアント側の検証がアクティブになり、ユーザーはクリックしてもデータを投稿できません。**送信**.

**GridWeb によって強調表示された間違った入力値** 

![todo:画像_代替_文章](add-cell-validations_4.png)
