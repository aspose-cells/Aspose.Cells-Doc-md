---
title: 将 Excel 转换为 ODS
type: docs
weight: 40
url: /zh/python-java/convert-excel-to-ods/
---
## **将 Excel 转换为 ODS**
ODS 文件由 Calc 程序创建，该程序是 Apache OpenOffice 套件的一部分。 ODS 文件存储按行和列组织的数据，并使用基于 OASIS OpenDocument XML 的标准进行格式化。

Aspose.Cells for Python via Java 支持工作 ODS 文件。以下示例演示将 Excel 转换为 ODS 文件。
### **直接转换**
将 Excel 文件转换为 ODS 的最简单方法是加载工作簿并通过传递[保存格式.ODS](https://reference.aspose.com/cells/python/asposecells.api/saveformat#ODS)作为第二个参数[工作簿.保存](https://reference.aspose.com/cells/python/asposecells.api/workbook#save\(java.lang.String,%20int\)） 方法。

以下代码片段演示了将 Excel 直接转换为 ODS

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-ConvertingToODSFiles.py" >}}
### **将 ODS 文档保存为 ODF 1.1 或 1.2 规范**
Aspose.Cells for Python via Java支持以ODF 1.1和ODF 1.2规范保存ODS文件。为此，API 提供[OdsSaveOptions.setStrictSchema11()](https://reference.aspose.com/cells/python/asposecells.api/odssaveoptions#IsStrictSchema11)财产。将此属性设置为**真的**将使用 ODF 1.1 规范保存文件。默认值[OdsSaveOptions.setStrictSchema11()](https://reference.aspose.com/cells/python/asposecells.api/odssaveoptions#IsStrictSchema11)是**错误的**所以没有特殊设置保存的ODS文件是用ODF 1.2规范保存的。

以下代码片段演示了如何使用 ODF 1.1 和 1.2 规范保存 ODS 文件。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-SaveODSFilesWithSpecifications.py" >}}
