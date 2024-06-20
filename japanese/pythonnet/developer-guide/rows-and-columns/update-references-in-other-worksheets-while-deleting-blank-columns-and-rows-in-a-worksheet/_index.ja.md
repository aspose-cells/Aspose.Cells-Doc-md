---
title: ワークシート内の空白の列と行を削除する際に、他のワークシートの参照を更新する
type: docs
weight: 5000
url: /ja/python-net/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/
description: この記事では、Aspose.Cells for Python via .NET APIを使用してワークシートの空白の列と行を削除しながら他のワークシート内の参照を更新する方法が紹介されています。
keywords: Python Excelライブラリ、Pythonでワークシートの空白の列と行を削除する際の他のワークシート内の参照の更新、Pythonでワークシートの空白の列と行を削除する際の参照の更新。
---

{{% alert color="primary" %}}

ワークシート内の空白の列と行を削除すると、他のワークシートでの参照が無効になります。この動作を回避し、他のワークシートでの現在のワークシートの参照も更新されるようにするには、[**DeleteOptions.update_reference**](https://reference.aspose.com/cells/python-net/aspose.cells/deleteoptions/update_reference/)プロパティを使用して**true**に設定してください。

{{% /alert %}}

## **ワークシート内の空白の列と行を削除する際に、他のワークシートの参照を更新する**

次に示すサンプルコードとそのコンソール出力を参照してください。 2番目のワークシートのセルE3には、最初のワークシートのセルC3を参照する=Sheet1!C3という式があります。 [**DeleteOptions.update_reference**](https://reference.aspose.com/cells/python-net/aspose.cells/deleteoptions/update_reference/)プロパティを**true**に設定すると、この式が更新され=Sheet1!A1になります。ただし、[**DeleteOptions.update_reference**](https://reference.aspose.com/cells/python-net/aspose.cells/deleteoptions/update_reference/)プロパティを**false**に設定すると、2番目のワークシートのセルE3の式は=Sheet1!C3のままで無効になります。

### **プログラミングサンプル**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-UpdateReferenceInWorksheets.py" >}}

### **コンソール出力**

上記のサンプルコードの[**DeleteOptions.update_reference**](https://reference.aspose.com/cells/python-net/aspose.cells/deleteoptions/update_reference/)プロパティが**true**に設定された場合のコンソール出力です。

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

上記のサンプルコードの[**DeleteOptions.update_reference**](https://reference.aspose.com/cells/python-net/aspose.cells/deleteoptions/update_reference/)プロパティが**false**に設定された場合のコンソール出力です。2番目のワークシートのセルE3の式が更新されず、セルの値は4から0になっています。

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
