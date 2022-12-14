---
title: تجميع وإلغاء تجميع الصفوف والأعمدة
type: docs
weight: 30
url: /ar/cpp/grouping-ungrouping-rows-and-columns/
---
## **مقدمة**
في ملف Excel Microsoft ، يمكنك إنشاء مخطط تفصيلي للبيانات للسماح لك بإظهار مستويات التفاصيل وإخفائها بنقرة واحدة بالماوس.

 انقر على**رموز المخطط التفصيلي**، 1 ، 2 ، 3 ، + و - لعرض الصفوف أو الأعمدة التي توفر ملخصات أو عناوين للأقسام في ورقة العمل فقط بسرعة ، أو يمكنك استخدام الرموز لمشاهدة التفاصيل ضمن عنوان أو ملخص فردي.
## **إدارة المجموعة للصفوف والأعمدة**
 Aspose.Cells يوفر فصل دراسي ،[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) الذي يمثل ملف إكسل Microsoft. ال[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) فئة تحتوي على[أوراق العمل](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection) مجموعة تسمح بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة[IWorksheet](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) صف دراسي. ال[IWorksheet](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) فئة توفر[آيسيلس](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)مجموعة تمثل جميع الخلايا في ورقة العمل.

 ال[آيسيلس](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)توفر المجموعة عدة طرق لإدارة الصفوف أو الأعمدة في ورقة العمل ، وقد تمت مناقشة القليل منها أدناه بمزيد من التفصيل.
### **تجميع الصفوف والأعمدة**
 من الممكن تجميع الصفوف أو الأعمدة عن طريق استدعاء[GroupRows](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a88e0180ed1a4a423e0bd3ac599ef9332) و[GroupColumns](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#aaa14179e2a84ba5c2857f8434570d3d8) طرق[آيسيلس](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)مجموعة. تأخذ كلتا الطريقتين المعلمات التالية:

- أول صف / فهرس العمود ، أول صف أو عمود في المجموعة.
- آخر صف / فهرس العمود ، آخر صف أو عمود في المجموعة.
- مخفي ، معلمة منطقية تحدد ما إذا كان سيتم إخفاء الصفوف / الأعمدة بعد التجميع أم لا.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-GroupingUngroupingRowsAndColumns-GroupingRowsColumns.cpp" >}}
#### **إعدادات المجموعة**
Microsoft يسمح لك Excel بتكوين إعدادات المجموعة لعرض:

- صفوف التلخيص أدناه التفاصيل.
- أعمدة التلخيص على يمين التفاصيل.
## **فك تجميع الصفوف والأعمدة**
 لفك تجميع أي صفوف أو أعمدة مجمعة ، قم باستدعاء[آيسيلس](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) المجموعة[UngroupRows](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#adc1f6418506854ab41707bfef453ddb1) و[UngroupColumns](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#aa3bf9a9510d4e85f68db9ebdcadc8406)طُرق. تأخذ كلتا الطريقتين معلمتين:

- الصف الأول أو فهرس العمود ، الصف / العمود الأول المراد فك تجميعه.
- آخر صف أو فهرس العمود ، آخر صف / عمود سيتم فك تجميعه.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-GroupingUngroupingRowsAndColumns-UnGroupingRowsColumns.cpp" >}}
