---
title: 前言
type: docs
weight: 20
url: /zh/reportingservices/preface/
---
{{% alert color="primary" %}} 

Reporting Services 的 Aspose.Cells 主要包含两个组件：Aspose.Cells.Report.Designer 和 Aspose.Cells.Renderer for Reporting Services。前者用于直接在Microsoft Excel中设计报表，后者负责渲染一个RDL报表到Microsoft Excel。

{{% /alert %}} 
### **使用报表设计器设计报表**
使用 Aspose.Cells.Report.Designer 设计报表的主要步骤是：

1. **创建数据源和查询**.
Microsoft Query 与 Aspose.Cells.Report.Designer 集成，用作创建数据源和查询的图形工具。用户还可以利用现有的 RDL 文件，其中的数据源和查询可用于操作。
1. **地图参数**.
如果查询的SQL语句中包含参数，用户需要创建报表参数并将SQL参数映射到报表参数。您可以在 Aspose.Cells.Report.Designer 中为报表参数指定有效值。
1. **设计 Microsoft Excel 报告模板内容、样式和格式**.
Aspose.Cells 报告模板可能包含任意数量的以下类型的报告项目：
 1.表
1.数据透视表
1.图表
1.文本框
1.矩阵
通常，查询（即 DataSet）用作报表项的数据源。您还可以使用 Reporting Services 参数、公式和全局变量作为某些类型的报表项的数据源。报表项的样式和格式只需设置组成报表项的单元格的样式和格式即可指定。
1. **发布报告**.
完成上述步骤后，报告就可以发布了。用户可以指定将报告发布到哪个文件夹。如果需要，您可以在报表服务器上指定一个共享数据源作为报表的数据源。
1. **预览报告**.
在报表服务器上选择要预览的报表时，系统会提示您指定要将其导出到的文件格式（例如 Microsoft Excel 97-2003 二进制 XLS 格式、SpreadsheetML 或 Microsoft Excel 2007 XLSX 格式），以及创建的任何输入报表参数在报表设计过程中。在此之后，报表将填充 Reporting Services 提供的数据。
