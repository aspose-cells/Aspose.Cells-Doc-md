---
title: ワークシートの空白の列と行を削除しながら、他のワークシートの参照を更新する
type: docs
weight: 5000
url: /ja/net/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/
---
{{% alert color="primary" %}}

ワークシートの空白の列と行を削除すると、他のワークシートでの参照が無効になります。この動作を回避し、他のワークシート内の現在のワークシートの参照も更新したい場合は、[**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference)プロパティに設定し、**真実**.

{{% /alert %}}

## **ワークシートの空白の列と行を削除しながら、他のワークシートの参照を更新する**

次のサンプル コードとそのコンソール出力を参照してください。 2 番目のワークシートのセル E3 には、最初のワークシートのセル C3 を参照する数式 =Sheet1!C3 があります。設定する場合[**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference)プロパティとして**真実**、この数式は更新され、最初のワークシートの空白の列と行を削除すると =Sheet1!A1 になります。ただし、設定する場合[**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference)プロパティとして**間違い**、2 番目のワークシートのセル E3 の数式は =Sheet1!C3 のままで無効になります。

### **プログラミングサンプル**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UpdateReferenceInWorksheets-UpdateReferenceInWorksheets.cs" >}}

### **コンソール出力**

これは、上記のサンプル コードのコンソール出力です。[**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference)プロパティは次のように設定されています**真実**.

{{< highlight "java" >}}

 Cell E3 before deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!C1

Cell Value: 4


Cell E3 after deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!A1

Cell Value: 4

{{< /highlight >}}

これは、上記のサンプル コードのコンソール出力です。[**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference)プロパティは次のように設定されています**間違い**.ご覧のとおり、2 番目のワークシートのセル E3 の数式は更新されておらず、そのセル値は無効な 4 ではなく 0 になっています。

{{< highlight "java" >}}

 Cell E3 before deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!C1

Cell Value: 4


Cell E3 after deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!C1

Cell Value: 0

{{< /highlight >}}
