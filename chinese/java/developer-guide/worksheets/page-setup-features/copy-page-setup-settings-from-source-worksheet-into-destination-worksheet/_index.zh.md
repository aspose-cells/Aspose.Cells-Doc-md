---
title: 将源工作表中的页面设置设置复制到目标工作表
type: docs
weight: 10
url: /zh/java/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/
---
## **可能的使用场景**

当您将新工作表添加到工作簿时，它包含默认的页面设置设置。有时您可能需要传输设置（[**页面设置**](https://reference.aspose.com/cells/java/com.aspose.cells/PageSetup)) 从一个工作表到另一个工作表。本文档说明如何使用 Aspose.Cells API 将页面设置设置从一个工作表复制到另一个工作表。

## **将源工作表中的页面设置设置复制到目标工作表**

以下示例代码说明了如何使用以下方法将页面设置设置从一个工作表复制到另一个工作表[**PageSetup.Copy()**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#copy(com.aspose.cells.PageSetup,%20com.aspose.cells.CopyOptions)） 方法。请参阅以下示例代码及其控制台输出以供参考。

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-PageSetupFeatures-CopyPageSetupSettingsFromSourceWorksheetToDestinationWorksheet.java" >}}

## **控制台输出**

{{< highlight "java" >}}

Before Paper Size: PAPER_A_3_EXTRA_TRANSVERSE

Before Paper Size: PAPER_LETTER

After Paper Size: PAPER_A_3_EXTRA_TRANSVERSE

After Paper Size: PAPER_A_3_EXTRA_TRANSVERSE

{{< /highlight >}}
