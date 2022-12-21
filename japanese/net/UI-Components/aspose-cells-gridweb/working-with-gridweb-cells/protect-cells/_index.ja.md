---
title: プロテクト Cells
type: docs
weight: 50
url: /ja/net/protect-cells/
---
{{% alert color="primary" %}} 

このトピックでは、セルを保護するためのいくつかの手法について説明します。これらの手法を使用すると、開発者は、ユーザーがワークシート内のすべてのセルまたは選択したセル範囲を編集することを制限できます。

{{% /alert %}} 
## **保護中 Cells**
 Aspose.Cells.GridWeb は、コントロールがセルにあるときにセルの保護レベルを制御するためのいくつかの異なる手法を提供します。[編集モード](/cells/ja/net/enable-different-gridweb-modes/#edit-mode)(デフォルトモード)。これにより、セルがエンド ユーザーによって変更されないように保護されます。
### **Cells をすべて読み取り専用にする**
ワークシート内のすべてのセルを読み取り専用に設定するには、ワークシートの SetAllCellsReadonly メソッドを呼び出します。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ProtectCells.aspx-MakeAllCellsReadOnly.cs" >}}
### **すべての Cells を編集可能にする**
すべてのセルの保護を解除するには、ワークシートの SetAllCellsEditable メソッドを呼び出します。このメソッドは、SetAllCellsReadonly メソッドとは逆の効果があります。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ProtectCells.aspx-MakeAllCellsEditable.cs" >}}
### **選択した Cells を読み取り専用にする**
セルの範囲のみを保護するには:

1. まず、SetAllCellsEditable メソッドを呼び出して、すべてのセルを編集可能にします。
1. ワークシートの SetReadonlyRange メソッドを呼び出して、保護するセルの範囲を指定します。このメソッドは、セルの範囲を指定するために行と列の数を取ります。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ProtectCells.aspx-MakeSelectedCellsReadOnly.cs" >}}
### **選択した Cells を編集可能にする**
セル範囲の保護を解除するには:

1. SetAllCellsReadonly メソッドを呼び出して、すべてのセルを読み取り専用にします。
1. ワークシートの SetEditableRange メソッドを呼び出して、編集可能にするセルの範囲を指定します。このメソッドは、セルの範囲を指定するために行と列の数を取ります。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ProtectCells.aspx-MakeSelectedCellsEditable.cs" >}}
