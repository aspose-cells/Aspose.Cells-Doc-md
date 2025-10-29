---  
title: 添加二色比例和三色比例条件格式 
linktitle: 添加二色比例和三色比例条件格式  
description: 如何通过 C++ 在 Node.js 中使用 Aspose.Cells 库为两个色比和三个色比添加条件格式。通过调整这些条件，您可以更好地控制单元格的外观。  
keywords: Aspose.Cells，条件格式，Node.js via C++，颜色比值，双色标度，三色标度  
type: docs  
weight: 20  
url: /zh/nodejs-cpp/adding-2-color-scale-and-3-color-scale-conditional-formattings/  
---  

{{% alert color="primary" %}}  
**双色标度**和**三色标度**条件格式的添加方式相同，不同之处在于 [**ColorScale.setIs3ColorScale(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/colorscale/#setIs3ColorScale-boolean-) 方法。对于双色标度，此方法为 **false**，而对于三色标度，则为 **true**。  
{{% /alert %}}  

以下示例代码添加了二色比例和三色比例条件格式。它生成了 [输出 Excel 文件](5115058.xlsx)。  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ConditionalFormatting-Adding2-ColorScaleAnd3-ColorScale.js" >}}


{{< app/cells/assistant language="nodejs-cpp" >}}
