---
title: PivotTableのPivotFieldのDisplayNameによってCellオブジェクトを取得する
type: docs
weight: 310
url: /ja/java/get-the-cell-object-by-displayname-of-pivotfield-of-pivottable/
---

{{% alert color="primary" %}} 

Aspose.Cellsは、[PivotTable.getCellByDisplayName()](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#getCellByDisplayName\(java.lang.String\))メソッドを提供し、ピボットテーブルの表示名によるセルオブジェクトへのアクセスに使用できます。このメソッドは、ピボットフィールドヘッダーを強調表示または書式設定する場合に有用です。この記事では、データフィールドの表示名によるセルオブジェクトの取得とその後の書式設定方法を説明しています。

{{% /alert %}} 
## **PivotTableのPivotFieldのDisplayNameによってCellオブジェクトを取得する**
次のコードは、ワークシートの最初のピボットテーブルにアクセスし、その後、ピボットテーブルの2番目のデータフィールドの表示名でセルを取得します。次に、セルの塗りつぶし色とフォントの色をそれぞれ水色と黒に変更します。以下のスクリーンショットは、コードの実行前と実行後のピボットテーブルの外観を示しています。
### **ピボットテーブル - 実行前**
![todo:image_alt_text](get-the-cell-object-by-displayname-of-pivotfield-of-pivottable_1.png)
### **ピボットテーブル - 実行後**
![todo:image_alt_text](get-the-cell-object-by-displayname-of-pivotfield-of-pivottable_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetCellObject-GetCellObject.java" >}}






