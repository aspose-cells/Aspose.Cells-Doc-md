---  
title: 如何管理日期和时间
type: docs  
weight: 600  
url: /zh/nodejs-cpp/how-to-manage-dates-and-times/  
description: 了解如何通过 Aspose.Cells for Node.js via C++ API 管理日期和时间。  
keywords: 如何管理日期和时间，1900日期系统，1904日期系统，设置日期和时间，获取日期和时间，管理日期和时间，在Excel中存储日期和时间，在单元格中显示日期和时间。  
---  

## **如何在Excel中存储日期和时间**  
日期和时间以数字形式存储在单元格中。因此，包含日期和时间的单元格的值属于数字类型。指定日期和时间的数字由日期（整数部分）和时间（小数部分）组成。Cell.DoubleValue属性返回此数字。  

## **如何在Aspose.Cells中显示日期和时间**  
要以日期和时间的格式显示数字，可以通过 [Style.getNumber()](https://reference.aspose.com/cells/nodejs-cpp/style/#getNumber--) 或 [Style.Custom]() 属性为单元格应用所需的日期和时间格式。CellValue.DateTimeValue 属性返回一个 DateTime 对象，指示由单元格中数字表示的日期和时间。  
<br>  
<image src="1.png" width="70%" />  

## **如何在Aspose.Cells中切换两个日期系统**  
MS-Excel 将日期存储为称为序列值的数字。 序列值是从日期系统中的第一天经过的天数，它是一个整数。 Excel 支持以下日期系统的序列值：  

1. 1900 年日期系统。 第一个日期是 1900 年 1 月 1 日，其序列值为 1。 最后一个日期是 9999 年 12 月 31 日，其序列值为 2,958,465。 此日期系统默认用于工作簿。  
1. 1904 日期系统。第一个日期是1904年1月1日，其序列值为0。最后一个日期是9999年12月31日，其序列值为2,957,003。要在工作簿中使用此日期系统，设置 [WorkbookSettings.getDate1904()](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getDate1904--) 属性为 true。  

此示例显示了在不同日期系统中存储的相同日期的序列值不同。  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DatesAndTimes-SwitchTwoDateSystems.js" >}}


输出结果：  
```  
A1 is Numeric Value: 45253  
use The 1904 date system====================  
A2 is Numeric Value: 43791  
```  

## **如何在 Aspose.Cells 中设置 DateTime 值**  
此示例在单元格 A1 和 A2 中设置 DateTime 值，设置 A1 的自定义格式和 A2 的数字格式，然后输出值类型。  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DatesAndTimes-SetDateTimeValue.js" >}}


输出结果：  
```  
A1 is Numeric Value: True  
Cell A1 contains a DateTime value.  
A2 is Numeric Value: True  
Cell A2 contains a DateTime value.  
```  

## **如何在 Aspose.Cells 中获取 DateTime 值**  
此示例在单元格 A1 和 A2 中设置 DateTime 值，设置 A1 的自定义格式和 A2 的数字格式，检查两个单元格的值类型，然后输出 DateTime 值和格式化字符串。  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DatesAndTimes-GetDateTimeValue.js" >}}


输出结果：  
```  
A1 is Numeric Value: True  
Cell A1 contains a DateTime value.  
A1 DateTime Value: 11/23/2023 5:59:09 PM  
A1 DateTime String Value: 11-23-23 17:59:09  
A2 is Numeric Value: True  
Cell A2 contains a DateTime value.  
A2 DateTime Value: 11/23/2023 5:59:09 PM  
A2 DateTime String Value: 11/23/2023 17:59  
```  

