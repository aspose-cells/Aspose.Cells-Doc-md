---
title: 行の高さと列の幅の調整
type: docs
weight: 10
url: /ja/java/adjusting-row-height-and-column-width/
---
{{% alert color="primary" %}} 

スプレッドシートを操作して行または列にデータを追加する場合、行の高さまたは列の幅を変更する必要がある場合があります。行または列に書式設定を適用すると、データを表示するために現在の高さまたは幅を変更する必要がある場合があります。通常、ユーザーは Microsoft Excel を使用して WYSIWYG 環境で行の高さと列の幅を調整します。ただし、Aspose.Cells を使用すると、開発者は実行時にこれらの操作を実行できます。行と列のインデックスは 0 から始まります。

{{% /alert %}} 
## **行の操作**
### **行の高さを調整する**
Aspose.Cells はクラスを提供し、[ワークブック](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)、Microsoft Excel ファイルを表します。の[ワークブック](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)クラスには[ワークシート コレクション](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)これにより、Excel ファイル内の各ワークシートにアクセスできます。ワークシートは、[ワークシート](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)クラス。の[ワークシート](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)クラスは[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)ワークシート内のすべてのセルを表すコレクション。

の[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)コレクションには、ワークシートの行または列を管理するためのメソッドがいくつか用意されています。これらのいくつかについては、以下で詳しく説明します。
### **行の高さの設定**
を呼び出して、単一の行の高さを設定することができます。[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)コレクションの[setRowHeight](https://reference.aspose.com/cells/java/com.aspose.cells/cells#setRowHeight\(int,%20double\)） 方法。の[setRowHeight](https://reference.aspose.com/cells/java/com.aspose.cells/cells#setRowHeight\(int,%20double\)メソッドは、次のパラメーターを取ります。

- **行インデックス**、高さを変更する行のインデックス。
- **行の高さ**、行に適用する行の高さ。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-SettingHeightOfRow-SettingHeightOfRow.java" >}}
### **すべての行の高さを設定する**
ワークシートのすべての行に同じ行の高さを設定するには、[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)コレクションの[setStandardHeight](https://reference.aspose.com/cells/java/com.aspose.cells/cells#StandardHeight)方法。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-SettingHeightAllRows-SettingHeightAllRows.java" >}}
## **列の操作**
### **列の幅の設定**
を呼び出して、列の幅を設定します。[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)コレクションの[setColumnWidth](https://reference.aspose.com/cells/java/com.aspose.cells/cells#setColumnWidth\(int,%20double\)） 方法。の[setColumnWidth](https://reference.aspose.com/cells/java/com.aspose.cells/cells#setColumnWidth\(int,%20double\)メソッドは、次のパラメーターを取ります。

- **列インデックス**、幅を変更する列のインデックス。
- **列幅**、目的の列幅。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-SettingWidthOfColumn-SettingWidthOfColumn.java" >}}
### **すべての列の幅の設定**
ワークシートのすべての列に同じ列幅を設定するには、[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)コレクションの[setStandardWidth](https://reference.aspose.com/cells/java/com.aspose.cells/cells#StandardWidth)方法。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-SettingWidthOfAllColumns-SettingWidthOfAllColumns.java" >}}
