---
title: استرجاع بيانات اتصال SQL باستخدام C++
linktitle: إسترداد بيانات اتصال SQL
type: docs
weight: 10
url: /ar/cpp/retrieving-sql-connection-data/
description: تعلم كيفية استرجاع بيانات اتصال SQL، بما في ذلك عنوان الخادم، اسم المستخدم، اسم الجدول، والمزيد باستخدام Aspose.Cells for C++.
---

{{% alert color="primary" %}}

يمكن لـ Aspose.Cells مساعدتك في استرداد بيانات اتصال SQL. يشمل ذلك أي وكل البيانات المطلوبة للاتصال بخادم SQL، على سبيل المثال، **رابط الخادم**, **اسم المستخدم**, **اسم الجدول**, **استعلام SQL كامل**, **نوع الاستعلام**, **موقع الجدول**, و**اسم النطاق المسمى** المرتبط به.

{{% /alert %}}

في برنامج Microsoft Excel، الاتصال بقاعدة بيانات عن طريق:

1. النقر على القائمة **البيانات** واختيار **من مصادر أخرى** تلاها **من خادم SQL**.
1. ثم اختيار **البيانات** تلاها **اتصالات**.
1. استخدام معالج الاتصالات للاتصال بقاعدة البيانات وإنشاء استعلام قاعدة البيانات.

يوفر Aspose.Cells طريقة `Workbook::get_DataConnections()` لاسترجاع الاتصالات الخارجية. تُرجع مجموعة من كائنات `ExternalConnection` في ملف العمل.

إذا احتوى كائن `ExternalConnection` على بيانات اتصال SQL، يمكن تحويله إلى كائن `DBConnection` واستخدام خصائصه لاسترجاع أمر قاعدة البيانات، نوع الأمر، وصف الاتصال، معلومات الاتصال، بيانات الاعتماد، وغيرها.

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
