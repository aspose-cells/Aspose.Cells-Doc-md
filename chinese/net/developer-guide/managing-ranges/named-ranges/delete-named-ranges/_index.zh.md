---
title: 删除命名范围
type: docs
weight: 90
url: /zh/net/Delete-named-ranges/
description: 您可以了解如何使用 Aspose.Cells for .Net 从 Excel 或 OpenOffice 文件中删除定义的名称或命名范围。
---
##  **介绍**
如果Excel文件中定义的名称或命名范围太多，我们必须清除一些，因为它们不会被再次引用。

##  **删除 MS Excel 中的命名范围**

要从 Excel 中删除命名范围，您可以按照以下步骤操作：
1. 打开 Microsoft Excel 并打开包含命名范围的工作簿。
2. 转到 Excel 功能区中的“公式”选项卡。
3. 单击“定义名称”组中的“名称管理器”按钮。这将打开“名称管理器”对话框。
4. 在“名称管理器”对话框中，选择要删除的命名范围。
5. 单击“删除”按钮。出现提示时确认删除。
6. 单击“关闭”按钮关闭名称管理器对话框。
7. 保存工作簿以保留更改。


##  **使用 Aspose.Cells for .Net 删除命名范围**
使用 .Net 的 Aspose.Cells，您可以通过以下方式删除命名范围或定义的名称[文本](https://reference.aspose.com/cells/net/aspose.cells/namecollection/remove/#remove)或者[指数](https://reference.aspose.com/cells/net/aspose.cells/namecollection/removeat/#removeat)在列表中。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Delete-named-range.cs" >}}

注意：如果定义的名称被公式引用，则无法删除。我们只能删除定义名称的公式。

##  **删除一些命名范围**
当我们删除一个定义的名称时，我们必须检查它是否被文件中的所有公式引用。
为了提高删除命名范围的性能，我们可以一起删除一些。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Delete-named-ranges.cs" >}}

##  **删除重复的定义名称**
某些 Excel 字段已损坏，因为某些定义的名称重复。所以我们可以删除这些重复的名称来修复文件。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Delete-duplicate-defined-names.cs" >}}



