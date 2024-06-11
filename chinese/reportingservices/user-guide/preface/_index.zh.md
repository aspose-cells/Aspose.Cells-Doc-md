---
title: 前言
type: docs
weight: 20
url: /zh/reportingservices/preface/
---

{{% alert color="primary" %}} 

Aspose.Cells for Reporting Services主要包含两个组件：Aspose.Cells.Report.Designer和Aspose.Cells.Renderer for Reporting Services。前者用于直接在Microsoft Excel中设计报表，后者负责将RDL报表呈现到Microsoft Excel。 

{{% /alert %}} 
### **使用报表设计器设计报表**
使用Aspose.Cells.Report.Designer设计报表的主要步骤是：

1. **创建数据源和查询**。
   Microsoft Query与Aspose.Cells.Report.Designer集成，用作创建数据源和查询的图形工具。 用户还可以利用现有的带有数据源和查询的RDL文件进行操作。
1. **映射参数**。
   如果查询的 SQL 语句包含参数，用户必须创建报表参数并将 SQL 参数映射到报表参数。您可以在 Aspose.Cells.Report.Designer 中为报表参数指定有效值。
1. **设计 Microsoft Excel 报表模板内容、样式和格式**。
   Aspose.Cells 报表模板可以包含以下任意类型的报表项： 
   1. 表格
   1. 透视表
   1. 图表
   1. 文本框
   1. 矩阵
      通常查询（即 DataSet）用作报告项的数据源。您还可以将 Reporting Services 参数、公式和全局变量用作某些类型报表项的数据源。报表项的样式和格式简单地通过设置构成报表项的单元格的样式和格式来指定。
1. **发布报表**。
   完成上述步骤后，报表已准备好发布。用户可以指定将报表发布到哪个文件夹。如有需要，您可以将报表服务器上的共享数据源指定为报表的数据源。
1. **预览报表**。
   在报表服务器上选择预览报表时，会提示您指定要将其导出为哪种文件格式（例如 Microsoft Excel 97-2003 二进制 XLS 格式、SpreadsheetML 或 Microsoft Excel 2007 XLSX 格式），以及在报表设计期间生成的任何输入报表参数。完成后，报表将填充由 Reporting Services 提供的数据。
