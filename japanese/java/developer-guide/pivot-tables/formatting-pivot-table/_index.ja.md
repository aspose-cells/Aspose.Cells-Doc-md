---
title: ピボット テーブルの書式設定
type: docs
weight: 60
url: /ja/java/formatting-pivot-table/
---
## **ピボット テーブルの外観**

[ピボット テーブルを作成する方法](/cells/ja/java/create-pivot-table/)簡単なピボット テーブルの作成方法を示しました。この記事ではさらに詳しく、プロパティを設定してピボット テーブルの外観をカスタマイズする方法について説明します。

### **ピボット テーブル形式オプションの設定**

の[**ピボットテーブル**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable)クラスを使用すると、ピボット テーブルのさまざまな書式設定オプションを設定できます。

#### **AutoFormat および PivotTableStyle タイプの設定**

次のコード例は、[**AutoFormatType**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#AutoFormatType)と[**ピボットテーブルのスタイル タイプ**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#PivotTableStyleType)プロパティ。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-SetAutoFormatandPivotTableStyleTypes-SetAutoFormatandPivotTableStyleTypes.java" >}}

#### **フォーマット オプションの設定**

次のコード サンプルは、行と列の総計の追加など、ピボット テーブル レポートのさまざまな書式設定オプションを設定する方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-SettingFormatOptions-SettingFormatOptions.java" >}}

### **ピボットフィールドのフォーマット オプションの設定**

Aspose.Cells for Java では、ピボット テーブル全体の書式設定を制御するだけでなく、行フィールド、列フィールド、およびページ フィールドの書式設定を微調整できます。

#### **行、列、およびページ フィールドのフォーマットの設定**

次のコード例は、行フィールドにアクセスする方法、特定の行にアクセスする方法、小計を設定する方法、自動並べ替えを適用する方法、および autoShow オプションを使用する方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-SetRowColumnPageFieldsFormat-SetRowColumnPageFieldsFormat.java" >}}

### **データ フィールド形式の設定**

次のコード行は、データ フィールドをフォーマットする方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-SettingDataFieldFormat-SettingDataFieldFormat.java" >}}

### **ピボット テーブルのクイック スタイルを変更する**

次のコード例は、ピボット テーブルに適用されるクイック スタイルを変更する方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-ModifyPivotTableQuickStyle-ModifyPivotTableQuickStyle.java" >}}

### **ピボット フィールドのクリア**

[**ピボットフィールド コレクション**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotFieldCollection)という名前のメソッドがあります[**クリア（）**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotfieldcollection#clear()ピボット フィールドをクリアします。ページ、列、行、データなど、すべての領域のピボット フィールドをクリアするために使用します。
次のコード サンプルは、データ領域のすべてのピボット フィールドをクリアする方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-ClearPivotFields-ClearPivotFields.java" >}}

## **連結機能**

### **ConsolidationFunction をピボット テーブルのデータ フィールドに適用する**

 Aspose.Cells を使用して、ConsolidationFunction をピボット テーブルのデータ フィールド (または値フィールド) に適用できます。 Microsoft Excel では、値フィールドを右クリックして、**値フィールドの設定...**オプションを選択し、タブを選択します**値の集計基準**.そこから、Sum、Count、Average、Max、Min、Product、Distinct Count などの任意の ConsolidationFunction を選択できます。

Aspose.Cells提供[**連結機能**](https://reference.aspose.com/cells/java/com.aspose.cells/ConsolidationFunction)次の連結関数をサポートするための列挙。

- [**ConsolidationFunction.AVERAGE**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#AVERAGE)
- [**ConsolidationFunction.COUNT**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#COUNT)
- [**ConsolidationFunction.COUNT_NUMS**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#COUNT_NUMS)
- [**ConsolidationFunction.DISTINCT_COUNT**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#DISTINCT_COUNT)
- [**ConsolidationFunction.MAX**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#MAX)
- [**ConsolidationFunction.MIN**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#MIN)
- [**ConsolidationFunction.PRODUCT**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#PRODUCT)
- [**ConsolidationFunction.STD_DEV**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#STD_DEV)
- [**ConsolidationFunction.STD_DEVP**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#STD_DEVP)
- [**ConsolidationFunction.SUM**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#SUM)
- [**ConsolidationFunction.VAR**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#VAR)
- [**ConsolidationFunction.VARP**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#VARP)

次のコードが適用されます**平均**最初のデータ フィールド (または値フィールド) への連結関数および**DistinctCount** 2 番目のデータ フィールド (または値フィールド) への連結関数。

{{% alert color="primary" %}}

DistinctCount 連結関数は、Microsoft Excel 2013 のみでサポートされています。

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-ConsolidationFunctions-ConsolidationFunctions.java" >}}
