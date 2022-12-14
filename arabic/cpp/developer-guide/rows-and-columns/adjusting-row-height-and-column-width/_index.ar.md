---
title: ضبط ارتفاع الصف وعرض العمود
type: docs
weight: 10
url: /ar/cpp/adjusting-row-height-and-column-width/
---
{{% alert color="primary" %}} 

عند العمل باستخدام جداول البيانات وإضافة البيانات إلى الصفوف أو الأعمدة ، قد تحتاج إلى تغيير ارتفاع الصفوف أو عرض الأعمدة. في بعض الأحيان ، يعني تطبيق التنسيق على الصفوف أو الأعمدة أن الارتفاع الحالي أو العرض يحتاج إلى التغيير لإظهار البيانات. عادة ، يقوم المستخدمون بضبط ارتفاعات الصفوف وعرض الأعمدة في بيئة WYSIWYG باستخدام Microsoft Excel. ولكن مع Aspose.Cells يمكن للمطورين تنفيذ هذه العمليات في وقت التشغيل.

{{% /alert %}} 
## **العمل مع الصفوف**
### **ضبط ارتفاع الصف**
 Aspose.Cells يوفر فصل دراسي ،[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) الذي يمثل ملف إكسل Microsoft. ال[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) فئة تحتوي على[IWorksheetCollection](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)يسمح بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة[IWorksheet](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) صف دراسي. ال[IWorksheet](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) فئة توفر أ[آيسيلس](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) مجموعة تمثل جميع الخلايا في ورقة العمل. ال[آيسيلس](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)توفر المجموعة عدة طرق لإدارة الصفوف أو الأعمدة في ورقة العمل. تمت مناقشة بعض هذه أدناه بمزيد من التفصيل.
#### **ضبط ارتفاع الصف**
 من الممكن ضبط ارتفاع صف واحد عن طريق استدعاء[آيسيلس](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) المجموعة[SetRowHeight](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a7aa441877e03639232299627261a7d1f) طريقة. ال[SetRowHeight](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a7aa441877e03639232299627261a7d1f)تأخذ الطريقة المعلمات التالية على النحو التالي:

- **فهرس الصف**، فهرس الصف الذي تقوم بتغيير ارتفاعه.
- **ارتفاع الصف**، ارتفاع الصف المراد تطبيقه على الصف.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingHeightOfRow.cpp" >}}


#### **ضبط ارتفاع كل الصفوف في ورقة عمل**
 إذا احتاج المطورون إلى تعيين ارتفاع الصف نفسه لجميع الصفوف في ورقة العمل ، فيمكنهم القيام بذلك باستخدام ملحق[SetStandardHeight](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a0b79a3163e2b601aa1b6a6a1e3f1467f) طريقة[آيسيلس](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)مجموعة.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingHeightOfAllRowsInWorksheet.cpp" >}}
## **العمل مع الأعمدة**
### **ضبط عرض العمود**
 اضبط عرض العمود عن طريق استدعاء[آيسيلس](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) المجموعة[SetColumnWidth](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ab1c6a4e89760d2a022d5bfba8bc40987) طريقة. ال[SetColumnWidth](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ab1c6a4e89760d2a022d5bfba8bc40987)تأخذ الطريقة المعلمات التالية:

- **فهرس العمود**، هو فهرس العمود الذي تقوم بتغيير عرضه.
- **عرض العمود**، عرض العمود المطلوب.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingWidthOfColumn.cpp" >}}
### **ضبط عرض كل الأعمدة في ورقة عمل**
 لتعيين نفس عرض العمود لجميع الأعمدة في ورقة العمل ، استخدم ملف[آيسيلس](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) المجموعة[SetStandardWidth](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a48f5dbccc3bf4bb9e6e882094b500bd7)طريقة.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingWidthOfAllColumnsInWorksheet.cpp" >}}
