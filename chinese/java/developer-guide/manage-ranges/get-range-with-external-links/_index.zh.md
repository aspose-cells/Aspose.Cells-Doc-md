---
title: 使用外部链接获取范围
type: docs
weight: 140
url: /zh/java/get-range-with-external-links/
---
## **使用外部链接获取范围**

很多时候，Excel 文件使用外部链接从其他 Excel 文件访问数据。 Aspose.Cells 提供了通过使用检索这些外部链接的选项[**名称.GetReferredAreas**](https://reference.aspose.com/cells/java/com.aspose.cells/name#getReferredAreas(boolean)） 方法。这[**名称.GetReferredAreas**](https://reference.aspose.com/cells/java/com.aspose.cells/name#getReferredAreas(boolean)) 方法返回类型数组[**推荐区域**](https://reference.aspose.com/cells/java/com.aspose.cells/ReferredArea).这[**推荐区域**](https://reference.aspose.com/cells/java/com.aspose.cells/ReferredArea)类提供了一个[**外部文件名**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#ExternalFileName)返回外部文件名称的属性。这[**推荐区域**](https://reference.aspose.com/cells/java/com.aspose.cells/ReferredArea)类公开以下成员。

- [**结束列**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#EndColumn)区域的结束列
- [**结束行**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#EndRow)区域的末行
- [**外部文件名**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#ExternalFileName)：如果这是外部引用，则获取外部文件名
- [**区域**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#IsArea)表示这是否是一个区域
- [**是外部链接**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#IsExternalLink)表示这是否是外部链接
- [**工作表名称**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#SheetName)：表示该引用在哪个工作表中
- [**起始列**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#StartColumn)：区域的起始列
- [**起始行**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#StartRow)：区域的起始行

下面给出的示例代码演示了使用[**名称.GetReferredAreas**](https://reference.aspose.com/cells/java/com.aspose.cells/name#getReferredAreas(boolean)方法来获取带有外部链接的范围。

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-GetRangeWithExternalLinks-1.java" >}}
