---
title: إدراج وحذف الصفوف والأعمدة
type: docs
weight: 40
url: /ar/cpp/inserting-deleting-rows-and-columns/
---
##  **مقدمة**
سواء قمت بإنشاء ورقة عمل جديدة من البداية أو العمل على ورقة عمل موجودة، فقد نحتاج إلى إضافة صفوف أو أعمدة إضافية لاستيعاب المزيد من البيانات. وعلى العكس من ذلك، قد نحتاج أيضًا إلى حذف صفوف أو أعمدة من مواضع محددة في ورقة العمل. لتحقيق هذه المتطلبات، يوفر Aspose.Cells مجموعة أبسط جدًا من الفئات والأساليب، الموضحة أدناه.
###  **إدارة الصفوف والأعمدة**
 Aspose.Cells يوفر فئة،[دفتر العمل](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) ، يمثل ملف Excel Microsoft. ال[دفتر العمل](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) يحتوي الفصل على[أوراق عمل](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)مجموعة تسمح بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة[ورقة عمل](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) فصل. ال[ورقة عمل](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) يوفر الفصل[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)المجموعة التي تمثل كافة الخلايا في ورقة العمل.

 ال[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)توفر المجموعة عدة طرق لإدارة الصفوف والأعمدة في ورقة العمل. وتناقش بعض هذه أدناه.

{{% alert color="primary" %}} 

عند إضافة صفوف أو أعمدة، يتم نقل المحتوى الموجود في ورقة العمل إلى الأسفل أو إلى اليمين، وإذا تمت إزالة الصفوف أو الأعمدة، يتم نقل المحتوى إلى الأعلى أو إلى اليسار.

{{% /alert %}} 
####  **إدراج صف**
 قم بإدراج صف في ورقة العمل في أي مكان عن طريق استدعاء[الصف إدراج](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrow/) طريقة[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) مجموعة. ال[الصف إدراج](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrow/)تأخذ الطريقة فهرس الصف الذي سيتم إدراج الصف الجديد فيه.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-InsertRow-new.cpp" >}}


####  **إدراج صفوف متعددة**
 لإدراج صفوف متعددة في ورقة عمل، قم باستدعاء[إدراج صفوف](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrows/) طريقة[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) مجموعة. ال[إدراج صفوف](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrows/)تأخذ الطريقة معلمتين:

- فهرس الصف، فهرس الصف الذي سيتم إدراج الصفوف الجديدة منه.
- عدد الصفوف، إجمالي عدد الصفوف التي يجب إدراجها.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-InsertingMultipleRows-new.cpp" >}}


####  **حذف صفوف متعددة**
 لحذف صفوف متعددة من ورقة العمل، اتصل بـ[حذف الصفوف](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterows/) طريقة[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) مجموعة. ال[حذف الصفوف](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterows/)تأخذ الطريقة معلمتين:

- فهرس الصف، فهرس الصف الذي سيتم حذف الصفوف منه.
- عدد الصفوف، إجمالي عدد الصفوف التي يجب حذفها.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-DeletingMultipleRows-new.cpp" >}}


####  **أدخل عمودًا**
 يمكن للمطورين أيضًا إدراج عمود في ورقة العمل في أي مكان عن طريق استدعاء[InsertColumn](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertcolumn/) طريقة[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) مجموعة.[InsertColumn](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertcolumn/)تأخذ الطريقة فهرس العمود الذي سيتم إدراج العمود الجديد فيه.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-InsertColumn-new.cpp" >}}


####  **حذف عمود**
 لحذف عمود من ورقة العمل في أي مكان، اتصل بـ[حذف العمود](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deletecolumn/) طريقة[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) مجموعة. ال[حذف العمود](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deletecolumn/)تأخذ الطريقة فهرس العمود المراد حذفه.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-DeleteColumn-new.cpp" >}}
