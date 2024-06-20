---
title: GridWebクライアント側スクリプトを記述する
type: docs
weight: 10
url: /ja/net/aspose-cells-gridweb/write-gridweb-client-side-script/
keywords: GridWeb,client,js,javascript
description: この記事では、GridWebでクライアントjs apiを使用する方法について紹介します。
---

{{% alert color="primary" %}} 

開発者はAspose.Cells.GridWebコントロールのためにクライアント側スクリプトを書くことができます。これは、JavaScript関数をクライアント側で呼び出して、GridWebコントロールに関連する特定のタスクを実行することが可能であることを意味します。たとえば、開発者はJavaScript関数を書いて、GridWebデータをサーバーに送信したり、検証エラーが発生したときにアラートメッセージを表示することができます。

このトピックでは、例を使用してこの機能を説明します。

{{% /alert %}} 
## **Aspose.Cells.GridWebのクライアント側スクリプトの記述**
### **基本情報**
Aspose.Cells.GridWebは、クライアント側スクリプトをサポートするために特別に作成された2つのプロパティを提供します:

- OnSubmitClientFunction
- OnValidationErrorClientFunction

ASPXページでJavaScript関数を作成し、これらの関数の名前をOnSubmitClientFunctionおよびOnValidationErrorClientFunctionプロパティに割り当てます。

{{% alert color="primary" %}} 

OnSubmitClientFunctionプロパティに割り当てるJavaScript関数は、以下に示すように適切に定義する必要があります:

**JavaScript**

{{< highlight csharp >}}

 function function_name(arg, cancelEdit)

 {

   //Add javascript code here

 }



{{< /highlight >}}

[arg]パラメータはコントロールによって生成されたコマンドを表し、そのコマンドは「保存」「送信」「元に戻す」などです。また、[cancelEdit]パラメータは、ユーザー入力がキャンセルされたかどうかを示すブール値です。

OnSubmitClientFunctionプロパティに割り当てられた任意のJavaScript関数は、GridWebコントロールがサーバーにGridWebデータを送信する前に常に呼び出されます。同様に、OnValidationErrorClientFunctionプロパティに関数が割り当てられている場合は、検証エラーが発生するたびにその関数が呼び出されます。

{{% /alert %}} 
### **クライアント側スクリプトの関数**
Aspose.Cells.GridWebは、特にクライアント側スクリプトのための関数も公開しています。これらのクライアント側関数は、以下を含みます:

|**関数**|**説明**|
| :- | :- |
|updateData(bool cancelEdit)| Aspose.Cells.GridWebのすべてのクライアントデータを更新してからサーバーに投稿します。 cancelEditパラメータがtrueの場合、GridWebはすべてのユーザー入力を破棄します。
|validateAll()| ユーザー入力に検証エラーがあるかどうかをチェックするために使用します。エラーがある場合はfalseを返し、それ以外の場合はtrueを返します。
|submit(string arg, bool cancelEdit)| この関数を呼び出して、ポストバックまたはデータをサーバーに送信します。この関数は、データを更新し、ユーザー入力を検証するという両方のタスクを実行します。この関数はさらに、サーバーサイドでコマンドイベントを発生させることもできます。コマンドを渡す場合は、argパラメータを使用します。たとえば、SAVEコマンドはGridWebコントロールのコマンドバーの**保存**ボタンをクリックするために使用され、CCMD:MYCOMMANDコマンドはカスタムコマンドイベントを発生させます。
|setActiveCell(int row, int column)| 特定のセルをアクティブにするために使用します。
|setCellValue(int row, int column, string value)| 行と列の数を指定して、任意のセルに値を入れるために使用します。
|getCellValue(int row, int column)| 指定されたセルの値を返します。
|getActiveRow()| getActiveColumn()関数とともに使用して、アクティブなセルの位置を決定するために使用します。
|getActiveColumn()| getActiveRow()関数とともに使用して、アクティブなセルの位置を決定するために使用します。
|getSelectRange()| 最後に選択された範囲を返します。
|setSelectRange()| 指定された範囲を選択します。
|clearSelections()|現在のアクティブなセルを除くすべての選択を解除します。
|getCellsArray()|getCellName()、getCellValuuByCell()、getCellRow()およびgetCellColumn()などの他の関連関数とともに使用されます。この関数の使用方法に関する詳細については、以下の記事を参照してください：[クライアントサイドでGridWebセルの値を読み取る](/cells/ja/net/aspose-cells-gridweb/read-the-values-of-the-gridweb-cells-on-client-side/)
Aspose.Cells.GridWebと連動するクライアントサイドスクリプトを含むテストアプリケーションを作成するには、以下の手順に従ってください：

1. GridWebによって呼び出されるJavaScript関数を作成します。
   These functions will be added to the ASP.NET page's <script></script> tag.
1. OnSubmitClientFunctionとOnValidationErrorClientFunctionプロパティに関数の名前を割り当てます。

コード例の出力は以下のようになります：

**C1セルにバリデーションが追加されました** 

![todo:image_alt_text](write-gridweb-client-side-script_1.png)

無効な値を追加して**保存**をクリックします。バリデーションエラーが発生し、ValidationErrorFunctionが実行されます。

**バリデーションエラーが発生したときにValidationErrorFunctionが呼び出されます** 

![todo:image_alt_text](write-gridweb-client-side-script_2.png)

有効な値を入力するまで、データはサーバーに送信されません。有効な値を入力して**保存**をクリックします。ConfirmFunctionが実行されます。

サーバーにデータを送信する前に**ConfirmFunction**が呼び出されます 

![todo:image_alt_text](write-gridweb-client-side-script_3.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-WriteClientSideScript-WriteClientSideScript.aspx" >}}

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-WriteClientSideScript.aspx-WriteClientSideScript.cs" >}}
