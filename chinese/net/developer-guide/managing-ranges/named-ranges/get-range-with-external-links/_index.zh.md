---
title: 使用外部链接获取范围
type: docs
weight: 120
url: /zh/net/get-range-with-external-links/
---
## **使用外部链接获取范围**

很多时候，Excel 文件使用外部链接从其他 Excel 文件访问数据。 Aspose.Cells 提供了通过使用检索这些外部链接的选项[**名称.GetReferredAreas**](https://reference.aspose.com/cells/net/aspose.cells/name/methods/getreferredareas)方法。这[**名称.GetReferredAreas**](https://reference.aspose.com/cells/net/aspose.cells/name/methods/getreferredareas)方法返回类型数组[**推荐区域**](https://reference.aspose.com/cells/net/aspose.cells/referredarea).这[**推荐区域**](https://reference.aspose.com/cells/net/aspose.cells/referredarea)类提供了一个[**外部文件名**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/externalfilename)返回外部文件名称的属性。这[**推荐区域**](https://reference.aspose.com/cells/net/aspose.cells/referredarea)类公开以下成员。

- [**结束列**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/endcolumn)区域的结束列
- [**结束行**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/endrow)区域的末行
- [**外部文件名**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/externalfilename)：如果这是外部引用，则获取外部文件名
- [**区域**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/isarea)表示这是否是一个区域
- [**是外部链接**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/isexternallink)表示这是否是外部链接
- [**工作表名称**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/sheetname)：表示该引用在哪个工作表中
- [**起始列**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/startcolumn)：区域的起始列
- [**起始行**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/startrow)：区域的起始行

下面给出的示例代码演示了使用[**名称.GetReferredAreas**](https://reference.aspose.com/cells/net/aspose.cells/name/methods/getreferredareas)使用外部链接获取范围的方法。

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-GetRangeWithExternalLinks-1.cs" >}}
