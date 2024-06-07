---
title: 在将Excel转为PDF时呈现Office附加组件
type: docs
weight: 90
url: /zh/java/render-office-add-ins-while-converting-excel-to-pdf/
---

## **可能的使用场景**
早先，Aspose.Cells 在将Excel文件保存为PDF格式时无法呈现Office附加组件。现在Aspose.Cells 可以正确呈现它。您无需使用任何特殊方法或属性来在输出PDF中呈现Office附加组件。只需将Excel文件保存为PDF格式，它将呈现Office附加组件。
## **在将Excel转为PDF时呈现Office附加组件**
以下示例代码保存了包含 Office Add-Ins 的 [示例 Excel 文件](60489783.xlsx)。请参阅以前版本（即 17.11）生成的[输出 PDF](60489781.pdf) 和新版本（即 17.12 及以上）生成的[输出 PDF](60489782.pdf)。以前版本的输出 PDF 是空白的，但新版本的输出 PDF 显示了 Office Add-In。
## **示例代码**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Rendering-RenderOfficeAdd_InsWhileConvertingExcelToPdf.java" >}}
