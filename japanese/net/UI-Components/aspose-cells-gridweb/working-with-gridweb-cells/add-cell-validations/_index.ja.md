---
title: セルに検証を追加する
type: docs
weight: 70
url: /ja/net/aspose-cells-gridweb/add-cell-validations/
keywords: GridWeb,GridValidation,リスト検証,カスタム式検証
description: この記事では、GridWebでリスト検証、ドロップダウンリスト検証、およびカスタム式検証を追加する方法について紹介します。
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWebの高度な機能の1つは、セル用の入力検証規則を追加することです。開発者は、入力値を制御し検証するためにさまざまなタイプの検証規則をセルに作成することができます。このトピックでは、サポートされている検証タイプとその作成方法について説明します。

{{% /alert %}} 
## **検証の種類**
Aspose.Cells.GridWebを使用して3種類の検証が適用できます:

- リストの検証。
- ドロップダウンリストの検証。
- カスタム式の検証。

それぞれについて詳しく説明します。
### **リストの検証**
リストの検証では、ユーザーがセル入力をタイプするか、メニューから値を選択することができます。 セルにリストの検証を作成するには：

1. Web フォームに Aspose.Cells.GridWeb コントロールを追加します。
1. ワークシートにアクセスします。
1. 検証を追加するセルにアクセスします。
1. セルの検証を作成し、検証のタイプをリストとして指定します。
1. リストの検証に値を追加します。

この例のコードは、C1 にリストの検証を追加します。 ユーザーがセルをクリックすると、リストが表示されます。

**出力：リストから値を選択** 

![todo:image_alt_text](add-cell-validations_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddListValidation.aspx-AddListValidation.cs" >}}
### **ドロップダウンリストの検証**
ドロップダウンリストの検証では、事前定義されたリストから値を選択してセルに入力することができます。 ドロップダウンリストの検証を作成するには：

1. Web フォームに Aspose.Cells.GridWeb コントロールを追加します。
1. ワークシートにアクセスします。
1. 検証を作成するセルにアクセスします。
1. セルの検証を作成し、タイプを DropDownList として指定します。
1. 検証の値を追加します。

この例のコードは、C1 にドロップダウンリストの検証を追加します。 ユーザーがセルをクリックすると、ドロップダウンが表示され、ユーザーはそこから値を選択できます。

**ドロップダウンから値を選択** 

![todo:image_alt_text](add-cell-validations_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddDropdownListValidation.aspx-AddDropDownListValidation.cs" >}}
### **カスタム式の検証**
カスタム式の検証では、開発者が独自の正規表現を使用して入力値を検証することができます。 カスタム式の検証を作成するには：

1. Web フォームに Aspose.Cells.GridWeb コントロールを追加します。
1. ワークシートにアクセスします。
1. 検証を作成するセルにアクセスします。
1. セルの検証を作成し、タイプを CustomExpression として指定します。
1. 検証の正規表現を設定します。

このサンプルコードは、C1 にカスタム式の検証を追加します。 ユーザーは、正規表現に指定されたフォーマットに従った日付のみセルに追加できます。

**正規表現に従って C1 に日付値を追加** 

![todo:image_alt_text](add-cell-validations_3.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddCustomValidation.aspx-AddCustomValidation.cs" >}}
### **検証の強制**
Aspose.Cells.GridWeb を使用すると、ユーザーは入力データをサーバーに送信できます。 さまざまなセルに検証ルールがあっても、GridWeb コントロールの ForceValidation プロパティが true に設定されていない場合、間違った入力データもサーバーに送信され、検証が強制されません。 GridWeb の ForceValidation プロパティは常にデフォルトで true に設定されています。

ForceValidation プロパティが true の場合、すべてのセルの入力値が有効でない限り、コントロールはデータを Web サーバーに送信しません。 たとえば、誰かがセルに無効な入力値を入力したり、値を入力しなかった場合、クライアント側の検証がアクティブ化され、ユーザーは**送信**をクリックしてもデータを送信できません。

**GridWeb によって強調表示された誤った入力値** 

![todo:image_alt_text](add-cell-validations_4.png)
