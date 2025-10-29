---
title: ملحقات الويب  إضافات Office باستخدام Golang عبر C++
linktitle: الإضافات الإلكترونية للويب  إضافات Office
type: docs
weight: 130
url: /ar/go-cpp/web-extensions-office-add-ins/
description: تعلم كيفية إضافة والوصول إلى ملحقات الويب (إضافات Office) في ملفات Excel باستخدام Aspose.Cells مع Golang عبر C++.
---

تمتد إضافات الويب تطبيقات Office وتتفاعل مع محتوى مستندات Office. تضيف إضافات الويب وظائف إضافية لعملاء Office لتحسين تجربة المستخدم والإنتاجية.

توفر Aspose.Cells أيضًا القدرة على العمل مع ملحقات الويب.

## **إضافة ملحق ويب**

 يمكنك إضافة إضافات الويب (إضافات Office) في إكسل بالنقر على علامة التبويب **إدراج** ثم النقر على رابط **المتجر** / **الحصول على الإضافات**. في مربع الإضافات، تصفح الإضافة التي تريدها وأضفها.

توفر Aspose.Cells أيضًا ميزة إضافة إضافات الويب باستخدام فئتي [**WebExtension**](https://reference.aspose.com/cells/go-cpp/webextension/) و [**WebExtensionTaskPane**](https://reference.aspose.com/cells/cpp/aspose.cells.webextensions/webextensiontaskpane/). يوضح نموذج الكود التالي استخدام فئتي [**WebExtension**](https://reference.aspose.com/cells/go-cpp/webextension/) و [**WebExtensionTaskPane**](https://reference.aspose.com/cells/cpp/aspose.cells.webextensions/webextensiontaskpane/) لإضافة إضافة ويب إلى ملف إكسل. يرجى مراجعة ملف إكسل الناتج [ملف الإكسل الناتج](89849869.xlsx) باستخدام الكود للمراجعة.

### **الكود المثالي**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WebExtensionsOfficeAddIns.go" >}}
## **الوصول إلى معلومات ملحق الويب**

توفر Aspose.Cells القدرة على الوصول إلى معلومات إضافات الويب في ملف إكسل. يوضح مثال الكود التالي كيف يمكن الوصول إلى معلومات الإضافة عن طريق تحميل ملف إكسل العينة [ملف إكسل عينة](89849870.xlsx). يرجى الاطلاع على مخرجات وحدة التحكم التي تم إنشاؤها بواسطة الكود للمراجعة.

### **الكود المثالي**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WebExtensionsOfficeAddIns-1.go" >}}
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
