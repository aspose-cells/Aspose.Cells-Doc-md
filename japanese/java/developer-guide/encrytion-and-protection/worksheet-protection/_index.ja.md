---
title: ワークシートの保護と保護解除
type: docs
weight: 50
url: /ja/java/protect-and-unprotect-worksheet/
---
## **ワークシートを保護する**

ワークシートが保護されている場合、ユーザーが実行できるアクションは制限されます。たとえば、データを入力したり、行や列を挿入または削除したりすることはできません。Microsoft Excel の一般的な保護オプションは次のとおりです。

- コンテンツ
- オブジェクト
- シナリオ

保護されたワークシートは機密データを隠したり保護したりしないため、ファイルの暗号化とは異なります。一般に、ワークシートの保護はプレゼンテーションの目的に適しています。これにより、エンド ユーザーはワークシートのデータ、コンテンツ、および書式を変更できなくなります。

### **保護の追加または削除**

Aspose.Cells はクラスを提供し、[**ワークブック**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)、Microsoft Excel ファイルを表します。 Workbook クラスには、Excel ファイル内の各ワークシートにアクセスできるようにする WorksheetCollection が含まれています。ワークシートは、[**ワークシート**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラス。

 Worksheet クラスは、[**守る**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#protect(int)ワークシートに保護を適用するために使用されるメソッド。 Protect メソッドは、次のパラメーターを受け入れます。

- 保護タイプ、ワークシートに適用する保護のタイプ。保護タイプは、[**保護タイプ**](https://reference.aspose.com/cells/java/com.aspose.cells/ProtectionType)列挙。
- 新しいパスワード。ワークシートを保護するために使用される新しいパスワード。
- 古いパスワード、ワークシートがすでにパスワードで保護されている場合の古いパスワード。ワークシートがまだ保護されていない場合は、null を渡します。

ProtectionType 列挙には、次の事前定義された保護の種類が含まれています。

|**保護の種類**|**説明**|
|:- |:- |
|[**全て**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#ALL)|ユーザーはこのワークシートで何も変更できません|
|[**コンテンツ**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#CONTENTS)|ユーザーはこのワークシートにデータを入力できません|
|[**オブジェクト**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#OBJECTS)|ユーザーは描画オブジェクトを変更できません|
|[**シナリオ**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#SCENARIOS)|ユーザーは保存されたシナリオを変更できません|
|[**構造**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#STRUCTURE)|ユーザーは保存された構造を変更できません|
|[**ウィンドウズ**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#WINDOWS)|ユーザーは保存されたウィンドウを変更できません|
|[**なし**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#NONE)|保護なし|

次の例は、ワークシートをパスワードで保護する方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ProtectingWorksheet-ProtectingWorksheet.java" >}}

上記のコードを使用してワークシートを保護した後、ワークシートを開いて保護を確認します。ファイルを開いてワークシートにデータを追加しようとすると、次のダイアログが表示されます。

**ユーザーがワークシートを変更できないことを警告するダイアログ** 

![todo:画像_代替_文章](protect-and-unprotect-worksheet_1.png)

ワークシートで作業するには、**保護**、 それから**シートの保護を解除**から**ツール**下図のようなメニュー項目。

**シート保護解除メニュー項目の選択** 

![todo:画像_代替_文章](protect-and-unprotect-worksheet_2.png)

パスワードの入力を求めるダイアログが開きます。

**パスワードを入力してワークシートの保護を解除しています** 

![todo:画像_代替_文章](protect-and-unprotect-worksheet_3.png)

### **少数を保護する Cells**

ワークシート内のいくつかのセルのみをロックする必要がある特定のシナリオがあるかもしれません。ワークシート内の特定のセルをロックする場合は、ワークシート内の他のすべてのセルのロックを解除する必要があります。ワークシート内のすべてのセルは、すでにロック用に初期化されています。これを確認して、任意の Excel ファイルを MS Excel で開き、**フォーマット | Cells...**見せる**フォーマット Cells**ダイアログ ボックスを開き、[保護] タブをクリックすると、デフォルトで [ロック] というラベルの付いたチェック ボックスがオンになっていることがわかります。

以下は、タスクを実装するための 2 つのアプローチです。

**方法1:**

次のポイントでは、MS Excel を使用していくつかのセルをロックする方法について説明します。この方法は、Microsoft Office Excel 97、2000、2002、2003 以降のバージョンに適用されます。

1. [すべて選択] ボタン (行 1 の行番号のすぐ上、列文字 A の左側にある灰色の四角形) をクリックして、ワークシート全体を選択します。
1. [フォーマット] メニューの [Cells] をクリックし、[保護] タブをクリックして、[ロック] チェック ボックスをオフにします。

これにより、ワークシートのすべてのセルのロックが解除されます

{{% alert color="primary" %}}

セル コマンドが使用できない場合は、ワークシートの一部が既にロックされている可能性があります。 [ツール] メニューの [保護] をポイントし、[シートの保護の解除] をクリックします。

{{% /alert %}}

1. ロックするセルだけを選択して手順 2 を繰り返しますが、今回は [ロック] チェック ボックスをオンにします。
1. 上で**ツール**メニュー、選択**保護** 、 クリック**プロテクトシート**をクリックし、**わかった**.

{{% alert color="primary" %}}

[シートの保護] ダイアログ ボックスには、パスワードを指定し、ユーザーが変更できるようにする要素を選択するオプションがあります。

{{% /alert %}}

**方法 2:**

この方法では、タスクを実行するためだけに Aspose.Cells API を使用します。

次の例は、ワークシート内のいくつかのセルを保護する方法を示しています。最初にワークシート内のすべてのセルのロックを解除し、次に 3 つのセル (A1、B1、C1) をロックします。最後に、ワークシートを保護します。行/列には、セット Locked メソッドをさらに含む Style API があります。このメソッドを使用して、行/列をロックまたはロック解除できます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ProtectingSpecificCellsinaWorksheet-ProtectingSpecificCellsinaWorksheet.java" >}}

### **ワークシートの行を保護する**

Aspose.Cells を使用すると、ワークシートの任意の行を簡単にロックできます。ここで、私たちは利用することができます[**applyStyle()**](https://reference.aspose.com/cells/java/com.aspose.cells/row#applyStyle(com.aspose.cells.Style,%20com.aspose.cells.StyleFlag) ）の方法[**行**](https://reference.aspose.com/cells/java/com.aspose.cells/Row)ワークシートの特定の行に Style を適用するクラス。このメソッドは 2 つの引数を取ります。[**スタイル**](https://reference.aspose.com/cells/java/com.aspose.cells/Style)オブジェクトと[**スタイルフラグ**](https://reference.aspose.com/cells/java/com.aspose.cells/StyleFlag)適用された書式設定に関連するすべてのメンバーを持つ構造体。

次の例は、ワークシートの行を保護する方法を示しています。最初にワークシート内のすべてのセルのロックを解除してから、その最初の行をロックします。最後に、ワークシートを保護します。行/列には、setCellLocked メソッドをさらに含む Style API があります。 StyleFlag 構造体を使用して、行/列をロックまたはロック解除できます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ProtectRowWorksheet-ProtectRowWorksheet.java" >}}

### **ワークシートの列を保護する**

Aspose.Cells を使用すると、ワークシート内の任意の列を簡単にロックできます。ここで、私たちは利用することができます[**applyStyle()**](https://reference.aspose.com/cells/java/com.aspose.cells/column#applyStyle(com.aspose.cells.Style,%20com.aspose.cells.StyleFlag) ）の方法[**桁**](https://reference.aspose.com/cells/java/com.aspose.cells/Column)ワークシートの特定の列に Style を適用するクラス。このメソッドは 2 つの引数を取ります。[**スタイル**](https://reference.aspose.com/cells/java/com.aspose.cells/Style)オブジェクトと[**スタイルフラグ**](https://reference.aspose.com/cells/java/com.aspose.cells/StyleFlag)適用された書式設定に関連するすべてのメンバーを持つ構造体。

次の例は、ワークシートの列を保護する方法を示しています。最初にワークシート内のすべてのセルのロックを解除してから、その最初の列をロックします。最後に、ワークシートを保護します。行/列には、セット Locked メソッドをさらに含む Style API があります。 StyleFlag 構造体を使用して、行/列をロックまたはロック解除できます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ProtectColumnWorksheet-ProtectColumnWorksheet.java" >}}

## **ワークシートの保護を解除する**

[ワークシートの保護](/cells/ja/java/protect-and-unprotect-worksheet/#protect-worksheets)と[Excel XP 以降の高度な保護設定](/cells/ja/java/protect-and-unprotect-worksheet/#advanced-protection-settings-since-excel-xp)ワークシートを保護するためのさまざまなアプローチについて説明しました。ファイルに変更を加えることができるように、開発者が実行時に保護されたワークシートから保護を解除する必要がある場合はどうすればよいでしょうか?これは、Aspose.Cells で簡単に実行できます。

### **Microsoft エクセルを使う**

ワークシートから保護を解除するには:

から**ツール**メニュー、選択**保護**に続く**シートの保護を解除**.

**保護解除シートの選択** 

![todo:画像_代替_文章](protect-and-unprotect-worksheet_4.png)

ワークシートがパスワードで保護されていない限り、保護は解除されます。この場合、パスワードの入力を求めるダイアログが表示されます。

**パスワードを入力してワークシートの保護を解除しています** 

![todo:画像_代替_文章](protect-and-unprotect-worksheet_5.png)

### **Aspose.Cells を使用**

を呼び出すことにより、ワークシートの保護を解除できます。[**ワークシート**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラス'[**保護解除**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#unprotect()） 方法。の[**保護解除**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#unprotect()メソッドは、以下で説明する 2 つの方法で使用できます。

### **単純に保護されたワークシートの保護を解除する**

単純に保護されたワークシートは、パスワードで保護されていないワークシートです。このようなワークシートは、パラメーターを渡さずに unprotect メソッドを呼び出すことで保護を解除できます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-UnprotectingSimplyProtectedWorksheet-UnprotectingSimplyProtectedWorksheet.java" >}}

### **パスワードで保護されたワークシートの保護を解除する**

パスワードで保護されたワークシートは、パスワードで保護されたワークシートです。このようなワークシートは、パスワードをパラメーターとして受け取る Unprotect メソッドのオーバーロードされたバージョンを呼び出すことによって保護を解除できます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-UnprotectProtectSheet-UnprotectProtectSheet.java" >}}

## **Excel XP 以降の高度な保護設定**

[ワークシートの保護](/cells/ja/java/protect-and-unprotect-worksheet/#protect-worksheets) Microsoft Excel 97 および 2000 でのワークシートの保護について説明しました。しかし、Excel 2002 または XP のリリース以降、Microsoft には多くの高度な保護設定が追加されました。これらの保護設定により、ユーザーは次のことが制限または許可されます。

- 行または列を削除します。
- コンテンツ、オブジェクト、またはシナリオを編集します。
- セル、行、または列をフォーマットします。
- 行、列、またはハイパーリンクを挿入します。
- ロックまたはロック解除されたセルを選択します。
- ピボット テーブルなどを使用します。

Aspose.Cells は、Excel XP 以降のバージョンで提供されるすべての高度な保護設定をサポートしています。

### **Excel XP 以降のバージョンを使用した高度な保護設定**

Excel XP で使用可能な保護設定を表示するには:

1. から**ツール**メニュー、選択**保護**に続く**プロテクトシート**.
ダイアログが表示されます。

   **Excel XP の保護オプションを表示するダイアログ**

![todo:画像_代替_文章](protect-and-unprotect-worksheet_6.png)

1. ワークシート機能を許可または制限するか、パスワードを適用します。

### **Aspose.Cells を使用した高度な保護設定**

Aspose.Cells は、すべての高度な保護設定をサポートしています。

Aspose.Cells はクラスを提供し、[**ワークブック**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) 、Microsoft Excel ファイルを表します。 Workbook クラスには、Excel ファイル内の各ワークシートへのアクセスを可能にする WorksheetCollection コレクションが含まれています。ワークシートは、[**ワークシート**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラス。

 Worksheet クラスは、これらの高度な保護設定を適用するために使用される Protection プロパティを提供します。 Protection プロパティは、実際には[**保護**](https://reference.aspose.com/cells/java/com.aspose.cells/protection)制限を無効または有効にするためのいくつかのブール型プロパティをカプセル化するクラス。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AdvancedProtectionSettingsUsingAsposeCells-AdvancedProtectionSettingsUsingAsposeCells.java" >}}

以下は小さなアプリケーション例です。 Excel ファイルを開き、Excel XP 以降のバージョンでサポートされている高度な保護設定のほとんどを使用します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AdvancedProtection-AdvancedProtection.java" >}}

{{% alert color="primary" %}}

ファイルを EXCEL97TO2003 または XLSX 形式で保存します。これらの高度な保護設定は、MS Excel XP 以降のバージョンでのみサポートされているためです。

{{% /alert %}}

### **Cell ロックの問題**

ユーザーによるセルの編集を制限する場合は、保護設定を適用する前にセルをロックする必要があります。そうしないと、ワークシートが保護されていてもセルを編集できます。 Microsoft Excel XP では、次のダイアログでセルをロックできます。

**Excel XP でセルをロックするためのダイアログ** 

![todo:画像_代替_文章](protect-and-unprotect-worksheet_7.png)

Aspose.Cells API を使用してセルをロックすることもできます。各セルには、setLocked メソッドをさらに含む Style API があります。それを使用して、セルをロックまたはロック解除します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-LockCell-LockCell.java" >}}
