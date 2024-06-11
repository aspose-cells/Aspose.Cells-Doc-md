---
title: 使用 LightCells API
type: docs
weight: 160
url: /zh/net/using-lightcells-api/
---

{{% alert color="primary" %}} 

有时您需要读写大量数据或工作表中的大量内容的大型Microsoft Excel文件。LightCells API 用于创建巨大的Excel电子表格非常有用：使用它，您需要更少的内存，并获得更好的性能和效率。

{{% /alert %}} 
# 事件驱动架构
Aspose.Cells 提供 LightCells API，主要设计用于逐个处理单元格数据，而无需将完整的数据模型块（使用 Cell 集合等）构建到内存中。它以事件驱动模式工作。

在保存工作簿时，保存组件会直接提供逐个单元格的单元格内容，然后将其保存到输出文件。

在读取模板文件时，组件会解析每个单元格，并逐个提供它们的值。

在这两个过程中，处理一个 Cell 对象然后丢弃它，Workbook 对象不会保留集合。因此，在导入和导出具有大数据集的 Microsoft Excel 文件时，将节省内存。

即使 LightCells API 在 XLSX 和 XLS 文件上以相同的方式处理单元格（它实际上并不将所有单元格加载到内存中，而是处理一个单元格然后丢弃它），但它对于 XLSX 文件比 XLS 文件更有效地节省内存，因为这两种格式的数据模型和结构不同。

但是，**对于 XLS 文件**，为了节省更多内存，开发人员可以指定在保存过程中保存生成的临时数据的临时位置。通常情况下，**使用 LightCells API 保存 XLSX 文件可能节省50%或更多内存**，**保存 XLS 可能节省大约20-40%内存**。
## 写一个大型的Excel文件
Aspose.Cells 提供了 LightCellsDataProvider 接口，需要在您的程序中实现。该接口表示大型电子表格文件的数据提供程序，以轻量级模式保存。

在通过此模式保存工作簿时，在保存工作簿中的每个工作表时都会检查 StartSheet(int)。对于一个工作表，如果 StartSheet(int) 为 true，则提供要保存的这个工作表的所有行和单元格的数据和属性。首先，调用 NextRow() 获取要保存的下一个行索引。如果返回有效的行索引（行索引必须按升序排列以保存行），则为实现提供代表该行的 Row 对象以设置其属性。

对于一个行，首先检查 NextCell()。如果返回有效的列索引（列索引必须按升序排列，以保存一行的所有单元格），则提供表示该单元格的 Cell 对象以由 StartCell(Cell) 设置其数据和属性。设置单元格的数据后，直接将单元格保存到生成的电子表格文件中，然后检查并处理下一个单元格。
### 读取大型Excel文件：示例
请查看以下示例代码，了解LightCells API的工作方式。根据您的需求添加和删除或更新代码段。

该程序在工作表中创建一个大型文件，其中有**10,000（10000x30矩阵）条记录**，并填充它们以虚拟数据。您可以通过更改 Main() 方法中的 rowsCount 和 colsCount 变量来指定自己的矩阵。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingLightCellsAPI-WritingLargeExcelFile.cs" >}}
## 读取大型Excel文件
Aspose.Cells 提供了一个接口，LightCellsDataHandler，需要在您的程序中实现。该接口表示用于以轻量级模式读取大型电子表格文件的数据提供程序。

在此模式下读取工作簿时，在读取工作簿中的每个工作表时都会检查StartSheet。 对于工作表，如果StartSheet返回true，则会检查并处理工作表的行和列中单元格的所有数据和属性，并由此接口的实现进行处理。对于每行，都会调用StartRow来检查是否需要处理。如果需要处理一行，则首先读取其属性，并且开发人员可以使用ProcessRow访问其属性。如果还需要处理该行的单元格，则ProcessRow应返回true，然后针对行中每个现有单元格调用StartCell来检查是否需要处理一个单元格。如果需要处理一个单元格，则调用ProcessCell来通过此接口的实现处理该单元格。
### 读取大型Excel文件示例
请查看以下示例代码，了解LightCells API的工作方式。根据您的需求添加和删除或更新代码段。

该程序读取一个worksheet中的数百万条记录的大文件。每个工作表的读取都需要一些时间。示例代码读取文件并检索每个工作表中的单元格总数，字符串计数和公式计数。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingLightCellsAPI-ReadingLargeExcelFile.cs" >}}
