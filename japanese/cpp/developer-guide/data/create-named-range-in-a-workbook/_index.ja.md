---
title: ワークブックに名前付き範囲を作成する
type: docs
weight: 60
url: /ja/cpp/create-named-range-in-a-workbook/
---
##  **考えられる使用シナリオ**
Aspose.Cells は名前付き範囲の作成をサポートしています。名前付き範囲を作成するにはさまざまな方法があります。最も簡単な方法の 1 つは、最初に作成することです。[範囲](https://reference.aspose.com/cells/cpp/aspose.cells/range)オブジェクトを作成し、次を使用してその名前を設定します[Range.SetName()](https://reference.aspose.com/cells/cpp/aspose.cells/range/setname)方法。 Microsoft Excel を使用すると、Excel ファイル内のすべての名前付き範囲を確認できます。*ネームマネージャー*インターフェース。
##  **ワークブックに名前付き範囲を作成する**
次のサンプル コードは、*名前付き範囲*Aspose.Cells経由。*名前付き範囲*が作成されると、内部に表示されます[Workbook.GetWorksheets().GetNames()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/getnames)コレクション。をご覧ください。[Excelファイルを出力する](23167006.xlsx)参照用のコードによって生成されます。
##  **サンプルコード**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-CreateNamedRangeInWorkbook-new.cpp" >}}
##  **コンソール出力**
次のコンソール出力は、次の値を出力します。[フルテキストの取得](https://reference.aspose.com/cells/cpp/aspose.cells/name/getfulltext/)そして[GetRefersTo](https://reference.aspose.com/cells/cpp/aspose.cells/name/getrefersto/)作成されたメソッド*名前付き範囲*上記のコードでは。

{{< highlight "java" >}}

 Full Text: MyNamedRange

Refers To: =Sheet1!$A$5:$C$10

{{< /highlight >}}
