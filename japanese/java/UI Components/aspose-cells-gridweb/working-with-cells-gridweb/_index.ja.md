---
title: Cells GridWeb の操作
type: docs
weight: 50
url: /ja/java/working-with-cells-gridweb/
---
## **ワークシートで Cells にアクセスする**
このトピックでは、GridWeb の最も基本的な機能であるセルへのアクセスを見て、セルについて説明します。

各ワークシートには、GridCell オブジェクトのコレクションである GridCells オブジェクトが含まれています。 GridCell オブジェクトは、Aspose.Cells.GridWeb 内のセルを表します。 GridWeb を使用して任意のセルにアクセスできます。推奨される方法は 2 つあります。

- [名前によるセルへのアクセス](/cells/ja/java/working-with-cells-gridweb/).
- [行と列のインデックスによるセルへのアクセス](/cells/ja/java/working-with-cells-gridweb/).

以下では、それぞれのアプローチについて説明します。
### **Cell名を使用**
すべてのセルには固有の名前があります。たとえば、A1、A2、B1、B2 などです。Aspose.Cells.GridWeb を使用すると、開発者はセル名を使用して目的のセルにアクセスできます。セル名を (インデックスとして) GridWorksheet の GridCells コレクションに渡すだけです。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-Accessingcellbyname-Accessingcellbyname.jsp" >}}


