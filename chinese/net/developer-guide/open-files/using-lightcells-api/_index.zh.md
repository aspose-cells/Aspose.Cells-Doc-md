---
title: 使用 LightCells API
type: docs
weight: 160
url: /zh/net/using-lightcells-api/
---
{{% alert color="primary" %}} 

有时您需要读取和写入工作表中包含大量数据或内容的大型 Microsoft Excel 文件。 LightCells API 对于创建大型 Excel 电子表格非常有用：有了它，您需要更少的内存并获得更好的性能和效率。

{{% /alert %}} 
# 事件驱动架构
Aspose.Cells 提供了LightCells API，主要是用来对cell数据进行逐个操作，而不需要将完整的数据模型块（使用Cell集合等）构建到内存中。它以事件驱动模式工作。

保存工作簿时，保存时逐格提供单元格内容，组件直接保存到输出文件中。

读取模板文件时，组件会解析每个单元格并一一提供它们的值。

在这两个过程中，一个 Cell 对象被处理然后被丢弃，Workbook 对象不保存集合。因此，在这种模式下，导入和导出具有大量数据集的 Microsoft Excel 文件时会节省内存，否则会占用大量内存。

即使 LightCells API 以相同的方式处理 XLSX 和 XLS 文件的单元格（它实际上并不将所有单元格加载到内存中，而是处理一个单元格然后丢弃它），它比 XLS 文件更有效地为 XLSX 文件节省内存，因为两种格式的不同数据模型和结构。

然而，**对于 XLS 文件**，为了节省更多的内存，开发者可以指定一个临时位置来保存Save过程中产生的临时数据。通常，**使用 LightCells API 保存 XLSX 文件可节省 50% 或更多内存**比使用常见的方式，**保存 XLS 可能会节省大约 20-40% 的内存**.
## 编写大型 Excel 文件
Aspose.Cells 提供一个接口，LightCellsDataProvider，需要在你的程序中实现。该接口表示用于以轻量级模式保存大型电子表格文件的数据提供者。

使用此模式保存工作簿时，在保存工作簿中的每个工作表时都会检查 StartSheet(int)。对于一张工作表，如果 StartSheet(int) 为真，则此工作表要保存的所有行和单元格的数据和属性均由此实现提供。首先，调用 NextRow() 以获取要保存的下一行索引。如果返回有效的行索引（行索引必须按升序排列才能保存行），则提供表示该行的 Row 对象供实现，以通过 StartRow(Row) 设置其属性。

对于一行，首先检查 NextCell()。如果返回有效的列索引（列索引必须按升序排列才能保存一行的所有单元格），则提供表示该单元格的 Cell 对象以供实现，以通过 StartCell(Cell) 设置其数据和属性。设置好单元格的数据后，直接将该单元格保存到生成的电子表格文件中，检查下一个单元格并进行处理。
### 编写大型 Excel 文件：示例
请查看以下示例代码以查看 LightCells API 的工作情况。根据您的需要添加和删除或更新代码段。

该程序创建了一个巨大的文件**10,000（10000x30 矩阵）条记录**在工作表中并用虚拟数据填充它们。您可以通过更改 Main() 方法中的 rowsCount 和 colsCount 变量来指定自己的矩阵。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingLightCellsAPI-WritingLargeExcelFile.cs" >}}
## 读取大型 Excel 文件
Aspose.Cells提供了一个接口LightCellsDataHandler，需要在你的程序中实现。该接口表示用于以轻量级模式读取大型电子表格文件的数据提供程序。

在这种模式下阅读工作簿时，会在阅读工作簿中的每个工作表时检查 StartSheet。对于一个工作表，如果StartSheet返回true，则该工作表的行和列中单元格的所有数据和属性都将通过该接口的实现进行检查和处理。对于每一行，都会调用 StartRow 来检查它是否需要处理。如果需要处理一行，则首先读取其属性，开发人员可以使用 ProcessRow 访问其属性。如果该行的单元格也需要处理，则 ProcessRow 应返回 true，然后为该行中的每个现有单元格调用 StartCell 以检查是否有一个单元格需要处理。如果需要处理一个单元格，则通过该接口的实现调用ProcessCell来处理该单元格。
### 读取大型 Excel 文件：示例
请查看以下示例代码以查看 LightCells API 的工作情况。根据您的需要添加和删除或更新代码段。

该程序读取工作表中包含数百万条记录的巨大文件。阅读工作簿中的每张纸需要一点时间。示例代码读取文件并检索每个工作表中的单元格总数、字符串计数和公式计数。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingLightCellsAPI-ReadingLargeExcelFile.cs" >}}
