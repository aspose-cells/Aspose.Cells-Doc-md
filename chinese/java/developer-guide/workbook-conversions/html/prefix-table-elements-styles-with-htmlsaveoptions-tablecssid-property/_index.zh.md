---
title: 使用HtmlSaveOptions.TableCssId属性前缀表元素样式
type: docs
weight: 110
url: /zh/java/prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property/
---

## **可能的使用场景**

Aspose.Cells允许您使用[**HtmlSaveOptions.TableCssId**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#TableCssId)属性为表元素样式添加前缀。假设您将此属性设置为某个值，例如*MyTest_TableCssId*，那么您将发现表元素样式如下所示

{{< highlight java >}}

table#MyTest_TableCssId

#MyTest_TableCssId tr

#MyTest_TableCssId col

#MyTest_TableCssId br

etc.

{{< /highlight >}}

以下截图显示了在输出HTML中使用 [**HtmlSaveOptions.TableCssId**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#TableCssId) 属性的效果

![todo:image_alt_text](prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property_1.png)

## **使用HtmlSaveOptions.TableCssId属性前缀表元素样式**

以下示例代码解释了如何使用[**HtmlSaveOptions.TableCssId**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#TableCssId)属性。请查看由代码生成的[输出HTML](60489791.zip)进行参考。

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-PrefixTableElementsStylesWithHtmlSaveOptions_TableCssIdProperty.java" >}}
