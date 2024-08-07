---
title: 锁定或解锁形状
linktitle: 锁定或解锁形状
type: docs
weight: 200
url: /zh/net/lock-or-unlock-shapes/
description: 该文章向您展示了使用 Aspose.Cells 库对形状进行锁定或解锁以保护它们的代码。
keywords: C# 锁定形状以保护它们，如何使用 C# 锁定或解锁形状，用于在 C# 中锁定或解锁形状以保护它们。
---

## **可能的使用场景**

有时，您需要保护工作表中的所有形状，以防止它们被不需要的情况破坏。在这种情况下，您需要锁定指定工作表中的所有形状。 

在电子表格或文档中锁定形状对多个原因都有益处：
1. 防止意外更改：锁定形状可以确保用户不会意外移动、调整大小或删除它们。这在形状可能被用于注释、插图或作为文档设计的一部分的复杂文档中尤为重要。
1. 保持布局和设计：形状通常在文档的布局和视觉设计中起着至关重要的作用。锁定它们可以保留预期的外观，确保文档保持专业和视觉上吸引人。
1. 数据完整性：在电子表格中，形状可用于突出显示重要数据点，添加注释或提供视觉解释。锁定这些形状可确保它们提供的上下文信息保持准确和完整。
1. 共享文档的一致性：在协作文档时，不同用户可能具有不同水平的专业知识。锁定形状有助于通过防止意外更改来保持文档的一致性。
1. 安全性：在敏感文档中，锁定形状可以成为保护信息的更广泛策略的一部分。例如，在财务报告或法律文件中，锁定的形状可用于保护提供关键背景的特定注释或突出显示。

有时，您需要能够修改特定受保护工作表中的某些形状，这种情况下，您需要解锁这些形状。本文将详细介绍如何锁定和解锁指定的形状。

## **如何锁定形状以在Excel中保护它们**

以下是您可以在 Microsoft Excel 中锁定单元格的方法：

1. 打开Excel文件：打开包含您想要锁定的形状的Excel文件。

1. 选择形状：单击要锁定的形状。您也可以通过按住Ctrl键并单击每个形状来选择多个形状。

1. 打开格式形状窗格：右键单击所选形状，然后选择“大小和属性”。或者，您可以转到功能区的“格式”选项卡，在“大小”组中，单击对话框启动器（一个小箭头）以打开“格式形状”窗格。
1. 锁定形状：在“格式形状”窗格中，转到“大小和属性”选项卡（图标看起来像一个带箭头的正方形）。在“属性”部分下，选中“锁定”复选框。
<br>
<img src="1.png" width=60% />
1. 保护工作表：转到功能区的“审阅”选项卡。单击“保护工作表”。设置密码（可选）并选择要允许的权限（例如，选择锁定的单元格，格式化单元格等）。单击“确定”。
<br>
<img src="2.png" width=60% />

## **如何在指定工作表中锁定所有形状**

要保护指定工作表中的所有形状，请使用 [Worksheet.Protect(ProtectionType.Objects)](https://reference.aspose.com/cells/net/aspose.cells/worksheet/protect/#protect) 方法。示例代码如下。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Lock-Or-Unlock-Shapes-1.cs" >}}

## **如何在受保护的工作表中解锁指定的形状**

要解锁受保护工作表中的指定形状，请使用 [shape.IsLocked](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/islocked/)，示例代码如下。

注意：只有在工作表被保护时 [shape.IsLocked](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/islocked/) 才有意义。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Lock-Or-Unlock-Shapes-2.cs" >}}

