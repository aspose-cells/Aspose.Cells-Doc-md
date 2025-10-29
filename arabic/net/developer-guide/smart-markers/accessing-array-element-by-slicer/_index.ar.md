---
title: استيراد عنصر المصفوفة بشكل ذكي بواسطة القطاعة في إكسيل باستخدام العلامات الذكية
type: docs
weight: 30
url: /ar/net/how-to-import-array-element-by-slicer-with-smart-markers/
---

## **لماذا الوصول إلى عنصر المصفوفة بواسطة القطاعة**
في العلامات الذكية لـ FastReport، يوفر الوصول إلى عناصر المصفوفة باستخدام القطاعة (مثل [array[1..3]]) طريقة مختصرة وفعالة للعمل مع أجزاء من البيانات.

1. تبسيط استخراج البيانات: يتطلب التكرار اليدوي على المصفوفات الكبيرة حلقات ونحوًا معقدًا من الصياغة. تتيح القطاعات استخراج النطاقات (مصفوفات فرعية) في سطر واحد. مثال: [Products[1..5].Name] يجلب أسماء أول 5 منتجات.
2. التقارير الديناميكية: إنشاء تقارير لأجزاء بيانات متغيرة (مثل "أفضل N عناصر"، العروض المفوترة). مثال: [Sales[0..{PageNo*10}]] تحميل البيانات ديناميكيًا لصفحات متعددة.
3. تحسين الأداء: تجنب تحميل كامل المصفوفات إلى الذاكرة. جلب العناصر الضرورية فقط. مثال: [Logs[^10..^1]] يسترجع آخر 10 مدخلات بكفاءة.
4. صياغة صريحة: عبّر عن النية مباشرة في علامات القالب. مثال: [Employees[3..7].Department] يختار بوضوح الأقسام من الإدخالات 3 إلى 7.
5. التكامل مع مصادر البيانات: يعمل مع المصفوفات من قواعد البيانات، JSON، أو الشفرة. مثال: ربط Invoice.Items[0..2] لعرض أول 3 بنود سطرية.
6. يقلل سلايسرز في Smart Markers من تعقيد الشفرة، ويحسن قابلية القراءة، ويحسن معالجة البيانات لمحات البيانات الجزئية. استخدمها عندما تحتاج إلى وصول سريع قائم على النطاق—مثالي للترقيم، قوائم أعلى-N، أو عروض البيانات النافذة. 

## **كيفية استيراد عنصر المصفوفة بواسطة سلايسر في إكسل باستخدام Smart Markers**
يدعم Aspose.Cells الوصول إلى عنصر المصفوفة بواسطة سلايسر في Smart Markers. يرجى مراجعة [ملف النموذج](ElementBySlicer.xlsx)، [ملف json](ElementBySlicer.json)، وصورة لقطة للشاشة لملف الإكسل الناتج الذي يُنشأ بالكود التالي.

|**ورقة العمل الأولى في ملف smartmarker.xlsx تظهر العلامات الذكية.**|
| :- |
|![todo:image_alt_text](ElementBySlicer1.png)|

|**لقطة شاشة لملف إكسل المخرّج.**|
| :- |
|![todo:image_alt_text](ElementBySlicer2.png)|

بيانات json على النحو التالي:
```json data
{
  "EntityCin": "EntityCin Test",
  "EntityName": "EntityName Test",
  "FirstName": "FirstName Test",
  "MiddleName": "MiddleName Test",
  "LastName": "LastName Test",
  "DOB": "2025-02-08",
  "SSN": "11111111",
  "Directors": [
    {
      "id": "director id 1",
      "FirstName": "director first 1",
      "MiddleName": "director middle 1",
      "LastName": "director last 1",
      "Reportees": [
        {
          "id": "aaa",
          "FirstName": "first aaa",
          "MiddleName": "middle aaa",
          "LastName": "last aaa",
          "Department": "aaa department",
          "City": "aaa city",
          "GST": "Yes",
          "ITR": "No"
        },
        {
          "id": "bbb",
          "FirstName": "first bbb",
          "MiddleName": "middle bbb",
          "LastName": "last bbb",
          "Department": "bbb department",
          "City": "bbb city",
          "GST": "Yes",
          "ITR": "Yes"
        },
        {
          "id": "ccc",
          "FirstName": "first ccc",
          "MiddleName": "middle ccc",
          "LastName": "last ccc",
          "Department": "ccc department",
          "City": "ccc city",
          "GST": "No",
          "ITR": "No"
        }
      ]
    },
    {
      "id": "director id 2",
      "FirstName": "director first 2",
      "MiddleName": "director middle 2",
      "LastName": "director last 2",
      "Reportees": [
        {
          "id": "eee",
          "FirstName": "first eee",
          "MiddleName": "middle eee",
          "LastName": "last eee",
          "Department": "eee department",
          "City": "eee city",
          "GST": "Yes",
          "ITR": "No"
        },
        {
          "id": "fff",
          "FirstName": "first fff",
          "MiddleName": "middle fff",
          "LastName": "last fff",
          "Department": "fff department",
          "City": "fff city",
          "GST": "No",
          "ITR": "No"
        }
      ]
    },
    {
      "id": "director id 3",
      "FirstName": "director first 2",
      "MiddleName": "director middle 2",
      "LastName": "director last 2",
      "Reportees": [
        {
          "id": "eee3",
          "FirstName": "first eee3",
          "MiddleName": "middle eee3",
          "LastName": "last eee3",
          "Department": "eee department3",
          "City": "eee city3",
          "GST": "Yes",
          "ITR": "No"
        },
        {
          "id": "fff3",
          "FirstName": "first fff3",
          "MiddleName": "middle fff3",
          "LastName": "last fff3",
          "Department": "fff department3",
          "City": "fff city",
          "GST": "No",
          "ITR": "No"
        }
      ]
    },
    {
      "id": "director id 4",
      "FirstName": "director first 4",
      "MiddleName": "director middle 4",
      "LastName": "director last 4",
      "Reportees": [
        {
          "id": "eee4",
          "FirstName": "first eee4",
          "MiddleName": "middle eee4",
          "LastName": "last eee4",
          "Department": "eee department4",
          "City": "eee city4",
          "GST": "Yes",
          "ITR": "No"
        },
        {
          "id": "fff4",
          "FirstName": "first fff4",
          "MiddleName": "middle fff4",
          "LastName": "last fff4",
          "Department": "fff department4",
          "City": "fff city4",
          "GST": "No",
          "ITR": "No"
        }
      ]
    }
  ]
}
```
المثال التالي يوضح كيف يعمل هذا.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "SmartMarkers-AccessElementBySlicer.cs" >}}

{{< app/cells/assistant language="csharp" >}}
