---
title: ワークブックに名前付き範囲を作成する
type: docs
weight: 60
url: /ja/cpp/create-named-range-in-a-workbook/
---
## **考えられる使用シナリオ**
Aspose.Cells は、名前付き範囲の作成をサポートしています。名前付き範囲を作成するには、さまざまな方法があります。最も簡単な方法の 1 つは、最初に作成することです。[IRange](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_range)オブジェクトを作成し、次を使用してその名前を設定します[IRange.SetName()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_range#a78480b6b6db0f24cffc8acc2b06552eb)方法。 Microsoft Excel を介して、Excel ファイル内のすべての名前付き範囲を表示できます。*ネームマネージャー*インターフェース。
## **ワークブックに名前付き範囲を作成する**
次のサンプル コードは、*名前付き範囲*Aspose.Cells経由。一度、*名前付き範囲*が作成され、[IWorkbook.GetIWorksheets().GetINames()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection#aa9e7bc07917a152a2c0de161cca133fa)コレクション。をご覧ください[出力エクセルファイル](23167006.xlsx)参照用のコードによって生成されます。
## **サンプルコード**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-CreateNamedRangeInWorkbook.cpp" >}}
## **コンソール出力**
次のコンソール出力は、[GetFullText](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_name#a5b450ef193365dec035c58280fbe9563)および作成された `GetRefersTo` メソッド*名前付き範囲*上記のコードで。

{{< highlight "java" >}}

 Full Text: MyNamedRange

Refers To: =Sheet1!$A$5:$C$10

{{< /highlight >}}
