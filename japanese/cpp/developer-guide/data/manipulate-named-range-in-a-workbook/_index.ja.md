---
title: ワークブックで名前付き範囲を操作する
type: docs
weight: 90
url: /ja/cpp/manipulate-named-range-in-a-workbook/
---
## **考えられる使用シナリオ**
Aspose.Cells は、既存の名前付き範囲の操作をサポートしています。すべての既存の名前付き範囲にアクセスできます[IWorkbook.GetIWorksheets().GetINames()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection#aa9e7bc07917a152a2c0de161cca133fa)コレクション。名前付き範囲にアクセスすると、さまざまなメソッドを変更できます。[GetFullText](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_name#a5b450ef193365dec035c58280fbe9563)と[GetRefersTo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_name#afdb10a12d8d395ae81de231f017eba36).
## **ワークブックで名前付き範囲を操作する**
次のサンプル コードは、内部の最初の名前付き範囲を読み取ります。[ソースエクセルファイル](23167008.xlsx)そしてそれを印刷します[全文](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_name#a5b450ef193365dec035c58280fbe9563)と[参照先](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_name#afdb10a12d8d395ae81de231f017eba36)コンソールのプロパティ。その後、`RefersTo` プロパティを変更して保存します。[出力エクセルファイル](23167009.xlsx).
## **サンプルコード**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-ManipulateNamedRangeInWorkbook.cpp" >}}
## **コンソール出力**
次のコンソール出力は、[全文](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_name#a5b450ef193365dec035c58280fbe9563)と[参照先](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_name#afdb10a12d8d395ae81de231f017eba36)既存のメンバー*名前付き範囲*上記のコードで。

{{< highlight "java" >}}

 Full Text: TestRange

Refers To: =Sheet1!$D$3:$G$6

{{< /highlight >}}
