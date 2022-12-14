---
title: الوصول إلى الجدول من Cell وإضافة القيم بداخله باستخدام إزاحة الصف والعمود
type: docs
weight: 110
url: /ar/java/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/
---
{{% alert color="primary" %}}

 عادة ، يمكنك إضافة القيم داخل الجدول أو باستخدام كائن القائمة[**Cell.putValue ()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#putValue(boolean)) طريقة. لكن في بعض الأحيان ، قد تحتاج إلى إضافة قيم داخل الجدول أو كائن القائمة باستخدام إزاحة الصف والعمود.

من أجل الوصول إلى جدول أو قائمة كائن من خلية ، استخدم[**Cell.getTable ()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getTable() ) طريقة. ولإضافة قيم بداخله باستخدام إزاحة الصفوف والعمود ، استخدم ملحق[**ListObject.putCellValue (rowOffset ، columnOffset ، value)**](https://reference.aspose.com/cells/java/com.aspose.cells/listobject#putCellValue(int,%20int,%20java.lang.Object)) طريقة.

{{% /alert %}}

## مثال

### لقطات تقارن المصدر والملفات الناتجة

 تُظهر لقطة الشاشة التالية ملف Excel المصدر المستخدم داخل الكود. يحتوي على الجدول الفارغ ويبرز الخلية D5 الموجودة داخل الجدول. سنصل إلى هذا الجدول من الخلية D5 باستخدام[**Cell.getTable ()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getTable() ) ثم أضف القيم بداخلها باستخدام كليهما[**Cell.putValue ()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#putValue(boolean) ) و[**ListObject.putCellValue (rowOffset ، columnOffset ، value)**](https://reference.aspose.com/cells/java/com.aspose.cells/listobject#putCellValue(int,%20int,%20java.lang.Object)) طُرق.

![ما يجب القيام به: image_بديل_نص](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_1.png)

تُظهر لقطة الشاشة التالية ملف Excel الناتج الذي تم إنشاؤه بواسطة الكود. كما ترى ، تحتوي الخلية D5 على قيمة والخلية F6 الموجودة في الإزاحة 2،2 من الجدول لها قيمة.

![ما يجب القيام به: image_بديل_نص](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_2.png)

### كود Java للتوصل إلى الجدول من الخلية ولإضافة قيم بداخله باستخدام إزاحة الصف والعمود

يقوم نموذج التعليمات البرمجية التالي بتحميل ملف Excel المصدر كما هو موضح في لقطة الشاشة أعلاه ويضيف قيمًا داخل الجدول وينشئ ملف Excel الناتج كما هو موضح أعلاه.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AccessingTablefromCell-AccessingTablefromCell.java" >}}
