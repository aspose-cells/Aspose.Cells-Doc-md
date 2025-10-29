---
title: معلمات سمارت ماركرز
type: docs
weight: 30
url: /ar/net/smart-marker-parameters/
---

## **الجدول البياني للمصمم والعلامات الذكية**
الأوراق العمل المصممة هي ملفات Excel القياسية التي تحتوي على تنسيقات بصرية وصيغ وعلامات ذكية. يمكن أن تحتوي على علامات ذكية تشير إلى مصدر بيانات واحد أو أكثر، مثل معلومات من مشروع ومعلومات لجهات الاتصال ذات الصلة. يتم كتابة العلامات الذكية في الخلايا حيث ترغب في الحصول على المعلومات.

تبدأ جميع العلامات الذكية بـ &=. مثال لعلامة بيانات هو &=اسمالطرف. إذا أدى مؤشر البيانات إلى أكثر من عنصر واحد، على سبيل المثال، صف كامل، فإن الصفوف التالية تتحرك تلقائيًا لتفسح المساحة للمعلومات الجديدة. بالتالي، يمكن وضع المجموعات الفرعية والإجماليات على الصف بشكل فوري بعد مؤشر البيانات لإجراء حسابات استنادًا إلى المعلومات المُدخلة. لإجراء حسابات على الصفوف المدخلة، استخدم **الصيغ الدينامية**.

تتكون العلامات الذكية من أجزاء **مصدر البيانات** و**اسم الحقل** لمعظم المعلومات. قد يتم أيضًا تمرير معلومات خاصة باستخدام المتغيرات ومصفوفات المتغيّرات. تملأ المتغيّرات دائمًا خلية واحدة فقط بينما قد تملأ مصفوفات المتغيّرات عدة. استخدم فقط علامة بيانات واحدة لكل خلية. يتم إزالة العلامات الذكية غير المستخدمة.

قد تحتوي العلامة الذكية أيضًا على معلمات. تتيح لك المعلمات تعديل كيفية توزيع المعلومات. يتم إضافتها إلى نهاية العلامة الذكية بين قوسين كفاصلة مفصولة.

## **خيارات العلامة الذكية**

```csharp
&=DataSource.FieldName 
&=[Data Source].[Field Name] 
&=$VariableName 
&=$VariableArray 
&==DynamicFormula 
&=&=RepeatDynamicFormula
```
## **معلمات سمارت ماركرز**
يُسمح بالمعلمات التالية:

- **noadd** - عدم إضافة صفوف إضافية لتناسب البيانات.
- **skip:n** - تخطي n عدد من الصفوف لكل صف من البيانات.
- **تصاعدي:n** أو **تنازلي:n** - ترتيب البيانات في العلامات الذكية. إذا كان n هو 1، فإن العمود هو المفتاح الأول لمُرتب. يتم فرز البيانات بعد معالجة مصدر البيانات. على سبيل المثال: &=جدول1.حقل3(تصاعدي:1).
- **أفقي** - اكتب البيانات من اليسار إلى اليمين بدلاً من الأعلى إلى الأسفل.
- **رقمي** - تحويل النص إلى رقم إذا كان ذلك ممكنًا.
- **shift** - تحريك البيانات إلى الأسفل أو اليمين، مما يخلق صفوفًا أو أعمدة إضافية لتناسب البيانات. يعمل المعلم الإضافي بنفس الطريقة كما هو الحال في Microsoft Excel. على سبيل المثال، في Microsoft Excel، عند تحديد مجموعة من الخلايا، بنقرة يمين الزر واختيار **Insert** ثم تحديد **shift cells down**، **shift cells right** وخيارات أخرى. بإختصار، يقوم المعلم **shift** بأداء نفس الوظيفة للعلامات الذكية الرأسية/العادية (من الأعلى إلى الأسفل) أو الأفقية (من اليسار إلى اليمين).
- **نسخالأسلوب** - استنساخ أسلوب الخلية الأساسية إلى جميع الخلايا في ذلك العمود.

يمكن دمج المعلمات noadd و skip لإدخال البيانات في الصفوف البديلة. نظرًا لأن القالب يتم معالجته من الأسفل إلى الأعلى ، يجب إضافة noadd في الصف الأول لتجنب إدراج صفوف إضافية قبل الصف البديل.

إذا كان لديك عدة معلمات، فاسمح بفصلها بفواصل، ولكن بدون مسافة: معلمة أ، معلمة ب، معلمة ج

تُظهر الصور التوضيحية التالية كيفية إدراج البيانات في كل صف آخر.

