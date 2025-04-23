---  
title: 在刷新AutoFilter后获取所有隐藏行索引 
type: docs  
weight: 320  
url: /zh/nodejs-cpp/get-all-hidden-rows-indices-after-refreshing-autofilter/  
description: 学习如何在刷新AutoFilter后，使用Aspose.Cells for Node.js via C++ API获取所有隐藏行索引。  
keywords: 刷新AutoFilter后获取所有隐藏行索引 Node.js via C++，通过C++获取刷新后所有隐藏行索引 Node.js，使用C++检索刷新后所有隐藏行索引  
---  

## **可能的使用场景**  

当你在工作表单元格上应用自动筛选时，有些行会被自动隐藏。但也可能有一些行是由Excel最终用户手动隐藏的，这些行不会被自动筛选隐藏。因此，难以区分哪些行是由自动筛选隐藏的，哪些是由用户手动隐藏的。Aspose.Cells for Node.js via C++使用`Array` [**AutoFilter.refresh(hideRows)**](https://reference.aspose.com/cells/nodejs-cpp/autofilter/#refresh-boolean-)解决此问题。此方法返回由自动筛选隐藏、非用户手动隐藏的所有行的索引。  

## **在刷新自动筛选后获取所有隐藏行索引**  

请查看以下示例代码，加载含有一些由Excel最终用户手动隐藏的行的[示例Excel文件](64716909.xlsx)。此代码应用自动筛选并使用`Array` [**AutoFilter.refresh(hideRows)**](https://reference.aspose.com/cells/nodejs-cpp/autofilter/#refresh-boolean-)方法刷新筛选，该方法返回所有由自动筛选隐藏的行的索引。然后，它将隐藏行的索引与单元格名称和数值一同打印到控制台。  

## **示例代码**  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-GetAllHiddenRowsIndicesAfterRefreshingAutoFilter.js" >}}


## **控制台输出**  

{{< highlight java >}}  

Printing Rows Indices, Cell Names and Values Hidden By AutoFilter.  

\--------------------------  

1       A2      Apple  

2       A3      Apple  

3       A4      Apple  

6       A7      Apple  

7       A8      Apple  

11      A12     Pear  

12      A13     Pear  

{{< /highlight >}}  
