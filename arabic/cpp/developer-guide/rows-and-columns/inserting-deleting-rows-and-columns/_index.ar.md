---
title: إدراج وحذف الصفوف والأعمدة
type: docs
weight: 40
url: /ar/cpp/inserting-deleting-rows-and-columns/
---

## **مقدمة**
سواء كنت تقوم بإنشاء ورقة عمل جديدة من الصفر أو العمل على ورقة عمل موجودة ، قد نحتاج أحيانًا إلى إضافة صفوف أو أعمدة إضافية لاستيعاب المزيد من البيانات. وبالمقابل ، قد نحتاج أيضًا إلى حذف الصفوف أو الأعمدة من المواقع المحددة في ورقة العمل. لتلبية هذه المتطلبات ، يوفر Aspose.Cells مجموعة بسيطة جدًا من الفئات والأساليب ، كما هو موضح أدناه.
### **إدارة الصفوف والأعمدة**
توفر Aspose.Cells فئة ، [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), التي تمثل ملف Microsoft Excel. تحتوي فئة [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) على مجموعة [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) تسمح بالوصول إلى كل ورقة عمل في ملف Excel. تمثل ورقة العمل بواسطة فئة [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) . توفر فئة [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) مجموعة [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) التي تمثل جميع الخلايا في ورقة العمل.

توفر مجموعة [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) العديد من الأساليب لإدارة الصفوف والأعمدة في ورقة العمل. يتم مناقشة بعض هذه الأساليب أدناه.

{{% alert color="primary" %}} 

عند إضافة صفوف أو أعمدة، يتم نقل المحتوى في ورقة العمل لأسفل أو لليمين، وإذا تمت إزالة الصفوف أو الأعمدة، يتم نقل المحتوى لأعلى أو لليسار.

{{% /alert %}} 
#### **إدراج صف**
قم بإدراج صف في ورقة العمل في أي موقع عن طريق استدعاء طريقة [InsertRow](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrow/) من مجموعة [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) . تأخذ طريقة [InsertRow](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrow/) مؤشر الصف حيث سيتم إدراج الصف الجديد.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-InsertRow-new.cpp" >}}


#### **إدراج صفوف متعددة**
لإدراج عدة صفوف في ورقة العمل ، قم باستدعاء طريقة [InsertRows](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrows/) من مجموعة [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) . تأخذ طريقة [InsertRows](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrows/) معها معها اثنين من المعلمات:

- فهرس الصف، الفهرس للصف من حيث إن الصفوف الجديدة ستدرج.
- عدد الصفوف، إجمالي عدد الصفوف التي يجب إدراجها.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-InsertingMultipleRows-new.cpp" >}}


#### **حذف صفوف متعددة**
لحذف عدة صفوف من ورقة العمل ، قم باستدعاء طريقة [DeleteRows](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterows/) من مجموعة [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) . تأخذ طريقة [DeleteRows](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterows/) معها اثنين من المعلمات:

- فهرس الصف، الفهرس للصف من حيث سيتم حذف الصفوف.
- عدد الصفوف، الإجمالي لعدد الصفوف التي يجب حذفها.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-DeletingMultipleRows-new.cpp" >}}


#### **إدراج عمود**
يمكن للمطورين أيضًا إدراج عمود في ورقة العمل في أي موقع عن طريق استدعاء طريقة [InsertColumn](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertcolumn/) من مجموعة [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) . تأخذ طريقة [InsertColumn](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertcolumn/) مؤشر العمود حيث سيتم إدراج العمود الجديد.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-InsertColumn-new.cpp" >}}


#### **حذف عمود**
لحذف عمود من ورقة العمل في أي موقع ، قم باستدعاء طريقة [DeleteColumn](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deletecolumn/) من مجموعة [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) . تأخذ طريقة [DeleteColumn](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deletecolumn/) مؤشر العمود الذي سيتم حذفه.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-DeleteColumn-new.cpp" >}}
