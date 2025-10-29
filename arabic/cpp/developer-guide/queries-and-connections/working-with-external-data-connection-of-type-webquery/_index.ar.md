---
title: العمل مع اتصال البيانات الخارجي من نوع WebQuery باستخدام C++
linktitle: العمل مع اتصال البيانات الخارجية من نوع الاستعلام عبر الويب
type: docs
weight: 30
url: /ar/cpp/working-with-external-data-connection-of-type-webquery/
description: تعلم كيفية العمل مع اتصال بيانات WebQuery في مايكروسوفت إكسل باستخدام Aspose.Cells مع C++.
---

{{% alert color="primary" %}}

يمكنك الوصول إلى اتصال البيانات الخارجية من أي نوع باستخدام مجموعة Workbook.DataConnections. نوع واحد من هذا النوع من اتصال البيانات هو استعلام الويب. سيوضح هذا المقال كيفية العمل مع اتصال بيانات استعلام الويب. يمكنك إنشاء اتصال بيانات استعلام الويب في برنامج Microsoft Excel باستخدام القائمة **البيانات** > **من الويب**.

{{% /alert %}}

## العمل مع اتصال البيانات الخارجية من نوع WebQuery

الكود التالي يوضح كيفية العمل مع اتصال البيانات الخارجية من نوع **WebQuery**. يستخدم [ملف الإكسل عينة](5112365.xlsx) الذي يمكنك تنزيله من الرابط المقدم. يمكنك أيضًا رؤية مخرجات الوحدة (console output) لهذا الكود فيما بعد.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::ExternalConnections;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"WebQuerySample.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the first external connection from the workbook
    ExternalConnection connection = workbook.GetDataConnections().Get(0);

    // Check if the connection is a WebQueryConnection
    if (connection.GetClassType() == ExternalConnectionClassType::WebQuery)
    {
        // Cast to WebQueryConnection
        WebQueryConnection webQuery(connection);

        // Print the URL of the web query
        std::cout << "Web Query URL: " << webQuery.GetUrl().ToUtf8() << std::endl;
    }

    Aspose::Cells::Cleanup();
}
```

## مخرج الكونسول

إليك مخرجات الوحدة للكود المذكور أعلاه مع هذا [ملف الإكسل العيني](5112365.xlsx).

{{< highlight java >}}

Web Query URL: https://docs.aspose.com/cells/net/

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
