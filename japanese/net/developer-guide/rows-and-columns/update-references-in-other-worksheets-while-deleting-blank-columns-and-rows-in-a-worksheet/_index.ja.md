---
title: ワークシート内の空白の列と行を削除する際に、他のワークシートの参照を更新する
type: docs
weight: 5000
url: /ja/net/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/
---

{{% alert color="primary" %}}

ワークシート内の空白の列と行を削除すると、他のワークシートでの参照が無効になります。この動作を回避し、他のワークシートでの現在のワークシートの参照も更新されるようにするには、[**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference)プロパティを使用して**true**に設定してください。

{{% /alert %}}

## **ワークシート内の空白の列と行を削除する際に、他のワークシートの参照を更新する**

次に示すサンプルコードとそのコンソール出力を参照してください。 2番目のワークシートのセルE3には、最初のワークシートのセルC3を参照する=Sheet1!C3という式があります。 [**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference)プロパティを**true**に設定すると、この式が更新され=Sheet1!A1になります。ただし、[**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference)プロパティを**false**に設定すると、2番目のワークシートのセルE3の式は=Sheet1!C3のままで無効になります。

### **プログラミングサンプル**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UpdateReferenceInWorksheets-UpdateReferenceInWorksheets.cs" >}}

### **コンソール出力**

上記のサンプルコードの[**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference)プロパティが**true**に設定された場合のコンソール出力です。

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

上記のサンプルコードの[**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference)プロパティが**false**に設定された場合のコンソール出力です。2番目のワークシートのセルE3の式が更新されず、セルの値は4から0になっています。

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
{{< app/cells/assistant language="csharp" >}}
