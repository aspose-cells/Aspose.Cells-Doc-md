---
title: 用 Node.js 通过 C++ 生成 HTML
linktitle: HTML
type: docs
weight: 230
url: /zh/nodejs-cpp/convert-excel-to-html/
---

## **将Excel工作簿转换为HTML**
Aspose.Cells API 提供了导出电子表格为 HTML 格式的支持。为此，Aspose.Cells 使用 [**HtmlSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions) 类，提供控制输出 HTML 各个方面的灵活性。

以下代码示例展示如何使用 Node.js 将工作簿保存为 HTML 文件：

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Save file to HTML format
workbook.save("out.html");
```


## **将Excel工作簿转换为MHTML文件**
MHTML将普通HTML与外部资源（如图片、动画、音频等）合并成一个文件。这些文件通常扩展名为.mht，用于电子邮件。Aspose.Cells支持读取和写入MHTML文件。

以下代码示例展示如何使用 Node.js 将工作簿保存为 MHTML 文件：

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Save file to mhtml format
workbook.save("out.mht");
```

## **高级主题**
- [加载HTML至工作簿时自适应调整列和行](/cells/zh/nodejs-cpp/autofit-columns-and-rows-while-loading-html-in-workbook/)
- [在从HTML导入时避免大数的使用指数表示法](/cells/zh/nodejs-cpp/avoid-exponential-notation-of-large-numbers-while-importing/)
- [更改 HTML 链接的目标类型](/cells/zh/nodejs-cpp/change-the-html-link-target-type/)
- [将 Excel 转换为带有工具提示的 HTML](/cells/zh/nodejs-cpp/convert-excel-to-html-with-tooltip/)
- [Create Transparent Image of Excel Worksheet](/cells/zh/nodejs-cpp/create-transparent-image-of-excel-worksheet/)
- [在导入HTML时删除换行后的多余空格](/cells/zh/nodejs-cpp/delete-redundant-spaces-after-line-break-while-importing/)
- [在保存为HTML时禁用下级可见的批注](/cells/zh/nodejs-cpp/disable-downlevel-revealed-comments-while-saving-to/)
- [禁用导出框架脚本和文档属性](/cells/zh/nodejs-cpp/disable-exporting-frame-scripts-and-document-properties/)
- [将Excel转换为HTML - 使用PresentationPreference选项获得更好的布局](/cells/zh/nodejs-cpp/excel-to-html-use-presentationpreference-option-for-better-layout/)
- [在将 Excel 转换为 HTML 时排除未使用的样式](/cells/zh/nodejs-cpp/exclude-unused-styles-during-excel-to-html-conversion/)
- [在将Excel文件导出为HTML时，将文本从右向左扩展](/cells/zh/nodejs-cpp/expanding-text-from-right-to-left-while-exporting-excel-file-to/)
- [在将Excel转换为HTML时，导出数据条、颜色刻度和图标集条件格式](/cells/zh/nodejs-cpp/export-databar-colorscale-and-iconset-conditional-formatting-while-excel-to-html-conversion/)
- [在将 Excel 文件保存为 HTML 时导出批注](/cells/zh/nodejs-cpp/export-comments-while-saving-excel-file-to/)
- [在Excel转换为HTML时导出文档工作簿和工作表属性](/cells/zh/nodejs-cpp/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/)
- [将Excel导出为带有网格线的HTML](/cells/zh/nodejs-cpp/export-excel-to-html-with-gridlines/)
- [将打印区域范围导出为HTML](/cells/zh/nodejs-cpp/export-print-area-range-to/)
- [在Web浏览器不支持边框样式时导出相似的边框样式](/cells/zh/nodejs-cpp/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/)
- [在输出 HTML 中单独导出工作表 CSS](/cells/zh/nodejs-cpp/export-worksheet-css-separately-in-output/)
- [在保存为 HTML 时隐藏重叠的内容与 CrossHideRight](/cells/zh/nodejs-cpp/hiding-overlaid-content-with-crosshideright-while-saving-to/)
- [使用 HtmlSaveOptions.TableCssId 属性为表格元素样式添加前缀](/cells/zh/nodejs-cpp/prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property/)
- [在保存为HTML时防止导出隐藏的工作表内容](/cells/zh/nodejs-cpp/prevent-exporting-hidden-worksheet-contents-on-saving-to/)
- [通过IFilePathProvider接口提供导出工作表的HTML文件路径](/cells/zh/nodejs-cpp/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/)
- [识别自封闭标签](/cells/zh/nodejs-cpp/recognise-self-closing-tags/)
- [在将电子表格转换为HTML时渲染WordArt的梯度填充](/cells/zh/nodejs-cpp/render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to/)
- [将列宽设置为可缩放单元，如em或百分比](/cells/zh/nodejs-cpp/set-column-width-to-scalable-unit-like-em-or-percent/)
- [在将电子表格渲染为HTML时设置默认字体](/cells/zh/nodejs-cpp/set-default-font-while-rendering-spreadsheet-to/)
- [使用HtmlCrossType指定输出HTML中如何交叉字符串](/cells/zh/nodejs-cpp/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/)
- [支持加载HTML到Excel工作簿时的DIV标签布局](/cells/zh/nodejs-cpp/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/)

- [在保存为HTML时启用CSS自定义属性](/cells/zh/nodejs-cpp/enable-css-custom-properties-while-saving-to-html/)
