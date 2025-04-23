---
title: تغييرات واجهة برمجة التطبيقات العامة في Aspose.Cells 8.5.1
type: docs
weight: 170
url: /ar/net/public-api-changes-in-aspose-cells-8-5-1/
---

{{% alert color="primary" %}} 

يصف هذا المستند التغييرات في واجهة برمجة التطبيقات Aspose.Cells من الإصدار 8.5.0 إلى 8.5.1 التي قد تكون مثيرة لاهتمام مطوري الوحدات / التطبيقات. يشمل ليس فقط الطرق العامة الجديدة والمحدثة، وإضافة الفئات، وما إلى ذلك، ولكن أيضاً وصفاً لأي تغييرات في السلوك وراء الكواليس في Aspose.Cells.

{{% /alert %}} 
## **واجهات برمجة التطبيقات الجديدة**
### **تمت إضافة طريقة Workbook.Dispose**
أصبح ينفذ كائن Workbook الآن واجهة System.IDisposable التي تحتوي على طريقة Dispose واحدة. يمكنك إما استدعاء طريقة Workbook.Dispose مباشرة أو إنشاء كائن Workbook في هيكل Using لاستدعاء هذه الطريقة تلقائياً.

**C#**

{{< highlight csharp >}}

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


### **أضيفت طريقة GetHeightOfValue في الخلية**
قام Aspose.Cells for .NET 8.5.1 بتعريض الطريقة Cell.GetHeightOfValue للحصول على ارتفاع قيمة الخلية. من خلال استخدام هذه الطريقة يمكنك حساب ارتفاع قيمة الخلية ثم ضبط ارتفاع صف تلك الخلية على التوالي. تحقق من المقال المفصل على [كيفية حساب ارتفاع وعرض الخلية](/cells/ar/net/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/).
### **تمت إضافة تصنيف TableDataSourceType**
قام Aspose.Cells for .NET 8.5.1 بتعريض تعداد Aspose.Cells.Tables.TableDataSourceType لاسترداد نوع مصدر البيانات لـ ListObject. تعداد TableDataSourceType كما يلي.

1. TableDataSourceType.QueryTable
1. TableDataSourceType.SharePoint
1. TableDataSourceType.Worksheet
1. TableDataSourceType.XML
### **تمت إضافة خاصية ListObject.DataSourceType**
مع إصدار v8.5.1، قامت واجهة برمجة التطبيقات Aspose.Cells بتعريض الخاصية القراءة فقط ListObject.DataSourceType التي يمكن استخدامها لاكتشاف نوع مصدر البيانات لكائن ListObject.

فيما يلي سيناريو الاستخدام الأبسط.

**C#**

{{< highlight csharp >}}

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
{{< app/cells/assistant language="csharp" >}}
