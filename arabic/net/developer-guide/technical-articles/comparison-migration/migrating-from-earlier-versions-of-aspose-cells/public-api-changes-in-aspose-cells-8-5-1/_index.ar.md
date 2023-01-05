---
title: عام API التغييرات في Aspose.Cells 8.5.1
type: docs
weight: 170
url: /ar/net/public-api-changes-in-aspose-cells-8-5-1/
---
{{% alert color="primary" %}} 

 توضح هذه الوثيقة التغييرات التي تم إجراؤها على Aspose.Cells API من الإصدار 8.5.0 إلى 8.5.1 والتي قد تهم مطوري الوحدة النمطية / التطبيق. لا يشمل فقط الأساليب العامة الجديدة والمحدثة ،[الفئات المضافة وما إلى ذلك.](/cells/ar/net/public-api-changes-in-aspose-cells-8-5-1/)ولكن أيضًا وصف لأية تغييرات في السلوك خلف الكواليس عام Aspose.Cells.

{{% /alert %}} 
## **تمت إضافة واجهات برمجة التطبيقات**
### **مصنف الطريقة**
يطبق كائن المصنف الآن واجهة System.IDisposable التي تحتوي على طريقة واحدة للتخلص. يمكنك إما استدعاء طريقة Workbook.Dispose أو إنشاء كائن مصنف في بنية باستخدام لاستدعاء هذه الطريقة تلقائيًا.

**C#**

{{< highlight "csharp" >}}

 //Create workbook object

Workbook book = new Workbook();

//Call Dispose method

book.Dispose();

//Call Dispose method via Using statement

using (Workbook book = new Workbook())

{

    //do processing

}

{{< /highlight >}}


### **الطريقة Cell.GetHeightOfValue مضافة**
 كشف Aspose.Cells for .NET 8.5.1 الطريقة Cell.GetHeightOfValue للحصول على ارتفاع قيمة الخلية. باستخدام هذه الطريقة ، يمكنك حساب ارتفاع قيمة الخلية ثم تعيين ارتفاع صف تلك الخلية على التوالي. تحقق من المقال المفصل على[كيفية حساب ارتفاع الخلية وعرضها](/cells/ar/net/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/).
### **تمت إضافة جدول التعداد**
كشف Aspose.Cells for .NET 8.5.1 التعداد Aspose.Cells.Tables.TableDataSourceType لاسترداد نوع مصدر البيانات من ListObject. تعداد TableDataSourceType كحقول التالية.

1. TableDataSourceType.QueryTable
1. TableDataSourceType
1. TableDataSourceType. ورقة عمل
1. TableDataSourceType.XML
### **تمت إضافة خاصية ListObject.DataSourceType**
مع إصدار v8.5.1 ، كشف Aspose.Cells API عن خاصية ListObject.DataSourceType للقراءة فقط والتي يمكن استخدامها للكشف عن نوع مصدر البيانات الخاص بـ ListObject.

هنا هو أبسط سيناريو استخدام.

**C#**

{{< highlight "csharp" >}}

 Workbook book = new Workbook("D:/book1.xlsx");

Worksheet sheet = book.Worksheets[0];

ListObject listObject = sheet.ListObjects[0];

if (listObject.DataSourceType == Aspose.Cells.Tables.TableDataSourceType.QueryTable)

{

    Console.WriteLine("Data Source Type is Query Table");

}

else if (listObject.DataSourceType == Aspose.Cells.Tables.TableDataSourceType.SharePoint)

{

    Console.WriteLine("Data Source Type is SharePoint Linked List");

}

else if (listObject.DataSourceType == Aspose.Cells.Tables.TableDataSourceType.Worksheet)

{

    Console.WriteLine("Data Source Type is Excel Worksheet Table");

}

else if (listObject.DataSourceType == Aspose.Cells.Tables.TableDataSourceType.XML)

{

    Console.WriteLine("Data Source Type is XML");

}

{{< /highlight >}}
