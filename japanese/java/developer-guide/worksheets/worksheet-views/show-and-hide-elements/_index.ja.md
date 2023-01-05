---
title: 要素の表示と非表示
type: docs
weight: 60
url: /ja/java/show-and-hide-elements/
---
{{% alert color="primary" %}}

Aspose.Cells を使用すると、ワークシート、行、列、タブ、スクロールバー、グリッド線、

{{% /alert %}}

## **ワークシートの表示と非表示**

Excel ファイルには、1 つまたは複数のワークシートを含めることができます。 Excel ファイルを作成するときはいつでも、作業している Excel ファイルにワークシートを追加します。 Excel ファイル内の各ワークシートは、独自のデータや書式設定などを持つことにより、他のワークシートから独立しています。開発者は、自分の興味のために Excel ファイルでいくつかのワークシートを非表示にし、他のワークシートを表示する必要がある場合があります。それで、**Aspose.Cells**開発者は、Excel ファイル内のワークシートの表示を制御できます。

**ワークシートの可視性の制御:**

Aspose.Cells はクラスを提供し、[**ワークブック**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)これは Excel ファイルを表します。[**ワークブック**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)クラスには[**ワークシート コレクション**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)これにより、Excel ファイル内の各ワークシートにアクセスできます。

ワークシートは、[**ワークシート**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラス。[**ワークシート**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラスには、ワークシートを管理するためのさまざまなプロパティとメソッドが用意されています。ただし、ワークシートの可視性を制御するために、開発者は[**setVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsVisible)の方法[**ワークシート**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラス。

### **ワークシートを表示する**

開発者は、渡すことでワークシートを表示できます**真実**へのパラメータとして[**setVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsVisible)の方法[**ワークシート**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラス。

### **ワークシートを非表示にする**

開発者は、渡すことでワークシートを非表示にできます**間違い**へのパラメータとして[**setVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsVisible)の方法[**ワークシート**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラス。

**例：**

の使用を示す完全な例を以下に示します。[**setVisible(偽)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsVisible)方法[**ワークシート**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラスを使用して、Excel ファイルの最初のワークシートを非表示にします。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-display-HideUnhideWorksheet-1.java" >}}

**ワークシート - 変更前:**

下のスクリーンショットでは、それを見ることができます**Book1.xls**ファイルには 3 つのワークシートが含まれています。**シート1** , **シート 2**と**シート3** .

![todo:画像_代替_文章](show-and-hide-elements_1.png)

**形：**変更前のワークシート ビュー

**ワークシート - サンプル コードの実行後:**

**Book1.xls**ファイルは、[**ワークブック**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)クラスの最初のワークシート**Book1.xls**ファイルが非表示になります。変更されたファイルは次のように保存されます。**出力.xls**ファイルの図を以下に示します。

![todo:画像_代替_文章](show-and-hide-elements_2.png)

**形：**変更後のワークシート ビュー

**VisibilityType の設定**

特別な方法でワークシートを非表示にすることもできます。この機能はワークシートを非表示にすることができるので、再度表示するには、[**VisibilityType.VERY_HIDDEN**](https://reference.aspose.com/cells/java/com.aspose.cells/visibilitytype#VERY_HIDDEN)のパラメータ値として[**setVisibilityType**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#VisibilityType)コード内のメソッド (ここで注意してください。ユーザーは、メニュー オプションを使用して直接 MS Excel でオブジェクトを表示することはできません)。ユーザーも使用できます[**getVisibilityType**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#VisibilityType)ワークシートが VeryHidden としてマークされているかどうかを確認するメソッド。

## **タブの表示または非表示**

Microsoft Excel ファイルの下部をよく見ると、多数のコントロールが表示されます。これらには以下が含まれます：

- シート タブ。
- タブスクロールボタン。

シート タブは、Excel ファイル内のワークシートを表します。任意のタブをクリックして、そのワークシートに切り替えます。ワークブック内のワークシートが多いほど、シート タブが多くなります。 Excel ファイルに十分な数のワークシートがある場合は、それらをナビゲートするためのボタンが必要です。そのため、Microsoft Excel には、シート タブをスクロールするためのタブ スクロール ボタンが用意されています。

**シート タブとタブ スクロール ボタン**

![todo:画像_代替_文章](show-and-hide-elements_3.png)

Aspose.Cells を使用すると、開発者は Excel ファイルのシート タブとタブ スクロール ボタンの表示を制御できます。

**タブの可視性の制御:**
Aspose.Cells はクラスを提供し、[**ワークブック**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)、Microsoft Excel ファイルを表します。の[**ワークブック**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)クラスには、Excel ファイルを管理するためのさまざまなプロパティとメソッドが用意されています。

### **タブを非表示にする**

を設定して、Excel ファイルのタブを非表示にします。[**ワークブック**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)クラス'[**getSettings().setShowTabs(false)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#ShowTabs)方法。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-HideTabs-1.java" >}}

### **タブを表示する**

タブを表示するには[**ワークブック**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)クラス'[**getSettings().setShowTabs(true)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#ShowTabs)方法。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-DisplayTab-1.java" >}}

**完全なコード例:**

以下は、Excel ファイル (book1.xls) を開き、そのタブを非表示にして、変更したファイルを output.xls として保存する完全な例です。

下の図では、Book1.xls ファイルにタブが含まれていることがわかります。以下の output.xls ファイルのスクリーンショットからわかるように、サンプル コードを実行すると、タブが非表示になります。

**book1.xls: 変更前の Excel ファイル**

![todo:画像_代替_文章](show-and-hide-elements_4.png)

**output.xls：修正後のExcelファイル**

![todo:画像_代替_文章](show-and-hide-elements_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-HideTabs-1.java" >}}

## **行と列の表示と非表示**

Excel ファイル内のすべてのワークシートは、行と列に配置されたセルで構成されています。すべての行と列には、それらを識別し、個々のセルを識別するために使用される一意の値があります。たとえば、行には 1、2、3、4 などの番号が付けられ、列は A、B、C、D などのアルファベット順に並べられます。行と列の値はヘッダーに表示されます。開発者は、Aspose.Cells を使用して、これらの行と列のヘッダーの表示を制御できます。

**ワークシートの可視性の制御:**

Aspose.Cells はクラスを提供し、[**ワークブック**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)、Microsoft Excel ファイルを表します。 Workbook クラスには、Excel ファイル内の各ワークシートへのアクセスを可能にする WorksheetCollection が含まれています。

ワークシートは、[**ワークシート**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラス。 Worksheet クラスは、ワークシートを管理するための幅広いプロパティとメソッドを提供します。行ヘッダーと列ヘッダーの表示を制御するには、Worksheet クラスの[**setRowColumnHeadersVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsRowColumnHeadersVisible)方法。

### **行/列ヘッダーの非表示**

を使用して行と列のヘッダーを非表示にします。[**ワークシート**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラス'[**setRowColumnHeadersVisible(false)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsRowColumnHeadersVisible)方法。

### **行/列ヘッダーを表示する**

を使用して、行と列のヘッダーを表示します。[**ワークシート**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラス'[**setRowColumnHeadersVisible(true)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsRowColumnHeadersVisible)方法。

の使用方法を示す完全な例を以下に示します。[**ワークシート**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラス'[**setRowColumnHeadersVisible(false)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsRowColumnHeadersVisible) Excel ファイルの最初のワークシートの行ヘッダーと列ヘッダーを非表示にするメソッド。

以下のスクリーンショットは、Book1.xls に Sheet1、Sheet2、Sheet3 の 3 つのワークシートが含まれていることを示しています。各ワークシートには、行と列のヘッダーが表示されています。

**Book1.xls: 修正前のワークシート**

![todo:画像_代替_文章](show-and-hide-elements_6.png)

Book1.xls は、[**ワークブック**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) class' であり、最初のワークシートの行と列のヘッダーは非表示になっています。変更されたファイルは、output.xls として保存されます。

**変更後のワークシート ビュー**

![todo:画像_代替_文章](show-and-hide-elements_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-HideUnhideWorksheet-1.java" >}}

## **スクロール バーの表示と非表示**

スクロール バーは、ファイルの内容をナビゲートするためによく使用されます。通常、スクロール バーには次の 2 種類があります。

- 垂直スクロール バー
- 水平スクロール バー

Microsoft Excel には、ユーザーがワークシートの内容をスクロールできるように、水平および垂直のスクロール バーも用意されています。 Aspose.Cells を使用すると、開発者は Excel ファイルで両方のタイプのスクロール バーの表示を制御できます。

**スクロール バーの表示を制御する:**

Aspose.Cells はクラスを提供し、[**ワークブック**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)これは Excel ファイルを表します。[**ワークブック**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)クラスには、Excel ファイルを管理するためのさまざまなプロパティとメソッドが用意されています。ただし、Excel ファイルのスクロール バーの表示を制御するために、開発者は[**setVScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsVScrollBarVisible) & [**setHScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsHScrollBarVisible)のメソッド[**ワークブック**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)クラス。

### **スクロール バーを非表示にする**

を設定してスクロール バーを非表示にします。[**ワークブック**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)クラス'[**setVScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsVScrollBarVisible)また[**setHScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsHScrollBarVisible)方法**間違い**.

### **スクロール バーを表示する**

Workbook クラスを設定して、スクロール バーを表示します。[**setVScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsVScrollBarVisible)また[**setHScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsHScrollBarVisible)方法**真実**.

**完全なコード例:**

以下は、Excel ファイル book1.xls を開き、両方のスクロール バーを非表示にしてから、変更したファイルを output.xls として保存する完全なコードです。

以下のスクリーンショットは、両方のスクロール バーを含む Book1.xls ファイルを示しています。変更されたファイルは output.xls ファイルとして保存されます。これも以下に示します。

**Book1.xls: 変更前の Excel ファイル**

![todo:画像_代替_文章](show-and-hide-elements_8.png)

**output.xls：修正後のExcelファイル**

![todo:画像_代替_文章](show-and-hide-elements_9.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-display-DisplayHideScrollBars-1.java" >}}

## **グリッド線の表示と非表示**

すべての Microsoft Excel ワークシートには、既定でグリッド線があります。セルの輪郭を描くのに役立ち、特定のセルにデータを簡単に入力できます。グリッド線を使用すると、ワークシートをセルのコレクションとして表示でき、各セルを簡単に識別できます。

Aspose.Cells では、グリッド線の表示を制御することもできます。

### **グリッド線の可視性の制御**

Aspose.Cells はクラスを提供し、[**ワークブック**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) Microsoft Excel ファイルを表します。の[**ワークブック**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)クラスには[**ワークシート コレクション**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)ファイル内の各ワークシートにアクセスできます。

ワークシートは、[**ワークシート**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラス。の[**ワークシート**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラスには、ワークシートを管理するためのさまざまなプロパティとメソッドが用意されています。グリッド線の可視性を制御するには、[**ワークシート**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラス'[**setGridlinesVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsGridlinesVisible)方法。

#### **グリッド線を表示する**

グリッド線を表示するには、[**ワークシート**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラス'[**setGridlinesVisible(true)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsGridlinesVisible)方法。

#### **グリッド線を非表示にする**

を使用してグリッド線を非表示にします[**ワークシート**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラス'[**setGridlinesVisible(false)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsGridlinesVisible)方法。

{{% alert color="primary" %}}

グリッド線はシート全体に適用されます。ワークシートのセクションでグリッド線を「非表示」にするには、次を使用します[境界線の書式設定](/cells/ja/java/create-table-by-using-border-lines-for-a-range/)シートの配色に溶け込む色に境界線を設定します。

{{% /alert %}}

**例: 特定のワークシートでグリッド線を非表示にする**

以下の例は、[**ワークシート**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラス'[**setGridlinesVisible(false)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsGridlinesVisible) Excel ファイルの最初のワークシートのグリッド線を非表示にするメソッド。

以下のスクリーンショットは、Book1.xls ファイルに Sheet1、Sheet2、Sheet3 の 3 つのワークシートが含まれていることを示しています。これらのワークシートにはすべてグリッド線があります。

**変更前のワークシート ビュー**

![todo:画像_代替_文章](show-and-hide-elements_10.png)

Book1.xls ファイルは、[**ワークブック**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)クラスを選択すると、最初のワークシートのグリッド線が非表示になります。変更されたファイルは、output.xls ファイルとして保存されます。

**変更後のワークシート ビュー**

![todo:画像_代替_文章](show-and-hide-elements_11.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-DisplayHideGridlines-DisplayHideGridlines.java" >}}

### **関連記事**

{{% alert color="primary" %}}

- [ページ設定機能](/cells/ja/java/page-setup-features/).
- [セルに罫線を追加して表を作成する](/cells/ja/java/create-table-by-using-border-lines-for-a-range/).

{{% /alert %}}
