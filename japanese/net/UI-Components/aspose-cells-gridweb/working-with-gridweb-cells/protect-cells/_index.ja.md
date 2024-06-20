---
title: セルの保護
type: docs
weight: 50
url: /ja/net/aspose-cells-gridweb/protect-cells/
keywords: GridWeb,protect,readonly,editable
description: この記事では、GridWeb でセルを保護する方法について紹介します。
---

{{% alert color="primary" %}} 

このトピックでは、セルを保護するためのいくつかのテクニックについて説明します。これらのテクニックを使用することで、ワークシート内のすべてまたは選択したセル範囲の編集をユーザーに制限することができます。

{{% /alert %}} 
## **セルの保護**
Aspose.Cells.GridWeb は、コントロールが [編集モード](/cells/ja/net/aspose-cells-gridweb/enable-different-gridweb-modes/#edit-mode) (デフォルトモード) にある場合に、セルの保護レベルを制御するためのいくつかの異なる技術を提供しています。これにより、エンドユーザーによるセルの変更を防ぐことができます。
### **すべてのセルを読み取り専用にする**
ワークシートのすべてのセルを読み取り専用に設定するには、ワークシートのSetAllCellsReadonlyメソッドを呼び出します。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ProtectCells.aspx-MakeAllCellsReadOnly.cs" >}}
### **すべてのセルを編集可能にする**
すべてのセルの保護を解除するには、ワークシートのSetAllCellsEditableメソッドを呼び出します。このメソッドは、SetAllCellsReadonlyメソッドの逆の効果を持ちます。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ProtectCells.aspx-MakeAllCellsEditable.cs" >}}
### **選択したセルを読み取り専用にする**
特定のセル範囲のみを保護するには:

1. SetAllCellsEditableメソッドを呼び出して、まずすべてのセルを編集可能にします。
1. ワークシートのSetReadonlyRangeメソッドを呼び出して、保護するセルの範囲を指定します。このメソッドは、行数と列数を指定してセルの範囲を取得します。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ProtectCells.aspx-MakeSelectedCellsReadOnly.cs" >}}
### **選択したセルを編集可能にする**
特定のセル範囲の保護を解除するには:

1. SetAllCellsReadonlyメソッドを呼び出して、まずすべてのセルを読み取り専用にします。
1. ワークシートのSetEditableRangeメソッドを呼び出して、編集可能にするセルの範囲を指定します。このメソッドは、行数と列数を指定してセルの範囲を取得します。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ProtectCells.aspx-MakeSelectedCellsEditable.cs" >}}
