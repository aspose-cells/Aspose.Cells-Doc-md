---
title: Copy Ranges of Excel
linktitle: Copy Ranges
type: docs
weight: 105
url: /net/copy-ranges-of-Excel/
---

## **Introduction**

In Excel, you can select a range, copy the range, then paste it with specific options to the same worksheet, other worksheets or other files.

## **Copy Ranges Using Aspose.Cells**

Aspose.Cells provides some overload [Range.Copy](https://reference.aspose.com/cells/net/aspose.cells/range/copy/#copy) methods to copy the range.
And [Range.CopyStyle](https://reference.aspose.com/cells/net/aspose.cells/range/copystyle/) only the copy style of the range; [Range.CopyData](https://reference.aspose.com/cells/net/aspose.cells/range/copydata/) only the copy value of the range

## **Copy Range**

Creating two ranges: the source range, the target range, then copying source range to target range with Range.Copy method.

See the following code:

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Copy-Range.cs" >}}

## **Paste Range With Options**

Aspose.Cells supports pasting the range with specific type.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Paste-Range.cs" >}}

## **Only Copy Data Of The Range.**
Also you can copy the data with Range.CopyData method as the following codes:

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Copy-Range-Data.cs" >}}


