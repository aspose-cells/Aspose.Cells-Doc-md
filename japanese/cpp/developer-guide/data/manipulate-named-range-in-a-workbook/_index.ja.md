---
title: ワークブック内の名前付き範囲を操作する
type: docs
weight: 90
url: /ja/cpp/manipulate-named-range-in-a-workbook/
---
##  **考えられる使用シナリオ**
Aspose.Cells は、既存の名前付き範囲の操作をサポートしています。既存のすべての名前付き範囲には、次からアクセスできます。[Workbook.GetWorksheets().GetNames()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/getnames/)コレクション。名前付き範囲にアクセスすると、そのさまざまなメソッドを変更できます。[フルテキストの取得](https://reference.aspose.com/cells/cpp/aspose.cells/name/getfulltext/)そして[GetRefersTo](https://reference.aspose.com/cells/cpp/aspose.cells/name/getrefersto/).
##  **ワークブック内の名前付き範囲を操作する**
次のサンプル コードは、[ソースエクセルファイル](23167008.xlsx)そしてそれを印刷します[全文](https://reference.aspose.com/cells/cpp/aspose.cells/name/getfulltext/)そして[参照先](https://reference.aspose.com/cells/cpp/aspose.cells/name/getrefersto/)コンソール上のプロパティ。その後、`RefersTo` プロパティを変更し、[Excelファイルを出力する](23167009.xlsx).
##  **サンプルコード**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-ManipulateNamedRangeInWorkbook-new.cpp" >}}
##  **コンソール出力**
次のコンソール出力は、次の値を出力します。[全文](https://reference.aspose.com/cells/cpp/aspose.cells/name/getfulltext/)そして[参照先](https://reference.aspose.com/cells/cpp/aspose.cells/name/getrefersto/)既存のメンバー*名前付き範囲*上記のコードでは。

{{< highlight "java" >}}

 Full Text: TestRange

Refers To: =Sheet1!$D$3:$G$6

{{< /highlight >}}
