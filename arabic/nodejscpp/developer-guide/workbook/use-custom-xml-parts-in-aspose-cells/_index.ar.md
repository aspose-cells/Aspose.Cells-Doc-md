---
title: استخدام أجزاء XML المخصصة في Aspose.Cells مع Node.js عبر C++
linktitle: استخدام أجزاء XML المخصصة في Aspose.Cells
type: docs
weight: 390
url: /ar/nodejs-cpp/use-custom-xml-parts-in-aspose-cells/
description: تعلّم كيفية استخدام الأجزاء XML المخصصة في Aspose.Cells for Node.js via C++. دمج البيانات XML الخارجية داخل ملفات إكسل بسلاسة.
--- 

## استخدام أجزاء XML المخصصة في Aspose.Cells

أجزاء XML المخصصة هي البيانات XML التي يتم تخزينها بواسطة تطبيقات مختلفة مثل SharePoint وغيرها داخل ملف إكسل. يتم استهلاك هذه البيانات بواسطة تطبيقات مختلفة تحتاجها. لا يستخدم Microsoft Excel هذه البيانات لذلك لا يوجد واجهة رسومية لإضافتها. يمكنك عرض هذه البيانات بتغيير امتداد **.xlsx** إلى **.zip** ثم فتحه باستخدام **WinZip**. يمكنك أيضًا فتح ملف ZIP باستخدام أي أداة ضغط من طرف ثالث على Windows مثل WinRAR أو WinZip. البيانات موجودة داخل مجلد **customXml**.

يمكنك إضافة أجزاء XML مخصصة باستخدام Aspose.Cells عبر طريقة [**ContentTypePropertyCollection**](https://reference.aspose.com/cells/nodejs-cpp/contenttypepropertycollection/).

يُظهر رمز المثال التالي استخدام طريقة [**ContentTypePropertyCollection**](https://reference.aspose.com/cells/nodejs-cpp/contenttypepropertycollection/) ويضيف **Book Catalog XML** واسمها **BookStore**. ويظهر الصورة التالية نتيجة هذا الرمز. كما ترى، تمت إضافة Book Catalog XML داخل عنصر BookStore الذي هو اسم الخاصية هذه.

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_1.png)

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_2.png)

## كود Node.js لاستخدام أجزاء XML المخصصة

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "output.xlsx");

// The sample XML that will be injected to Workbook
const booksXML = `<catalog>
<book>
<title>Complete C#</title>
<price>44</price>
</book>
<book>
<title>Complete Java</title>
<price>76</price>
</book>
<book>
<title>Complete SharePoint</title>
<price>55</price>
</book>
<book>
<title>Complete PHP</title>
<price>63</price>
</book>
<book>
<title>Complete VB.NET</title>
<price>72</price>
</book>
</catalog>`;

// Create an instance of Workbook class
const workbook = new AsposeCells.Workbook();

// Add Custom XML Part to ContentTypePropertyCollection
workbook.getContentTypeProperties().add("BookStore", booksXML);

// Save the resultant spreadsheet
workbook.save(filePath);
```

## مقال ذو صلة

- [إضافة خصائص مخصصة مرئية داخل لوحة معلومات الوثيقة](/cells/ar/nodejs-cpp/adding-custom-properties-visible-inside-document-information-panel/)
{{< app/cells/assistant language="nodejs-cpp" >}}
