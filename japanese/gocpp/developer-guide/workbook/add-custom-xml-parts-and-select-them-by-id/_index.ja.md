---
title: GolangとC++を使ってカスタムXMLパーツを追加し、IDで選択する
linktitle: カスタムXMLパーツの追加およびIDでの選択
type: docs
weight: 70
url: /ja/go-cpp/add-custom-xml-parts-and-select-them-by-id/
description: Aspose.CellsとGolangを使ってExcelファイルにカスタムXMLパーツを追加し、選択する方法
---

## **可能な使用シナリオ**

カスタムXMLパーツは、Microsoft Excelドキュメント内部に格納されたXMLデータであり、それらと連携するアプリケーションによって利用されます。現時点では、Microsoft ExcelのUIを使って直接追加する方法はありません。ただし、VSTOやAspose.Cellsを使用してプログラム的に追加できます。[**Workbook.CustomXmlParts.Add()**](https://reference.aspose.com/cells/go-cpp/customxmlpartcollection/add/)メソッドを使用してAspose.Cells APIでカスタムXMLパーツを追加し、[**CustomXmlPart.GetID()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpart/getid/)プロパティでIDを設定できます。IDで選択したい場合は、[**Workbook.CustomXmlParts.SelectByID()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpartcollection/selectbyid/)メソッドを使用します。

## **カスタムXMLパーツの追加およびIDでの選択**

以下のサンプルコードは、まず[**Workbook.CustomXmlParts.Add()**](https://reference.aspose.com/cells/go-cpp/customxmlpartcollection/add/)メソッドを使って4つのカスタムXMLパーツを追加し、その後[**CustomXmlPart.GetID()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpart/getid/)プロパティを使ってIDを設定します。最後に、[**Workbook.CustomXmlParts.SelectByID()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpartcollection/selectbyid/)メソッドを使用して追加したカスタムXMLパーツの1つを検索または選択します。コードのコンソール出力も参考にしてください。

## **サンプルコード**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AddCustomXmlPartsAndSelectThemById.go" >}}
## **コンソール出力**

{{< highlight java >}}
Found: CustomXmlPart ID Sport
{{< /highlight >}}
