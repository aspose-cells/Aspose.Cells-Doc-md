---
title: 将Excel转换为ODS
type: docs
weight: 40
url: /zh/python-java/convert-excel-to-ods/
---

## **将Excel转换为ODS**
ODS文件是由Apache OpenOffice套件的Calc程序创建的。ODS文件存储以行和列组织的数据，并使用OASIS OpenDocument基于XML的标准进行格式化。

Aspose.Cells for Python via Java支持处理ODS文件。以下示例演示了将Excel转换为ODS文件。
### **直接转换**
将Excel文件转换为ODS的最简单方法是加载工作簿并通过将[SaveFormat.ODS](https://reference.aspose.com/cells/python/asposecells.api/saveformat#ODS)作为[Workbook.save](https://reference.aspose.com/cells/python/asposecells.api/workbook#save\(java.lang.String,%20int\))方法的第二个参数进行保存。

以下代码片段演示了将Excel直接转换为ODS

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-ConvertingToODSFiles.py" >}}
### **将ODS文档保存在ODF 1.1或1.2规范中**
Aspose.Cells for Python via Java支持在ODF 1.1和ODF 1.2规范中保存ODS文件。为此，API提供[OdsSaveOptions.setStrictSchema11()](https://reference.aspose.com/cells/python/asposecells.api/odssaveoptions#IsStrictSchema11)属性。将此属性设置为**true**将使用ODF 1.1规范保存文件。[OdsSaveOptions.setStrictSchema11()](https://reference.aspose.com/cells/python/asposecells.api/odssaveoptions#IsStrictSchema11)的默认值为**false**，因此没有特殊设置保存的ODS文件将使用ODF 1.2规范保存。

以下代码片段演示了使用ODF 1.1和1.2规范保存ODS文件。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-SaveODSFilesWithSpecifications.py" >}}
