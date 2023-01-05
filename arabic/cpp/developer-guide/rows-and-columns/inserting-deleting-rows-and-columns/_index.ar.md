---
title: إدراج وحذف الصفوف والأعمدة
type: docs
weight: 40
url: /ar/cpp/inserting-deleting-rows-and-columns/
---
## **مقدمة**
سواء أكنت تنشئ ورقة عمل جديدة من البداية أو تعمل على ورقة عمل موجودة ، فقد نحتاج إلى إضافة صفوف أو أعمدة إضافية لاستيعاب المزيد من البيانات. بشكل عكسي ، قد نحتاج أيضًا إلى حذف الصفوف أو الأعمدة من المواضع المحددة في ورقة العمل. للوفاء بهذه المتطلبات ، يوفر Aspose.Cells أبسط مجموعة من الفئات والطرق الموضحة أدناه.
### **إدارة الصفوف والأعمدة**
 Aspose.Cells يوفر فصل دراسي ،[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) ، يمثل ملف Excel Microsoft. ال[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) فئة تحتوي على[أوراق العمل](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection) مجموعة تسمح بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة[IWorksheet](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) صف دراسي. ال[IWorksheet](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) فئة توفر[آيسيلس](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)مجموعة تمثل جميع الخلايا في ورقة العمل.

 ال[آيسيلس](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)توفر المجموعة عدة طرق لإدارة الصفوف والأعمدة في ورقة العمل. تمت مناقشة بعض هذه أدناه.

{{% alert color="primary" %}} 

عند إضافة صفوف أو أعمدة ، يتم إزاحة المحتوى في ورقة العمل لأسفل أو إلى اليمين ، وإذا تمت إزالة الصفوف أو الأعمدة ، يتم إزاحة المحتوى لأعلى أو لليسار.

{{% /alert %}} 
#### **أدخل صفًا**
 أدخل صفًا في ورقة العمل في أي مكان عن طريق استدعاء ملف[الصف إدراج](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ad9c067ccb5f34a7740f5d1cc3dbefbe7) طريقة[آيسيلس](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) مجموعة. ال[الصف إدراج](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ad9c067ccb5f34a7740f5d1cc3dbefbe7)تأخذ الطريقة فهرس الصف حيث سيتم إدراج الصف الجديد.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-InsertRow.cpp" >}}


#### **إدراج صفوف متعددة**
 لإدراج عدة صفوف في ورقة عمل ، قم باستدعاء[إدراج صفوف](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a61e4cd6dcaeeb0d11afd54616df75ee0) طريقة[آيسيلس](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) مجموعة. ال[إدراج صفوف](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a61e4cd6dcaeeb0d11afd54616df75ee0)تأخذ الطريقة معلمتين:

- فهرس الصف ، فهرس الصف حيث سيتم إدراج الصفوف الجديدة.
- عدد الصفوف ، العدد الإجمالي للصفوف التي يجب إدراجها.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-InsertingMultipleRows.cpp" >}}


#### **حذف عدة صفوف**
لحذف عدة صفوف من ورقة العمل ، قم باستدعاء[DeleteRows](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a251261027b564ebdf27c2c6d5149c0e1) طريقة[آيسيلس](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) مجموعة. ال[DeleteRows](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a251261027b564ebdf27c2c6d5149c0e1)تأخذ الطريقة معلمتين:

- فهرس الصف ، فهرس الصف الذي سيتم حذف الصفوف منه.
- عدد الصفوف ، العدد الإجمالي للصفوف التي يجب حذفها.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-DeletingMultipleRows.cpp" >}}


#### **أدخل عمود**
 يمكن للمطورين أيضًا إدراج عمود في ورقة العمل في أي مكان عن طريق استدعاء[إدراج العمود](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a8e8cb6d0812129669258378649b3fd55) طريقة[آيسيلس](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) مجموعة.[إدراج العمود](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a8e8cb6d0812129669258378649b3fd55)تأخذ الطريقة فهرس العمود حيث سيتم إدراج العمود الجديد.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-InsertColumn.cpp" >}}


#### **احذف عمود**
 لحذف عمود من ورقة العمل في أي مكان ، قم باستدعاء[DeleteColumn](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ae00721fd2be220e7b73b2cab6a70e89b) طريقة[آيسيلس](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) مجموعة. ال[DeleteColumn](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ae00721fd2be220e7b73b2cab6a70e89b)الأسلوب يأخذ فهرس العمود لحذفه.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-DeleteColumn.cpp" >}}
