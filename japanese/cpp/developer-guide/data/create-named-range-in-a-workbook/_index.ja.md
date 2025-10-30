---
title: ブック内の名前付き範囲を作成
type: docs
weight: 60
url: /ja/cpp/create-named-range-in-a-workbook/
---

## **可能な使用シナリオ**
Aspose.Cells は名前付き範囲の作成をサポートしています。名前付き範囲を作成する方法はさまざまあります。最も簡単な方法の1つはまず [Range](https://reference.aspose.com/cells/cpp/aspose.cells/range) オブジェクトを作成し、その後 [Range.SetName()](https://reference.aspose.com/cells/cpp/aspose.cells/range/setname) メソッドを使用してその名前を設定することです。Microsoft Excel の *名前の管理* インターフェースを通じてエクセルファイル内のすべての名前付き範囲を表示できます。
## **ブック内で名前付き範囲を作成する**
以下のサンプルコードでは、Aspose.Cells を使用して *名前付き範囲* を作成する方法を説明しています。一度名前付き範囲が作成されると、[Workbook.GetWorksheets().GetNames()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/getnames) コレクション内で見えるようになります。コードによって生成された [出力エクセルファイル](23167006.xlsx) を参照してください。
## **サンプルコード**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-CreateNamedRangeInWorkbook-new.cpp" >}}
## **コンソール出力**
以下のコンソール出力は、上記のコードで作成された *名前付き範囲* の [GetFullText](https://reference.aspose.com/cells/cpp/aspose.cells/name/getfulltext/) および [GetRefersTo](https://reference.aspose.com/cells/cpp/aspose.cells/name/getrefersto/) メソッドの値を出力します。

{{< highlight java >}}

 Full Text: MyNamedRange

Refers To: =Sheet1!$A$5:$C$10

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
