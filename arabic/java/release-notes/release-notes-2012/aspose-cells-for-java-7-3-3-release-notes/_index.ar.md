﻿---
title: Aspose.Cells for Java 7.3.3 ملاحظات الإصدار
type: docs
weight: 20
url: /ar/java/aspose-cells-for-java-7-3-3-release-notes/
---
{{% alert color="primary" %}} 

 تحتوي هذه الصفحة على ملاحظات الإصدار لـ[Aspose.Cells for Java 7.3.3](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-7.3.3/)

{{% /alert %}} 

نحن
 يسعدني أن نعلن Aspose.Cells for Java v7.3.3!

 ميزات جديدة

- أضف طريقة Row.getLastDataCell () للحصول على الخلية الأخيرة التي تحتوي على بيانات في صف واحد
- تمت إضافة واجهات برمجة تطبيقات جديدة للحصول على نفس Styleobject للخلايا ذات إعدادات النمط نفسها

 التحسينات

- أضف علامات اقتباس إلى قيمة (قيم) خلية فارغة عند تصدير CSV مع

 اختيار

 استثناءات

- فشل التنسيق الشرطي بأحرف أحادية
- تسبب إعداد الصيغة قبل إضافة مناطق للتنسيق الشرطي ثم إعادة تسمية ورقة العمل في حدوث خطأ عند حفظ المصنف
- تسبب إعادة حفظ ملف قالب XLS في NegativeArraySizeException

 البق

- كانت قيمة التاريخ المنسق مختلفة عما هو معروض في MS Excel
- تُفقد أسماء سلاسل المخططات إذا تم مسح مجموعة الخلايا
- لا يعمل عرض الفراغ على هيئة فجوات / أصفار لملفات XLSX
- تنسيق تسمية البيانات للمخططات ليس دقيقًا
- اختفى تسطير الخط في ملف PDF الذي تم طرحه
- لم يؤثر تعيين أنماط الخطوط على XLSX في وضع LightCells
- تم فقد جزء من التذييل عند الحفظ بالرقم PDF