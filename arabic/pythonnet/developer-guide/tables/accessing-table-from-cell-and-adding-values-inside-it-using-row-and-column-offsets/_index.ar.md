---
title: الوصول إلى الجدول من الخلية وإضافة القيم داخله باستخدام إزاحة الصف والعمود
type: docs
weight: 230
url: /ar/python-net/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/
---

{{% alert color="primary" %}}

عادةً ما تضيف القيم داخل الجدول أو كائن القائمة باستخدام الطريقة [**Cell.put_value()**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#bool). ولكن في بعض الأحيان، قد تحتاج إلى إضافة القيم داخل الجدول أو كائن القائمة باستخدام إزاحة الصف والعمود.

للوصول إلى جدول أو كائن القائمة من خلية، استخدم الطريقة [**Cell.get_table()**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_table/#). لإضافة القيم داخلها باستخدام إزاحة الصف والعمود، استخدم الطريقة [**ListObject.put_cell_value**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject/put_cell_value/#int-int-any).

{{% /alert %}}

تُظهر اللقطة الشاشية التالية ملف Excel المصدر المستخدم داخل الكود. يحتوي على جدول فارغ ويبرز الخلية D5 التي تقع داخل الجدول. سنتمكن من الوصول إلى هذا الجدول من الخلية D5 باستخدام الطريقة [**Cell.get_table()**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_table/#) ثم إضافة القيم داخله باستخدام كل من الطريقة [**Cell.put_value()**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#bool) و [**ListObject.put_cell_value**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject/put_cell_value/#int-int-any).

## مثال

### لقطات شاشة تقارن الملفات المصدرية والإخراجية

|![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_1.png)|
| :- |

اللقطة الشاشية التالية تُظهر ملف Excel الناتج الذي تم إنشاؤه بواسطة الكود. كما يمكنك رؤية الخلية D5 التي تحتوي على قيمة والخلية F6 والتي تقع في الإزاحة 2،2 من الجدول وتحتوي على قيمة.

|![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_2.png)|
| :- |

### رمز بايثون للوصول إلى الجدول من الخلية وإضافة القيم بداخله باستخدام إزاحة الصف والعمود

يقوم الكود النموذجي التالي باستخدام ملف Excel المصدر كما هو موضح في اللقطة الشاشية أعلاه ويضيف القيم داخل الجدول ويولد ملف Excel الناتج كما هو موضح أعلاه.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Tables-AccessTableFromCellAndAddValue.py" >}}
{{< app/cells/assistant language="python-net" >}}
