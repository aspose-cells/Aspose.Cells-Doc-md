---
title: إظهار وإخفاء خطوط الشبكة ورؤوس الصف والعمود
type: docs
weight: 30
url: /ar/python-net/show-and-hide-gridlines-and-row-column-headers/
description: تقدم هذه المقالة رمز عينة لاستخدام API من Aspose.Cells لـ Python via .NET لإخفاء أو إظهار خطوط الشبكة، رؤوس الصفوف والأعمدة لورقة عمل Excel برمجيًا.
keywords: مكتبة Excel لـ Python، إظهار وإخفاء خطوط الشبكة في Python، كيفية إظهار وإخفاء رؤوس الصفوف والأعمدة في Python، كيفية إظهار وإخفاء خطوط الشبكة ورؤوس الصفوف والأعمدة في Python.
---

{{% alert color="primary" %}}

 يدعم Aspose.Cells لـ Python via .NET إخفاء وإظهار خطوط الشبكة لورقة العمل التي تكون مرئية بشكل افتراضي. كما يوفر التحكم في رأسا رؤوس الصفوف والأعمدة.

{{% /alert %}}

## **إظهار وإخفاء خطوط الشبكة**

تحتوي جميع ورقات العمل في Excel على خطوط شبكية افتراضيًا. تساعد في تحديد الخلايا بحيث يكون من السهل إدخال البيانات في خلايا معينة. تمكِّن الخطوط الشبكية من عرض ورقة العمل كمجموعة من الخلايا، حيث يمكن تحديد كل خلية بسهولة.

### **التحكم في رؤية خطوط الشبكة**

 يوفر Aspose.Cells لـ Python via .NET فئة، [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/)، تمثل ملف Excel من Microsoft. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/) على مجموعة [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/) تتيح للمطورين الوصول إلى كل ورقة عمل في ملف Excel. تمثل ورقة العمل بواسطة الفئة [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/). توفر فئة [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/) مجموعة واسعة من الخصائص والطرق لإدارة ورقة العمل. للتحكم في رؤية خطوط الشبكة، استخدم الخاصية [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/) من فئة [**is_gridlines_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_gridlines_visible/). [**is_gridlines_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_gridlines_visible/) هي خاصية Boolean، مما يعني أنها يمكن أن تخزن فقط قيمة **true** أو **false**.

#### **جعل خطوط الشبكة مرئية**

قم بجعل خطوط الشبكة مرئية عن طريق تعيين خاصية الفئة [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) [**is_gridlines_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_gridlines_visible/) إلى **true**.

#### **إخفاء خطوط الشبكة**

إخفاء خطوط الشبكة عن طريق تعيين خاصية الفئة [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) [**is_gridlines_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_gridlines_visible/) إلى **false**.

يتم تقديم مثال كامل أدناه الذي يوضح استخدام الخاصية [**is_gridlines_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_gridlines_visible/) عن طريق فتح ملف Excel (book1.xls)، إخفاء خطوط الشبكة على أول ورقة عمل وحفظ الملف المعدل بوصفه output.xls.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Views-Display-DisplayHideGridlines-1.py" >}}

## **إظهار وإخفاء رؤوس الصف والعمود**

تتكون جميع أوراق العمل في ملف Excel من خلايا مرتبة في صفوف وأعمدة. جميع الصفوف والأعمدة لها قيم فريدة تُستخدم للتعرف عليها والتعرف على خلايا فردية. على سبيل المثال، ترقم الصفوف - 1، 2، 3، 4، إلخ، وترتب الأعمدة أبجديًا - A، B، C، D، إلخ. تُعرض قيم الصفوف والأعمدة في الرؤوس. باستخدام Aspose.Cells لـ Python via .NET، يمكن للمطورين التحكم في رؤية رؤوس الصفوف والأعمدة هذه.

### **التحكم في رؤية ورقات العمل**

توفر Aspose.Cells لـ Python via .NET فئة، [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/)، تمثل ملف Excel من Microsoft. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/) على مجموعة [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/) تتيح للمطورين الوصول إلى كل ورقة عمل في الملف. تمثل ورقة العمل بواسطة الفئة [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/). توفر الفئة [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/) مجموعة واسعة من الخصائص والطرق لإدارة ورقة العمل. للتحكم في رؤية رؤوس الصفوف والأعمدة، استخدم الخاصية [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/) من فئة [**is_row_column_headers_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_row_column_headers_visible/). [**is_row_column_headers_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_row_column_headers_visible/) هي خاصية Boolean، مما يعني أنها يمكن أن تخزن فقط قيمة **true** أو **false**.

#### **جعل رؤوس الصف/العمود مرئية**

جعل رؤوس الصف والعمود مرئية عن طريق تعيين خاصية الفئة [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) [**is_row_column_headers_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_row_column_headers_visible/) إلى **true**.

#### **إخفاء رؤوس الصف/العمود**

إخفاء رؤوس الصف والعمود عن طريق تعيين خاصية الفئة [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) [**is_row_column_headers_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_row_column_headers_visible/) إلى **false**.

يتم تقديم مثال كامل أدناه الذي يوضح كيفية استخدام الخاصية [**is_row_column_headers_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_row_column_headers_visible/) عن طريق فتح ملف Excel (book1.xls)، إخفاء رؤوس الصف والعمود على أول ورقة عمل وحفظ الملف المعدل بوصفه output.xls.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Views-Display-DisplayHideRowColumnHeaders-1.py" >}}

{{% alert color="primary" %}}

من الممكن أيضًا استخدام طرق [**unhide_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_rows) و [**unhide_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_columns)  للفئة [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) لجعل عدة صفوف وأعمدة مرئية.

{{% /alert %}}
{{< app/cells/assistant language="python-net" >}}
