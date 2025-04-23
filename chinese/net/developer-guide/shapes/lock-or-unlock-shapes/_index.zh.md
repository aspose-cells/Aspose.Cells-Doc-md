---
title: 锁定或解锁形状
linktitle: 锁定或解锁形状
type: docs
weight: 200
url: /zh/net/lock-or-unlock-shapes/
description: 本文示范了如何使用Aspose.Cells库对形状进行上锁或解锁以保护它们的代码。
keywords: C#锁定形状以保护它们，如何使用C#锁定或解锁形状，保护形状的方法。
---

## **可能的使用场景**

有时，您需要保护工作表中的所有形状，以防止它们被不需要的情况破坏。在这种情况下，您需要锁定指定工作表中的所有形状。 

在电子表格或文档中锁定形状可能有多种好处：
1. 防止意外更改：锁定形状可确保用户不小心移动、调整大小或删除它们。这在复杂文档中尤为重要，形状可能用于注释、插图或作为文档设计的一部分。
1. 维护布局和设计：形状常在文档的布局和视觉设计中发挥关键作用。锁定它们可保持预期外观，确保文档保持专业和视觉吸引力。
1. 数据完整性：在电子表格中，形状可用来突出重要数据点、添加注释或提供视觉解释。锁定这些形状可确保它们提供的上下文信息保持准确完整。
1. 共享文档中的一致性：协作时，不同用户可能具有不同的专业水平。锁定形状有助于保持文档的一致性，防止意外更改。
1. 安全性：在敏感文档中，锁定形状可以作为保护信息的整体策略的一部分。例如，在财务报告或法律文件中，锁定形状可用来保护关键的注释或高亮部分，提供重要上下文。

有时候，你需要在某些受保护的工作表中修改特定形状，因此需要解锁这些形状。本文将详细介绍如何锁定和解锁指定的形状。

## **如何在Excel中锁定形状以保护它们**

下面介绍在Microsoft Excel中锁定单元格的方法：

1. 打开您的Excel文件：打开包含您要锁定的形状的Excel文件。

1. 选择形状：点击您要锁定的形状。也可以按住 Ctrl 键同时点击多个形状以选择。

1. 打开“格式形状”窗格：右键点击已选的形状，选择“大小和属性”。或者，在“开始”选项卡中，点击“格式”区域中的对话框启动器（一个小箭头）打开“格式形状”窗格。
1. 锁定形状：在“格式形状”窗格中，转到“大小与属性”选项卡（图标像一个带箭头的方块）。在“属性”部分，勾选“已锁定”。
<br>
<img src="1.png" width=60% />
1. 保护工作表：在功能区的“审阅”选项卡中，点击“保护工作表”。设置密码（可选）并选择你想允许的权限（例如选择锁定单元格、设置单元格格式等）。点击“确定”。
<br>
<img src="2.png" width=60% />

## **如何在指定工作表中锁定所有形状**

要保护指定工作表中的所有形状，请使用 [Worksheet.Protect(ProtectionType.Objects)](https://reference.aspose.com/cells/net/aspose.cells/worksheet/protect/#protect) 方法。示例代码如下。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Lock-Or-Unlock-Shapes-1.cs" >}}

## **如何在受保护的工作表中解锁指定形状**

要解锁受保护工作表中的指定形状，请使用 [shape.IsLocked](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/islocked/)，示例代码如下。

注意：只有在工作表被保护时 [shape.IsLocked](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/islocked/) 才有意义。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Lock-Or-Unlock-Shapes-2.cs" >}}

{{< app/cells/assistant language="csharp" >}}
