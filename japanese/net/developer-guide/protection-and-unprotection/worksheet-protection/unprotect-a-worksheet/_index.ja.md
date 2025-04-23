---
title: ワークシートの保護解除
type: docs
weight: 20
url: /ja/net/unprotect-a-worksheet/
---

{{% alert color="primary" %}}

開発者が保護されたワークシートから保護を解除してファイルに変更を加える必要がある場合は？ Aspose.Cells を使用して簡単に行うことができます。

{{% /alert %}}

## **ワークシートの保護を解除する**

### **Microsoft Excel の使用**

ワークシートから保護を解除するには：

**ツール** メニューから **保護** を選択し、その後 **シートの保護解除** を選択します。 ワークシートがパスワードで保護されていない限り、保護は解除されます。 その場合、パスワードの入力を求めるダイアログが表示されます。 パスワードを入力すると、ワークシートが保護解除されます。

### **Aspose.Cells を使用して単純に保護されたワークシートの保護解除**

ワークシートは [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) クラスの [**Unprotect**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/unprotect/index) メソッドを呼び出すことで保護解除できます。
単純に保護されたワークシートはパスワードで保護されていないワークシートです。 そのようなワークシートはパラメータを渡さずに [**Unprotect**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/unprotect/index) メソッドを呼び出すことで保護解除できます。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Unprotect-UnprotectingSimplyProtectedWorksheet-1.cs" >}}

### **Aspose.Cells を使用してパスワードで保護されたワークシートの保護解除**

パスワードで保護されたワークシートとは、パスワードで保護されたワークシートのことです。 そのようなワークシートは、パスワードをパラメータとして取る [**Unprotect**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/unprotect/methods/1) メソッドのオーバーロードバージョンを呼び出すことで保護解除できます。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Unprotect-UnprotectingPasswordProtectedWorksheet-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
