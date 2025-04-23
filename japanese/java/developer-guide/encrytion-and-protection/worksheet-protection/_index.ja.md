---
title: ワークシートの保護と保護解除
type: docs
weight: 50
url: /ja/java/protect-and-unprotect-worksheet/
---

## **ワークシートを保護**

ワークシートが保護されている場合、ユーザーが行うことができる操作は制限されます。たとえば、データの入力、行または列の挿入や削除などはできません。Microsoft Excelの一般的な保護オプションは次のとおりです：

- コンテンツ
- オブジェクト
- シナリオ

保護されたワークシートは、機密データを非表示または保護しないため、ファイルの暗号化とは異なります。一般的に、ワークシートの保護はプレゼンテーションの目的に適しています。これにより、エンドユーザーがワークシート内のデータ、コンテンツ、および書式を変更できなくなります。

### **保護の追加または削除**

Aspose.Cellsは、Microsoft Excelファイルを表すクラスであるWorkbookクラスを提供します。Workbookクラスには、Excelファイルの各ワークシートにアクセスできるWorksheetCollectionが含まれています。ワークシートはWorksheetクラスによって表されます。

Worksheetクラスには、ワークシートに保護を適用するために使用されるProtectメソッドが提供されています。Protectメソッドは次のパラメータを受け入れます。

- 保護の種類、ワークシートに適用する保護の種類。保護の種類はProtectionType列挙型のヘルプを使用して適用されます。
- 新しいパスワード、ワークシートを保護するために使用する新しいパスワード。
- 古いパスワード、既にワークシートがパスワードで保護されている場合は、古いパスワードを渡します。ワークシートがまだ保護されていない場合は、単にnullを渡します。

ProtectionType列挙型には、次の事前定義された保護タイプが含まれています。

