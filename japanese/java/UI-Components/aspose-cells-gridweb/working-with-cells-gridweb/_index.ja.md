---
title: Cells GridWeb の操作
type: docs
weight: 50
url: /ja/java/working-with-cells-gridweb/
---
##  **ワークシートで Cells にアクセスする**
このトピックでは、GridWeb の最も基本的な機能であるセルへのアクセスについて説明し、セルについて説明します。

各ワークシートには、GridCell オブジェクトのコレクションである GridCells オブジェクトが含まれています。 GridCell オブジェクトは、Aspose.Cells.GridWeb のセルを表します。 GridWeb を使用して任意のセルにアクセスできます。推奨される方法は 2 つあります。

- [名前によるセルへのアクセス](/cells/ja/java/working-with-cells-gridweb/).
- [行インデックスと列インデックスによるセルへのアクセス](/cells/ja/java/working-with-cells-gridweb/).

以下では、それぞれのアプローチについて説明します。
###  **Cell の名前を使用する**
すべてのセルには一意の名前が付いています。たとえば、A1、A2、B1、B2 などです。 Aspose.Cells.GridWeb を使用すると、開発者はセル名を使用して任意のセルにアクセスできます。セル名を (インデックスとして) GridWorksheet の GridCells コレクションに渡すだけです。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-Accessingcellbyname-Accessingcellbyname.jsp" >}}


