---
title: ブック内の名前付き範囲の操作
type: docs
weight: 90
url: /ja/cpp/manipulate-named-range-in-a-workbook/
---

## **可能な使用シナリオ**
Aspose.Cells は既存の名前付き範囲の操作をサポートしています。すべての既存の名前付き範囲には [Workbook.GetWorksheets().GetNames()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/getnames/) コレクションからアクセスできます。名前付き範囲にアクセスしたら、 [GetFullText](https://reference.aspose.com/cells/cpp/aspose.cells/name/getfulltext/) および [GetRefersTo](https://reference.aspose.com/cells/cpp/aspose.cells/name/getrefersto/) などのさまざまなメソッドを変更することができます。
## **ブック内の名前付き範囲の操作**
以下のサンプルコードでは、[ソースエクセルファイル](23167008.xlsx) 内の最初の名前付き範囲を読み込み、その [FullText](https://reference.aspose.com/cells/cpp/aspose.cells/name/getfulltext/) および [RefersTo](https://reference.aspose.com/cells/cpp/aspose.cells/name/getrefersto/) プロパティをコンソールに出力します。その後、`RefersTo` プロパティを変更し、 [出力エクセルファイル](23167009.xlsx) を保存します。
## **サンプルコード**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-ManipulateNamedRangeInWorkbook-new.cpp" >}}
## **コンソール出力**
次のコンソール出力は、上記のコード内の既存の*Named Range*の[FullText](https://reference.aspose.com/cells/cpp/aspose.cells/name/getfulltext/) と [RefersTo](https://reference.aspose.com/cells/cpp/aspose.cells/name/getrefersto/) メンバーの値を出力します。

{{< highlight java >}}

 Full Text: TestRange

Refers To: =Sheet1!$D$3:$G$6

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
