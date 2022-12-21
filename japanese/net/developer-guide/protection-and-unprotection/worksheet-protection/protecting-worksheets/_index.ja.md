---
title: ワークシートの保護
type: docs
weight: 10
url: /ja/net/protecting-worksheets/
---
{{% alert color="primary" %}}

ワークシートが保護されている場合、ユーザーが実行できるアクションは制限されます。たとえば、データを入力したり、行や列を挿入または削除したりすることはできません。

{{% /alert %}}

## **ワークシートを保護する**

### **序章**

Microsoft Excel の一般的な保護オプションは次のとおりです。

- コンテンツ
- オブジェクト
- シナリオ

保護されたワークシートは機密データを隠したり保護したりしないため、ファイルの暗号化とは異なります。一般に、ワークシートの保護はプレゼンテーションの目的に適しています。これにより、エンド ユーザーはワークシートのデータ、コンテンツ、および書式を変更できなくなります。

### **ワークシートを保護する**

Aspose.Cells はクラスを提供し、[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)Microsoft Excel ファイルを表します。の[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスには[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)Excel ファイル内の各ワークシートにアクセスできるコレクション。ワークシートは、[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラス。

の[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスが提供する[**守る**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/protect/index)ワークシートに保護を適用するために使用されるメソッド。[**守る**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/protect/methods/1)メソッドは次のパラメーターを受け入れます。

- 保護タイプ、ワークシートに適用する保護のタイプ。保護タイプは、[**保護タイプ**](https://reference.aspose.com/cells/net/aspose.cells/protectiontype)列挙。
- 新しいパスワード。ワークシートを保護するために使用される新しいパスワード。
- 古いパスワード、ワークシートがすでにパスワードで保護されている場合の古いパスワード。ワークシートがまだ保護されていない場合は、null を渡します。

の[**保護タイプ**](https://reference.aspose.com/cells/net/aspose.cells/protectiontype)列挙には、次の事前定義された保護タイプが含まれています。

|**保護の種類**|**説明**|
|:- |:- |
|全て|ユーザーはこのワークシートで何も変更できません|
|コンテンツ|ユーザーはこのワークシートにデータを入力できません|
|オブジェクト|ユーザーは描画オブジェクトを変更できません|
|シナリオ|ユーザーは保存されたシナリオを変更できません|
|構造|ユーザーは構造を変更できません|
|Windows|ウィンドウに保護が適用されます|
|なし|保護は適用されません|

次の例は、ワークシートをパスワードで保護する方法を示しています。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-ProtectingWorksheet-1.cs" >}}

上記のコードを使用してワークシートを保護した後、ワークシートを開いて保護を確認できます。ファイルを開いてワークシートにデータを追加しようとすると、次のダイアログが表示されます。

|**ユーザーがワークシートを変更できないことを警告するダイアログ**|
|:- |
|![todo:画像_代替_文章](protecting-worksheets_1.png)|

ワークシートで作業するには、**保護**、 それから**シートの保護を解除**から**ツール**メニュー項目。

[シートの保護を解除] メニュー項目を選択すると、以下に示すようにワークシートで作業できるように、パスワードの入力を求めるダイアログが開きます。

|![todo:画像_代替_文章](protecting-worksheets_2.png)|

### **Microsoft Excel を使用して、ワークシートのいくつかの Cells を保護します**

ワークシート内のいくつかのセルのみをロックする必要がある特定のシナリオがあるかもしれません。ワークシート内の特定のセルをロックする場合は、ワークシート内の他のすべてのセルのロックを解除する必要があります。ワークシート内のすべてのセルは、すでにロック用に初期化されています。これを確認して、任意の Excel ファイルを MS Excel で開き、**フォーマット | Cells...**見せる**フォーマット Cells**ダイアログ ボックスをクリックし、**保護**タブをクリックすると、「ロック済み」というラベルの付いたチェックボックスがデフォルトでオンになっていることがわかります。

次のポイントでは、MS Excel を使用していくつかのセルをロックする方法について説明します。この方法は、Microsoft Office Excel 97、2000、2002、2003 以降のバージョンに適用されます。

1. をクリックして、ワークシート全体を選択します。**すべて選択**ボタン (行 1 の行番号の真上、列文字 A の左にある灰色の長方形)。
1. クリック**Cells**上で**フォーマット**メニューで、**保護**タブをクリックしてから、**ロックされた**チェックボックス。
これにより、ワークシートのすべてのセルのロックが解除されます
もし**Cells**ワークシートの一部がすでにロックされている可能性があります。上で**ツール**メニュー、ポイント**保護**をクリックし、**シートの保護を解除**.
1. ロックしたいセルだけを選択して手順 2 を繰り返しますが、今回は**ロックされた**チェックボックス。
1. 上で**ツール**メニュー、ポイント**保護** 、 クリック**プロテクトシート**そしてクリック**わかった**.
1. の中に**プロテクトシート**ダイアログ ボックスで、パスワードを指定し、ユーザーが変更できるようにする要素を選択するオプションがあります。

### **Aspose Cells を使用して、ワークシートのいくつかの Cells を保護します**

この方法では、タスクを実行するためだけに Aspose.Cells API を使用します。

例: 次の例は、ワークシート内のいくつかのセルを保護する方法を示しています。最初にワークシート内のすべてのセルのロックを解除し、次に 3 つのセル (A1、B1、C1) をロックします。最後に、ワークシートを保護します。の[**スタイル**](https://reference.aspose.com/cells/net/aspose.cells/style)オブジェクトにはブール値のプロパティが含まれています。[**ロックされています**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked) .設定できます[**ロックされています**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked)プロパティを true または false にして適用する*列/行.ApplyStyle()*目的の属性で行/列をロックまたはロック解除する方法。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-ProtectingSpecificCellsinaWorksheet-1.cs" >}}

### **ワークシートの行を保護する**

Aspose.Cells を使用すると、ワークシートの任意の行を簡単にロックできます。ここで、私たちは利用することができます[**ApplyStyle()**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/applystyle)方法[**Aspose.Cells.Row**](https://reference.aspose.com/cells/net/aspose.cells/row)申し込むクラス[**スタイル**](https://reference.aspose.com/cells/net/aspose.cells/style)ワークシートの特定の行に。このメソッドは 2 つの引数を取ります。[**スタイル**](https://reference.aspose.com/cells/net/aspose.cells/style)オブジェクトと[**スタイルフラグ**](https://reference.aspose.com/cells/net/aspose.cells/styleflag)適用された書式設定に関連するすべてのメンバーを持つオブジェクト。

次の例は、ワークシートの行を保護する方法を示しています。最初にワークシート内のすべてのセルのロックを解除してから、その最初の行をロックします。最後に、ワークシートを保護します。の[**スタイル**](https://reference.aspose.com/cells/net/aspose.cells/style)オブジェクトにはブール値のプロパティが含まれています。[**ロックされています**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked) .設定できます[**ロックされています**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked)プロパティを true または false に設定して、[**スタイルフラグ**](https://reference.aspose.com/cells/net/aspose.cells/styleflag)物体。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-ProtectingSpecificRowInWorksheet-1.cs" >}}

### **ワークシートの列を保護する**

Aspose.Cells を使用すると、ワークシート内の任意の列を簡単にロックできます。ここで、私たちは利用することができます[**ApplyStyle()**](https://reference.aspose.com/cells/net/aspose.cells/column/methods/applystyle)方法[**Aspose.Cells.Column**](https://reference.aspose.com/cells/net/aspose.cells/column)申し込むクラス[**スタイル**](https://reference.aspose.com/cells/net/aspose.cells/style)ワークシートの特定の列に。このメソッドは 2 つの引数を取ります。[**スタイル**](https://reference.aspose.com/cells/net/aspose.cells/style)オブジェクトと[**スタイルフラグ**](https://reference.aspose.com/cells/net/aspose.cells/styleflag)適用された書式設定に関連するすべてのメンバーを持つオブジェクト。

次の例は、ワークシートの列を保護する方法を示しています。最初にワークシート内のすべてのセルのロックを解除してから、その最初の列をロックします。最後に、ワークシートを保護します。の[**スタイル**](https://reference.aspose.com/cells/net/aspose.cells/style)オブジェクトにはブール値のプロパティが含まれています。[**ロックされています**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked) .設定できます[**ロックされています**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked)プロパティを true または false に設定して、[**スタイルフラグ**](https://reference.aspose.com/cells/net/aspose.cells/styleflag)物体。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-ProtectColumnWorksheet-1.cs" >}}

### **ユーザーが範囲を編集できるようにする**

次の例は、ユーザーが保護されたワークシートの範囲を編集できるようにする方法を示しています。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-EditRangesWorksheet-1.cs" >}}
