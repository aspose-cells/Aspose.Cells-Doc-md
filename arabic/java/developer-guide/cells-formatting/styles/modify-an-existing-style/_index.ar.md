---
title: تعديل نمط موجود
type: docs
weight: 50
url: /ar/java/modify-an-existing-style/
description: تعلم كيفية تغيير الأنماط في Excel مع Microsoft Excel ومع واجهة برمجة التطبيقات Aspose.Cells for Java.
keywords: تعديل نمط موجود اكسل، تعديل نمط موجود اكسل جافا، تعديل نمط موجود اكسل، تعديل نمط موجود اكسل جافا، تغيير نمط موجود في اكسل، تغيير نمط موجود في اكسل جافا، كيفية تغيير النمط في اكسل، كيفية تغيير النمط في اكسل مع جافا، كيفية تغيير النمط في اكسل مع جافا، كيفية تغيير النمط في اكسل باستخدام جافا، تغيير نمط موجود في اكسل جافا، تغيير نمط موجود في اكسل
---

{{% alert color="primary" %}}

لتطبيق نفس خيارات التنسيق على الخلايا، قم بإنشاء كائن نمط تنسيق جديد. كائن نمط التنسيق هو مزيج من السمات التنسيقية مثل الخط، حجم الخط، البدء، العدد، الحدود، الأنماط، الخ، معروفة ومخزنة كمجموعة. عند تطبيقها، يتم تطبيق جميع التنسيقات في هذا النمط.

يمكنك أيضا استخدام نمط موجود، حفظه مع الدفتر واستخدامه لتنسيق المعلومات بنفس السمات.

عندما لا تتم تنسيق الخلايا بشكل صريح، يتم تطبيق النمط العادي (نمط الافتراضي للدفتر). Microsoft Excel يعرف مسبقا العديد من الأنماط بالإضافة إلى النمط العادي بما في ذلك Comma و Currency و Percent.

تسمح Aspose.Cells بتعديل أي من هذه الأنماط أو أي نمط آخر تعرفه بالسمات المرغوبة.

{{% /alert %}}

## **استخدام Microsoft Excel**

لتحديث نمط في Microsoft Excel 97-2003:

1. في قائمة **تنسيق**، انقر على **نمط**.
1. حدد النمط الذي تريد تعديله من قائمة **اسم النمط**.
1. انقر على **تعديل**.
1. اختر خيارات النمط التي تريدها باستخدام علامات التبويب في مربع حوار تنسيق الخلايا.
1. انقر على **موافق**.
1. في **يتضمن النمط**, حدد ميزات النمط التي تريدها.
1. انقر **موافق** لحفظ النمط وتطبيقه على النطاق المحدد.

## **استخدام Aspose.Cells**

توفر Aspose.Cells الطريقة [**Style.update**](https://reference.aspose.com/cells/java/com.aspose.cells/style#update--) لتحديث نمط موجود.

لتغيير نمط مسمى، سواء تم إنشاؤه ديناميكيًا باستخدام Aspose.Cells أو محددًا مسبقًا، قم بالاتصال بالطريقة [**Style.update**](https://reference.aspose.com/cells/java/com.aspose.cells/style#update--) لعكس أي تغييرات في النمط المطبق على خلية أو نطاق.

الطريقة [**Style.update**](https://reference.aspose.com/cells/java/com.aspose.cells/style#update--) تتصرف مثل زر **موافق** في مربع حوار النمط: بعد إجراء تغييرات في نمط موجود، اتصل لتنفيذ التغيير. إذا كنت قد قمت بالفعل بتطبيق نمط على مجموعة من الخلايا، قم بتعديل سمات النمط واستدعاء الطريقة، يتم تحديث تنسيق تلك الخلايا تلقائيًا

### **إنشاء وتعديل نمط**

هذا المثال ينشئ كائن نمط، يطبقه على مجموعة من الخلايا ويعدل كائن النمط. يتم تطبيق التعديلات تلقائيًا على الخلية والنطاق الذي تم تطبيق النمط عليه.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatingStyle-CreatingStyle.java" >}}

### **تعديل نمط موجود**

يستخدم هذا المثال ملف Excel قالبي بسيط تم تطبيق نمط يُسمى النسبة على نطاق معين بالفعل. المثال:

1. يستلم النمط,
1. ينشئ كائن نمط و
1. يعدل تنسيق النمط.

يتم تطبيق التعديلات تلقائيًا على النطاق الذي تم تطبيق النمط عليه.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ModifyExistingStyle-ModifyExistingStyle.java" >}}
{{< app/cells/assistant language="java" >}}
