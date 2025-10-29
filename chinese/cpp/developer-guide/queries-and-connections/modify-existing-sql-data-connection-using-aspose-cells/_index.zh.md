---
title: 使用Aspose.Cells用C++修改现有SQL数据连接
linktitle: 修改现有SQL数据连接
type: docs
weight: 20
url: /zh/cpp/modify-existing-sql-data-connection-using-aspose-cells/
description: 学习如何使用Aspose.Cells和C++修改Excel文件中的现有SQL数据连接。
---

{{% alert color="primary" %}}

Aspose.Cells支持修改现有SQL数据连接。本文将介绍如何使用Aspose.Cells修改不同的SQL数据连接属性。

你可以通过**数据 > 连接**菜单命令在Microsoft Excel中添加或查看数据连接。

同样，Aspose.Cells提供了访问和修改数据连接的方法，使用`Workbook.DataConnections`集合。

{{% /alert %}}

## 使用Aspose.Cells修改现有的SQL数据连接

以下示例说明了如何使用Aspose.Cells修改工作簿的SQL数据连接。你可以从以下链接下载用于此代码的源Excel文件和代码生成的输出Excel文件。

- [源Excel文件](5112357.xlsx)
- [输出Excel文件](5112356.xlsx)

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"DataConnection.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output_out.xlsx";

    // Create workbook object
    Workbook workbook(inputFilePath);

    // Access first Data Connection
    ExternalConnection conn = workbook.GetDataConnections().Get(0);

    // Change the Data Connection Name and Odc file
    conn.SetName(u"MyConnectionName");
    conn.SetOdcFile(u"C:\\Users\\MyDefaulConnection.odc");

    // Change the Command Type, Command and Connection String
    DBConnection dbConn = conn;
    dbConn.SetCommandType(OLEDBCommandType::SqlStatement);
    dbConn.SetCommand(u"Select * from AdminTable");
    dbConn.SetConnectionString(u"Server=myServerAddress;Database=myDataBase;User ID=myUsername;Password=myPassword;Trusted_Connection=False");

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Data connection updated successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
