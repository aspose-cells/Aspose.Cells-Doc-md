---
title: تعديل نمط موجود
type: docs
weight: 50
url: /ar/java/modify-an-existing-style/
description: تعرف على كيفية تغيير الأنماط في Excel باستخدام Microsoft Excel وباستخدام Aspose.Cells for Java API.
keywords: modify an existing style excel, modify an existing style excel java, modify existing style excel, modify existing style excel java, change existing style in excel, change existing style in excel java, how to change style in excel, how to change style in excel with java, how to change style in excel with java, how to change style in excel using java, changing existing style in excel java, changing existing style in excel
---
{{% alert color="primary" %}}

لتطبيق نفس خيارات التنسيق على الخلايا ، قم بإنشاء كائن نمط تنسيق جديد. كائن نمط التنسيق عبارة عن مجموعة من خصائص التنسيق ، مثل الخط وحجم الخط والمسافة البادئة والرقم والحد والنماذج وما إلى ذلك ، يتم تسميتها وتخزينها كمجموعة. عند تطبيقه ، يتم تطبيق كل التنسيقات بهذا النمط.

يمكنك أيضًا استخدام نمط موجود وحفظه في المصنف واستخدامه لتنسيق المعلومات بنفس السمات.

 عندما لا يتم تنسيق الخلايا بشكل صريح ، فإن ملف**طبيعي** يتم تطبيق النمط (النمط الافتراضي للمصنف). يعرف Microsoft Excel مسبقًا عدة أنماط بالإضافة إلى النمط العادي بما في ذلك الفاصلة والعملة والنسبة المئوية.

يسمح Aspose.Cells بتعديل أي من هذه الأنماط أو أي نمط آخر تقوم بتعريفه بالسمات التي تريدها.

{{% /alert %}}

## **باستخدام Microsoft إكسل**

لتحديث نمط في Microsoft Excel 97-2003:

1.  على ال**شكل** القائمة ، انقر فوق**أسلوب**.
1.  حدد النمط الذي تريد تعديله من ملف**اسم النمط** قائمة.
1.  انقر**تعديل**.
1. حدد خيارات النمط التي تريدها باستخدام علامات التبويب في مربع الحوار تنسيق Cells.
1.  انقر**نعم**.
1.  تحت**يشمل النمط**، حدد ميزات النمط التي تريدها.
1.  انقر**نعم** لحفظ النمط وتطبيقه على النطاق المحدد.

## **باستخدام Aspose.Cells**

 يوفر Aspose.Cells ملف[**النمط. التحديث**](https://reference.aspose.com/cells/java/com.aspose.cells/style#update()) لتحديث نمط موجود.

 لتغيير نمط مسمى ، سواء تم إنشاؤه ديناميكيًا باستخدام Aspose.Cells أو معرف مسبقًا ، قم باستدعاء[**النمط. التحديث**](https://reference.aspose.com/cells/java/com.aspose.cells/style#update()) لعكس أي تغييرات في النمط المطبق على خلية أو نطاق.

 ال[**النمط. التحديث**](https://reference.aspose.com/cells/java/com.aspose.cells/style#update() ) طريقة تتصرف مثل**نعم** زر في مربع حوار النمط: بعد إجراء تغييرات على نمط موجود ، اتصل بتنفيذ التغيير. إذا قمت بالفعل بتطبيق نمط على نطاق من الخلايا ، فقم بتعديل سمات النمط واستدعاء الطريقة ، يتم تحديث تنسيق هذه الخلايا تلقائيًا

### **إنشاء وتعديل النمط**

ينشئ هذا المثال كائن نمط ويطبقه على نطاق من الخلايا ويعدل كائن النمط. يتم تطبيق التعديلات تلقائيًا على الخلية والنطاق الذي تم تطبيق النمط عليه.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatingStyle-CreatingStyle.java" >}}

### **تعديل نمط موجود**

يستخدم هذا المثال ملف Excel نموذجيًا بسيطًا تم تطبيق نمط يسمى النسبة المئوية بالفعل على نطاق. المثال:

1. يحصل على الاسلوب
1. يخلق كائن نمط و
1. يعدل تنسيق النمط.

يتم تطبيق التعديلات تلقائيًا على النطاق الذي تم تطبيق النمط عليه.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ModifyExistingStyle-ModifyExistingStyle.java" >}}
