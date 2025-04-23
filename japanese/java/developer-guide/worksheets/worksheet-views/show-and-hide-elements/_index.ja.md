---
title: 要素の表示と非表示
type: docs
weight: 60
url: /ja/java/show-and-hide-elements/
---

{{% alert color="primary" %}}

Aspose.Cellsを使用すると、ワークブックの要素（ワークシート、行、列、タブ、スクロールバー、グリッド線など）の表示および非表示を制御することができます。

{{% /alert %}}

## **ワークシートの表示と非表示**

Excelファイルには1つ以上のワークシートが含まれることがあります。Excelファイルを作成するときには、作業するExcelファイルにワークシートを追加します。Excelファイル内の各ワークシートは、独自のデータや書式設定などを持つため、他のワークシートから独立しています。開発者は時々、Excelファイル内で特定のワークシートを非表示にし、他のワークシートを表示したい場合があります。そのため、Aspose.Cellsは開発者がExcelファイル内のワークシートの表示を制御することを可能にします。

**ワークシートの表示を制御する:**

Aspose.Cellsは、Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)クラスには、Excelファイル内の各ワークシートにアクセスするための[**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)が含まれています。

ワークシートは[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラスには、ワークシートを管理するための様々なプロパティやメソッドがあります。ただし、ワークシートの表示の制御には、[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラスの[**setVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsVisible)メソッドを使用することができます。

### **ワークシートを表示する**

開発者は、[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラスの[**setVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsVisible)メソッドに**true**をパラメータとして渡すことで、ワークシートを表示することができます。

### **ワークシートを非表示にする**

開発者は、[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラスの[**setVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsVisible)メソッドに**false**をパラメータとして渡すことで、ワークシートを非表示にすることができます。

**例:**

以下は、[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラスの[**setVisible(false)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsVisible)メソッドを使用してExcelファイルの最初のワークシートを非表示にする方法を示す完全な例です。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-display-HideUnhideWorksheet-1.java" >}}

**ワークシート - 修改前:**

下のスクリーンショットでは、**Book1.xls** ファイルには **Sheet1**、 **Sheet2**、 **Sheet3** の3つのワークシートが含まれていることがわかります。

![todo:image_alt_text](show-and-hide-elements_1.png)

**図: ** どのような変更も加わる前のワークシートビュー

**ワークシート - 例のコードを実行後:**

**Book1.xls** ファイルは **[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)** クラスを使用して開かれ、その後 **Book1.xls** ファイルの最初のワークシートが非表示にされます。変更したファイルは **output.xls** ファイルとして保存され、その視覚的なビューが以下に示されています：

![todo:image_alt_text](show-and-hide-elements_2.png)

**図: ** 変更後のワークシートビュー

**VisibilityTypeの設定**

ユーザーはワークシートを特別な方法で非表示にすることもできます。この機能を使用することで、ワークシートを非表示にし、MS Excelのメニューオプションを使用して直接表示する唯一の方法が、コード内で[**setVisibilityType**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#VisibilityType)メソッドのパラメータ値として[**VisibilityType.VERY_HIDDEN**](https://reference.aspose.com/cells/java/com.aspose.cells/visibilitytype#VERY-HIDDEN)を指定することです（ここで注意する必要がありますが、ユーザーはオブジェクトをMS Excelで直接表示することはできません）。ユーザーはまた、[**getVisibilityType**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#VisibilityType)メソッドを使用して、ワークシートがVeryHiddenとしてマークされているかどうかを確認することもできます。

## **タブの表示または非表示**

Microsoft Excelの下部をよく見ると、いくつかのコントロールが表示されます。これには次のものが含まれます:

- シートタブ。
- タブのスクロールボタン。

シートタブはExcelファイル内のワークシートを表します。任意のタブをクリックするとそのワークシートに切り替えることができます。ワークブック内にワークシートが多いほど、シートタブも多く表示されます。Excelファイルに多くのワークシートが含まれている場合は、それらをナビゲートするためのボタンが必要になります。そのため、Microsoft Excelはシートタブのスクロールボタンを提供しています。

**シートのタブとタブのスクロールボタン**

![todo:image_alt_text](show-and-hide-elements_3.png)

Aspose.Cellsを使用すると、開発者はExcelファイル内のシートタブとタブのスクロールボタンの表示を制御できます。

**タブの表示を制御する:**
Aspose.Cells は、Microsoft Excel ファイルを表す [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) クラスは、Excelファイルの管理に広範なプロパティやメソッドを提供します。

### **タブを非表示にする**

Excelファイルのタブを [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) クラスの [**getSettings().setShowTabs(false)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#ShowTabs) メソッドを設定して非表示にします。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-HideTabs-1.java" >}}

### **タブを表示する**

[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) クラスの [**getSettings().setShowTabs(true)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#ShowTabs) メソッドを使用してタブを表示します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-DisplayTab-1.java" >}}

**完全なコード例:**

以下は、Excelファイル（book1.xls）を開き、そのタブを非表示にして変更したファイルをoutput.xlsとして保存する完全な例です。

Book1.xlsファイルにタブが含まれていることが以下の図からわかります。例のコードが実行された後、タブが非表示になっていることがoutput.xlsファイルのスクリーンショットから確認できます。

**book1.xls: 修正前のExcelファイル**

![todo:image_alt_text](show-and-hide-elements_4.png)

**output.xls: 修正後のExcelファイル**

![todo:image_alt_text](show-and-hide-elements_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-HideTabs-1.java" >}}

## **行や列の表示と非表示**

Excelファイルのすべてのワークシートは、行と列に配置されたセルで構成されています。すべての行と列には、それぞれ固有の値があり、それを使用して識別し、個々のセルを識別します。たとえば、行は1、2、3、4などと番号がつけられ、列はA、B、C、Dなどとアルファベット順に並べられます。行と列の値はヘッダーに表示されます。Aspose.Cellsを使用すると、開発者はこれらの行と列のヘッダーの表示を制御できます。

**ワークシートの表示を制御する:**

Aspose.Cells は、Microsoft Excel ファイルを表す [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) クラスを提供します。Workbook クラスには、Excelファイル内の各ワークシートにアクセスできる WorksheetCollection が含まれています。

ワークシートは [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) クラスによって表されます。Worksheet クラスは、ワークシートを管理するための広範なプロパティやメソッドを提供します。行と列のヘッダーの表示を制御するには、Worksheet クラスの [**setRowColumnHeadersVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsRowColumnHeadersVisible) メソッドを使用します。

### **行/列ヘッダーを非表示にする**

[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) クラスの [**setRowColumnHeadersVisible(false)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsRowColumnHeadersVisible) メソッドを使用して行や列のヘッダーを非表示にします。

### **行/列ヘッダーを表示する**

[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) クラスの [**setRowColumnHeadersVisible(true)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsRowColumnHeadersVisible) メソッドを使用して行や列のヘッダーを表示します。

以下に、Excelファイルの最初のワークシートの行や列のヘッダーを非表示にする方法を示す完全な例が示されています。

以下のスクリーンショットでは、Book1.xls に Sheet1、Sheet2、Sheet3 の3つのワークシートが含まれていることが示されています。それぞれのワークシートは行や列のヘッダーが表示されています。

**Book1.xls: 修正前のワークシート**

![todo:image_alt_text](show-and-hide-elements_6.png)

Book1.xls を [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) クラスを使用して開き、最初のワークシートの行や列のヘッダーを非表示にしました。修正されたファイルは output.xls として保存されています。

**修正後のワークシートビュー**

![todo:image_alt_text](show-and-hide-elements_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-HideUnhideWorksheet-1.java" >}}

## **スクロールバーの表示と非表示**

スクロールバーは、ファイルの内容を移動するために非常によく使用されます。通常、次の2種類のスクロールバーがあります。

- 垂直スクロールバー
- 水平スクロールバー

Microsoft Excelは、ユーザーがワークシートの内容をスクロールできるように、水平および垂直のスクロールバーを提供しています。Aspose.Cellsを使用すると、Excelファイルの両方のタイプのスクロールバーの表示/非表示を制御することができます。

**スクロールバーの表示を制御する:**

Aspose.CellsはExcelファイルを表すクラス、[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)を提供しています。[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)クラスは、Excelファイルを管理するための幅広いプロパティとメソッドを提供しています。ただし、Excelファイル内のスクロールバーの表示を制御するには、開発者は[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)クラスの[**setVScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsVScrollBarVisible)および[**setHScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsHScrollBarVisible)メソッドを使用することができます。

### **スクロールバーを非表示にする**

[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)クラスの[**setVScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsVScrollBarVisible)または[**setHScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsHScrollBarVisible)メソッドを**false**に設定することで、スクロールバーを非表示にします。

### **スクロールバーを表示する**

[**setVScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsVScrollBarVisible)クラスの[**setHScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsHScrollBarVisible)メソッドを**true**に設定することで、スクロールバーを表示する。

**完全なコード例:**

以下は、Excelファイルであるbook1.xlsを開き、両方のスクロールバーを非表示にし、変更されたファイルをoutput.xlsとして保存する完全なコードです。

下のスクリーンショットは、スクロールバーが含まれているBook1.xlsファイルを示しています。変更されたファイルはoutput.xlsファイルとして保存され、下にも表示されています。

**Book1.xls: 修正前のExcelファイル**

![todo:image_alt_text](show-and-hide-elements_8.png)

**output.xls: 修正後のExcelファイル**

![todo:image_alt_text](show-and-hide-elements_9.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-display-DisplayHideScrollBars-1.java" >}}

## **グリッド線の表示と非表示**

すべてのMicrosoft Excelワークシートには、デフォルトでグリッド線があります。これにより、セルを区切ることができ、特定のセルにデータを入力しやすくなります。グリッド線により、ワークシートをセルの集合として表示し、各セルを簡単に識別できます。

Aspose.Cellsを使用すると、グリッド線の表示を制御することができます。

### **グリッド線の表示を制御する**

Aspose.CellsはMicrosoft Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)クラスを提供しています。[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)クラスには、ファイル内の各ワークシートにアクセスできる[**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)が含まれています。

ワークシートは[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラスには、ワークシートを管理するための幅広いプロパティとメソッドが含まれています。グリッド線の表示を制御するには、[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラスの[**setGridlinesVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsGridlinesVisible)メソッドを使用します。

#### **グリッド線を表示する**

グリッド線を表示するには、[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラスの[**setGridlinesVisible(true)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsGridlinesVisible)メソッドを使用します。

#### **グリッド線を非表示にする**

グリッド線を[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラスの[**setGridlinesVisible(false)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsGridlinesVisible)メソッドを使用して非表示にします。

{{% alert color="primary" %}}

グリッド線はワークシート全体に適用されます。ワークシートのセクションでグリッド線を非表示にするには、[border formatting](/cells/ja/java/create-table-by-using-border-lines-for-a-range/)を使用して、そのボーダーをシートのカラースキームに溶け込む色に設定します。

{{% /alert %}}

**例: 特定のワークシートでグリッド線を非表示にする**

以下の例は、Excelファイルの最初のワークシートのグリッド線を非表示にするための[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラスの[**setGridlinesVisible(false)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsGridlinesVisible)メソッドの使用方法を示しています。

下のスクリーンショットは、Book1.xlsファイルがSheet1、Sheet2、Sheet3の3つのワークシートを含むことを示しています。これらのすべてのワークシートにはグリッド線があります。

**修正前のワークシートビュー**

![todo:image_alt_text](show-and-hide-elements_10.png)

Book1.xlsファイルは[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)クラスを使用して開かれ、その後、最初のワークシートのグリッド線が非表示にされます。変更したファイルはoutput.xlsファイルとして保存されます。

**修正後のワークシートビュー**

![todo:image_alt_text](show-and-hide-elements_11.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-DisplayHideGridlines-DisplayHideGridlines.java" >}}

### **関連記事**

{{% alert color="primary" %}}

- [ページ設定機能](/cells/ja/java/page-setup-features/)
- [セルに境界線を追加してテーブルを作成する](/cells/ja/java/create-table-by-using-border-lines-for-a-range/)

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
