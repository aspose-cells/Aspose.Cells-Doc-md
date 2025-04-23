---
title: 删除命名范围
type: docs
weight: 90
url: /zh/net/Delete-named-ranges/
description: 您可以学习如何使用Aspose.Cells for .Net从Excel或OpenOffice文件中删除已定义的名称或命名范围。
---

## **介绍**
如果 Excel 文件中有太多的定义名称或命名范围，我们必须清除一些，因为它们再也不会被引用。

## **在MS Excel中删除命名区域**

要从Excel中删除命名区域，可以按照以下步骤进行：
1. 打开Microsoft Excel并打开包含命名区域的工作簿。
2. 转到Excel功能区中的“公式”选项卡。
3. 单击“已定义名称”组中的“名称管理器”按钮。这将打开名称管理器对话框。
4. 在名称管理器对话框中，选择要删除的命名区域。
5. 单击“删除”按钮。在提示时确认删除。
6. 单击“关闭”按钮关闭名称管理器对话框。
7. 保存工作簿以保留更改。


## **使用Aspose.Cells for .Net删除命名范围**
使用Aspose.Cells for .Net，您可以通过列表中的[text](https://reference.aspose.com/cells/net/aspose.cells/namecollection/remove/#remove)或[index](https://reference.aspose.com/cells/net/aspose.cells/namecollection/removeat/#removeat) 删除命名范围或已定义的名称。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Delete-named-range.cs" >}}

注意：如果已定义的名称由公式引用，则不能删除。我们只能删除已定义名称的公式。

## **删除一些已命名范围**
当我们删除已定义名称时，必须检查它是否被文件中的所有公式引用。
为了提高删除命名范围的性能，我们可以一起删除一些。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Delete-named-ranges.cs" >}}

## **删除重复的已定义名称**
一些Excel文件损坏是因为某些已定义名称是重复的。因此，我们可以删除这些重复名称以修复文件。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Delete-duplicate-defined-names.cs" >}}



{{< app/cells/assistant language="csharp" >}}
