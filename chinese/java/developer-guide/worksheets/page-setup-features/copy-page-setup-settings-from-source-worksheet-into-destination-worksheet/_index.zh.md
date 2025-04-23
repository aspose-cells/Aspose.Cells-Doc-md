---
title: 从源工作表复制页面设置设置到目标工作表的可能使用场景
type: docs
weight: 10
url: /zh/java/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/
---

## **可能的使用场景**

向工作簿添加新工作表时，它包含默认的页面设置。有时您需要将一个工作表的设置（[**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/PageSetup)）传输到另一个工作表。本文档介绍如何使用Aspose.Cells API将一个工作表的页面设置复制到另一个工作表。

## **将源工作表中的页面设置复制到目标工作表**

以下示例代码说明了如何使用[**PageSetup.Copy()**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#copy-com.aspose.cells.PageSetup-com.aspose.cells.CopyOptions-)方法从一个工作表复制页面设置到另一个工作表。请参考以下示例代码和其控制台输出。

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-PageSetupFeatures-CopyPageSetupSettingsFromSourceWorksheetToDestinationWorksheet.java" >}}

## **控制台输出**

{{< highlight java >}}

Before Paper Size: PAPER_A_3_EXTRA_TRANSVERSE

Before Paper Size: PAPER_LETTER

After Paper Size: PAPER_A_3_EXTRA_TRANSVERSE

After Paper Size: PAPER_A_3_EXTRA_TRANSVERSE

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
