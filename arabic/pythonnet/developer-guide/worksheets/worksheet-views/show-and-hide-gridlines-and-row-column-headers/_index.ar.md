---
title: إظهار وإخفاء خطوط الشبكة ورؤوس الصف والعمود
type: docs
weight: 30
url: /ar/python-net/show-and-hide-gridlines-and-row-column-headers/
description: هذه المقالة توفر كودًا عينيًا لاستخدام Aspose.Cells for Python via .NET API لإخفاء أو عرض خطوط الشبكة، رؤوس الصف والعمود بشكل برمجي لورقة العمل في Excel.
keywords: مكتبة Python Excel، عرض وإخفاء الخطوط الشبكية في Python، كيفية إظهار وإخفاء رؤوس الصف والعمود في Python، كيفية إظهار وإخفاء الخطوط الشبكية ورؤوس الصف والعمود في Python.
---

{{% alert color="primary" %}}

تدعم Aspose.Cells for Python via .NET إخفاء وعرض شبكة الصفحة التي يكون ظهورها افتراضيًا. كما توفر السيطرة على ظهور رؤوس الصف والعمود في ورقة العمل.

{{% /alert %}}

## **إظهار وإخفاء خطوط الشبكة**

تحتوي جميع ورقات العمل في Excel على خطوط شبكية افتراضيًا. تساعد في تحديد الخلايا بحيث يكون من السهل إدخال البيانات في خلايا معينة. تمكِّن الخطوط الشبكية من عرض ورقة العمل كمجموعة من الخلايا، حيث يمكن تحديد كل خلية بسهولة.

### **التحكم في رؤية خطوط الشبكة**

توفر Aspose.Cells for Python via .NET فئة، [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/)، تمثل ملف Microsoft Excel. تحتوي الفئة [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/) على مجموعة [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/) تسمح للمطورين بالوصول إلى كل ورقة عمل في ملف Excel. تمثل ورقة العمل بالفئة [**Worksheet**](https://reference.aspose.com/cells/python-et/aspose.cells/worksheet/). توفر الفئة [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/) مجموعة واسعة من الخصائص والطرق لإدارة ورقة العمل. للتحكم في ظهور خطوط الشبكة، استخدم خاصية الفئة [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/). [**is_gridlines_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_gridlines_visible/) هي خاصية بوليانية، وهذا يعني أنها يمكنها فقط تخزين قيمة **صحيحة** أو **كاذبة**.

#### **جعل خطوط الشبكة مرئية**

قم بجعل خطوط الشبكة مرئية عن طريق تعيين خاصية الفئة [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) [**is_gridlines_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_gridlines_visible/) إلى **true**.

#### **إخفاء خطوط الشبكة**

إخفاء خطوط الشبكة عن طريق تعيين خاصية الفئة [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) [**is_gridlines_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_gridlines_visible/) إلى **false**.

يتم تقديم مثال كامل أدناه الذي يوضح استخدام الخاصية [**is_gridlines_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_gridlines_visible/) عن طريق فتح ملف Excel (book1.xls)، إخفاء خطوط الشبكة على أول ورقة عمل وحفظ الملف المعدل بوصفه output.xls.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Views-Display-DisplayHideGridlines-1.py" >}}

## **إظهار وإخفاء رؤوس الصف والعمود**

جميع ورقات العمل في ملف Excel تتكون من خلايا منظمة في صفوف وأعمدة. تحتوي جميع الصفوف والأعمدة على قيم فريدة تُستخدم لتحديد هويتها ولتحديد الخلايا الفردية. على سبيل المثال، تُرقم الصفوف بأرقام - 1، 2، 3، 4، وما إلى ذلك - وتُرتب الأعمدة ترتيبًا أبجديًا - A، B، C، D، وما إلى ذلك. تُعرض قيم الصف والعمود في رؤوس. باستخدام Aspose.Cells for Python via .NET، يمكن للمطورين التحكم في ظهور هذه الرؤوس للصفوف والأعمدة.

### **التحكم في رؤية ورقات العمل**

توفر Aspose.Cells for Python via .NET فئة، [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/)، تمثل ملف Microsoft Excel. تحتوي الفئة [**Workbook**](https://reference.aspose.com/cells/pytho-net/aspose.cells/workbook/) على مجموعة [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/) تسمح للمطورين بالوصول إلى كل ورقة عمل في ملف Excel. تمثل ورقة العمل بالفئة [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/). توفر الفئة [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/) مجموعة واسعة من الخصائص والطرق لإدارة ورقة العمل. للتحكم في ظهور رؤوس الصف والعمود، استخدم خاصية الفئة [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/). [**is_row_column_headers_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_row_column_headers_visible/) هي خاصية بوليانية، وهذا يعني أنها يمكنها فقط تخزين قيمة **صحيحة** أو **كاذبة**.

#### **جعل رؤوس الصف/العمود مرئية**

جعل رؤوس الصف والعمود مرئية عن طريق تعيين خاصية الفئة [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) [**is_row_column_headers_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_row_column_headers_visible/) إلى **true**.

#### **إخفاء رؤوس الصف/العمود**

إخفاء رؤوس الصف والعمود عن طريق تعيين خاصية الفئة [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) [**is_row_column_headers_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_row_column_headers_visible/) إلى **false**.

يتم تقديم مثال كامل أدناه الذي يوضح كيفية استخدام الخاصية [**is_row_column_headers_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_row_column_headers_visible/) عن طريق فتح ملف Excel (book1.xls)، إخفاء رؤوس الصف والعمود على أول ورقة عمل وحفظ الملف المعدل بوصفه output.xls.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Views-Display-DisplayHideRowColumnHeaders-1.py" >}}

{{% alert color="primary" %}}

من الممكن أيضًا استخدام طرق [**unhide_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_rows) و [**unhide_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_columns)  للفئة [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) لجعل عدة صفوف وأعمدة مرئية.

{{% /alert %}}
