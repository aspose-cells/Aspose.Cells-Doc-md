---
title: قراءة وكتابة الاتصال الخارجي لملفات XLS و XLSB باستخدام C++
linktitle: قراءة وكتابة اتصال الخارجي لملفات XLS و XLSB
type: docs
weight: 80
url: /ar/cpp/read-and-write-external-connection-of-xls-and-xlsb-files/
description: تعلم كيفية قراءة وتعديل اتصالات قواعد البيانات الخارجية في ملفات XLS/XLSB باستخدام Aspose.Cells for C++.
---

## **سيناريوهات الاستخدام المحتملة**

يدعم Aspose.Cells for C++ قراءة وكتابة الاتصالات الخارجية لملفات XLSX ويوسع الآن هذه القدرة إلى تنسيق XLSB و XLS. نفس هيكل الكود يعمل لجميع أنواع الملفات المدعومة.

## **قراءة وكتابة اتصال خارجي لملف XLS/XLSB**

يعرض الكود النموذجي التالي تحميل ملف XLSB نموذجي (يعمل أيضًا مع XLS) وتعديل أول اتصال خارجي به (عادةً اتصال قاعدة بيانات Microsoft Access). يُظهر الكود كيفية:

1. تحميل ملف الجدولة الإلكترونية
2. الوصول إلى الاتصالات الخارجية
3. تعديل خصائص الاتصال
4. حفظ الملف المعدل

![todo:image_alt_text](read-and-write-external-connection-of-xls-and-xlsb-files_1.png)

## **الكود المثالي**

يعمل هذا الكود لكل من ملفات XLSB و XLS عن طريق تعديل امتدادات الملفات المدخلة/المخرجة.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directories
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // File paths
    U16String inputFilePath = srcDir + u"sampleExternalConnection_XLSB.xlsb";
    U16String outputFilePath = outDir + u"outputExternalConnection_XLSB.xlsb";

    // Load source workbook
    Workbook workbook(inputFilePath);

    // Get first external connection
    ExternalConnectionCollection connections = workbook.GetDataConnections();
    DBConnection dbCon = connections.Get(0);

    // Print connection details
    std::cout << "Connection Name: " << dbCon.GetName().ToUtf8() << std::endl;
    std::cout << "Command: " << dbCon.GetCommand().ToUtf8() << std::endl;
    std::cout << "Connection Info: " << dbCon.GetConnectionString().ToUtf8() << std::endl;

    // Modify connection name
    dbCon.SetName(u"NewCust");

    // Save modified workbook
    workbook.Save(outputFilePath);

    std::cout << "External connection updated successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

**مكافئ C++:**

```cpp
#include <iostream>
#include <Aspose.Cells.h>

using namespace Aspose::Cells;
using namespace Aspose::Cells::ExternalConnections;

int main() {
    Aspose::Cells::Startup();
    // Load source workbook
    Workbook workbook(u"source.xlsb");
    // Access first external connection
    DBConnection conn(workbook.GetDataConnections().Get(0));

    // Output original connection details
    std::cout << "Connection Name: " << conn.GetName().ToUtf8() << std::endl;
    std::cout << "Command: " << conn.GetCommand().ToUtf8() << std::endl;
    std::cout << "Connection Info: " << conn.GetConnectionInfo().ToUtf8() << std::endl;

    // Modify connection name
    conn.SetName(u"Cust_Modified");

    // Save updated workbook
    workbook.Save(u"output.xlsb");
    Aspose::Cells::Cleanup();
    return 0;

}
```

## **مخرجات الوحدة**

{{< highlight cpp >}}
Connection Name: Cust
Command: Customer
Connection Info: Provider=Microsoft.ACE.OLEDB.12.0;Password="";User ID=Admin;Data Source=C:\TempSha\Cust.accdb;Mode=Share Deny Write;Extended Properties="";Jet OLEDB:System database="";Jet OLEDB:Registry Path="";Jet OLEDB:Database Password="";Jet OLEDB:Engine Type=6;Jet OLEDB:Database Locking Mode=0;Jet OLEDB:Global Partial Bulk Ops=2;Jet OLEDB:Global Bulk Transactions=1;Jet OLEDB:New Database Password="";Jet OLEDB:Create System Database=False;Jet OLEDB:Encrypt Database=False;Jet OLEDB:Don't Copy Locale on Compact=False;Jet OLEDB:Compact Without Replica Repair=False;Jet OLEDB:SFP=False;Jet OLEDB:Support Complex Data=False;Jet OLEDB:Bypass UserInfo Validation=False;Jet OLEDB:Limited DB Caching=False;Jet OLEDB:Bypass ChoiceField Validation=False
{{< /highlight >}}
