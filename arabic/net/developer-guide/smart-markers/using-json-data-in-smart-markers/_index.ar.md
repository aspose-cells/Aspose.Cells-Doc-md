---
title: استيراد JSON بشكل ذكي إلى إكسل باستخدام العلامات الذكية
type: docs
weight: 30
url: /ar/net/how-to-import-json-into-excel-with-smart-markers/
alias: [/net/using-json-data-in-smart-markers/]
---

## **لماذا نستخدم بيانات Json للعلامات الذكية**
لماذا نستخدم بيانات JSON كبيانات أصلية للعلامات الذكية؟
JSON (تنسيق كائن جافا سكريبت) هو تنسيق تبادل بيانات خفيف وسهل القراءة للبشر، وهو مثالي لبناء البيانات الهرمية. إليك سبب ملائمته كبيانات أصلية للعلامات الذكية (م enklات ديناميكية تملأ تلقائيًا جداول البيانات أو المستندات أو لوحات المعلومات):

1. دعم البيانات المنظمة والهرمية
يدعم JSON بشكل أصلي الكائنات المتداخلة والمصفوفات (مثلاً { "المستخدم": { "الاسم": "Alice"، "الطلبات": [ ... ] } }). يمكن للعلامات الذكية تصفح هذا التسلسل الهرمي (مثلاً {{user.orders[0].price}})، مما يسهل ربط البيانات المعقدة بالقوالب.

2. غير محدود اللغة والمنصة
يوجد محللات JSON في جميع لغات البرمجة تقريبًا (بايثون، جافا سكريبت، جافا، وغيرها). أدوات مثل Excel Power Query، Google Apps Script، أو منصات بدون ترميز (مثل Airtable) تستوعب JSON بسهولة.

3. مناسب لواجهات برمجة التطبيقات (API)
تعيد معظم واجهات برمجة التطبيقات الحديثة (مثل REST، GraphQL) البيانات بصيغة JSON. يمكن للعلامات الذكية استهلاك JSON مباشر من خدمات الويب، مما يتيح تحديثات البيانات في الوقت الحقيقي (مثل أسعار الأسهم، الطقس).

4. تفهم للإنسان وقابلة للتصحيح
هيكل JSON النصي واضح وسهل: التحقق من الصحة (مثل استخدام JSONLint)، التعديل اليدوي أو عبر السكربتات، وتصحيح الأخطاء عند ربط البيانات بالعلامات.

5. قابلية التوسع والمرونة
إضافة/حذف الحقول في JSON بدون تعطيل العلامات الذكية الموجودة (إذا تمت معالجة الحقول الاختيارية بشكل لائق). يدعم أنواع البيانات المتنوعة: النصوص، الأرقام، القيم المنطقية، المصفوفات، والكائنات.

6. توافق مع النظام البيئي
يعمل مع أدوات البيانات الحديثة: قواعد البيانات (مثل MongoDB، PostgreSQL مع JSONB)، أدوات الأتمتة (مثل Zapier، Integromat)، خطوط أنابيب البيانات (مثل Apache NiFi، Talend).

## **استخدام نموذج القالب المتداخل في إكسل مع بيانات JSON**
يدعم Aspose.Cells for .NET بيانات json في العلامات الذكية، يمكن أن تكون بيانات json متداخلة هرميًا. يرجى التحقق من [ملف القالب](smartmarker.xlsx)، [ملف json](smartmarker.json) وصورة لقطة للشاشة لملف الاكسل الناتج الذي تم إنشاؤه باستخدام الكود التالي.

|**ورقة العمل الأولى في ملف smartmarker.xlsx تظهر العلامات الذكية.**|
| :- |
|![todo:image_alt_text](jsontemplate.png)|

|**لقطة شاشة لملف إكسل المخرّج.**|
| :- |
|![todo:image_alt_text](jsonresult.png)|

