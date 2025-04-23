---
title: ワークシートビュー
type: docs
weight: 40
url: /ja/go-cpp/worksheet-views/
---

## **ページブレークプレビュー**

すべてのワークシートは次の2つのモードで表示できます:

- 通常の表示。
- ページブレークプレビュー。

通常の表示はワークシートのデフォルトの表示方法です。ページブレークプレビューは、ワークシートを印刷時の表示として提供する編集ビューです。ページブレークプレビューでは、どのデータが各ページに表示されるかを表示し、印刷範囲やページブレークを調整できます。Aspose.Cellsを使用すると、通常の表示またはページブレークプレビューモードを有効にできます。

### **表示モードの制御**

Aspose.Cellsは [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) クラスを提供しており、Microsoft Excel ファイルを表します。[Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) クラスは [Worksheets](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) コレクションを含み、各ワークシートにアクセス可能です。

ワークシートは [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) クラスで表されます。 [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) クラスはワークシートの管理に役立つ多くのメソッドを提供します。ページ区切りプレビューまたは通常モードに切り替えるには、[SetIsPageBreakPreview](https://reference.aspose.com/cells/go-cpp/worksheet/setispagebreakpreview/) メソッドを使用します。[IsPageBreakPreview](https://reference.aspose.com/cells/go-cpp/worksheet/ispagebreakpreview/) はブール値を返し、**true** または **false** のみを格納できます。

#### **通常の表示の有効化**

[SetIsPageBreakPreview](https://reference.aspose.com/cells/go-cpp/worksheet/setispagebreakpreview/) メソッドを **false** に設定することで、ワークシートを通常ビューに設定します。

#### **ページブレークプレビューの有効化**

[SetIsPageBreakPreview](https://reference.aspose.com/cells/go-cpp/worksheet/setispagebreakpreview/) メソッドを **true** に設定することで、ワークシートをページ区切りプレビューに切り替えます。これにより、ワークシートは通常ビューからページ区切りプレビューに切り替わります。

以下に例を示します。これにより、[SetIsPageBreakPreview](https://reference.aspose.com/cells/go-cpp/worksheet/setispagebreakpreview/) メソッドを使用してExcelファイルの最初のワークシートのページ区切りプレビュー モードを有効にする方法が示されています。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-EnablingPageBreakPreview.go" >}}

## **ズームファクター**

### **Microsoft Excel の使用**

Microsoft Excel には、ワークシートのズームやスケーリング要素を設定する機能があります。この機能は、ユーザーがワークシートの内容を小さなビューまたは大きなビューで表示するのに役立ちます。ユーザーは、ズーム要素を任意の値に設定できます。

### **Aspose.Cells & ズーム要素**

Aspose.Cells はワークシートのズーム倍率を設定できる機能も提供しています。 [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) クラスは Microsoft Excel ファイルを表します。

ワークシートは [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) クラスで表されます。 [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) クラスはワークシートの管理に役立つ多くのメソッドを提供します。ズーム倍率を設定するには、[SetZoom](https://reference.aspose.com/cells/go-cpp/worksheet/setzoom/) メソッドを使用します。ズーム倍率は、数値（整数）を [SetZoom](https://reference.aspose.com/cells/go-cpp/worksheet/setzoom/) メソッドに割り当てることで設定します。

以下に例を示します。これにより、[SetZoom](https://reference.aspose.com/cells/go-cpp/worksheet/setzoom/) メソッドを使用してExcelファイルの最初のワークシートのズーム倍率を設定できます。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ZoomFactor.go" >}}

## **ウィンドウ枠の固定**

### **Microsoft Excel の使用**

ウィンドウ枠の固定は、Microsoft Excel が提供する機能です。枠を固定すると、ワークシートをスクロールしても表示され続けるデータを選択できます。

### **Aspose.Cells & ウィンドウ枠の固定**

Aspose.Cellsは、実行時にシートにフリーズペインを適用することも可能です。Aspose.Cellsは、Microsoft Excelファイルを表す[Workbook](https://reference.aspose.com/cells/go-cpp/workbook/)クラスを提供します。 [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/)クラスには、各Excelファイル内のワークシートにアクセスできる[Worksheets](https://reference.aspose.com/cells/go-cpp/worksheetcollection/)コレクションが含まれています。

ワークシートは、[Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/)クラスによって表されます。[Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/)クラスは、ワークシート管理用のさまざまなメソッドを提供します。フリーズペインを設定するには、[Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/)クラスの[FreezePanes](https://reference.aspose.com/cells/go-cpp/worksheet/freezepanes_int_int_int_int/)メソッドを呼び出します。[FreezePanes](https://reference.aspose.com/cells/go-cpp/worksheet/freezepanes_int_int_int_int/)メソッドは、次のパラメータを取ります。

- **行**、枠が開始するセルの行インデックス。
- **列**、枠が開始するセルの列インデックス。
- **固定行**、上部枠内に表示される行数。
- **固定列**、左部枠内に表示される列数。

以下に、[FreezePanes](https://reference.aspose.com/cells/go-cpp/worksheet/freezepanes_int_int_int_int/)メソッドを使用して、Excelファイルの最初のワークシートの行と列（C4から開始、4行目と3列目、行と列は0から始まる）を固定する方法を示した完全な例を示します。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FreezePanes.go" >}}

## **画面の分割**

ワークシート内で二つの異なるビューを取得するには、画面を分割する必要があります。Microsoft Excel は、ワークシートのコピーを複数表示し、各パネで独立してスクロールできる非常に便利な機能を提供しています：画面の分割。

パネは同時に動作します。片方で変更を加えると、同時に他方にも変更が表示されます。Aspose.Cells は、ユーザーに対して画面の分割機能を提供しています。

### **画面の分割の適用と解除**

#### **画面の分割**

Aspose.Cellsは、Microsoft Excelファイルを表す[Workbook](https://reference.aspose.com/cells/go-cpp/workbook/)クラスを提供します。[Workbook](https://reference.aspose.com/cells/go-cpp/workbook/)クラスは、Excelファイルの管理に関するさまざまなメソッドを提供します。スプリットビューを実装するには、[Split](https://reference.aspose.com/cells/go-cpp/worksheet/split/)メソッドを使用します。分割ペインを解除するには、[RemoveSplit](https://reference.aspose.com/cells/go-cpp/worksheet/removesplit/)メソッドを使用します。

例では、シンプルなテンプレート ファイルをロードして、最初のワークシートのセルに分割パネル機能を適用し、更新されたファイルを保存します。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SplitPanes.go" >}}

#### **パネルの削除**

[RemoveSplit](https://reference.aspose.com/cells/go-cpp/worksheet/removesplit/)メソッドを使って分割ペインを削除します。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RemovingPanes.go" >}}
