---
title: ワークシートの保護解除
type: docs
weight: 20
url: /ja/python-net/unprotect-a-worksheet/
---

{{% alert color="primary" %}}

保護されたワークシートの保護をランタイムで解除し、変更を行いたい場合はどうすればよいですか？これはAspose.Cells for Python via .NETで簡単に実現できます。

{{% /alert %}}

## **ワークシートの保護を解除する**

### **Microsoft Excel の使用**

ワークシートから保護を解除するには：

**ツール** メニューから **保護** を選択し、その後 **シートの保護解除** を選択します。 ワークシートがパスワードで保護されていない限り、保護は解除されます。 その場合、パスワードの入力を求めるダイアログが表示されます。 パスワードを入力すると、ワークシートが保護解除されます。

### **Aspose.Cells for Python via .NETを使った保護解除の方法**

ワークシートは [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) クラスの [**unprotect**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/unprotect) メソッドを呼び出すことで保護解除できます。
単純に保護されたワークシートはパスワードで保護されていないワークシートです。 そのようなワークシートはパラメータを渡さずに [**unprotect**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/unprotect) メソッドを呼び出すことで保護解除できます。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-UnprotectingSimplyProtectedWorksheet-1.py" >}}

### **Aspose.Cells for Python via .NETを使用してパスワード保護されたワークシートの保護解除方法**

パスワードで保護されたワークシートとは、パスワードで保護されたワークシートのことです。 そのようなワークシートは、パスワードをパラメータとして取る [**unprotect**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/unprotect/) メソッドのオーバーロードバージョンを呼び出すことで保護解除できます。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-UnprotectingPasswordProtectedWorksheet-1.py" >}}