### **行と列のインデックスの使用**
セルは、行インデックスと列インデックスの位置によっても認識できます。セルの行と列のインデックスを GridWorksheet の GridCells コレクションに渡すだけです。このアプローチは、上記のアプローチよりも高速です。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-Accessingcellbyrowandcolumnindices-Accessingcellbyrowandcolumnindices.jsp" >}}
## **Cell の値へのアクセスと変更**
[ワークシートで Cells にアクセスする](/cells/ja/java/working-with-cells-gridweb/#workingwithcellsgridweb-accessingcellsintheworksheet)セルへのアクセスについて説明しました。このトピックでは、その説明を拡張して、GridWeb API を使用してセル値にアクセスして変更する方法を示します。
### **Cell の値へのアクセスと変更**
#### **文字列値**
セルの値にアクセスして変更する前に、セルへのアクセス方法を知っておく必要があります。セルにアクセスするためのさまざまなアプローチの詳細については、次を参照してください。[ワークシートで Cells にアクセスする](/cells/ja/java/working-with-cells-gridweb/#workingwithcellsgridweb-accessingcellsintheworksheet).

各セルには、getStringValue() という名前のプロパティがあります。セルにアクセスすると、開発者は getStringValue() メソッドにアクセスしてセルの文字列値にアクセスできます。

{{% alert color="primary" %}} 

重要: 5 種類の値 (Boolean、int、double、DateTime、および string) をセルに格納できますが、getValue()/setValue() メソッドはオブジェクト値へのアクセス/変更にのみ使用できます。

{{% /alert %}} 

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AccessingModifyingCellStringValue-AccessingModifyingCellStringValue.jsp" >}}
#### **すべてのタイプの値**
Aspose.Cells.GridWeb は、各セルに対して特別なメソッド putValue も提供します。このメソッドを使用すると、セルに任意のタイプの値 (Boolean、int、double、DateTime、および string) を挿入または変更できます。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AccessingModifyingCell-AccessingModifyingCell.jsp" >}}



文字列形式の任意の種類の値を取り、適切なデータ型に自動的に変換できる、オーバーロードされたバージョンの putValue メソッドもあります。これを実現するには、以下の例に示すように、ブール値 true を putValue メソッドの別のパラメーターに渡します。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AccessingModifyingCellAllTypeValue-AccessingModifyingCellAllTypeValue.jsp" >}}
## **Cells への数式の追加**
Aspose.Cells.GridWeb が提供する最も価値のある機能は、数式または関数のサポートです。 Aspose.Cells.GridWeb には、ワークシートの数式を計算する独自の数式エンジンがあります。 Aspose.Cells.GridWeb は、組み込み関数とユーザー定義関数または数式の両方をサポートしています。このトピックでは、Aspose.Cells.GridWeb API を使用してセルに数式を追加する方法について詳しく説明します。
### **数式を追加して計算する方法は?**
セルの Formula プロパティを使用して、セル内の数式を追加、アクセス、および変更することができます。 Aspose.Cells.GridWeb は、単純なものから複雑なものまで、ユーザー定義の数式をサポートしています。ただし、多数の組み込み関数または数式 (Microsoft Excel に類似) も Aspose.Cells.GridWeb で提供されます。組み込み関数の完全なリストを表示するには、これを参照してください。[サポートされている関数のリスト。](/cells/ja/net/list-of-supported-functions/)

{{% alert color="primary" %}} 

式の構文は、Microsoft Excel 構文と互換性がある必要があります。たとえば、すべての式は等号 (=) で始まる必要があります。

プログラムで式を追加する場合、**=** 記号を使用しなくても Aspose.Cells.GridWeb はそれを式として認識しますが、GUI で作業するエンド ユーザーがそれを使用する必要がある場合。

{{% /alert %}} 

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AddingFormulastoCells-AddingFormulastoCells.jsp" >}}



**数式が B3 セルに追加されましたが、GridWeb によって計算されませんでした** 

![todo:画像_代替_文章](working-with-cells-gridweb_1.png)

上のスクリーンショットでは、式が B3 に追加されていますが、まだ計算されていないことがわかります。すべての数式を計算するには、以下に示すようにワークシートに数式を追加した後、GridWeb コントロールの GridWorksheetCollection の calculateFormula メソッドを呼び出します。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-CalculateFormula-CalculateFormula.jsp" >}}

をクリックして数式を計算することもできます。**送信**.

**GridWebのSubmitボタンをクリック** 

![todo:画像_代替_文章](working-with-cells-gridweb_2.png)

**重要** ユーザーが**セーブ**また**元に戻す**ボタン、またはシート タブ、すべての式は GridWeb によって自動的に計算されます。

**計算後の数式結果** 

![todo:画像_代替_文章](working-with-cells-gridweb_3.png)
### **他のワークシートから Cells を参照する**
Aspose.Cells.GridWeb を使用すると、異なるワークシートに保存されている値を数式で参照して、複雑な数式を作成できます。

別のワークシートからセル値を参照するための構文は、SheetName!CellName です。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-ReferencingCellsfromOtherWorksheets-ReferencingCellsfromOtherWorksheets.jsp" >}}
## **GridWeb の GridCell でデータ検証を作成する**
Aspose.Cells.GridWeb を使用すると、追加できます**データ検証**GridWorksheet.getValidations().add() メソッドを使用します。このメソッドを使用して、指定する必要があります**Cell 範囲**.ただし、単一の GridCell でデータ検証を作成する場合は、GridCell.createValidation() メソッドを使用して直接行うことができます。同様に、あなたは削除することができます**データ検証**GridCell.removeValidation() メソッドを使用して GridCell から。

次のサンプル コードは、**データ検証**セル B3 に20 ～ 40 以外の値を入力すると、セル B3 が表示されます。**検証エラー**の形で**赤XXXX**このスクリーンショットに示すように。

![todo:画像_代替_文章](working-with-cells-gridweb_4.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-CreateDataValidationinGridCellofGridWeb-CreateDataValidationinGridCellofGridWeb.jsp" >}}
## **カスタム コマンド ボタンの作成**
Aspose.Cells.GridWeb には、送信、保存、元に戻すなどの特別なボタンが含まれています。これらのボタンはすべて、Aspose.Cells.GridWeb の特定のタスクを実行します。カスタム タスクを実行するカスタム ボタンを追加することもできます。このトピックでは、この機能の使用方法について説明します。

次のサンプル コードでは、カスタム コマンド ボタンを作成する方法と、そのクリック イベントを処理する方法について説明します。カスタム コマンド ボタンには任意のアイコンを使用できます。説明のために、このイメージ アイコンを使用しました。

![todo:画像_代替_文章](working-with-cells-gridweb_5.png)

次のスクリーンショットでわかるように、ユーザーがカスタム コマンド ボタンをクリックすると、セル A1 にテキストが追加されます。**「カスタム コマンド ボタンがクリックされました。」**

![todo:画像_代替_文章](working-with-cells-gridweb_6.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-CreatingCustomCommandButtons-CreatingCustomCommandButtons.jsp" >}}
### **カスタム コマンド ボタンのイベント処理**
次のサンプル コードでは、カスタム コマンド ボタンのイベント処理を実行する方法について説明します。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-EventHandlingofCustomCommandButton-EventHandlingofCustomCommandButton.jsp" >}}
## **GridWeb のセルの書式設定**
### **考えられる使用シナリオ**
GridWeb では、ユーザーが 3% などのパーセンテージ形式でセル データを入力できるようになり、セル内のデータは自動的に 3.00% としてフォーマットされます。ただし、セル スタイルをパーセンテージ形式に設定する必要があります。これは GridTableItemStyle.NumberType が 9 または 10 のいずれかです。数値 9 は 3% を 3% として書式設定しますが、数値 10 は 3% を 3.00% として書式設定します。

{{% alert color="primary" %}} 

セル スタイルをパーセント形式に設定していない場合、入力データ 3% は 0.03 として表示されます。

{{% /alert %}} 
### **Cell GridWebワークシートのデータをパーセンテージ形式で入力**
次のサンプル コードは、セル A1 GridTableItemStyle.NumberType を 10 に設定するため、スクリーンショットに示すように、入力データ 3% は自動的に 3.00% としてフォーマットされます。

![todo:画像_代替_文章](working-with-cells-gridweb_7.png)
### **サンプルコード**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-EnterCellDataofGridWebWorksheet-EnterCellDataofGridWebWorksheet.jsp" >}}
