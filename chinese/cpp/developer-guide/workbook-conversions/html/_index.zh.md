---
title: 用C++的HTML
linktitle: HTML
type: docs
weight: 230
url: /zh/cpp/convert-excel-to-html/
description: 使用Aspose.Cells将Excel转换为HTML和MHTML格式。
---

## **将Excel工作簿转换为HTML**
Aspose.Cells API 提供了导出电子表格为 HTML 格式的支持。为此，Aspose.Cells 使用 [**HtmlSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions) 类，提供控制输出 HTML 各个方面的灵活性。

以下示例展示如何使用C++保存工作簿为HTML文件：

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load your source workbook
    Workbook workbook(u"Book1.xlsx");

    // Save file to HTML format
    workbook.Save(u"out.html");

    std::cout << "Workbook saved to HTML format successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **将Excel工作簿转换为MHTML文件**
MHTML将普通HTML与外部资源（如图片、动画、音频等）合并成一个文件。这些文件通常扩展名为.mht，用于电子邮件。Aspose.Cells支持读取和写入MHTML文件。

以下示例展示如何用C++将工作簿另存为MHTML文件：

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load your source workbook
    U16String inputFilePath(u"Book1.xlsx");
    std::unique_ptr<Workbook> workbook = std::make_unique<Workbook>(inputFilePath);

    // Save file to mhtml format
    U16String outputFilePath(u"out.mht");
    workbook->Save(outputFilePath, SaveFormat::MHtml);

    std::cout << "Workbook saved to MHTML format successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **高级主题**
- [加载HTML至工作簿时自适应调整列和行](/cells/zh/cpp/autofit-columns-and-rows-while-loading-html-in-workbook/)
- [在从HTML导入时避免大数的使用指数表示法](/cells/zh/cpp/avoid-exponential-notation-of-large-numbers-while-importing-from/)
- [更改 HTML 链接的目标类型](/cells/zh/cpp/change-the-html-link-target-type/)
- [将 Excel 转换为带有工具提示的 HTML](/cells/zh/cpp/convert-excel-to-html-with-tooltip/)
- [Create Transparent Image of Excel Worksheet](/cells/zh/cpp/create-transparent-image-of-excel-worksheet/)
- [在导入HTML时删除换行后的多余空格](/cells/zh/cpp/delete-redundant-spaces-after-line-break-while-importing/)
- [在保存为HTML时禁用下级可见的批注](/cells/zh/cpp/disable-downlevel-revealed-comments-while-saving-to/)
- [禁用导出框架脚本和文档属性](/cells/zh/cpp/disable-exporting-frame-scripts-and-document-properties/)
- [将Excel转换为HTML - 使用PresentationPreference选项获得更好的布局](/cells/zh/cpp/excel-to-html-use-presentationpreference-option-for-better-layout/)
- [在将 Excel 转换为 HTML 时排除未使用的样式](/cells/zh/cpp/exclude-unused-styles-during-excel-to-html-conversion/)
- [在将Excel文件导出为HTML时，将文本从右向左扩展](/cells/zh/cpp/expanding-text-from-right-to-left-while-exporting-excel-file-to/)
- [在将Excel转换为HTML时，导出数据条、颜色刻度和图标集条件格式](/cells/zh/cpp/export-databar-colorscale-and-iconset-conditional-formatting-while-excel-to-html-conversion/)
- [在将 Excel 文件保存为 HTML 时导出批注](/cells/zh/cpp/export-comments-while-saving-excel-file-to/)
- [在Excel转换为HTML时导出文档工作簿和工作表属性](/cells/zh/cpp/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/)
- [将Excel导出为带有网格线的HTML](/cells/zh/cpp/export-excel-to-html-with-gridlines/)
- [将打印区域范围导出为HTML](/cells/zh/cpp/export-print-area-range-to/)
- [在Web浏览器不支持边框样式时导出相似的边框样式](/cells/zh/cpp/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/)
- [在输出 HTML 中单独导出工作表 CSS](/cells/zh/cpp/export-worksheet-css-separately-in-output/)
- [在保存为 HTML 时隐藏重叠的内容与 CrossHideRight](/cells/zh/cpp/hiding-overlaid-content-with-crosshideright-while-saving-to/)
- [使用 HtmlSaveOptions.TableCssId 属性为表格元素样式添加前缀](/cells/zh/cpp/prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property/)
- [在保存为HTML时防止导出隐藏的工作表内容](/cells/zh/cpp/prevent-exporting-hidden-worksheet-contents-on-saving-to/)
- [识别自封闭标签](/cells/zh/cpp/recognise-self-closing-tags/)
- [在将电子表格转换为HTML时渲染WordArt的梯度填充](/cells/zh/cpp/render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to/)
- [将列宽设置为可缩放单元，如em或百分比](/cells/zh/cpp/set-column-width-to-scalable-unit-like-em-or-percent/)
- [在将电子表格渲染为HTML时设置默认字体](/cells/zh/cpp/set-default-font-while-rendering-spreadsheet-to/)
- [使用HtmlCrossType指定输出HTML中如何交叉字符串](/cells/zh/cpp/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/)
- [支持加载HTML到Excel工作簿时的DIV标签布局](/cells/zh/cpp/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/)
- [在保存为HTML时启用CSS自定义属性](/cells/zh/cpp/enable-css-custom-properties-while-saving-to-html/)
{{< app/cells/assistant language="cpp" >}}
