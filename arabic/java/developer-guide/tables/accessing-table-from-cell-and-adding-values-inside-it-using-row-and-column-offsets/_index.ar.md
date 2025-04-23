---
title: الوصول إلى الجدول من الخلية وإضافة القيم داخله باستخدام إزاحة الصف والعمود
type: docs
weight: 110
url: /ar/java/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/
---

{{% alert color="primary" %}}

عادةً ما تضيف القيم داخل الجدول أو كائن القائمة باستخدام الطريقة [**Cell.putValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#putValue-boolean-). ولكن في بعض الأحيان، قد تحتاج إلى إضافة القيم داخل الجدول أو كائن القائمة باستخدام إزاحة الصف والعمود.

من أجل الوصول إلى جدول أو كائن قائمة من الخلية، استخدم الطريقة [**Cell.getTable()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getTable--). ولإضافة القيم داخله باستخدام إزاحة الصف والعمود، استخدم الطريقة [**ListObject.putCellValue(rowOffset,columnOffset,value)**](https://reference.aspose.com/cells/java/com.aspose.cells/listobject#putCellValue-int-int-java.lang.Object-).

{{% /alert %}}

## مثال

### لقطات شاشة تقارن الملفات المصدرية والإخراجية

تُظهر اللقطة الشاشية التالية ملف Excel المصدر المستخدم داخل الكود. يحتوي على جدول فارغ ويبرز الخلية D5 التي تقع داخل الجدول. سنتمكن من الوصول إلى هذا الجدول من الخلية D5 باستخدام الطريقة [**Cell.getTable()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getTable--) ثم إضافة القيم داخله باستخدام كل من الطريقة [**Cell.putValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#putValue-boolean-) و [**ListObject.putCellValue(rowOffset,columnOffset,value)**](https://reference.aspose.com/cells/java/com.aspose.cells/listobject#putCellValue-int-int-java.lang.Object-).

![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_1.png)

اللقطة الشاشية التالية تُظهر ملف Excel الناتج الذي تم إنشاؤه بواسطة الكود. كما يمكنك رؤية الخلية D5 التي تحتوي على قيمة والخلية F6 والتي تقع في الإزاحة 2،2 من الجدول وتحتوي على قيمة.

![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_2.png)

### الشيفرة في جافا للوصول إلى الجدول من الخلية وإضافة القيم داخلها باستخدام تعويضات الصف والعمود

يقوم الكود النموذجي التالي باستخدام ملف Excel المصدر كما هو موضح في اللقطة الشاشية أعلاه ويضيف القيم داخل الجدول ويولد ملف Excel الناتج كما هو موضح أعلاه.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AccessingTablefromCell-AccessingTablefromCell.java" >}}
{{< app/cells/assistant language="java" >}}