###  **行と列のインデックスの使用**
セルは、行インデックスと列インデックスの観点からその位置によって認識することもできます。セルの行インデックスと列インデックスを GridWorksheet の GridCells コレクションに渡すだけです。このアプローチは上記のアプローチよりも高速です。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-Accessingcellbyrowandcolumnindices-Accessingcellbyrowandcolumnindices.jsp" >}}
##  **Cell の値へのアクセスと変更**
[ワークシートで Cells にアクセスする](/cells/ja/java/working-with-cells-gridweb/#workingwithcellsgridweb-accessingcellsintheworksheet)セルへのアクセスについて説明しました。このトピックでは、その説明を拡張して、GridWeb API を使用してセル値にアクセスし、変更する方法を示します。
###  **Cell の値へのアクセスと変更**
####  **文字列値**
セルの値にアクセスして変更する前に、セルにアクセスする方法を知っておく必要があります。セルにアクセスするためのさまざまなアプローチの詳細については、を参照してください。[ワークシートで Cells にアクセスする](/cells/ja/java/working-with-cells-gridweb/#workingwithcellsgridweb-accessingcellsintheworksheet).

各セルには getStringValue() という名前のプロパティがあります。セルにアクセスすると、開発者は getStringValue() メソッドにアクセスしてセルの文字列値にアクセスできます。

{{% alert color="primary" %}} 

重要: 5 種類の値 (Boolean、int、double、DateTime、string) をセルに格納できますが、getValue()/setValue() メソッドはオブジェクト値へのアクセスや変更にのみ使用できます。

{{% /alert %}} 

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AccessingModifyingCellStringValue-AccessingModifyingCellStringValue.jsp" >}}
####  **すべてのタイプの値**
Aspose.Cells.GridWeb は、各セルに対して特別なメソッド putValue も提供します。このメソッドを使用すると、セルに任意のタイプの値 (Boolean、int、double、DateTime、string) を挿入または変更できます。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AccessingModifyingCell-AccessingModifyingCell.jsp" >}}



putValue メソッドのオーバーロードされたバージョンもあり、文字列形式であらゆる種類の値を受け取り、それを適切なデータ型に自動的に変換できます。これを実現するには、以下の例に示すように、ブール値 true を putValue メソッドの別のパラメーターに渡します。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AccessingModifyingCellAllTypeValue-AccessingModifyingCellAllTypeValue.jsp" >}}
##  **Cells に数式を追加する**
Aspose.Cells.GridWeb が提供する最も価値のある機能は、数式または関数のサポートです。 Aspose.Cells.GridWeb には、ワークシート内の数式を計算する独自の数式エンジンがあります。 Aspose.Cells.GridWeb は、組み込み関数とユーザー定義の関数または数式の両方をサポートしています。このトピックでは、Aspose.Cells.GridWeb API を使用してセルに数式を追加する方法について詳しく説明します。
###  **数式を追加して計算するにはどうすればよいですか?**
セルの Formula プロパティを使用して、セル内の数式を追加、アクセス、および変更することができます。 Aspose.Cells.GridWeb は、単純なものから複雑なものまで、ユーザー定義の数式をサポートしています。ただし、多数の組み込み関数または数式 (Microsoft Excel と同様) も Aspose.Cells.GridWeb で提供されます。組み込み関数の完全なリストを確認するには、これを参照してください。[サポートされている機能のリスト。](/cells/ja/net/list-of-supported-functions/)

{{% alert color="primary" %}} 

数式の構文は Microsoft Excel の構文と互換性がある必要があります。たとえば、すべての数式は等号 (=) で始まる必要があります。

プログラムで数式を追加するには、*=* 記号を使用しなくても、Aspose.Cells.GridWeb はその数式を数式として認識しますが、GUI で作業するエンド ユーザーがそれを使用する必要がある場合に限ります。

{{% /alert %}} 

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AddingFormulastoCells-AddingFormulastoCells.jsp" >}}



**B3 セルに数式が追加されましたが、GridWeb によって計算されませんでした** 

![todo:image_alt_text](working-with-cells-gridweb_1.png)

上のスクリーンショットでは、数式が B3 に追加されましたが、まだ計算されていないことがわかります。すべての数式を計算するには、以下に示すようにワークシートに数式を追加した後、 GridWeb コントロールの GridWorksheetCollection の CalculateFormula メソッドを呼び出します。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-CalculateFormula-CalculateFormula.jsp" >}}

ユーザーは、[*送信**] をクリックして数式を計算することもできます。

**GridWebのSubmitボタンをクリック** 

![todo:image_alt_text](working-with-cells-gridweb_2.png)

**重要**: ユーザーが [**保存] をクリックすると、**または**元に戻す**ボタン、またはシート タブ、すべての数式は GridWeb によって自動的に計算されます。

**計算後の計算結果** 

![todo:image_alt_text](working-with-cells-gridweb_3.png)
###  **他のワークシートから Cells を参照する**
Aspose.Cells.GridWeb を使用すると、さまざまなワークシートに保存されている値を数式で参照し、複雑な数式を作成することができます。

別のワークシートのセル値を参照するための構文は SheetName!CellName です。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-ReferencingCellsfromOtherWorksheets-ReferencingCellsfromOtherWorksheets.jsp" >}}
##  **GridWeb の GridCell でデータ検証を作成する**
Aspose.Cells.GridWeb を使用すると追加できます**データ検証**GridWorksheet.getValidations().add() メソッドを使用します。このメソッドを使用する場合は、**Cell 範囲**。ただし、単一の GridCell でデータ検証を作成する場合は、GridCell.createValidation() メソッドを使用して直接実行できます。同様に、**データ検証を削除できます。** GridCell.removeValidation() メソッドを使用して GridCell から取得します。

次のサンプル コードは、**データ検証**セルB3内。 20 ～ 40 の範囲外の値を入力すると、セル B3 に次のように表示されます。**検証エラー**の形で**レッドXXXX**このスクリーンショットに示されているように。

![todo:image_alt_text](working-with-cells-gridweb_4.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-CreateDataValidationinGridCellofGridWeb-CreateDataValidationinGridCellofGridWeb.jsp" >}}
##  **カスタムコマンドボタンの作成**
Aspose.Cells.GridWeb には、送信、保存、元に戻すなどの特別なボタンが含まれています。これらのボタンはすべて、Aspose.Cells.GridWeb の特定のタスクを実行します。カスタム タスクを実行するカスタム ボタンを追加することもできます。このトピックでは、この機能の使用方法について説明します。

次のサンプル コードでは、カスタム コマンド ボタンを作成する方法と、そのクリック イベントを処理する方法を説明します。カスタム コマンド ボタンには任意のアイコンを使用できます。説明のために、この画像アイコンを使用しました。

![todo:image_alt_text](working-with-cells-gridweb_5.png)

次のスクリーンショットでわかるように、ユーザーがカスタム コマンド ボタンをクリックすると、セル A1 に次のテキストが追加されます。**「カスタム コマンド ボタンがクリックされました。」**

![todo:image_alt_text](working-with-cells-gridweb_6.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-CreatingCustomCommandButtons-CreatingCustomCommandButtons.jsp" >}}
###  **カスタムコマンドボタンのイベント処理**
次のサンプル コードは、カスタム コマンド ボタンのイベント処理を実行する方法を説明します。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-EventHandlingofCustomCommandButton-EventHandlingofCustomCommandButton.jsp" >}}
##  **GridWeb のセルの書式設定**
###  **考えられる使用シナリオ**
GridWeb では、ユーザーがセル データを 3% などのパーセント形式で入力できるようになりました。セル内のデータは自動的に 3.00% として形式設定されます。ただし、セル スタイルを Percentage Format (GridTableItemStyle.NumberType の 9 または 10) に設定する必要があります。数値 9 は 3% を 3% としてフォーマットしますが、数値 10 は 3% を 3.00% としてフォーマットします。

{{% alert color="primary" %}} 

セル スタイルをパーセント形式に設定していない場合、入力データ 3% は 0.03 として表示されます。

{{% /alert %}} 
###  **GridWeb ワークシートの Cell データをパーセント形式で入力します**
次のサンプル コードでは、セル A1 GridTableItemStyle.NumberType を 10 に設定します。したがって、スクリーンショットに示すように、入力データ 3% は自動的に 3.00% として書式設定されます。

![todo:image_alt_text](working-with-cells-gridweb_7.png)
###  **サンプルコード**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-EnterCellDataofGridWebWorksheet-EnterCellDataofGridWebWorksheet.jsp" >}}
