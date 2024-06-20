---
title: Cells GridWebでの作業
type: docs
weight: 50
url: /ja/java/working-with-cells-gridweb/
---

## **ワークシート内のセルへのアクセス**
このトピックでは、セルにアクセスするためのGridWebの基本的な機能であるセルへのアクセスについて説明します。

各ワークシートにはGridCellsオブジェクト、GridCellオブジェクトのコレクションが含まれています。GridCellオブジェクトはAspose.Cells.GridWebのセルを表します。GridWebを使用して任意のセルにアクセスすることができます。2つの推奨される方法があります。

- [名前によるセルのアクセス](/cells/ja/java/working-with-cells-gridweb/)
- [行および列インデックスによるセルのアクセス](/cells/ja/java/working-with-cells-gridweb/)

以下では、それぞれのアプローチについて説明します。
### **セル名の使用**
すべてのセルにはユニークな名前があります。例えば、A1、A2、B1、B2などです。Aspose.Cells.GridWebを使用すると、目的のセルにcell nameを使ってアクセスすることができます。単にcell name（インデックスとして）をGridWorksheetのGridCellsコレクションに渡します。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-Accessingcellbyname-Accessingcellbyname.jsp" >}}


### **行と列のインデックスを使用する**
セルは、行および列インデックスの位置によっても認識できます。セルの行および列インデックスをGridWorksheetのGridCellsコレクションに渡すだけです。このアプローチは、上記のものよりも高速です。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-Accessingcellbyrowandcolumnindices-Accessingcellbyrowandcolumnindices.jsp" >}}
## **セルの値へのアクセスと変更**
[ワークシート内のセルへのアクセス](/cells/ja/java/working-with-cells-gridweb/#workingwithcellsgridweb-accessingcellsintheworksheet) でセルへのアクセス方法について説明しました。このトピックでは、GridWeb APIを使用してセルの値にアクセスして変更する方法について説明します。
### **セルの値のアクセスおよび変更**
#### **文字列の値**
セルの値へのアクセスと変更の前に、どのようにセルにアクセスするかを知る必要があります。セルへのアクセスの異なるアプローチの詳細については、[ワークシート内のセルへのアクセス](/cells/ja/java/working-with-cells-gridweb/#workingwithcellsgridweb-accessingcellsintheworksheet) を参照してください。

各セルには、getStringValue()というプロパティがあります。セルにアクセスすると、開発者はgetStringValue()メソッドを使用してセルの文字列値にアクセスできます。

{{% alert color="primary" %}} 

重要: セルには真偽値、整数、倍精度浮動小数点数、日付と時刻、文字列の5種類の値を格納することができますが、getValue()/setValue()メソッドはオブジェクトの値にしかアクセス/変更できません。

{{% /alert %}} 

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AccessingModifyingCellStringValue-AccessingModifyingCellStringValue.jsp" >}}
#### **すべての種類の値**
Aspose.Cells.GridWebは各セルに対してputValueという特別なメソッドも提供しています。このメソッドを使うと、セルに真偽値、整数、倍精度浮動小数点数、日付と時刻、文字列など、任意の種類の値を挿入または変更できます。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AccessingModifyingCell-AccessingModifyingCell.jsp" >}}



putValueメソッドには、任意の種類の値を文字列形式で受け取り、自動的に適切なデータ型に変換するオーバーロードされたバージョンもあります。これを実現するためには、putValueメソッドの別のパラメータにtrueという真偽値を渡します。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AccessingModifyingCellAllTypeValue-AccessingModifyingCellAllTypeValue.jsp" >}}
## **セルに数式を追加する**
Aspose.Cells.GridWebが提供する最も価値のある機能は、数式や関数のサポートです。Aspose.Cells.GridWebには、ワークシート内の数式を計算するための独自の数式エンジンがあります。Aspose.Cells.GridWebは、組み込みの関数やユーザー定義の関数または数式の両方をサポートしています。このトピックでは、Aspose.Cells.GridWeb APIを使用してセルに数式を追加する方法について詳しく説明します。
### **数式の追加と計算方法**
セルのFormulaプロパティを使用することで、セルに数式を追加し、アクセスして変更することが可能です。Aspose.Cells.GridWebは、単純なものから複雑なものまでのユーザー定義の数式をサポートしています。ただし、大量の組み込み関数または数式（Microsoft Excelに類似）もAspose.Cells.GridWebには付属しています。組み込みの関数の完全なリストを見るには、[サポートされている関数のリスト](/cells/ja/net/list-of-supported-functions/)を参照してください。

{{% alert color="primary" %}} 

数式の構文は、Microsoft Excelの構文と互換性がある必要があります。たとえば、すべての数式は等号（=）で始まらなければなりません。

Aspose.Cells.GridWebでは数式をプログラムで追加する場合、**=**を使用しなくてもAspose.Cells.GridWebはそれを数式として認識しますが、GUIで作業するエンドユーザーがそれを使用する必要があります。

{{% /alert %}} 

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AddingFormulastoCells-AddingFormulastoCells.jsp" >}}



**B3セルに追加された数式をGridWebによって計算されていません** 

![todo:image_alt_text](working-with-cells-gridweb_1.png)

上記のスクリーンショットでは、B3に数式が追加されていますが、まだ計算されていません。すべての数式を計算するには、数式がワークシートに追加された後、GridWebコントロールのGridWorksheetCollectionのcalculateFormulaメソッドを呼び出してください。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-CalculateFormula-CalculateFormula.jsp" >}}

ユーザーは**送信**をクリックして数式を計算することもできます。

**GridWebの送信ボタンをクリック** 

![todo:image_alt_text](working-with-cells-gridweb_2.png)

**重要**: ユーザーが**保存**ボタン、**元に戻す**ボタン、またはシートタブをクリックすると、すべての数式が自動的にGridWebによって計算されます。

**計算後の数式の結果** 

![todo:image_alt_text](working-with-cells-gridweb_3.png)
### **他のワークシートからセルを参照する**
Aspose.Cells.GridWebを使用すると、異なるワークシートに格納されている値をその数式で参照して、複雑な数式を作成することが可能です。

異なるワークシートからセルの値を参照する構文はSheetName!CellNameです。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-ReferencingCellsfromOtherWorksheets-ReferencingCellsfromOtherWorksheets.jsp" >}}
## **GridWebのGridCellにデータの妥当性を作成する**
Aspose.Cells.GridWebでは、GridWorksheet.getValidations().add()メソッドを使用して**データの妥当性**を追加できます。このメソッドを使用すると、**セル範囲**を指定する必要があります。ただし、単一のGridCellにデータの妥当性を作成する場合は、GridCell.createValidation()メソッドを直接使用することができます。同様に、GridCell.removeValidation()メソッドを使用してGridCellから**データの妥当性**を削除することもできます。

次のサンプルコードは、セルB3に**データの妥当性**を作成します。20から40の範囲外の値を入力すると、このスクリーンショットに示されているように、セルB3に**バリデーションエラー**が**赤のXXXX**の形で表示されます。

![todo:image_alt_text](working-with-cells-gridweb_4.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-CreateDataValidationinGridCellofGridWeb-CreateDataValidationinGridCellofGridWeb.jsp" >}}
## **カスタムコマンドボタンの作成**
Aspose.Cells.GridWebには、送信、保存、元に戻すといった特別なボタンがあります。これらのボタンはAspose.Cells.GridWebの特定のタスクを実行します。また、カスタムタスクを実行するカスタムボタンを追加することも可能です。このトピックでは、この機能の使用方法について説明します。

次のサンプルコードは、カスタムコマンドボタンの作成方法とそのクリックイベントの処理方法を説明しています。カスタムコマンドボタンには任意のアイコンを使用できます。理解しやすくするために、この画像アイコンを使用しました。

![todo:image_alt_text](working-with-cells-gridweb_5.png)

次のスクリーンショットでわかるように、ユーザーがカスタムコマンドボタンをクリックすると、セルA1に**"My Custom Command Button is Clicked."**というテキストが追加されます。

![todo:image_alt_text](working-with-cells-gridweb_6.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-CreatingCustomCommandButtons-CreatingCustomCommandButtons.jsp" >}}
### **カスタムコマンドボタンのイベント処理**
次のサンプルコードでは、カスタムコマンドボタンのイベント処理方法について説明しています。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-EventHandlingofCustomCommandButton-EventHandlingofCustomCommandButton.jsp" >}}
## **GridWebのセルの書式設定**
### **可能な使用シナリオ**
GridWebは今、ユーザーが3%などのパーセント形式でセルデータを入力できるようにサポートしており、セルのデータは自動的に3.00%のようにフォーマットされます。しかし、セルスタイルをパーセンテージ形式に設定する必要があります。これはGridTableItemStyle.NumberTypeの9または10です。数字9は3%を3%としてフォーマットしますが、数字10は3%を3.00%としてフォーマットします。

{{% alert color="primary" %}} 

セルスタイルをパーセント形式に設定していない場合、入力データ3%は0.03として表示されます。

{{% /alert %}} 
### **GridWebワークシートのセルデータをパーセント形式で入力する**
次のサンプルコードはセルA1のGridTableItemStyle.NumberTypeを10に設定しています。したがって、入力データ3%は自動的に3.00%としてフォーマットされます（スクリーンショットを参照）。

![todo:image_alt_text](working-with-cells-gridweb_7.png)
### **サンプルコード**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-EnterCellDataofGridWebWorksheet-EnterCellDataofGridWebWorksheet.jsp" >}}
