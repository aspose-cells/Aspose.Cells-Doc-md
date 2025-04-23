---
title: العمل مع اتصال البيانات الخارجي من نوع WebQuery باستخدام Node.js عبر C++
linktitle: العمل مع اتصال البيانات الخارجية من نوع الاستعلام عبر الويب
type: docs
weight: 30
url: /ar/nodejs-cpp/working-with-external-data-connection-of-type-webquery/
description: تعلم كيفية العمل مع اتصالات البيانات الخارجية من نوع WebQuery باستخدام Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

يمكنك الوصول إلى اتصال البيانات الخارجية من أي نوع باستخدام مجموعة Workbook.DataConnections. نوع واحد من هذا النوع من اتصال البيانات هو استعلام الويب. سيوضح هذا المقال كيفية العمل مع اتصال بيانات استعلام الويب. يمكنك إنشاء اتصال بيانات استعلام الويب في برنامج Microsoft Excel باستخدام القائمة **البيانات** > **من الويب**.

{{% /alert %}}

## العمل مع اتصال البيانات الخارجية من نوع WebQuery

الكود التالي يوضح كيفية العمل مع اتصال البيانات الخارجية من نوع **WebQuery**. يستخدم [ملف الإكسل عينة](5112365.xlsx) الذي يمكنك تنزيله من الرابط المقدم. يمكنك أيضًا رؤية مخرجات الوحدة (console output) لهذا الكود فيما بعد.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "WebQuerySample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

const connections = workbook.getDataConnections();
if (connections.getCount() > 0) {
const connection = connections.get(0);

if (connection instanceof AsposeCells.WebQueryConnection) {
const webQuery = connection;
console.log("Web Query URL: " + webQuery.getUrl());
}
}
```

## مخرج الكونسول

إليك مخرجات الوحدة للكود المذكور أعلاه مع هذا [ملف الإكسل العيني](5112365.xlsx).

{{< highlight javascript >}}

Web Query URL: https://docs.aspose.com/cells/nodejs-cpp/

{{< /highlight >}}
