---
title: 使用LightCells API
type: docs
weight: 160
url: /zh/net/using-lightcells-api/
---

{{% alert color="primary" %}} 

有时您需要读取和写入大量数据或内容的大型Microsoft Excel文件。LightCells API适用于创建大型Excel电子表格：使用它，您需要更少的内存，并且获得更好的性能和效率。

{{% /alert %}} 
# 事件驱动架构
Aspose.Cells提供了LightCells API，主要设计用于在不构建完整数据模型块（使用单元格集合等）到内存中的情况下操作单元格数据。它以事件驱动模式工作。

保存工作簿时，在保存时逐个提供单元格内容，并且组件将其直接保存到输出文件。

在读取模板文件时，组件会逐个解析每个单元格并提供它们的值。

在这两种情况下，一个单元格对象会被处理然后丢弃，工作簿对象不会保留该集合。因此，在导入和导出包含大数据集的 Microsoft Excel 文件时，该模式能节省内存。

虽然 LightCells API 对 XLSX 和 XLS 文件的处理方式相同（实际上并不将所有单元格加载到内存中，而是处理一个单元格然后丢弃它），但对于 XLSX 文件比 XLS 文件更有效地节省了内存，因为这两种格式的数据模型和结构有所不同。

然而，对于 XLS 文件，为了节省更多内存，开发人员可以指定一个用于保存保存过程中生成的临时数据的临时位置。通常情况下，使用 LightCells API 来保存 XLSX 文件可以比使用常规方式节省50%或更多内存，而保存 XLS 可以节省大约20-40%的内存。
## 编写大型 Excel 文件
Aspose.Cells 提供了一个需要在您的程序中实现的接口 LightCellsDataProvider。该接口表示用于在轻量模式下保存大型电子表格文件的数据提供程序。

通过这种模式保存工作簿时，会在保存工作簿中的每个工作表时检查 StartSheet(int)。对于一个工作表，如果 StartSheet(int) 为 true，则由此实现提供要保存的该工作表中行和单元格的所有数据和属性。首先调用 NextRow() 来获取要保存的下一行索引。如果返回一个有效行索引（行索引必须按升序排列以便保存行），则由实现提供表示此行的 Row 对象以设置其属性 StartRow(Row)。

对于一行，首先检查 NextCell()。如果返回一个有效的列索引（对于要保存的一行的所有单元格，列索引必须按升序排序），则由实现提供表示该单元格的 Cell 对象以通过 StartCell(Cell) 设置其数据和属性。在设置完单元格的数据后，直接将单元格保存到生成的电子表格文件中，然后检查并处理下一个单元格。
### 编写大型 Excel 文件示例
请查看以下示例代码，了解 LightCells API 的工作方式。根据您的需要添加、删除或更新代码段。

该程序在一个工作表中创建了一个拥有 10,000 条（10000x30 矩阵）记录的巨大文件，并用虚拟数据填充。您可以通过更改 Main() 方法中的 rowsCount 和 colsCount 变量来指定自己的矩阵。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingLightCellsAPI-WritingLargeExcelFile.cs" >}}
## 读取大型 Excel 文件
Aspose.Cells 提供了一个需要在您的程序中实现的接口 LightCellsDataHandler。该接口表示用于在轻量模式下读取大型电子表格文件的数据提供程序。

通过这种模式读取工作簿时，会在读取工作簿中的每个工作表时检查 StartSheet。对于一个工作表，如果 StartSheet 返回 true，则由此接口的实现来检查和处理该工作表中行和列中单元格的所有数据和属性。对于每一行，首先调用 StartRow 来检查其是否需要处理。如果需要处理一行，则首先读取其属性，开发人员可以通过 ProcessRow 访问其属性。如果还需要处理该行的单元格，则 ProcessRow 应返回 true，然后对于该行中的每个现有单元格，都将调用 StartCell 来检查是否需要处理一个单元格。如果需要处理一个单元格，则将调用 ProcessCell 以由该接口的实现来处理单元格。
### 读取大型 Excel 文件示例
请查看以下示例代码，了解 LightCells API 的工作方式。根据您的需要添加、删除或更新代码段。

该程序读取一个工作表中有数百万条记录的巨大文件。在读取工作簿的每个工作表时都需要一些时间。示例代码读取文件并获取每个工作表中的单元格总数、字符串计数和公式计数。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingLightCellsAPI-ReadingLargeExcelFile.cs" >}}
