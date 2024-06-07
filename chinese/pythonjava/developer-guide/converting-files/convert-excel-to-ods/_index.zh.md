---
title: 将Excel转换为ODS
type: docs
weight: 40
url: /zh/python-java/convert-excel-to-ods/
---

## **将Excel转换为ODS**
ODS文件是由Apache OpenOffice套件的Calc程序创建的。ODS文件存储以行和列组织的数据，并使用OASIS OpenDocument基于XML的标准进行格式化。

通过Java的Aspose.Cells支持工作ODS文件的Python。以下示例演示将Excel转换为ODS文件。
### **直接转换**
将Excel文件转换为ODS的最简单方法是通过将“SaveFormat.ODS”作为 [Workbook.save] 方法的第二个参数来加载工作簿并保存它。

以下代码片段演示了直接将Excel转换为ODS

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-ConvertingToODSFiles.py" >}}
### **将ODS文档保存在ODF 1.1或1.2规范中**
通过Java的Aspose.Cells支持保存ODS文件在ODF 1.1和ODF 1.2规范中。为此，API提供了OdsSaveOptions.setStrictSchema11()属性。将此属性设置为true将使用ODF 1.1规范保存文件。OdsSaveOptions.setStrictSchema11()的默认值为false，因此未经特殊设置保存的ODS文件将以ODF 1.2规范保存。

以下代码片段演示了使用ODF 1.1和1.2规范保存ODS文件。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-SaveODSFilesWithSpecifications.py" >}}
