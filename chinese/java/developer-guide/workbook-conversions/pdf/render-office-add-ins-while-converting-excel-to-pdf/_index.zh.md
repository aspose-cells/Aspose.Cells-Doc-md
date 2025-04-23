---
title: 转换Excel为PDF时呈现Office加载项
type: docs
weight: 90
url: /zh/java/render-office-add-ins-while-converting-excel-to-pdf/
---

## **可能的使用场景**
之前，当将Excel文件保存为PDF格式时，Aspose.Cells无法呈现Office加载项。现在Aspose.Cells可以很好地呈现它。您不需要使用任何特殊的方法或属性来在输出PDF中呈现Office加载项。只需将您的Excel文件保存为PDF格式，它将呈现Office加载项。
## **在将Excel转换为PDF时呈现Office加载项**
以下示例代码保存包含Office加载项的[样本Excel文件](60489783.xlsx)。请查看由之前版本即17.11生成的[输出PDF](60489781.pdf)和由新版本即17.12及以后版本生成的[输出PDF](60489782.pdf)。之前版本的输出PDF为空白的，而新版本的输出PDF显示了Office加载项。
## **示例代码**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Rendering-RenderOfficeAdd_InsWhileConvertingExcelToPdf.java" >}}
{{< app/cells/assistant language="java" >}}
