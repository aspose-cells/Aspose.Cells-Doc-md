---
title: ワークシートの保護
type: docs
weight: 10
url: /ja/net/protecting-worksheets/
---

{{% alert color="primary" %}}

ワークシートが保護されている場合、ユーザーが行うことができるアクションが制限されます。たとえば、データの入力、行または列の挿入または削除などができません。

{{% /alert %}}

## **ワークシートを保護**

### **紹介**

Microsoft Excelの一般的な保護オプション:

- コンテンツ
- オブジェクト
- シナリオ

保護されたワークシートは機密データを非表示または保護しないため、ファイルの暗号化とは異なります。一般的に、ワークシートの保護はプレゼンテーション目的に適しています。ユーザーはワークシート内のデータ、コンテンツ、および書式設定を変更できなくなります。

### **ワークシートを保護する**

Aspose.Cellsは、Microsoft Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスには、Excelファイル内の各ワークシートにアクセスを許可する[**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)コレクションが含まれています。ワークシートは[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスで表されます。

[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスは、ワークシートに保護を適用するために使用される[**Protect**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/protect/index)メソッドを提供します。[**Protect**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/protect/methods/1)メソッドは以下のパラメータを受け付けます:

- 保護タイプ、ワークシートに適用する保護の種類。保護タイプは[**ProtectionType**](https://reference.aspose.com/cells/net/aspose.cells/protectiontype)列挙型のヘルプを使用して適用されます。
- 新しいパスワード、ワークシートを保護するために使用する新しいパスワード。
- 古いパスワード、ワークシートがすでにパスワードで保護されている場合は、古いパスワードを渡します。ワークシートがすでに保護されていない場合は、nullを渡します。

[**ProtectionType**](https://reference.aspose.com/cells/net/aspose.cells/protectiontype)列挙型には、次の事前定義の保護タイプが含まれています:

|**保護タイプ**|**説明**|
| :- | :- |
|All|このワークシート上で何も変更できない|
|Contents|このワークシートにデータを入力できない|
|Objects|描画オブジェクトを変更できない|
|Scenarios|保存されたシナリオを変更できない|
|Structure|ユーザーは構造を変更できません|
|Windows|保護はウィンドウに適用されています|
|None|保護は適用されていません|

以下の例は、ワークシートにパスワードを設定して保護する方法を示しています。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-ProtectingWorksheet-1.cs" >}}

上記のコードを使用してワークシートを保護した後、ワークシートの保護を開いて確認することができます。ファイルを開いてワークシートにデータを追加しようとすると、次のダイアログが表示されます:

|**ユーザーがワークシートを変更できないと警告するダイアログ**|
| :- |
|![todo:image_alt_text](protecting-worksheets_1.png)|

ワークシートで作業するには、**ツール**メニューの**保護**から**ワークシートの保護を解除**を選択します。

ワークシートの保護を解除メニュー項目を選択すると、次のようなダイアログが開きます。パスワードを入力するように求められます。

|![todo:image_alt_text](protecting-worksheets_2.png)|

### **Microsoft Excelを使用してワークシート内の一部のセルを保護する**

ワークシート内の特定のセルをロックする必要がある場合があります。ワークシート内の特定のセルをロックするには、ワークシートの他のすべてのセルをロック解除する必要があります。ワークシートのすべてのセルは既にロックされています。MS Excelに任意のExcelファイルを開いて**書式 | セル...**をクリックして**セルの書式**ダイアログボックスを表示し、**保護**タブをクリックし、「ロック」のチェックボックスがデフォルトでチェックされていることを確認できます。

次のポイントは、MS Excelを使用していくつかのセルをロックする方法を説明しています。この方法は、Microsoft Office Excel 97、2000、2002、2003およびそれ以降のバージョンに適用されます。

1. **全選択**ボタン(行1の行番号の直上および列文字Aの左直上の灰色の四角形)をクリックしてワークシート全体を選択します。
1. **書式**メニューの**セル**をクリックし、**保護**タブをクリックし、**ロック**のチェックボックスをクリアします。
   これにより、ワークシートのすべてのセルがロック解除されます
   **セル**コマンドが利用できない場合、ワークシートの一部は既にロックされている可能性があります。 **ツール**メニューで、**保護**を指して、**ワークシートの保護を解除**をクリックします。
1. ロックしたいセルだけを選択し、ステップ2を繰り返しますが、この時に**ロック**のチェックボックスを選択します。
1. **ツール**メニューで**保護**を指して、**ワークシートの保護**をクリックし、**OK**をクリックします。
1. **ワークシートの保護**ダイアログボックスでは、ユーザーが変更できる要素を指定するオプションとパスワードを指定することができます。

### **Aspose Cellsを使用してワークシート内の一部のセルを保護する**

この方法では、Aspose.Cells APIのみを使用してタスクを実行します。

例: 次の例は、ワークシート内の一部のセルを保護する手順を示しています。まずワークシートのすべてのセルをロック解除し、それから3つのセル（A1、B1、C1）をロックします。最後にワークシートを保護します。 [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)オブジェクトには、真偽値プロパティ[**IsLocked**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked)が含まれています。 [**IsLocked**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked)プロパティをtrueまたはfalseに設定し、*Column/Row.ApplyStyle()*メソッドを使用して希望の属性で行または列をロックまたはロック解除できます。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-ProtectingSpecificCellsinaWorksheet-1.cs" >}}

### **ワークシート内の行を保護する**

Aspose.Cellsを使用すると、ワークシート内の任意の行を簡単にロックできます。ここでは、ワークシート内の特定の行に[**ApplyStyle()**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/applystyle)メソッドを[**Aspose.Cells.Row**](https://reference.aspose.com/cells/net/aspose.cells/row)クラスを使用して[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)を適用できます。このメソッドは、[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)オブジェクトと[**StyleFlag**](https://reference.aspose.com/cells/net/aspose.cells/styleflag)オブジェクトを引数に取り、適用される書式に関連するすべてのメンバーを持っています。

次の例は、ワークシート内の行を保護する手順を示しています。まず、ワークシートのすべてのセルをロック解除してから、第1行をロックします。最後にワークシートを保護します。 [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)オブジェクトには、真偽値プロパティ[**IsLocked**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked)が含まれています。 [**IsLocked**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked)プロパティをtrueまたはfalseに設定することで、[**StyleFlag**](https://reference.aspose.com/cells/net/aspose.cells/styleflag)オブジェクトを使用して行または列をロックまたはロック解除できます。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-ProtectingSpecificRowInWorksheet-1.cs" >}}

### **ワークシート内の列を保護する**

Aspose.Cellsを使用すると、ワークシート内の任意の列を簡単にロックできます。ここでは、ワークシート内の特定の列に[**ApplyStyle()**](https://reference.aspose.com/cells/net/aspose.cells/column/methods/applystyle)メソッドを[**Aspose.Cells.Column**](https://reference.aspose.com/cells/net/aspose.cells/column)クラスを使用して[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)を適用できます。このメソッドは、[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)オブジェクトと[**StyleFlag**](https://reference.aspose.com/cells/net/aspose.cells/styleflag)オブジェクトを引数に取り、適用される書式に関連するすべてのメンバーを持っています。

次の例は、ワークシート内の列を保護する手順を示しています。まず、ワークシートのすべてのセルをロック解除してから、第1列をロックします。最後にワークシートを保護します。 [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)オブジェクトには、真偽値プロパティ[**IsLocked**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked)が含まれています。 [**IsLocked**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked)プロパティをtrueまたはfalseに設定することで、[**StyleFlag**](https://reference.aspose.com/cells/net/aspose.cells/styleflag)オブジェクトを使用して行または列をロックまたはロック解除できます。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-ProtectColumnWorksheet-1.cs" >}}

### **ユーザーに範囲の編集を許可する**

次の例は、保護されたワークシートで範囲の編集を許可する方法を示しています。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-EditRangesWorksheet-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