بيانات json على النحو التالي:
```json data
{
    "EntityCin" : "EntityCin Test",
    "EntityName" : "EntityName Test",
    "FirstName" : "FirstName Test",
    "MiddleName" : "MiddleName Test",
    "LastName" : "LastName Test",
    "DOB" : "2025-02-08",
    "SSN" : "11111111",
    "Directors" : [
        {
            "id" : "director id 1",
            "FirstName" : "director first 1",
            "MiddleName" : "director middle 1",
            "LastName" : "director last 1",
            "Reportees" : [
                {
                    "id" : "aaa",
                    "FirstName" : "first aaa",
                    "MiddleName" : "middle aaa",
                    "LastName" : "last aaa",
                    "Department" : "aaa department",
                    "City" : "aaa city",
                    "GST" : "Yes",
                    "ITR" : "No"
                },
                {
                    "id" : "bbb",
                    "FirstName" : "first bbb",
                    "MiddleName" : "middle bbb",
                    "LastName" : "last bbb",
                    "Department" : "bbb department",
                    "City" : "bbb city",
                    "GST" : "Yes",
                    "ITR" : "Yes"
                },
                {
                    "id" : "ccc",
                    "FirstName" : "first ccc",
                    "MiddleName" : "middle ccc",
                    "LastName" : "last ccc",
                    "Department" : "ccc department",
                    "City" : "ccc city",
                    "GST" : "No",
                    "ITR" : "No"
                }
            ]
        },
        {
            "id" : "director id 2",
            "FirstName" : "director first 2",
            "MiddleName" : "director middle 2",
            "LastName" : "director last 2",
            "Reportees" : [
                {
                    "id" : "eee",
                    "FirstName" : "first eee",
                    "MiddleName" : "middle eee",
                    "LastName" : "last eee",
                    "Department" : "eee department",
                    "City" : "eee city",
                    "GST" : "Yes",
                    "ITR" : "No"
                },
                {
                    "id" : "fff",
                    "FirstName" : "first fff",
                    "MiddleName" : "middle fff",
                    "LastName" : "last fff",
                    "Department" : "fff department",
                    "City" : "fff city",
                    "GST" : "No",
                    "ITR" : "No"
                }
            ]
        }
    ]
}
```
المثال التالي يوضح كيف يعمل هذا.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "SmartMarkers-Using-JSON-Data.cs" >}}


## **استخدام قالب التلخيص في إكسل مع بيانات JSON**
يدعم Aspose.Cells for .NET بيانات json في العلامات الذكية، يمكن أن تكون بيانات json متداخلة هرميًا. تم استخدام التلخيص لإحصائيات البيانات في قالب الإكسل. يرجى التحقق من [ملف القالب](jsonExcelTemplate.xlsx)، [ملف json](jsonData.json) وصورة لقطة للشاشة لملف الاكسل الناتج الذي تم إنشاؤه باستخدام الكود التالي.

|**ورقة العمل الأولى من ملف jsonExcelTemplate.xlsx تظهر العلامات الذكية.**|
| :- |
|![todo:image_alt_text](jsontemplate2.png)|

|**لقطة شاشة لملف إكسل المخرّج.**|
| :- |
|![todo:image_alt_text](jsonresult2.png)|

بيانات json على النحو التالي:
```json data
{
    "number": 10,
    "test": "test abc",
    "date": "2011-10-05T14:48:00.000Z",
    "arrayNumber": [1,2,3,4,5],
    "arrayWords": ["x1","xy2","yz3","z4"],
    "arrayOfObjects": [
      {"valNumber":12,"valString": "aa"},
      {"valNumber":15,"valString": "bb"},
      {"valNumber":1,"valString": "cc"},
      {"valNumber":20,"valString": "dd"}

    ],
    "nestedArray": [
      {"valNumber":12,"valString": "xy","nestArr": [{"val": 1,"some": "aa"}]},
      {"valNumber":15,"valString": "y","nestArr": [{"val": 2,"some": "bb"}]},
      {"valNumber":1,"valString": "yz","nestArr": [{"some": "cc"}]},
      {"valNumber":20,"valString": "z","nestArr": [{"some": "dd"}]}
    ],
  "Products": [
    { "ProductID": "A101", "ProductName": "Apples", "Units": 5 },
    { "ProductID": "A101", "ProductName": "Apples", "Units": 10 },
    { "ProductID": "B202", "ProductName": "Bananas", "Units": 7 },
    { "ProductID": "B202", "ProductName": "Bananas", "Units": 3 },
    { "ProductID": "C303", "ProductName": "Cherries", "Units": 8 }
  ]
}
```
المثال التالي يوضح كيف يعمل هذا.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "SmartMarkers-Using-JSON-Data-Subtotal.cs" >}}

{{< app/cells/assistant language="csharp" >}}
