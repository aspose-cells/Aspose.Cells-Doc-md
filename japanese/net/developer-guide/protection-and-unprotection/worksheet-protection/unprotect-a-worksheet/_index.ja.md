---
title: ワークシートの保護を解除する
type: docs
weight: 20
url: /ja/net/unprotect-a-worksheet/
---
{{% alert color="primary" %}}

ファイルに変更を加えることができるように、開発者が実行時に保護されたワークシートから保護を削除する必要がある場合は?これは、Aspose.Cells で簡単に実行できます。

{{% /alert %}}

## **ワークシートの保護を解除する**

### **Microsoft エクセルを使う**

ワークシートから保護を解除するには:

から**ツール**メニュー、選択**保護**に続く**シートの保護を解除**.ワークシートがパスワードで保護されていない限り、保護は解除されます。この場合、パスワードの入力を求めるダイアログが表示されます。パスワードを入力すると、ワークシートは保護されなくなります。

### **Aspose.Cells を使用して単純に保護されたワークシートの保護を解除する**

を呼び出すことにより、ワークシートの保護を解除できます。[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラス'[**保護解除**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/unprotect/index)方法。
単純に保護されたワークシートは、パスワードで保護されていないワークシートです。このようなワークシートは、[**保護解除**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/unprotect/index)パラメータを渡さないメソッド。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Unprotect-UnprotectingSimplyProtectedWorksheet-1.cs" >}}

### **Aspose.Cells を使用してパスワードで保護されたワークシートの保護を解除する**

パスワードで保護されたワークシートは、パスワードで保護されたワークシートです。このようなワークシートは、オーバーロードされたバージョンの[**保護解除**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/unprotect/methods/1)パスワードをパラメータとして受け取るメソッド。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Unprotect-UnprotectingPasswordProtectedWorksheet-1.cs" >}}