|**保護タイプ**|**説明**|
| :- | :- |
|[**ALL**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#ALL)|ユーザーはこのワークシート上で何も変更できません|
|[**CONTENTS**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#CONTENTS)|ユーザーはこのワークシートにデータを入力できません|
|[**OBJECTS**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#OBJECTS)|ユーザーは描画オブジェクトを変更できません|
|[**SCENARIOS**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#SCENARIOS)|ユーザーは保存されたシナリオを変更できません|
|[**STRUCTURE**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#STRUCTURE)|ユーザーは保存された構造を変更できません|
|[**WINDOWS**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#WINDOWS)|ユーザーは保存されたウィンドウを変更できません|
|[**NONE**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#NONE)|保護なし|

以下の例は、ワークシートにパスワードを設定して保護する方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ProtectingWorksheet-ProtectingWorksheet.java" >}}

上記のコードを使用してワークシートを保護した後、ワークシートの保護を確認するには、ファイルを開いてください。ファイルを開いてワークシートにデータを追加しようとすると、次のダイアログボックスが表示されます。

**ユーザーがワークシートを変更できないことを警告するダイアログ** 

![todo:image_alt_text](protect-and-unprotect-worksheet_1.png)

ワークシートで作業するには、以下に示すように**Protection**から**シートの保護解除**を選択してワークシートの保護を解除してください。

**シートの保護解除メニューアイテムを選択する** 

![todo:image_alt_text](protect-and-unprotect-worksheet_2.png)

パスワードを求めるダイアログが開きます。

**ワークシートの保護を解除するためのパスワード入力** 

![todo:image_alt_text](protect-and-unprotect-worksheet_3.png)

### **一部のセルを保護する**

ワークシートで特定のセルのみをロックする必要がある場合があります。ワークシートで特定のセルのみをロックする場合は、ワークシートの他のすべてのセルのロックを解除する必要があります。ワークシートのすべてのセルは既にロックされるように初期化されています。これを確認するには、MS Excelで任意のExcelファイルを開き、**書式 | セル...**をクリックして**セルの書式**ダイアログボックスを表示し、その後、**保護**タブをクリックして、デフォルトでチェックされた"ロック"と表示されるチェックボックスを確認できます。

次に、このタスクを実装するための2つのアプローチを示します。

**方法1:**

次のポイントは、MS Excelを使用していくつかのセルをロックする方法を説明しています。この方法は、Microsoft Office Excel 97、2000、2002、2003およびそれ以降のバージョンに適用されます。

1. シート全体を選択するには、Select Allボタンをクリックします（行1の行番号の直上および列Aの左にある灰色の四角形）。
1. フォーマットメニューからセルをクリックし、「保護」タブをクリックし、その後「ロックされている」チェックボックスをクリアします。

   これにより、ワークシートのすべてのセルがロック解除されます

{{% alert color="primary" %}}

セルコマンドが利用できない場合は、ワークシートの一部がすでにロックされている可能性があります。ツールメニューで、「保護」を選択し、「シートの保護を解除」をクリックします。

{{% /alert %}}

1. ロックしたいセルを選択し、ステップ2を繰り返しますが、この時に「ロックされている」チェックボックスを選択します。
1. **ツール**メニューで**保護**を選択し、**シートの保護**をクリックし、その後**OK**をクリックします。

{{% alert color="primary" %}}

保護シートダイアログボックスで、パスワードを指定して、ユーザーが変更できる要素を選択するオプションがあります。

{{% /alert %}}

**メソッド2:**

この方法では、Aspose.Cells APIのみを使用してタスクを実行します。

次の例は、ワークシート内の数個のセルを保護する方法を示しています。ますます、ワークシートのすべてのセルをアンロックし、それから(A1、B1、C1)の3つのセルをロックします。最後に、ワークシートを保護します。行/列にはStyle APIがあり、さらにセルロックを設定するメソッドが含まれています。このメソッドを使用して行/列をロックまたはアンロックできます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ProtectingSpecificCellsinaWorksheet-ProtectingSpecificCellsinaWorksheet.java" >}}

### **ワークシート内の行を保護する**

Aspose.Cellsを使用すると、ワークシート内の任意の行を簡単にロックできます。ここでは、ワークシート内の特定の行にStyleを適用するための[**applyStyle()**](https://reference.aspose.com/cells/java/com.aspose.cells/row#applyStyle-com.aspose.cells.Style-com.aspose.cells.StyleFlag-)メソッドを{1}クラスの[**applyStyle()**](https://reference.aspose.com/cells/java/com.aspose.cells/row#applyStyle-com.aspose.cells.Style-com.aspose.cells.StyleFlag-)メソッドを使用できます。このメソッドには2つの引数があります。[**Style**](https://reference.aspose.com/cells/java/com.aspose.cells/Style)オブジェクトと適用された書式に関連するすべてのメンバーを持つ[**StyleFlag**](https://reference.aspose.com/cells/java/com.aspose.cells/StyleFlag)構造体です。

次の例は、ワークシート内の行をロックする方法を示しています。ますます、ワークシートのすべてのセルをアンロックし、それから最初の行をロックします。最後に、ワークシートを保護します。行/列にはStyle APIがあり、セルをロックまたはアンロックするメソッドを含んでいます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ProtectRowWorksheet-ProtectRowWorksheet.java" >}}

### **ワークシート内の列を保護する**

Aspose.Cellsを使用すると、ワークシート内の任意の列を簡単にロックできます。ここでは、ワークシート内の特定の列にStyleを適用するための[**applyStyle()**](https://reference.aspose.com/cells/java/com.aspose.cells/column#applyStyle-com.aspose.cells.Style-com.aspose.cells.StyleFlag-)メソッドを{1}クラスの[**applyStyle()**](https://reference.aspose.com/cells/java/com.aspose.cells/column#applyStyle-com.aspose.cells.Style-com.aspose.cells.StyleFlag-)メソッドを使用できます。このメソッドには2つの引数があります。[**Style**](https://reference.aspose.com/cells/java/com.aspose.cells/Style)オブジェクトと適用された書式に関連するすべてのメンバーを持つ[**StyleFlag**](https://reference.aspose.com/cells/java/com.aspose.cells/StyleFlag)構造体です。

次の例は、ワークシート内の列をロックする方法を示しています。ますます、ワークシートのすべてのセルをアンロックし、それから最初の列をロックします。最後に、ワークシートを保護します。行/列にはStyle APIがあり、セルをロックまたはアンロックするメソッドを含んでいます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ProtectColumnWorksheet-ProtectColumnWorksheet.java" >}}

## **ワークシートの保護を解除する**

[ワークシートの保護](/cells/ja/java/protect-and-unprotect-worksheet/#protect-worksheets)と[Excel XP以降の高度な保護設定](/cells/ja/java/protect-and-unprotect-worksheet/#advanced-protection-settings-since-excel-xp)は、保護したワークシートから保護を解除してファイルを変更できるようにする必要が開発者にある場合に異なるアプローチについて説明しています。これはAspose.Cellsで簡単に実行できます。

### **Microsoft Excel の使用**

ワークシートから保護を解除するには：

**ツール**メニューから**保護**を選択し、その後**シートの保護を解除**を選択します。

**シートの保護を解除**を選択 

![todo:image_alt_text](protect-and-unprotect-worksheet_4.png)

保護が解除されます（ワークシートがパスワードで保護されていない場合）。この場合、パスワードを入力するダイアログボックスが表示されます。

**ワークシートの保護を解除するためのパスワード入力** 

![todo:image_alt_text](protect-and-unprotect-worksheet_5.png)

### **Aspose.Cellsの使用**

ワークシートを[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラスの[**Unprotect**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#unprotect--)メソッドを呼び出すことで保護を解除できます。[**Unprotect**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#unprotect--)メソッドは2つの方法で使用できます。以下で説明します。

### **単純に保護されたワークシートの保護解除**

単純に保護されたワークシートはパスワードで保護されていないワークシートです。このようなワークシートはパラメータを渡さずに解除メソッドを呼び出すことで保護解除できます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-UnprotectingSimplyProtectedWorksheet-UnprotectingSimplyProtectedWorksheet.java" >}}

### **パスワードで保護されたワークシートの保護解除**

パスワードで保護されたワークシートはパスワードで保護されたワークシートです。このようなワークシートはパラメータとしてパスワードを取るUnprotectメソッドのオーバーロードバージョンを呼び出すことで保護解除できます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-UnprotectProtectSheet-UnprotectProtectSheet.java" >}}

## **Excel XP以降の高度な保護設定**

[ワークシートの保護](/cells/ja/java/protect-and-unprotect-worksheet/#protect-worksheets)では、Microsoft Excel 97および2000のワークシートの保護について説明しました。しかし、Excel 2002またはXPのリリース以降、Microsoftは多くの高度な保護設定を追加しました。これらの保護設定により、ユーザーに制限をかけることができます。

- 行または列の削除。
- 内容、オブジェクト、またはシナリオの編集。
- セル、行、または列の書式設定。
- 行、列、またはハイパーリンクの挿入。
- ロックされたセルまたはロックされていないセルの選択。
- ピボットテーブルなどの使用。

Aspose.Cellsは、Excel XPおよびそれ以降のバージョンで提供されるすべての高度な保護設定をサポートしています。

### **Excel XPおよびそれ以降のバージョンを使用した高度な保護設定**

Excel XPで利用可能な保護設定を表示するには：

1. **ツール** メニューから **保護** を選択し、続いて **シートを保護** を選択します。
   ダイアログが表示されます。

   **Excel XPで保護オプションを表示するためのダイアログ**

![todo:image_alt_text](protect-and-unprotect-worksheet_6.png)

1. ワークシートの機能の許可または制限、またはパスワードを適用します。

### **Aspose.Cellsを使用した高度な保護設定**

Aspose.Cellsはすべての高度な保護設定をサポートしています。

Aspose.Cellsは、Microsoft Excelファイルを表すWorkbookクラスを提供します。 Workbookクラスには、Excelファイル内の各ワークシートにアクセスを可能にするWorksheetCollectionコレクションが含まれています。ワークシートは[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) クラスで表されます。

Worksheetクラスには、これらの高度な保護設定を適用するために使用されるProtectionプロパティがあります。 Protectionプロパティは、実際には[**Protection**](https://reference.aspose.com/cells/java/com.aspose.cells/protection)クラスのオブジェクトで、制限の無効化または有効化のための複数のブールプロパティをカプセル化しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AdvancedProtectionSettingsUsingAsposeCells-AdvancedProtectionSettingsUsingAsposeCells.java" >}}

以下は小さなサンプルアプリケーションです。それはExcelファイルを開いて、Excel XPおよびそれ以降のバージョンでサポートされる高度な保護設定のほとんどを使用します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AdvancedProtection-AdvancedProtection.java" >}}

{{% alert color="primary" %}}

これらの高度な保護設定は、MS Excel XPおよびそれ以降のバージョンでのみサポートされているため、ファイルをEXCEL97TO2003またはXLSX形式で保存してください。

{{% /alert %}}

### **セルロックの問題**

ワークシートが保護されている場合でもセルを編集できるようにするには、保護設定が適用される前にセルをロックする必要があります。Microsoft Excel XPでは、次のダイアログを使用してセルをロックできます:

**Excel XPでセルをロックするためのダイアログ** 

![todo:image_alt_text](protect-and-unprotect-worksheet_7.png)

Aspose.CellsのAPIを使用してセルをロックすることも可能です。各セルは、さらにsetLockedメソッドを含むStyle APIを持っており、これを使用してセルをロックまたはロック解除できます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-LockCell-LockCell.java" >}}
{{< app/cells/assistant language="java" >}}
