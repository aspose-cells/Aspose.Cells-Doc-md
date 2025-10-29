---  
title: 使用原始值搜索数据
type: docs  
weight: 380  
url: /zh/nodejs-cpp/search-data-using-original-values/  
description: 学习如何通过 Aspose.Cells for Node.js via C++ API 使用原始值搜索数据。  
keywords: 使用 C++ 在 Node.js 中通过原始值搜索数据，使用 C++ 在 Node.js 中查找原始值，使用 C++ 通过原始值搜索数据，Node.js 通过原始值查找数据  
---  

{{% alert color="primary" %}}  

有时，数据的值因为以某种方式格式化而被隐藏。例如，假设单元格 D4 公式为 =Sum(A1:A2) 并且其值为 20 但格式为---，那么值 20 将被隐藏，并且无法使用 Microsoft Excel 查找选项找到。但是，您可以使用 Aspose.Cells 使用 [**LookInType.OriginalValues**](https://reference.aspose.com/cells/nodejs-cpp/lookintype) 找到它  

{{% /alert %}}  

以下示例代码说明了上述观点。它会找到无法使用Microsoft Excel的查找选项找到的单元格D4，但Aspose.Cells可以使用[**LookInType.OriginalValues**](https://reference.aspose.com/cells/nodejs-cpp/lookintype)找到它。请阅读代码内的注释以获取更多信息。  

## 使用 Node.js 通过原始值搜索数据的代码示例  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-SearchData-SearchDataUsingOriginalValues.js" >}}


## 示例代码生成的控制台输出  

这是上面示例代码的控制台输出。  

{{< highlight java >}}  

Aspose.Cells.Cell [ D4; ValueType : IsNumeric; Value : ---; Formula:=SUM(A1:A2)]  

{{< /highlight >}}  

{{< app/cells/assistant language="nodejs-cpp" >}}
