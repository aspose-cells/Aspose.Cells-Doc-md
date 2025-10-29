---  
title: 查找或搜索数据
type: docs  
weight: 50  
url: /zh/nodejs-cpp/find-or-search-data/  
description: 了解如何通过 Aspose.Cells for Node.js via C++ API 查找或搜索包含指定数据的单元格。  
keywords: 通过 C++ 在 Node.js 中查找数据，在 Node.js 中搜索数据，通过 C++ 在 Node.js 查找包含公式的单元格，通过 C++ 在 Node.js 中搜索包含公式的单元格，使用 FindOptions 在 Node.js 中查找数据或公式，搜索数据或公式使用 FindOptions 在 Node.js 中，查找或搜索包含特定字符串值或数字的单元格，在 Node.js 中查找或搜索包含特定数据的单元格  
---  

{{% alert color="primary" %}}  
Microsoft Excel 允许用户在工作表中查找包含指定数据的单元格。  
{{% /alert %}}  

## **查找包含指定数据的单元格**  

### **使用Microsoft Excel**  

Microsoft Excel 允许用户在工作表中查找包含指定数据的单元格。如果在 Microsoft Excel 中选择 **查找** 菜单中的 **编辑**，你会看到一个对话框，可以在其中指定搜索值。  

在这里，我们正在查找值"橙子"。 Aspose.Cells 还允许开发人员查找工作表中包含指定值的单元格。  

### **使用 Aspose.Cells for Node.js via C++**  

Aspose.Cells 提供一个类 [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)，代表一个 Microsoft Excel 文件。[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) 类包含一个 [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) 集合，用于访问 Excel 文件中的每个工作表。工作表由 [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) 类表示。[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) 类提供一个 [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) 集合，表示工作表中的所有单元格。[**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) 集合提供多种方法，用于查找包含用户指定数据的单元格。以下部分更详细地介绍了这些方法中的一些。  

{{% alert color="primary" %}}  
所有查找方法返回包含指定数据的单元格的引用。  
{{% /alert %}}  

## **查找包含公式的单元格**  

开发者可以通过调用 [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) 集合的 [**find**](https://reference.aspose.com/cells/nodejs-cpp/cells/#find-object-cell-findoptions-) 方法，在工作表中查找指定的公式。通常，[**find**](https://reference.aspose.com/cells/nodejs-cpp/cells/#find-object-cell-findoptions-) 方法接受三个参数：  

- **对象：** 要搜索的对象。类型应为 int、double、DateTime、string 或 bool。  
- **前一个单元格：** 具有相同对象的前一个单元格。如果从头开始搜索，可以将此参数设为 null。  
- **查找选项：** 查找所需对象的选项。  

以下示例使用工作表数据来练习查找方法：  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-SearchData-FindCellsContainFormula.js" >}}


## **使用 FindOptions 查找数据或公式**  

可以使用 [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) 集合的 [**Cells.find(object, Cell)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#find-object-cell-) 方法，结合各种 [**FindOptions**](https://reference.aspose.com/cells/nodejs-cpp/findoptions)，查找指定的值。通常，[**find**](https://reference.aspose.com/cells/nodejs-cpp/cells/#find-object-cell-findoptions-) 方法接受以下参数：  

- **搜索值**，要搜索的数据或值。  
- **前一个单元格**，上一个包含相同值的单元格。如果从开头开始搜索，可以将此参数设置为null。  
- **查找选项**，查找选项。  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-SearchData-FindDataUsingFindOptions.js" >}}


## **查找包含指定字符串值或数字的单元格**  

也可以调用同在 [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) 集合中的 [**find**](https://reference.aspose.com/cells/nodejs-cpp/cells/#find-object-cell-findoptions-) 方法，结合各种 [**FindOptions**](https://reference.aspose.com/cells/nodejs-cpp/findoptions)，查找指定的字符串值。  

指定 [**FindOptions.setLookInType**](https://reference.aspose.com/cells/nodejs-cpp/findoptions/#setLookInType-lookintype-) 和 [**FindOptions.setLookAtType**](https://reference.aspose.com/cells/nodejs-cpp/findoptions/#setLookAtType-lookattype-) 属性。以下示例代码演示了如何使用这些属性查找在单元格字符串的**开头**、**中间**或**结尾**的各种字符串。  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-SearchData-FindCellsContainSpecifyString.js" >}}



## **高级主题**  
- [查找具有特定样式的单元格](/cells/zh/nodejs-cpp/find-cells-with-specific-style/)  
- [查找单元格值是否以单引号开始](/cells/zh/nodejs-cpp/find-if-the-cell-value-starts-with-single-quote-mark/)  
- [使用原始值搜索数据](/cells/zh/nodejs-cpp/search-data-using-original-values/)  

{{< app/cells/assistant language="nodejs-cpp" >}}
