---
title: 从文档中导入数据
type: docs
weight: 20
url: /zh/net/import-data-from-document/
---

数据是原始事实的集合，我们创建电子表格文档或报告来以更有意义的方式呈现这些原始事实。通常，我们自己添加数据到电子表格中，但有时我们需要重复使用现有的数据资源，这时就需要从不同的数据源导入数据到电子表格中。在本主题中，我们将讨论一些从不同数据源导入数据到工作表的技术。

**使用Aspose.Cells导入数据** 
当您使用**Aspose.Cells**打开Excel文件时，文件中的所有数据都会被自动导入，但Aspose.Cells还支持从不同的数据源导入数据。以下列出了一些这些数据源：

- **数组**
- **ArrayList**
- **DataTable**
- **DataColumn**
- **DataView**
- **DataGrid**
- **DataReader**
- **GridView**

Aspose.Cells提供了一个名为Workbook的类，代表一个Excel文件。Workbook类包含一个Worksheets集合，允许访问Excel文件中的每个工作表。工作表由Worksheet类表示。Worksheet类提供了一个Cells集合。

Cells集合提供了非常有用的方法，用于从不同的数据源导入数据。

本节包括以下主题：

- [从数组导入](/cells/zh/net/importing-from-array/)
- [从ArrayList导入](/cells/zh/net/importing-from-arraylist/)
- [从自定义对象导入](/cells/zh/net/importing-from-custom-objects/)
- [从DataTable导入](/cells/zh/net/importing-from-datatable/)
