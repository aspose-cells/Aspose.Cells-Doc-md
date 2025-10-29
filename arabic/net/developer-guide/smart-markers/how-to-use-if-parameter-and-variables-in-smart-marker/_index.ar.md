---
title: كيفية استخدام معلمة if والمتغيرات في SmartMarkers
type: docs
weight: 10
url: /ar/net/how-to-use-if-parameter-and-Variables-in-smart-markers/
---

## **لماذا استخدام معلمة if والمتغيرات في Smart Markers**
Smart Markers هي أدوات قوية تُستخدم في سياقات مختلفة. يستخدم استخدام المعلمات والمتغيرات داخل Smart Markers بشكل كبير في تعزيز مرونتها، وكفاءتها، ووظائفها.

1. معالجة البيانات الديناميكية والمرونة: تسمح المعلمات والمتغيرات لـ Smart Markers بمعالجة البيانات بشكل ديناميكي، والتكيف مع المدخلات المتغيرة بدون الحاجة لضبط يدوي للنموذج أو الشفرة.
2. التحكم في السلوك والعمليات: تُحسن المعلمات من سلوك Smart Markers، مما يمكّن عمليات مثل التجميع، الفرز، حساب المجموع، والتنسيق الشرطي.
3. دعم للتركيبات الهيكلية المعقدة للبيانات: تمكّن المتغيرات Smart Markers من العمل مع مصادر بيانات معقدة، بما في ذلك المصفوفات، الكائنات، والبيانات متعددة الأبعاد.
4. الكفاءة والأتمتة: تقوم المعلمات والمتغيرات بأتمتة المهام المتكررة، مما يقلل من الجهد اليدوي والأخطاء المحتملة.
5. المنطق الشرطي والترشيح: على الرغم من محدوديتها في بعض السياقات، إلا أن المعلمات والمتغيرات يمكن أن تنفذ منطقًا شرطيًا.
6. التخصيص وتفاعل المستخدم: تسمح المتغيرات بإدخالات المستخدم لتخصيص سلوك Smart Marker بشكل ديناميكي.
7. تحسين الأداء: تساعد المعلمات على تحسين الأداء من خلال التحكم في كيفية معالجة البيانات.


## **كيفية استخدام معلمة if والمتغيرات في SmartMarkers**
أحيانًا، تحتاج إلى إضافة حكم شرط if إلى المعلمات المتغيرة في SmartMarkers. يجعل Aspose.Cells من الممكن استخدام معلمة if والمتغيرات في SmartMarkers. يرجى مراجعة [ملف النموذج](template.xlsx)، [ملف json](data.json)، وصورة لقطة للشاشة للملف إكسل الناتج الذي يُنشأ بالكود التالي.

|**الورقة الأولى من ملف template.xlsx التي تظهر المتغيرات.**|
| :- |
|![todo:image_alt_text](variables.png)|

|**الورقة الثانية من ملف template.xlsx التي تعرض السلايسرز الذكية.**|
| :- |
|![todo:image_alt_text](template.png)|

|**لقطة شاشة لملف إكسل المخرّج.**|
| :- |
|![todo:image_alt_text](result.png)|

بيانات json على النحو التالي:
```json data
{
    "Directors": [
        {
            "FirstName": "director first 1",
            "id": "director id 1",
            "LastName": "director last 1",
            "MiddleName": "director middle 1",
            "Reportees": [
                {
                    "City": "aaa city",
                    "Department": "aaa department",
                    "FirstName": "first aaa",
                    "GST": "Yes",
                    "id": "aaa",
                    "ITR": "No",
                    "LastName": "last aaa",
                    "MiddleName": "middle aaa"
                },
                {
                    "City": "bbb city",
                    "Department": "bbb department",
                    "FirstName": "first bbb",
                    "GST": "Yes",
                    "id": "bbb",
                    "ITR": "Yes",
                    "LastName": "last bbb",
                    "MiddleName": "middle bbb"
                },
                {
                    "City": "ccc city",
                    "Department": "ccc department",
                    "FirstName": "first ccc",
                    "GST": "No",
                    "id": "ccc",
                    "ITR": "No",
                    "LastName": "last ccc",
                    "MiddleName": "middle ccc"
                }
            ]
        },
        {
            "FirstName": "director first 2",
            "id": "director id 2",
            "LastName": "director last 2",
            "MiddleName": "director middle 2",
            "Reportees": [
                {
                    "City": "eee city",
                    "Department": "eee department",
                    "FirstName": "first eee",
                    "GST": "Yes",
                    "id": "eee",
                    "ITR": "No",
                    "LastName": "last eee",
                    "MiddleName": "middle eee"
                },
                {
                    "City": "fff city",
                    "Department": "fff department",
                    "FirstName": "first fff",
                    "GST": "No",
                    "id": "fff",
                    "ITR": "No",
                    "LastName": "last fff",
                    "MiddleName": "middle fff"
                }
            ]
        }
    ],
    "DOB": "2025-02-08",
    "EntityCin": "EntityCin Test",
    "EntityName": "EntityName Test",
    "FirstName": "FirstName Test",
    "LastName": "LastName Test",
    "MiddleName": "MiddleName Test",
    "SSN": "11111111"
}
```
المثال التالي يوضح كيف يعمل هذا.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "SmartMarkers-Using-If-Parameter-And-Variables.cs" >}}

{{< app/cells/assistant language="csharp" >}}
