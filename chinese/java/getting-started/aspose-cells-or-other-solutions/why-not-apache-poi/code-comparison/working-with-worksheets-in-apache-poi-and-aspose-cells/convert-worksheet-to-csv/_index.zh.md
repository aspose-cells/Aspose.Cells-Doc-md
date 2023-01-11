﻿---
title: 将工作表转换为 CSV
type: docs
weight: 30
url: /zh/java/convert-worksheet-to-csv/
---
## **Aspose.Cells - 将工作表转换为 CSV**
如果开发人员需要将他们的文件保存到某个存储位置，那么他们可以简单地指定文件名（及其完整的存储路径）和所需的文件格式（使用**文件格式类型**枚举），同时调用**救球**的方法**工作簿**目的。

**Java**

{{< highlight "java" >}}

 //Instantiate a new workbook with Excel file path

Workbook workbook = new Workbook(dataPath + "workbook.xls");

//Save the document in PDF format

workbook.save(dataPath + "AsposeWorkbookCSV.csv", SaveFormat.CSV);

{{< /highlight >}}
## **Apache POI SS - HSSF 和 XSSF - 将工作表转换为 CSV**
下面的代码显示了如何使用 Apache POI HSSF 和 XSSF 将工作表转换为 CSV API 与 Aspose.Cells Java API 相比。

**Java**

{{< highlight "java" >}}

 /**

\* 一个基本的 XLSX -> CSV 处理器仿照

\* Nick Burch 的 POI 示例程序 XLS2CSVmra 来自

\* 包 org.apache.poi.hssf.eventusermodel.examples。

\* 与 HSSF 版本不同，这个完全忽略了

\* 缺少行。

\* <p/>

\* 使用 SAX 解析器读取数据表以保持

\* 内存占用比较小，所以应该这样

\* 能够阅读大量的工作簿。样式表和

\* 共享字符串表必须保存在内存中。这

\* 使用标准 POI 样式表类，但自定义

\*（只读）类用于共享字符串表

\* 因为标准 POI SharedStringsTable 增长非常快

\* 快速添加唯一字符串的数量。

\* <p/>

\* 感谢 Eric Smith 提供的修复问题的补丁

\* 由具有多个“t”元素的单元格触发，即

\* Excel 如何表示不同的格式（例如，一个单词

\* 普通和一个单词粗体）。

\*

\* @author 克里斯·洛特

*/

public class ApacheXLSX2CSV {