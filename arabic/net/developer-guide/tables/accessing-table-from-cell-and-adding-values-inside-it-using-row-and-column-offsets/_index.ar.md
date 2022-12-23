---
title: الوصول إلى الجدول من Cell وإضافة القيم بداخله باستخدام إزاحة الصف والعمود
type: docs
weight: 230
url: /ar/net/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/
---
{{% alert color="primary" %}}

 عادة ، يمكنك إضافة القيم داخل الجدول أو باستخدام كائن القائمة[**Cell.PutValue ()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index)طريقة. لكن في بعض الأحيان ، قد تحتاج إلى إضافة قيم داخل الجدول أو كائن القائمة باستخدام إزاحة الصف والعمود.

من أجل الوصول إلى جدول أو قائمة كائن من خلية ، استخدم[**Cell. GetTable ()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/gettable) طريقة. لإضافة قيم بداخله باستخدام إزاحة الصفوف والعمود ، استخدم ملحق[**ListObject.PutCellValue**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/methods/putcellvalue) طريقة.

{{% /alert %}}

 تُظهر لقطة الشاشة التالية ملف Excel المصدر المستخدم داخل الكود. يحتوي على الجدول الفارغ ويبرز الخلية D5 الموجودة داخل الجدول. سنصل إلى هذا الجدول من الخلية D5 باستخدام[**Cell. GetTable ()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/gettable) الطريقة ثم قم بإضافة القيم بداخلها باستخدام كليهما[**Cell.PutValue ()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) و[**ListObject.PutCellValue**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/methods/putcellvalue)أساليب.

## مثال

### لقطات تقارن المصدر والملفات الناتجة

|![ما يجب القيام به: image_بديل_نص](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_1.png)|
|:- |

تُظهر لقطة الشاشة التالية ملف Excel الناتج الذي تم إنشاؤه بواسطة الكود. كما ترى ، تحتوي الخلية D5 على قيمة والخلية F6 الموجودة في الإزاحة 2،2 من الجدول لها قيمة.

|![ما يجب القيام به: image_بديل_نص](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_2.png)|
|:- |

### كود C# للتوصل إلى الجدول من الخلية ولإضافة قيم بداخله باستخدام إزاحة الصف والعمود

يقوم نموذج التعليمات البرمجية التالي بتحميل ملف Excel المصدر كما هو موضح في لقطة الشاشة أعلاه ويضيف قيمًا داخل الجدول وينشئ ملف Excel الناتج كما هو موضح أعلاه.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-AccessTableFromCellAndAddValue-AccessTableFromCellAndAddValue.cs" >}}
