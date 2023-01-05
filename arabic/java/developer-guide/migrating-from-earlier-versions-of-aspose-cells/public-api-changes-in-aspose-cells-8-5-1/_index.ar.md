---
title: عام API التغييرات في Aspose.Cells 8.5.1
type: docs
weight: 180
url: /ar/java/public-api-changes-in-aspose-cells-8-5-1/
---
{{% alert color="primary" %}} 

 توضح هذه الوثيقة التغييرات التي تم إجراؤها على Aspose.Cells API من الإصدار 8.5.0 إلى 8.5.1 والتي قد تهم مطوري الوحدة النمطية / التطبيق. لا يشمل فقط الأساليب العامة الجديدة والمحدثة ،[الفئات المضافة وما إلى ذلك.](/cells/ar/java/public-api-changes-in-aspose-cells-8-5-1/)ولكن أيضًا وصف لأية تغييرات في السلوك خلف الكواليس عام Aspose.Cells.

{{% /alert %}} 
## **تمت إضافة واجهات برمجة التطبيقات**
### **مصنف الطريقة**
كشف Aspose.Cells for Java 8.5.1 طريقة Workbook.dispose لتحرير الموارد غير المُدارة لكائن المصنف. يتم استخدام نمط التخلص فقط للكائنات التي تصل إلى موارد غير مُدارة ، مثل مقابض الملفات والأنابيب أو مقابض التسجيل أو مقابض الانتظار أو مؤشرات كتل الذاكرة غير المُدارة. هذا لأن جامع القمامة فعال للغاية في استعادة الكائنات المدارة غير المستخدمة ، لكنه غير قادر على استعادة الكائنات غير المُدارة.

**Java**

{{< highlight "csharp" >}}

 //Create workbook object

Workbook book = new Workbook();

//Call dispose method

book.dispose();

{{< /highlight >}}
### **الطريقة Cell.getHeightOfValue مضافة**
 كشف Aspose.Cells for Java 8.5.1 طريقة Cell.getHeightOfValue للحصول على ارتفاع قيمة الخلية. باستخدام هذه الطريقة ، يمكنك حساب ارتفاع قيمة الخلية ثم تعيين ارتفاع صف تلك الخلية على التوالي. تحقق من المقال المفصل على[كيفية حساب ارتفاع الخلية وعرضها](/cells/ar/java/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/).
### **تمت إضافة جدول التعداد**
Aspose.Cells for Java 8.5.1 كشف التعداد com.aspose.cells.TableDataSourceType لاسترجاع نوع مصدر البيانات من ListObject. تعداد TableDataSourceType كحقول التالية.

1. TableDataSourceType.QUERY_TABLE
1. TableDataSourceType.SHARE_POINT
1. TableDataSourceType.WORKSHEET
1. TableDataSourceType.XML
### **تمت إضافة خاصية ListObject.DataSourceType**
مع إصدار v8.5.1 ، كشف Aspose.Cells API عن خاصية ListObject.DataSourceType للقراءة فقط والتي يمكن استخدامها للكشف عن نوع مصدر البيانات الخاص بـ ListObject.

هنا هو أبسط سيناريو استخدام.

**Java**

{{< highlight "csharp" >}}

 Workbook book = new Workbook("D:/book1.xlsx");

Worksheet sheet = book.getWorksheets().get(0);

ListObject listObject = sheet.getListObjects().get(0);

if (listObject.getDataSourceType() == com.aspose.cells.TableDataSourceType.QUERY_TABLE)

{

	System.out.println("Data Source Type is Query Table");

}

else if (listObject.getDataSourceType() == com.aspose.cells.TableDataSourceType.SHARE_POINT)

{

	System.out.println("Data Source Type is SharePoint Linked List");

}

else if (listObject.getDataSourceType() == com.aspose.cells.TableDataSourceType.WORKSHEET)

{

	System.out.println("Data Source Type is Excel Worksheet Table");

}

else if (listObject.getDataSourceType() == com.aspose.cells.TableDataSourceType.XML)

{

	System.out.println("Data Source Type is XML");

}

{{< /highlight >}}
