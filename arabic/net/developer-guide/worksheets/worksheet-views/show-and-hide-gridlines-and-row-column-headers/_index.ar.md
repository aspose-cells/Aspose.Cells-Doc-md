---
title: إظهار وإخفاء خطوط الشبكة ورؤوس أعمدة الصفوف
type: docs
weight: 30
url: /ar/net/show-and-hide-gridlines-and-row-column-headers/
description: توفر هذه المقالة نموذج التعليمات البرمجية لاستخدام C# API أو .NET Library لإخفاء أو إظهار خطوط الشبكة ورؤوس الصفوف والأعمدة لورقة عمل Excel برمجيًا.
---
{{% alert color="primary" %}}

يدعم Aspose.Cells الاخفاء وإظهار خطوط الشبكة الخاصة بورقة العمل والتي تكون مرئية بشكل افتراضي. كما يوفر إمكانية التحكم في رؤية رؤوس أعمدة الصف في ورقة العمل.

{{% /alert %}}

## **إظهار وإخفاء خطوط الشبكة**

تحتوي جميع أوراق عمل Excel على خطوط شبكة بشكل افتراضي. إنها تساعد في تحديد الخلايا بحيث يسهل إدخال البيانات في خلايا معينة. تمكننا خطوط الشبكة من عرض ورقة العمل كمجموعة من الخلايا ، حيث يمكن التعرف على كل خلية بسهولة.

### **التحكم في رؤية خطوط الشبكة**

Aspose.Cells يوفر فصل دراسي ،[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook)، يمثل ملف Excel Microsoft. ال[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook)فئة تحتوي على[**أوراق عمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)مجموعة تسمح للمطورين بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) صف دراسي. ال[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) توفر class مجموعة واسعة من الخصائص والأساليب لإدارة ورقة العمل. للتحكم في رؤية خطوط الشبكة ، استخدم ملف[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) صف دراسي[**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) خاصية.[**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) هي خاصية منطقية ، مما يعني أنه يمكنها فقط تخزين ملف**حقيقي** أو**خاطئة** القيمة.

#### **جعل خطوط الشبكة مرئية**

 اجعل خطوط الشبكة مرئية عن طريق ضبط[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) صف دراسي[**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) ملكية ل**حقيقي**.

#### **إخفاء خطوط الشبكة**

 إخفاء خطوط الشبكة عن طريق تعيين ملف[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) صف دراسي[**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) ملكية ل**خاطئة**.

 ويرد أدناه مثال كامل يوضح استخدام[**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible)الخاصية عن طريق فتح ملف Excel (book1.xls) ، وإخفاء خطوط الشبكة في ورقة العمل الأولى وحفظ الملف المعدل باسم output.xls.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-DisplayHideGridlines-1.cs" >}}

## **إظهار وإخفاء رؤوس أعمدة الصفوف**

تتكون جميع أوراق العمل في ملف Excel من خلايا مرتبة في صفوف وأعمدة. تحتوي جميع الصفوف والأعمدة على قيم فريدة تُستخدم لتعريفها ولتعريف الخلايا الفردية. على سبيل المثال ، يتم ترقيم الصفوف - 1 ، 2 ، 3 ، 4 ، وما إلى ذلك - ويتم ترتيب الأعمدة أبجديًا - A ، B ، C ، D ، إلخ. يتم عرض قيم الصفوف والأعمدة في الرؤوس. باستخدام Aspose.Cells ، يمكن للمطورين التحكم في رؤية رؤوس الصفوف والأعمدة هذه.

### **التحكم في رؤية أوراق العمل**

Aspose.Cells يوفر فصل دراسي ،[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook)، يمثل ملف Excel Microsoft. ال[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook)فئة تحتوي على[**أوراق عمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)مجموعة تسمح للمطورين بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)صف دراسي. ال[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) توفر class مجموعة واسعة من الخصائص والأساليب لإدارة ورقة العمل. للتحكم في رؤية رؤوس الصفوف والأعمدة ، استخدم ملحق[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) صف دراسي[**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) خاصية.[**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) هي خاصية منطقية ، مما يعني أنه يمكنها فقط تخزين ملف**حقيقي** أو**خاطئة**القيمة.

#### **جعل رؤوس الصفوف / الأعمدة مرئية**

 اجعل رؤوس الصفوف والأعمدة مرئية عن طريق تعيين[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) صف دراسي[**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) ملكية ل**حقيقي**.

#### **إخفاء رؤوس الصفوف / الأعمدة**

 إخفاء رؤوس الصفوف والأعمدة عن طريق تعيين ملف[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) صف دراسي[**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) ملكية ل**خاطئة**.

ويرد أدناه مثال كامل يوضح كيفية استخدام ملف[**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible)الخاصية عن طريق فتح ملف Excel (book1.xls) ، وإخفاء رؤوس الصفوف والأعمدة في ورقة العمل الأولى وحفظ الملف المُعدَّل باسم output.xls.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-DisplayHideRowColumnHeaders-1.cs" >}}

{{% alert color="primary" %}}

 من الممكن أيضًا استخدام ملف[**إظهار الصفوف**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhiderows) و[**UnhideColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhidecolumns) طرق[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) فئة لإظهار العديد من الصفوف والأعمدة.

{{% /alert %}}
