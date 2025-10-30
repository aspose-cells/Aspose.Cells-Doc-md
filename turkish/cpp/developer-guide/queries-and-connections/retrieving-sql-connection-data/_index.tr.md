---
title: SQL Bağlantı Verilerini C++ ile Alma
linktitle: SQL Bağlantı Verilerini Almak
type: docs
weight: 10
url: /tr/cpp/retrieving-sql-connection-data/
description: Aspose.Cells for C++ kullanarak SQL bağlantı verilerini, sunucu URL si, kullanıcı adı, tablo adı ve daha fazlasını nasıl alacağınızı öğrenin.
---

{{% alert color="primary" %}}

Aspose.Cells, SQL bağlantı verilerini almanıza yardımcı olabilir. Bu, SQL sunucusuna bağlantı kurmak için gereken tüm veriyi içerir; örneğin, **sunucu URL'si**, **kullanıcı adı**, **tablo adı**, **tam SQL sorgusu**, **sorgu türü**, **tablonun yeri** ve onunla ilişkilendirilmiş **adlandırılmış aralığın adı**.

{{% /alert %}}

Microsoft Excel'de, bir veritabanına bağlanmak için:

1. **Veri** menüsünü tıklayın ve **Diğer Kaynaklardan, SQL Server'dan** ardından **Veri Al**'ı seçin.
1. Ardından **Veri**'yi ve ardından **Bağlantılar**'ı seçin.
1. Bağlantı sihirbazını kullanarak veritabanına bağlanın ve bir veritabanı sorgusu oluşturun.

Aspose.Cells, dış bağlantıları almak için `Workbook::get_DataConnections()` metodunu sağlar. Bu, çalışma kitabındaki `ExternalConnection` nesneleri koleksiyonunu döndürür.

`ExternalConnection` nesnesi SQL bağlantı verilerini içeriyorsa, bu nesne `DBConnection` nesnesine dönüştürülebilir ve özellikleri kullanılarak veritabanı komutu, komut türü, bağlantı açıklaması, bağlantı bilgileri, kimlik bilgileri ve benzeri alınabilir.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::ExternalConnections;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create a workbook object from source file
    Workbook workbook(srcDir + u"connection.xlsx");

    // Access the external collections
    ExternalConnectionCollection connections = workbook.GetDataConnections();

    int connectionCount = connections.GetCount();

    ExternalConnection connection;

    for (int i = 0; i < connectionCount; i++)
    {
        connection = connections.Get(i);

        // Check if the Connection is DBConnection, then retrieve its various properties
        if (connection.GetClassType() == ExternalConnectionClassType::Database)
        {
            DBConnection dbConn = static_cast<DBConnection&>(connection);

            // Retrieve DB Connection Command
            std::cout << "Command: " << dbConn.GetCommand().ToUtf8() << std::endl;

            // Retrieve DB Connection Command Type
            std::cout << "Command Type: " << static_cast<int>(dbConn.GetCommandType()) << std::endl;

            // Retrieve DB Connection Description
            std::cout << "Description: " << dbConn.GetConnectionDescription().ToUtf8() << std::endl;

            // Retrieve DB Connection ID
            std::cout << "Id: " << dbConn.GetId() << std::endl;

            // Retrieve DB Connection Info
            std::cout << "Info: " << dbConn.GetConnectionString().ToUtf8() << std::endl;

            // Retrieve DB Connection Credentials
            std::cout << "Credentials: " << static_cast<int>(dbConn.GetCredentialsMethodType()) << std::endl;

            // Retrieve DB Connection Name
            std::cout << "Name: " << dbConn.GetName().ToUtf8() << std::endl;

            // Retrieve DB Connection ODC File
            std::cout << "OdcFile: " << dbConn.GetOdcFile().ToUtf8() << std::endl;

            // Retrieve DB Connection Source File
            std::cout << "Source file: " << dbConn.GetSourceFile().ToUtf8() << std::endl;

            // Retrieve DB Connection Type
            std::cout << "Type: " << static_cast<int>(dbConn.GetSourceType()) << std::endl;

            // Retrieve DB Connection Parameters Collection
            ConnectionParameterCollection paramCollection = dbConn.GetParameters();

            int paramCount = paramCollection.GetCount();

            // Iterate the Parameter Collection
            for (int j = 0; j < paramCount; j++)
            {
                ConnectionParameter param = paramCollection.Get(j);

                // Retrieve Parameter Cell Reference
                std::cout << "Cell reference: " << param.GetCellReference().ToUtf8() << std::endl;

                // Retrieve Parameter Name
                std::cout << "Parameter name: " << param.GetName().ToUtf8() << std::endl;

                // Retrieve Parameter Prompt
                std::cout << "Prompt: " << param.GetPrompt().ToUtf8() << std::endl;

                // Retrieve Parameter SQL Type
                std::cout << "SQL Type: " << static_cast<int>(param.GetSqlType()) << std::endl;

                // Retrieve Parameter Type
                std::cout << "Param Type: " << static_cast<int>(param.GetType()) << std::endl;

                // Retrieve Parameter Value
                std::cout << "Param Value: " << param.GetValue().ToString().ToUtf8() << std::endl;

            } // End for
        } // End if
    } // End for

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
