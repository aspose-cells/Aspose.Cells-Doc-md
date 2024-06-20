---
title: ضبط ارتفاع الصف وعرض العمود
type: docs
weight: 10
url: /ar/cpp/adjusting-row-height-and-column-width/
---

{{% alert color="primary" %}} 

عند العمل مع أوراق العمل وإضافة البيانات إلى الصفوف أو الأعمدة، قد تحتاج أحيانًا إلى تغيير ارتفاع الصفوف أو عرض الأعمدة. أحيانًا، تعني تطبيق التنسيق على الصفوف أو الأعمدة أن ارتفاع الصف الحالي أو عرض العمود بحاجة إلى تغيير لعرض البيانات. عادةً ما يقوم المستخدمون بضبط ارتفاع الصفوف وعرض الأعمدة في بيئة WYSIWYG باستخدام مايكروسوفت إكسل. ولكن مع Aspose.Cells، يمكن للمطورين تنفيذ هذه العمليات في وقت التشغيل.

{{% /alert %}} 
## **العمل مع الصفوف**
### **ضبط ارتفاع الصف**
توفر Aspose.Cells فئة تمثل [دفتر العمل](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) الذي يمثل ملف Microsoft Excel. تحتوي فئة [دفتر العمل](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) على [مجموعة أوراق العمل](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) التي تسمح بالوصول إلى كل ورقة عمل في ملف Excel. تمثل ورقة العمل بواسطة فئة [ورقة العمل](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) وتوفر فئة [ورقة العمل](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) مجموعة [الخلايا](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) التي تمثل جميع الخلايا في ورقة العمل. تقدم مجموعة [الخلايا](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) عدة أساليب لإدارة الصفوف أو الأعمدة في ورقة العمل. يتم مناقشة بعض هذه الأساليب أدناه بتفصيل أكثر.
#### **تعيين ارتفاع الصف**
من الممكن تعيين ارتفاع صف واحد عن طريق استدعاء [مجموعة الخلايا](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) و[تعيين ارتفاع الصف](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setrowheight/) والتي تأخذ المعلمات التالية كما يلي:

- **مؤشر الصف**, مؤشر الصف الذي كنت تغير ارتفاعه.
- **ارتفاع الصف**, ارتفاع الصف المطبق على الصف.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingHeightOfRow-new.cpp" >}}


#### **تعيين ارتفاع جميع الصفوف في ورقة العمل**
إذا كان لدى المطورين حاجة لتعيين نفس ارتفاع الصف لجميع الصفوف في ورقة العمل، فيمكنهم فعل ذلك باستخدام [مجموعة الخلايا](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) و[تعيين ارتفاع قياسي](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setstandardheight/) للصفوف.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingHeightOfAllRowsInWorksheet-new.cpp" >}}
## **العمل مع الأعمدة**
### **ضبط عرض العمود**
قم بتعيين عرض العمود عن طريق استدعاء [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)  ‎ ‎ ‎ ‎‎مجموعة [SetColumnWidth](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setcolumnwidth/)  ‎‎‎استخدم الأسلوب. [SetColumnWidth](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setcolumnwidth/) يأخذ البيانات التالية:

- **فهرس العمود**, فهرس العمود الذي تريد تغيير عرضه.
- **عرض العمود**, العرض المطلوب للعمود.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingWidthOfColumn-new.cpp" >}}
### **تعيين عرض جميع الأعمدة في ورقة العمل**
لتعيين نفس عرض العمود لجميع الأعمدة في ورقة العمل، استخدم الأسلوب [SetStandardWidth](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setstandardwidth/)  ‎ من مجموعة [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)‎.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingWidthOfAllColumnsInWorksheet-new.cpp" >}}
