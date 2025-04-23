---
title: ワークシート内の空白の列と行を削除する際に、他のワークシートの参照を更新する
type: docs
weight: 700
url: /ja/java/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/
---

{{% alert color="primary" %}} 

ワークシート内の空白の列と行を削除すると、他のワークシートでのその参照が無効になります。この動作を回避し、それらの参照も更新したい場合は、[DeleteOptions.UpdateReference](https://reference.aspose.com/cells/java/com.aspose.cells/deleteoptions#UpdateReference) を **true** に設定してください。

{{% /alert %}} 
## **ワークシート内の空白の列と行を削除する際に、他のワークシートの参照を更新する**
次のサンプルコードとそのコンソール出力をご覧ください。第2のワークシートのセルE3には、第1のワークシートのセルC3を参照する式 =Sheet1!C3 があります。空白の列と行を第1のワークシートから削除すると、[DeleteOptions.UpdateReference](https://reference.aspose.com/cells/java/com.aspose.cells/deleteoptions#UpdateReference) プロパティを **true** に設定すると、この式は更新されて =Sheet1!A1 になります。ただし、[DeleteOptions.UpdateReference](https://reference.aspose.com/cells/java/com.aspose.cells/deleteoptions#UpdateReference) プロパティを **false** に設定すると、第2のワークシートのセルE3の式は =Sheet1!C3 のままで無効になります。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-management-Updatereferencesinotherworksheetswhiledeletingblankcolumnsandrowsinworksheet-1.java" >}}
## **コンソール出力**
[DeleteOptions.UpdateReference](https://reference.aspose.com/cells/java/com.aspose.cells/deleteoptions#UpdateReference) プロパティが **true** に設定された場合の上記サンプルコードのコンソール出力です。

{{< highlight java >}}

 Cell E3 before deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!C1

Cell Value: 4


Cell E3 after deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!A1

Cell Value: 4

{{< /highlight >}}

[DeleteOptions.UpdateReference](https://reference.aspose.com/cells/java/com.aspose.cells/deleteoptions#UpdateReference) プロパティが **false** に設定された場合の上記サンプルコードのコンソール出力です。第2のワークシートのセルE3の式が更新されず、セルの値は4から0になっています。

{{< highlight java >}}

 Cell E3 before deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!C1

Cell Value: 4


Cell E3 after deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!C1

Cell Value: 0

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
