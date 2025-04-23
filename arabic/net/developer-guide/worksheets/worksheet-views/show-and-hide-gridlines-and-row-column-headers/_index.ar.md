---
title: إظهار وإخفاء خطوط الشبكة ورؤوس الصف والعمود
type: docs
weight: 30
url: /ar/net/show-and-hide-gridlines-and-row-column-headers/
description: يقدم هذا المقال شيفرة المثالية لاستخدام واجهة برمجة تطبيقات C# أو مكتبة .NET بشكل برمجي لإخفاء أو عرض خطوط الشبكة ورؤوس الصف والعمود في ورقة عمل Excel.
---

{{% alert color="primary" %}}

يدعم Aspose.Cells إخفاء وعرض خطوط الشبكة لورقة العمل التي يكون ظهورها افتراضيًا. كما يوفر التحكم في رؤوس الصف والعمود لورقة العمل.

{{% /alert %}}

## **إظهار وإخفاء خطوط الشبكة**

تحتوي جميع ورقات العمل في Excel على خطوط شبكية افتراضيًا. تساعد في تحديد الخلايا بحيث يكون من السهل إدخال البيانات في خلايا معينة. تمكِّن الخطوط الشبكية من عرض ورقة العمل كمجموعة من الخلايا، حيث يمكن تحديد كل خلية بسهولة.

### **التحكم في رؤية خطوط الشبكة**

Aspose.Cells توفر فئة، [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)، التي تمثل ملف Microsoft Excel. تحتوي الفئة [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) على مجموعة [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) تتيح للمطورين الوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). توفر الفئة [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) مجموعة واسعة من الخصائص والأساليب لإدارة ورقة العمل. للتحكم في رؤية خطوط الشبكة، استخدم خاصية الفئة [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) [**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible). [**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) هي خاصية Boolean، مما يعني أنه يمكنها تخزين قيمة **true** أو **false** فقط.

#### **جعل خطوط الشبكة مرئية**

قم بجعل خطوط الشبكة مرئية عن طريق تعيين خاصية الفئة [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) [**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) إلى **true**.

#### **إخفاء خطوط الشبكة**

إخفاء خطوط الشبكة عن طريق تعيين خاصية الفئة [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) [**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) إلى **false**.

يتم تقديم مثال كامل أدناه الذي يوضح استخدام الخاصية [**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) عن طريق فتح ملف Excel (book1.xls)، إخفاء خطوط الشبكة على أول ورقة عمل وحفظ الملف المعدل بوصفه output.xls.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-DisplayHideGridlines-1.cs" >}}

## **إظهار وإخفاء رؤوس الصف والعمود**

جميع ورقات العمل في ملف Excel مكونة من خلايا مرتبة في صفوف وأعمدة. جميع الصفوف والأعمدة لها قيم فريدة يتم استخدامها لتحديدها وتحديد الخلايا الفردية. على سبيل المثال، يتم ترقيم الصفوف - 1، 2، 3، 4، الخ. - وترتيب الأعمدة ترتيبها أبجديًا - أ، ب، ج، د، الخ. تظهر قيم الصف والعمود في الرؤوس. باستخدام Aspose.Cells، يمكن للمطورين التحكم في رؤية هذه الرؤوس للصف والعمود.

### **التحكم في رؤية ورقات العمل**

توفر Aspose.Cells فئة [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) التي تمثل ملف Microsoft Excel. الفئة [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) تحتوي على مجموعة [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) التي تسمح للمطورين بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة الفئة [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). توفر الفئة [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) مجموعة واسعة من الخصائص والأساليب لإدارة ورقة العمل. للتحكم في رؤية رؤوس الصف والعمود، استخدم خاصية الفئة [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible). [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) هي خاصية Boolean، مما يعني أنها يمكنها تخزين قيمة **true** أو **false** فقط.

#### **جعل رؤوس الصف/العمود مرئية**

جعل رؤوس الصف والعمود مرئية عن طريق تعيين خاصية الفئة [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) إلى **true**.

#### **إخفاء رؤوس الصف/العمود**

إخفاء رؤوس الصف والعمود عن طريق تعيين خاصية الفئة [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) إلى **false**.

يتم تقديم مثال كامل أدناه الذي يوضح كيفية استخدام الخاصية [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) عن طريق فتح ملف Excel (book1.xls)، إخفاء رؤوس الصف والعمود على أول ورقة عمل وحفظ الملف المعدل بوصفه output.xls.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-DisplayHideRowColumnHeaders-1.cs" >}}

{{% alert color="primary" %}}

من الممكن أيضًا استخدام طرق [**UnhideRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhiderows) و [**UnhideColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhidecolumns)  للفئة [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) لجعل عدة صفوف وأعمدة مرئية.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
