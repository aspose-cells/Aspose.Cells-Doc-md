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
   Microsoft Query与Aspose.Cells.Report.Designer集成，并用作图形工具来创建数据源和查询。用户还可以利用包含数据源和查询的现有RDL文件进行操作。
1. **映射参数**。
   如果查询的SQL语句包括参数，用户必须创建报表参数并将SQL参数映射到报表参数。您可以在Aspose.Cells.Report.Designer中为报表参数指定有效值。
1. **设计Microsoft Excel报表模板内容、样式和格式**。
   Aspose.Cells报表模板可以包含以下类型的任意数量的报表项： 
   1. 表
   1. 数据透视表
   1. 图表
   1. 文本框
   1. 矩阵
      通常，查询（即DataSet）用作报表项的数据源。您还可以将Reporting Services参数、公式和全局变量用作某些报表项的数据源。报表项的样式和格式只需通过设置组成报表项的单元格的样式和格式来指定。
1. **发布报表**。
   在上述步骤之后，报告已准备好发布。用户可以指定报告发布到哪个文件夹。如果需要，您可以将 Report Server 上的共享数据源指定为报告的数据源。
1. **预览报告**。
   在 Report Server 上选择报告进行预览时，会提示您指定导出的文件格式（例如 Microsoft Excel 97-2003 二进制 XLS 格式、SpreadsheetML 或 Microsoft Excel 2007 XLSX 格式），以及在报告设计期间创建的任何输入报告参数。之后，报告将填充由 Reporting Services 提供的数据。
