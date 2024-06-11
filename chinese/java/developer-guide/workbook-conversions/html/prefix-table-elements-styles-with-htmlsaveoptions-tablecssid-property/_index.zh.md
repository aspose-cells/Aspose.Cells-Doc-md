---
title: 使用 HtmlSaveOptions.TableCssId 属性为表格元素样式添加前缀
type: docs
weight: 110
url: /zh/java/prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property/
---

## **可能的使用场景**

Aspose.Cells 允许您使用 [**HtmlSaveOptions.TableCssId**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#TableCssId) 属性为表格元素样式添加前缀。假设您将此属性设置为 *MyTest_TableCssId* 等某个值，则将找到如下所示的表格元素样式。

{{< highlight java >}}

table#MyTest_TableCssId

#MyTest_TableCssId tr

#MyTest_TableCssId col

#MyTest_TableCssId br

etc.

{{< /highlight >}}

以下屏幕截图显示了使用 [**HtmlSaveOptions.TableCssId**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#TableCssId) 属性对输出 HTML 的影响。

![todo:image_alt_text](prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property_1.png)

## **使用 HtmlSaveOptions.TableCssId 属性为表格元素样式添加前缀**

以下示例代码说明了如何使用 [**HtmlSaveOptions.TableCssId**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#TableCssId) 属性。请参考代码生成的 [输出 HTML](60489791.zip) 进行参考。

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-PrefixTableElementsStylesWithHtmlSaveOptions_TableCssIdProperty.java" >}}