|**ملف القالب**|**ملف الإخراج**|
| :- | :- |
|![todo:image_alt_text](using-smart-markers_1.jpg)|![todo:image_alt_text](using-smart-markers_2.jpg)|

## **الصيغ الديناميكية**
تتيح الصيغ الديناميكية لك إدراج صيغ Excel في الخلايا حتى عندما تشير الصيغة إلى الصفوف التي سيتم إدراجها أثناء عملية التصدير. يمكن للصيغ الديناميكية أن تتكرر لكل صف تم إدراجه أو تستخدم فقط الخلية التي يتم وضع علامة البيانات فيها.

تسمح الصيغ الديناميكية بالخيارات الإضافية التالية:

- r - رقم الصف الحالي.
- 2، -1 - الإزاحة إلى رقم الصف الحالي.

على سبيل المثال:

{{< highlight java >}}

 &=&=B{-1}/C{-1}~(skip:1)

{{< /highlight >}}

في علامة الصيغة الديناميكية ، "-1" يعني التحريك إلى الصف الحالي في الأعمدة B و C على التوالي والتي سيتم تعيينها لعملية القسمة ، المعلمة التخطي هي صف واحد. علاوة على ذلك ، يجب علينا تحديد الحرف التالي:

{{< highlight java >}}

 "~"

{{< /highlight >}}

كحرف فاصل لتطبيق المعلمات الإضافية في الصيغ الديناميكية.

توضح اللقطات الشاشة التالية صيغة ديناميكية متكررة وورقة Excel الناتجة.

|**ملف القالب**|**ملف الإخراج**|
| :- | :- |
|![todo:image_alt_text](using-smart-markers_3.jpg)|![todo:image_alt_text](using-smart-markers_4.jpg)|
الخلية "C1" تحتوي على الصيغة **= A1*B1** ، والخلية "C2" تحتوي على **= A2*B2** والخلية "C3" تحتوي على **= A3*B3**.

من السهل جدًا معالجة العلامات الذكية. يوضح الكود المثال التالي كيفية استخدام الصيغ الديناميكية في العلامات الذكية. نقوم بتحميل [ملف القالب](templateDynamicFormulas.xlsx) وإنشاء بيانات اختبارية، ثم معالجة العلامات لملء البيانات في الخلايا مقابل العلامة. 

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-DynamicFormulas-1.cs" >}}

## **كيفية استخدام الصيغ الديناميكية والمتغيرات في SmartMarkers**
أحيانًا، تحتاج إلى استخدام الصيغ الديناميكية والمتغيرات في SmartMarkers. لتمثيل الصيغ الديناميكية، يرجى إضافة حرف خاص (~) كفاصل. تتيح Aspose.Cells استخدام الصيغ والمتغيرات الديناميكية في SmartMarkers. يرجى الاطلاع على [ملف النموذج](template.xlsx)، [ملف JSON](employees-data.json)، وصورة الشاشة لملف الإكسل الناتج باستخدام الكود التالي.

|**الورقة الأولى من ملف template.xlsx تعرض المتغيرات.**|
| :- |
|![todo:image_alt_text](template_variables.png)|

|**الورقة الثانية من ملف template.xlsx تعرض سمارت ماركرز.**|
| :- |
|![todo:image_alt_text](template_data.png)|

|**لقطة شاشة لملف إكسل المخرّج.**|
| :- |
|![todo:image_alt_text](template_result.png)|

بيانات json على النحو التالي:
```json data
{
  "RootData": {
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
          },
          {
            "City": "ddd city",
            "Department": "ddd department",
            "FirstName": "first ddd",
            "GST": "No",
            "id": "ddd",
            "ITR": "No",
            "LastName": "last ddd",
            "MiddleName": "middle ddd"
          },
          {
            "City": "eee city",
            "Department": "eee department",
            "FirstName": "first eee",
            "GST": "No",
            "id": "eee",
            "ITR": "No",
            "LastName": "last eee",
            "MiddleName": "middle eee"
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
    "DOB": "2025-02-28",
    "EntityCin": "EntityCin Test",
    "EntityName": "EntityName Test",
    "FirstName": "FirstName Test",
    "LastName": "LastName Test",
    "MiddleName": "MiddleName Test",
    "SSN": "11111111",
	"CtcPerEmployee": 100000,
	"CountOfEmployees": 132
  }
}
```
المثال التالي يوضح كيف يعمل هذا.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "SmartMarkers-Using-DynamicFormula-And-Variables.cs" >}}
