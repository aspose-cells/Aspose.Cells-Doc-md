---
title: Изменить существующее соединение с SQL данными с помощью C++ и Aspose.Cells
linktitle: Изменить существующее соединение с SQL данными
type: docs
weight: 20
url: /ru/cpp/modify-existing-sql-data-connection-using-aspose-cells/
description: Узнайте, как изменить существующее соединение с SQL данными в файлах Excel с помощью Aspose.Cells и C++.
---

{{% alert color="primary" %}}

Aspose.Cells поддерживает изменение существующего соединения с SQL-данными. В этой статье объясняется, как использовать Aspose.Cells для изменения различных свойств соединения с SQL-данными.

Вы можете добавить или просмотреть соединения с данными внутри Microsoft Excel, следуя команде меню **Данные > Соединения**.

Аналогично, Aspose.Cells предоставляет средства для доступа и изменения соединений данных с помощью коллекции `Workbook.DataConnections`.

{{% /alert %}}

## Изменение существующего SQL-соединения с данными с использованием Aspose.Cells

Следующий пример иллюстрирует использование Aspose.Cells для изменения SQL-соединения данных в книге Excel. Вы можете загрузить исходный файл Excel, используемый в этом коде, и выходной файл Excel, сгенерированный кодом, по следующим ссылкам.

- [Исходный файл Excel](5112357.xlsx)
- [Выходной файл Excel](5112356.xlsx)

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
