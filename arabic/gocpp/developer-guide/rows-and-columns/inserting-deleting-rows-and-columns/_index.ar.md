---
title: إدراج وحذف الصفوف والأعمدة
type: docs
weight: 40
url: /ar/go-cpp/inserting-deleting-rows-and-columns/
---

## **مقدمة**

سواء كنت تقوم بإنشاء ورقة عمل جديدة من الصفر أو العمل على ورقة عمل موجودة ، قد نحتاج أحيانًا إلى إضافة صفوف أو أعمدة إضافية لاستيعاب المزيد من البيانات. وبالمقابل ، قد نحتاج أيضًا إلى حذف الصفوف أو الأعمدة من المواقع المحددة في ورقة العمل. لتلبية هذه المتطلبات ، يوفر Aspose.Cells مجموعة بسيطة جدًا من الفئات والأساليب ، كما هو موضح أدناه.

### **إدارة الصفوف والأعمدة**

يوفر Aspose.Cells فئة [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) التي تمثل ملف Excel. تحتوي فئة [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) على مجموعة [Worksheets](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) التي تمكنك من الوصول إلى كل ورقة عمل في ملف Excel. تمثل ورقة العمل بواسطة فئة [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/). توفر فئة [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) مجموعة [Cells](https://reference.aspose.com/cells/go-cpp/cells/) التي تمثل جميع الخلايا في ورقة العمل.

توفر مجموعة [Cells](https://reference.aspose.com/cells/go-cpp/cells/) عدة طرق لإدارة الصفوف والأعمدة في ورقة العمل، وسيتم مناقشة بعض منها بمزيد من التفصيل أدناه.

{{% alert color="primary" %}}

عند إضافة صفوف أو أعمدة، يتم نقل المحتوى في ورقة العمل لأسفل أو لليمين، وإذا تمت إزالة الصفوف أو الأعمدة، يتم نقل المحتوى لأعلى أو لليسار.

{{% /alert %}}

قم بإدراج صف في ورقة العمل في أي موقع عن طريق استدعاء طريقة [InsertRow](https://reference.aspose.com/cells/go-cpp/cells/insertrow/) لمجموعة [Cells](https://reference.aspose.com/cells/go-cpp/cells/). تأخذ طريقة [InsertRow](https://reference.aspose.com/cells/go-cpp/cells/insertrow/) مؤشر الصف حيث سيتم إدراج الصف الجديد.
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-InsertRow.go" >}}

#### **إدراج صفوف متعددة**

لإدراج صفوف متعددة في ورقة العمل، استدعي طريقة [InsertRows](https://reference.aspose.com/cells/go-cpp/cells/insertrows_int_int/) لمجموعة [Cells](https://reference.aspose.com/cells/go-cpp/cells/). تأخذ طريقة [InsertRows](https://reference.aspose.com/cells/go-cpp/cells/insertrowinsertrows_int_ints/) معامليْن:

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-InsertingMultipleRows.go" >}}

#### **حذف صفوف متعددة**

لحذف عدة صفوف من ورقة عمل، استدعِ طريقة [DeleteRows](https://reference.aspose.com/cells/go-cpp/cells/deleterows_int_int_bool/) من مجموعة [Cells](https://reference.aspose.com/cells/go-cpp/cells/). تتطلب طريقة [DeleteRows](https://reference.aspose.com/cells/go-cpp/cells/deleterows_int_int_bool/) معلمات اثنين:

- فهرس الصف، الفهرس للصف من حيث سيتم حذف الصفوف.
- عدد الصفوف، الإجمالي لعدد الصفوف التي يجب حذفها.

#### **إدراج عمود**

يمكن للمطورين أيضًا إدراج عمود في ورقة العمل في أي مكان عن طريق استدعاء طريقة [InsertColumn](https://reference.aspose.com/cells/go-cpp/cells/insertcolumn_int/) من مجموعة [Cells](https://reference.aspose.com/cells/go-cpp/cells/). تأخذ طريقة [InsertColumn](https://reference.aspose.com/cells/go-cpp/cells/insertcolumn_int/) فهرس العمود حيث سيتم إدراج العمود الجديد.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-InsertColumn.go" >}}

لحذف عمود من ورقة العمل في أي مكان، استدعِ طريقة [DeleteColumn](https://reference.aspose.com/cells/go-cpp/cells/deletecolumn_int/) من مجموعة [Cells](https://reference.aspose.com/cells/go-cpp/cells/). تتطلب طريقة [DeleteColumn](https://reference.aspose.com/cells/go-cpp/cells/deletecolumn_int/) فهرس العمود المراد حذفه.
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DeleteColumn.go" >}}
