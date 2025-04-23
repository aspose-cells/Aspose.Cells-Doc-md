---
title: ピボットテーブルの書式設定
type: docs
weight: 60
url: /ja/java/formatting-pivot-table/
---

## **ピボットテーブルの外観**

[ピボットテーブルの作成方法](/cells/ja/java/create-pivot-table/) では、単純なピボットテーブルの作成方法を示しました。この記事では、プロパティを設定することでピボットテーブルの外観をカスタマイズする方法についてさらに説明します。

### **ピボットテーブルの書式オプションの設定**

[**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable)クラスを使用すると、ピボットテーブルのさまざまなフォーマットオプションを設定できます。

#### **オートフォーマットとPivotTableStyleのタイプを設定する**

以下のコード例は、[**AutoFormatType**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#AutoFormatType)および[**PivotTableStyleType**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#PivotTableStyleType)プロパティを使用してオートフォーマットタイプとピボットテーブルスタイルタイプを設定する方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-SetAutoFormatandPivotTableStyleTypes-SetAutoFormatandPivotTableStyleTypes.java" >}}

#### **書式オプションの設定**

次のコードサンプルは、行と列の合計を追加するなど、ピボットテーブルレポートの多くのフォーマットオプションを設定する方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-SettingFormatOptions-SettingFormatOptions.java" >}}

### **PivotFieldsのフォーマットオプションを設定する**

全体のピボットテーブルのフォーマットを制御するだけでなく、Aspose.Cells for Javaは行フィールド、列フィールド、ページフィールドのフォーマットを細かく制御できます。

#### **行、列、およびページフィールドのフォーマットを設定する**

以下のコード例では、行フィールドにアクセスし、特定の行にアクセスし、小計を設定し、自動ソートを適用し、autoShowオプションを使用する方法が示されています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-SetRowColumnPageFieldsFormat-SetRowColumnPageFieldsFormat.java" >}}

### **データフィールドのフォーマットを設定する**

以下のコード行は、データフィールドのフォーマット方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-SettingDataFieldFormat-SettingDataFieldFormat.java" >}}

### **ピボットテーブルのクイックスタイルを変更する**

次に続くコード例では、ピボットテーブルに適用されるクイックスタイルを変更する方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-ModifyPivotTableQuickStyle-ModifyPivotTableQuickStyle.java" >}}

### **ピボットフィールドのクリア**

[**PivotFieldCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotFieldCollection)にはピボットフィールドをクリアするための[**clear()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotfieldcollection#clear--)というメソッドがあります。たとえば、ページ、列、行、またはデータなどのすべてのエリアでピボットフィールドをクリアするために使用します。
以下のコードサンプルは、データ領域のすべてのピボットフィールドをクリアする方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-ClearPivotFields-ClearPivotFields.java" >}}

## **集約関数**

### **ピボットテーブルのデータフィールドに統合機能を適用する**

Aspose.Cellsを使用して、ピボットテーブルのデータフィールド（または値フィールド）にConsolidationFunctionを適用できます。Microsoft Excelでは、値フィールドを右クリックし、**値フィールドの設定...**オプションを選択し、次に**集計方法**タブを選択します。そこから、合計、カウント、平均、最大、最小、積、一意のカウントなどのConsolidationFunctionを選択できます。

Aspose.Cellsは、次の統合機能をサポートするための[**ConsolidationFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ConsolidationFunction)列挙型を提供します。

- [**ConsolidationFunction.AVERAGE**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#AVERAGE)
- [**ConsolidationFunction.COUNT**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#COUNT)
- [**ConsolidationFunction.COUNT_NUMS**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#COUNT-NUMS)
- [**ConsolidationFunction.DISTINCT_COUNT**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#DISTINCT-COUNT)
- [**ConsolidationFunction.MAX**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#MAX)
- [**ConsolidationFunction.MIN**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#MIN)
- [**ConsolidationFunction.PRODUCT**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#PRODUCT)
- [**ConsolidationFunction.STD_DEV**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#STD-DEV)
- [**ConsolidationFunction.STD_DEVP**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#STD-DEVP)
- [**ConsolidationFunction.SUM**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#SUM)
- [**ConsolidationFunction.VAR**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#VAR)
- [**ConsolidationFunction.VARP**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#VARP)

次のコードは、最初のデータフィールド（または値フィールド）に**平均**のConsolidationFunctionを適用し、2番目のデータフィールド（または値フィールド）に**DistinctCount**のConsolidationFunctionを適用します。

{{% alert color="primary" %}}

重複排除の統合機能は、Microsoft Excel 2013でのみサポートされています。

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-ConsolidationFunctions-ConsolidationFunctions.java" >}}
{{< app/cells/assistant language="java" >}}
