---
title: 使用 HtmlSaveOptions.TableCssId 属性为表格元素样式添加前缀
type: docs
weight: 110
url: /zh/net/prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property/
---

## **可能的使用场景**

Aspose.Cells允许您使用[**HtmlSaveOptions.TableCssId**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/tablecssid)属性前缀表元素样式。假设将此属性设置为某个值，如**MyTest_TableCssId**，那么您将找到类似下面显示的表元素样式

{{< highlight java >}}

 table#MyTest_TableCssId

#MyTest_TableCssId tr

#MyTest_TableCssId col

#MyTest_TableCssId br

etc.

{{< /highlight >}}

以下屏幕截图显示了使用 [**HtmlSaveOptions.TableCssId**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/tablecssid) 属性对输出 HTML 的影响。

![todo:image_alt_text](prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property_1.png)

## **使用 HtmlSaveOptions.TableCssId 属性为表格元素样式添加前缀**

以下示例代码演示了如何利用[**HtmlSaveOptions.TableCssId**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/tablecssid)属性。请查看代码生成的[output HTML](60489790.zip) 以供参考。

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-PrefixTableElementsStylesWithHtmlSaveOptions_TableCssIdProperty.cs" >}}
