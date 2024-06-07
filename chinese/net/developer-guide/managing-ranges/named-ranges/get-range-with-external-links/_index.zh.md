---
title: 获取带有外部链接的范围
type: docs
weight: 120
url: /zh/net/get-range-with-external-links/
---

## **获取带有外部链接的范围**

很多时候，Excel文件使用外部链接访问其他Excel文件中的数据。Aspose.Cells提供了通过使用[**Name.GetReferredAreas**](https://reference.aspose.com/cells/net/aspose.cells/name/methods/getreferredareas)方法检索这些外部链接的选项。[**Name.GetReferredAreas**](https://reference.aspose.com/cells/net/aspose.cells/name/methods/getreferredareas)方法返回一个类型为[**ReferredArea**](https://reference.aspose.com/cells/net/aspose.cells/referredarea)的数组。[**ReferredArea**](https://reference.aspose.com/cells/net/aspose.cells/referredarea)类提供一个[**ExternalFileName**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/externalfilename)属性，返回外部文件的名称。[**ReferredArea**](https://reference.aspose.com/cells/net/aspose.cells/referredarea)类公开以下成员。

- [**EndColumn**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/endcolumn)：该区域的结束列
- [**EndRow**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/endrow)：该区域的结束行
- [**ExternalFileName**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/externalfilename)：如果这是一个外部引用，则获取外部文件名
- [**IsArea**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/isarea)：指示这是否是一个区域
- [**IsExternalLink**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/isexternallink)：指示这是否是一个外部链接
- [**SheetName**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/sheetname)：指示此引用所在的工作表
- [**StartColumn**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/startcolumn)：该区域的起始列
- [**StartRow**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/startrow)：该区域的起始行

下面给出的示例代码演示了如何使用[**Name.GetReferredAreas**](https://reference.aspose.com/cells/net/aspose.cells/name/methods/getreferredareas)方法获取带有外部链接的范围。

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-GetRangeWithExternalLinks-1.cs" >}}
