---
title: استخدام بيانات Json في علامات ذكية
type: docs
weight: 30
url: /ar/java/using-json-data-in-smart-markers/
---

## **لماذا تستخدم بيانات Json في العلامات الذكية**
لماذا تستخدم بيانات JSON كبيانات أصلية للعلامات الذكية؟
JSON (تنسيق تبادل البيانات كائن جافا سكريبت) هو تنسيق تبادل بيانات خفيف، مقروء للبشر، مثالي لتنظيم البيانات الهرمية. إليك لماذا هو مناسب كبيانات أصلية للعلامات الذكية (مؤشرات ديناميكية تملأ تلقائيًا جداول البيانات أو المستندات أولوحات المعلومات):

1. دعم البيانات المهيكلة والهرمية
يدعم JSON بشكل أصلي الكائنات والمصفوفات المتداخلة (مثل { "user": { "name": "Alice", "orders": [ ... ] } }). يمكن للعلامات الذكية استكشاف هذا التسلسل الهرمي (مثلاً {{user.orders[0].price}})، مما يجعل من السهل ربط البيانات المعقدة بالنماذج.

2. منصة ولغة غير مرتبطة
توفر أدوات تحليل JSON في جميع لغات البرمجة تقريبًا (بايثون، جافا سكريبت، جافا، إلخ). تتضمن أدوات مثل Power Query في إكسل، جوجل أبس سكريبت، أو منصات بدون رمز (مثل Airtable) استهلاك JSON بسهولة.

3. ملائمة لواجهات برمجة التطبيقات
تعيد معظم واجهات برمجة التطبيقات الحديثة (مثل REST، GraphQL) البيانات بصيغة JSON. يمكن للعلامات الذكية استهلاك JSON مباشر من خدمات الويب، مما يتيح تحديث البيانات في الوقت الحقيقي (مثل أسعار الأسهم، الطقس).

4. مقروء للبشر وقابل للتصحيح
هيكل JSON النصي بسيط وسهل: التحقق (مثل استخدام JSONLint). التعديل يدويًا أو عبر السكريبتات. التصحيح عند ربط البيانات بالعلامات.

5. القابلية للتوسع والمرونة
إضافة/حذف الحقول في JSON دون كسر العلامات الذكية الموجودة (إذا تم التعامل مع الحقول الاختيارية بشكل مناسب). يدعم أنواع بيانات متنوعة: سلاسل، أرقام، منطق، مصفوفات، وكائنات.

6. توافق مع النظام البيئي
يتوافق مع أدوات البيانات الحديثة: قواعد البيانات: MongoDB، PostgreSQL (JSONB)، إلخ. أدوات الأتمتة: Zapier، Integromat. خطوط بيانات: Apache NiFi، Talend.

## **استخدام قالب إكسل متداخل مع بيانات JSON**
يدعم Aspose.Cells for Java بيانات JSON في العلامات الذكية، يمكن أن تكون البيانات JSON متداخلة بشكل هرمي. يرجى التحقق من [ملف النموذج](smartmarker.xlsx)، [ملف JSON](smartmarker.json) ولقطة شاشة لملف إكسل الناتج الذي تم إنشاؤه باستخدام الكود التالي.

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

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "SmartMarkers-Using-JSON-Data.java" >}}


## **استخدام قالب اجماليات إكسل مع بيانات JSON**
يدعم Aspose.Cells for Java بيانات JSON في العلامات الذكية، يمكن أن تكون البيانات JSON متداخلة بشكل هرمي. تم استخدام الإجماليات لإحصائيات البيانات في قالب إكسل. يرجى التحقق من [ملف النموذج](jsonExcelTemplate.xlsx)، [ملف JSON](jsonData.json) ولقطة شاشة لملف إكسل المنتج باستخدام الكود التالي.

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

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "SmartMarkers-Using-JSON-Data-Subtotal.java" >}}

{{< app/cells/assistant language="java" >}}
