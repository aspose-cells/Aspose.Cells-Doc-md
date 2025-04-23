---
title: تعديل اتصال بيانات SQL موجود باستخدام C++ مع Aspose.Cells
linktitle: تعديل اتصال بيانات SQL موجود
type: docs
weight: 20
url: /ar/cpp/modify-existing-sql-data-connection-using-aspose-cells/
description: تعلم كيفية تعديل اتصال بيانات SQL موجود في ملفات Excel باستخدام Aspose.Cells مع C++.
---

{{% alert color="primary" %}}

يدعم Aspose.Cells تعديل اتصال بيانات SQL موجود. ستوضح هذه المقالة كيفية استخدام Aspose.Cells لتعديل خصائص اتصال بيانات SQL مختلفة.

يمكنك إضافة أو رؤية اتصالات البيانات داخل Microsoft Excel باستخدام أمر القائمة الخاص بالبيانات > اتصالات.

وبالمثل، يوفر Aspose.Cells وسيلة للوصول إلى اتصالات البيانات وتعديلها باستخدام مجموعة `Workbook.DataConnections`.

{{% /alert %}}

## تعديل اتصال البيانات الحالي باستخدام Aspose.Cells

يوضح المثال التالي استخدام Aspose.Cells لتعديل اتصال البيانات الحالي للورقة العمل. يمكنك تنزيل ملف Excel المصدر المستخدم في هذا الكود وملف Excel الناتج الذي تم إنشاؤه بواسطة الشفرة من الروابط التالية.

- [ملف Excel المصدر](5112357.xlsx)
- [ملف Excel الناتج](5112356.xlsx)

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
