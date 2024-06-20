---
title: カスタムXMLパーツの追加およびIDでの選択
type: docs
weight: 10
url: /ja/java/add-custom-xml-parts-and-select-them-by-id/
---

## **可能な使用シナリオ**

カスタムXMLパーツは、Microsoft Excelドキュメント内に格納されているXMLデータであり、それらを扱うアプリケーションによって使用されます。現時点ではMicrosoft Excel UIを使用して直接追加する方法はありません。ただし、*VSTO*、*Aspose.Cells*などを使用してプログラムでさまざまな方法で追加できます。Aspose.Cells APIを使用してカスタムXMLパーツを追加する場合は、[**Workbook.getCustomXmlParts().add()**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpartcollection#add(java.lang.Object))メソッドを使用してください。同様に、そのIDを設定する場合は、[**CustomXmlPart.ID**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpart#ID)プロパティを使用します。また、IDでカスタムXMLパーツを選択する場合は、[**Workbook.getCustomXmlParts().selectByID()**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpartcollection#selectByID(java.lang.String))メソッドを使用できます。

## **カスタムXMLパーツの追加およびIDでの選択**

以下のサンプルコードでは、まず[**Workbook.getCustomXmlParts().add()**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpartcollection#add(java.lang.Object))メソッドを使用して4つのカスタムXMLパーツを追加します。次に、それらのIDを[**CustomXmlPart.ID**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpart#ID)プロパティを使用して設定します。最後に、[**Workbook.getCustomXmlParts().selectByID()**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpartcollection#selectByID(java.lang.String))メソッドを使用して追加したカスタムXMLパーツのうち1つを見つけたり選択したりします。以下のコードのコンソール出力も参照してください。

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Workbook-AddCustomXMLPartsAndSelectThemByID.java" >}}

## **コンソール出力**

{{< highlight java >}}

Found: CustomXmlPart ID Sport

{{< /highlight >}}
