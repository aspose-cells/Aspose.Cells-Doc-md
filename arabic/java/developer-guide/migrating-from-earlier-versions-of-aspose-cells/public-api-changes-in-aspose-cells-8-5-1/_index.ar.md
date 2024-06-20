---
title: تغييرات واجهة برمجة التطبيقات العامة في Aspose.Cells 8.5.1
type: docs
weight: 180
url: /ar/java/public-api-changes-in-aspose-cells-8-5-1/
---

{{% alert color="primary" %}} 

يصف هذا المستند التغييرات في واجهة برمجة التطبيقات Aspose.Cells من الإصدار 8.5.0 إلى 8.5.1 التي قد تكون مثيرة لاهتمام مطوري الوحدات/التطبيقات. يشمل ليس فقط الطرق العامة الجديدة والمحدثة و[الفصول المضافة الخ..](/cells/ar/java/public-api-changes-in-aspose-cells-8-5-1/)، ولكن أيضًا وصفًا لأي تغييرات في السلوك الكامن في Aspose.Cells.

{{% /alert %}} 
## **واجهات برمجة التطبيقات الجديدة**
### **تمت إضافة طريقة Workbook.Dispose**
Aspose.Cells for Java 8.5.1 قام بتعريض طريقة Workbook.dispose لإطلاق موارد غير المُدارة لكائن Workbook. يتم استخدام نمط الإطلاق فقط لكائنات تصل إلى موارد غير مُدارة، مثل مقابض الملفات والأنابيب ومقابض التسجيل ومقابض الانتظار أو مؤشرات على كتل من الذاكرة غير المُدارة. يعود ذلك إلى أن جمع القمامة كفء جدا في استعادة الكائنات المُدارة غير المستخدمة، لكنه غير قادر على استرداد الكائنات غير المدارة.

**Java**

{{< highlight csharp >}}

 //Create workbook object

Workbook book = new Workbook();

//Call dispose method

book.dispose();

{{< /highlight >}}
### **تمت إضافة طريقة Cell.getHeightOfValue**
Aspose.Cells for Java 8.5.1 قام بتعريض طريقة Cell.getHeightOfValue للحصول على ارتفاع قيمة الخلية. باستخدام هذه الطريقة، يمكنك حساب ارتفاع قيمة الخلية، ثم تعيين ارتفاع صف تلك الخلية على التوالي. تحقق من المقالة المفصلة حول [كيفية حساب ارتفاع وعرض الخلية](/cells/ar/java/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/).
### **تمت إضافة تصنيف TableDataSourceType**
Aspose.Cells for Java 8.5.1 قام بتعريض التصنيف com.aspose.cells.TableDataSourceType لاسترداد نوع مصدر البيانات لكائن ListObject. يحتوي تصنيف TableDataSourceType على الحقول التالية. 

1. TableDataSourceType.QUERY_TABLE
1. TableDataSourceType.SHARE_POINT
1. TableDataSourceType.WORKSHEET
1. TableDataSourceType.XML
### **تمت إضافة خاصية ListObject.DataSourceType**
مع إصدار v8.5.1، قامت واجهة برمجة التطبيقات Aspose.Cells بتعريض الخاصية القراءة فقط ListObject.DataSourceType التي يمكن استخدامها لاكتشاف نوع مصدر البيانات لكائن ListObject.

فيما يلي سيناريو الاستخدام الأبسط.

**Java**

{{< highlight csharp >}}

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
