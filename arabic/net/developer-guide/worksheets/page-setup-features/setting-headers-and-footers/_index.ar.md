﻿---
title: تعيين الرؤوس والتذييلات
type: docs
weight: 30
url: /ar/net/setting-headers-and-footers/
---
{{% alert color="primary" %}}

الرؤوس والتذييلات هي أسطر النص المعروضة أسفل الهامش العلوي أو أعلى الهامش السفلي على التوالي. من الممكن إضافة رؤوس وتذييلات إلى أوراق العمل أيضًا. يمكن استخدام الرؤوس والتذييلات لعرض معلومات مفيدة مثل رقم الصفحة أو اسم المؤلف أو اسم الموضوع أو التاريخ والوقت. تتم إدارة الرؤوس والتذييلات باستخدام إعدادات إعداد الصفحة.

{{% /alert %}}

## **تعيين الرؤوس والتذييلات**

يسمح لك Aspose.Cells بإضافة الرؤوس والتذييلات إلى أوراق العمل في وقت التشغيل ولكننا نوصي بتعيين الرؤوس والتذييلات يدويًا في ملف مصمم مسبقًا للطباعة. يمكنك استخدام Microsoft Excel كأداة GUI لضبط الرؤوس والتذييلات لتوفير الجهد ووقت التطوير. Aspose.Cells يمكنه استقبال الملف وحفظ المحددات.

لإضافة رؤوس وتذييلات في وقت التشغيل ، يوفر Aspose.Cells مكالمات API وأوامر نصية خاصة لتنسيق الرؤوس والتذييلات.

### **أوامر البرنامج النصي**

أوامر البرنامج النصي هي أوامر خاصة تسمح لك بتعيين تنسيق الرأس والتذييل.

|**أوامر البرنامج النصي**|**وصف**|
|:- |:- |
|& ص|رقم الصفحة الحالية|
|& ج|صورة|
|&ن|العدد الإجمالي للصفحات|
|&د|التاريخ الحالي|
|& ت|الوقت الحالي|
|&أ|اسم ورقة العمل|
|&F|اسم الملف بدون مساره|
|&"\<FontName>"|يمثل اسم الخط. على سبيل المثال: & "Arial"|
|&"\<FontName>, \<FontStyle>"|يمثل اسم الخط مع النمط. على سبيل المثال: & "Arial، Bold"|
|&\<FontSize>|يمثل حجم الخط. على سبيل المثال: "& 14abc". ولكن ، إذا كان هذا الأمر متبوعًا برقم عادي ليتم طباعته في الرأس ، فيجب فصله بمسافة عن حجم الخط. على سبيل المثال: "& 14123".|

### **تعيين الرؤوس والتذييلات**

 ال[**اعداد الصفحة**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) فئة توفر طريقتين ،[**SetHeader**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/setheader) و[**SetFooter**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/setfooter)، تستخدم لإضافة رأس وتذييل إلى ورقة العمل. تأخذ هذه الطرق معلمتين فقط:

- **الجزء** - القسم الذي يجب وضع الرأس أو التذييل فيه. هناك ثلاثة أقسام: اليسار والوسط واليمين ممثلة بـ 0 و 1 و 2 على التوالي.
- **النصي** - النص الذي سيتم استخدامه للرأس أو التذييل. يحتوي هذا البرنامج النصي على أوامر نصية لتنسيق الرؤوس أو التذييلات.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetHeadersAndFooters-1.cs" >}}

### **أدخل صورة في رأس أو تذييل**

 ال[**اعداد الصفحة**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) فئة لها طريقتان إضافيتان ،[**SetHeaderPicture**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/setheaderpicture) و[**SetFooterPicture**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/setfooterpicture)، تستخدم لإضافة الصور في رأس الصفحة وتذييلها. تأخذ هذه الطرق المعلمات:

- **الجزء** قسم الرأس أو التذييل حيث سيتم وضع الصورة. هناك ثلاثة أقسام ، يسار ووسط ويمين ، ممثلة بالقيم 0 و 1 و 2 على التوالي.
- **مجموعة بايت** - البيانات الرسومية (يجب كتابة البيانات الثنائية في المخزن المؤقت لصفيف البايت).

بعد تنفيذ الكود أدناه وفتح الملف ، تحقق من رأس ورقة العمل عن طريق:

1.  على ال**ملف** القائمة ، حدد**اعداد الصفحة**. سيتم عرض مربع حوار.
1.  حدد ملف**تذييل الرأس** التبويب.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-InsertImageInHeaderFooter-1.cs" >}}