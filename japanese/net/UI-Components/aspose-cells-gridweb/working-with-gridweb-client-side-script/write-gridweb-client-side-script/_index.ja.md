---
title: GridWeb クライアント側スクリプトの記述
type: docs
weight: 10
url: /ja/net/write-gridweb-client-side-script/
---
{{% alert color="primary" %}} 

開発者は、Aspose.Cells.GridWeb コントロールのクライアント側スクリプトを作成できます。これは、クライアント側で JavaScript 関数を呼び出して、GridWeb コントロールに関連する特定のタスクを実行できることを意味します。たとえば、開発者は JavaScript 関数を記述して、GridWeb データをサーバーに送信したり、検証エラーが発生したときにアラート メッセージを表示したりできます。

このトピックでは、例を使用してこの機能について説明します。

{{% /alert %}} 
## **Aspose.Cells.GridWeb のクライアント側スクリプトの作成**
### **基本情報**
Aspose.Cells.GridWeb は、クライアント側のスクリプトをサポートするために特別に作成された 2 つのプロパティを提供します。

- OnSubmitClientFunction
- OnValidationErrorClientFunction

ASPX ページで JavaScript 関数を作成し、これらの関数の名前を OnSubmitClientFunction および OnValidationErrorClientFunction プロパティに割り当てます。

{{% alert color="primary" %}} 

OnSubmitClientFunction プロパティに割り当てられる JavaScript 関数は、以下に示すように適切に定義する必要があります。

**JavaScript**

{{< highlight "csharp" >}}

 function function_name(arg, cancelEdit)

 {

   //Add javascript code here

 }



{{< /highlight >}}

[arg] パラメータは、コントロールによって生成されたコマンドを表します。コマンドは「保存」、「送信」、「元に戻す」などで、[cancelEdit] パラメータはブール値で、ユーザー入力がキャンセルされたかどうかを示します。

OnSubmitClientFunction プロパティに割り当てられた JavaScript 関数は、GridWeb データをサーバーに送信する前に、GridWeb コントロールによって毎回呼び出されます。同様に、関数が OnValidationErrorClientFunction プロパティに割り当てられている場合、検証エラーが発生するたびにその関数が呼び出されます。

{{% /alert %}} 
### **クライアント側スクリプトの関数**
Aspose.Cells.GridWeb は、特にクライアント側スクリプト用の機能も公開しています。これらの関数を JavaScript 関数内で使用して、Aspose.Cells.GridWeb をより詳細に制御できます。これらのクライアント側関数には、次のものがあります。

|**機能**|**説明**|
|:- |:- |
|updateData(bool cancelEdit)|サーバーに投稿する前に、Aspose.Cells.GridWeb のすべてのクライアント データを更新します。 cancelEdit パラメータが true の場合、GridWeb はすべてのユーザー入力を破棄します。|
|validateAll()|ユーザー入力に検証エラーがあるかどうかを確認するために使用されます。エラーがある場合、関数は false を返し、それ以外の場合は true を返します。|
|submit(string arg, bool cancelEdit)|この関数を呼び出して、データをサーバーにポストバックまたは送信します。この関数は、データの更新とユーザー入力の検証の両方のタスクを実行します。この関数は、サーバー側でコマンド イベントを発生させることもできます。 arg パラメータを使用してコマンドを渡します。例: SAVE コマンドは、**セーブ**ボタンをクリックし、CCMD:MYCOMMAND コマンドが CustomCommand イベントを発生させます。|
|setActiveCell(int 行、int 列)|特定のセルをアクティブにするために使用されます。|
|setCellValue(int 行、int 列、文字列値)|行番号と列番号を使用して指定された任意のセルに値を入力するために使用されます。|
|getCellValue(int 行、int 列)|指定されたセルの値を返します。|
|getActiveRow()|getActiveColumn() 関数と組み合わせて使用し、アクティブ セルの位置を決定します。|
|getActiveColumn()|getActiveRow() 関数と組み合わせて使用し、アクティブ セルの位置を決定します。|
|getSelectRange()|最後に選択された範囲を返します。|
|setSelectRange()|指定された範囲を選択します。|
|clearSelections()|現在アクティブなセルを除くすべての選択をクリアします。|
|getCellsArray()|これは、getCellName()、getCellValueByCell()、getCellRow()、および getCellColumn() などの他の関連関数とともに使用されます。この関数の使用法に関する詳細については、この記事をお読みください。[クライアント側で GridWeb セルの値を読み取る](/cells/ja/net/read-the-values-of-the-gridweb-cells-on-client-side/)|
Aspose.Cells.GridWeb で動作するクライアント側スクリプトを含むテスト アプリケーションを作成するには、次の手順に従います。

1. GridWeb によって呼び出される JavaScript 関数を作成します。
これらの関数は、ASP.NET ページの<script></script>鬼ごっこ。
1. 関数の名前を OnSubmitClientFunction および OnValidationErrorClientFunction プロパティに割り当てます。

コード例の出力を以下に示します。

**C1 セルに追加された検証** 

![todo:画像_代替_文章](write-gridweb-client-side-script_1.png)

無効な値を追加してクリック**セーブ**.検証エラーが発生し、ValidationErrorFunction が実行されます。

**検証エラーで呼び出される ValidationErrorFunction** 

![todo:画像_代替_文章](write-gridweb-client-side-script_2.png)

有効な値を入力するまで、データはサーバーに送信されません。有効な値を入力してクリックします**セーブ**ConfirmFunction が実行されます。

**GridWeb データをサーバーに送信する前に呼び出される ConfirmFunction** 

![todo:画像_代替_文章](write-gridweb-client-side-script_3.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-WriteClientSideScript-WriteClientSideScript.aspx" >}}

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-WriteClientSideScript.aspx-WriteClientSideScript.cs" >}}
