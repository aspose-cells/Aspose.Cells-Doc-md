---
title: الإضافات الإلكترونية للويب  إضافات Office
type: docs
weight: 130
url: /ar/python-net/web-extensions-office-add-ins/
---

ملحقات الويب توسع تطبيقات Office وتتفاعل مع محتوى مستندات Office. تضيف ملحقات الويب وظائف إضافية إلى عميل Office لتحسين تجربة المستخدم وزيادة الإنتاجية.

كما يوفر Aspose.Cells لبايثون via .NET القدرة على العمل مع ملحقات الويب.

## **إضافة ملحق ويب**

يمكنك إضافة ملحقات الويب (ملحقات Office) في Excel عن طريق النقر فوق علامة التبويب **إدراج** ثم النقر فوق الرابط **متجر**/**الحصول على الملحقات**. في مربع الملحقات، تصفح الإضافة التي تريدها وأضفها.

كما يوفر Aspose.Cells لبايثون via .NET ميزة إضافة ملحقات الويب باستخدام فئتي [**WebExtension**](https://reference.aspose.com/cells/python-net/aspose.cells.webextensions/webextension) و [**WebExtensionTaskPane**](https://reference.aspose.com/cells/python-net/aspose.cells.webextensions/webextensiontaskpane). يُوضح رمز العينة التالي استخدام فئتي [**WebExtension**](https://reference.aspose.com/cells/python-net/aspose.cells.webextensions/webextension) و [**WebExtensionTaskPane**](https://reference.aspose.com/cells/python-net/aspose.cells.webextensions/webextensiontaskpane) لإضافة ملحق ويب لملف إكسل. يُرجى الاطلاع على ملف إكسل الناتج (89849869.xlsx) الذي تم توليده بواسطة الرمز للمراجعة.

### **الكود المثالي**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-WebExtension-Workbook-AddWebExtension-1.py" >}}

## **الوصول إلى معلومات ملحق الويب**

يوفر Aspose.Cells لبايثون via .NET القدرة على الوصول إلى معلومات ملحقات الويب في ملف إكسل. يوصل الكود التالي كيفية الوصول إلى معلومات ملحق الويب عن طريق تحميل ملف إكسل النموذجي (89849870.xlsx). يُرجى الاطلاع على مخرجات الطرفية التي تم إنشاؤها بواسطة الكود للمراجعة.

### **الكود المثالي**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-WebExtension-Workbook-AccessWebExtensionInformation-1.py" >}}

### **مخرجات الوحدة**

{{< highlight java >}}

Width: 350

IsVisible: True

IsLocked: False

DockState: right

StoreName: en-US

StoreType: OMEX

WebExtension.Id: 95D7ECE8-1355-492B-B6BF-27D25D0B0EEF

{{< /highlight >}}
