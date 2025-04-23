---  
title: 应用Microsoft Excel的高级筛选以显示符合复杂条件的记录
type: docs  
weight: 280  
url: /zh/nodejs-cpp/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/  
description: 学习如何使用Aspose.Cells for Node.js via C++ API应用Microsoft Excel的高级筛选以显示符合复杂条件的记录。  
keywords: 通过C++在Node.js中应用高级筛选，设置高级筛选，添加高级筛选，创建高级筛选，如何在范围内添加高级筛选 Node.js通过C++  
---  

## **可能的使用场景**  

Microsoft Excel允许在工作表数据上应用*高级筛选*以显示满足复杂条件的记录。你可以通过*数据 > 高级*命令应用高级筛选，如此截屏所示。  

![todo:image_alt_text](1.png)  

Aspose.Cells for Node.js via C++还允许你使用[**Worksheet.advanced_Filter()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#advanced_Filter-boolean-string-string-string-boolean-)方法应用高级筛选。就像Microsoft Excel一样，它接受以下参数。  

**isFilter**  

-**listRange**- 列表范围。  

-**criteriaRange**- 条件范围。  

列表范围。  

**criteriaRange**  

条件范围。  

**copyTo**  

拷贝数据的范围。  

**uniqueRecordOnly**  

仅显示或拷贝唯一行。  

## **将 Microsoft Excel 的高级筛选应用于显示符合复杂条件的记录**  

以下示例代码在[示例Excel文件](48496692.xlsx)上应用高级筛选，并生成[输出Excel文件](48496691.xlsx)。截图显示两个文件以供比较。如截图所示，数据已根据复杂条件在输出Excel文件中被筛选。  

![todo:image_alt_text](2.png)  

## **示例代码**  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-AdvancedFilter.js" >}}


