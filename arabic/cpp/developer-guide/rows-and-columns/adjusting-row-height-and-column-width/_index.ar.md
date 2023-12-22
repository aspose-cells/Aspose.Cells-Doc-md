---
title: ضبط ارتفاع الصف وعرض العمود
type: docs
weight: 10
url: /ar/cpp/adjusting-row-height-and-column-width/
---
{{% alert color="primary" %}} 

عند العمل باستخدام جداول البيانات وإضافة البيانات إلى الصفوف أو الأعمدة، قد تحتاج إلى تغيير ارتفاع الصفوف أو عرض الأعمدة. في بعض الأحيان، يعني تطبيق التنسيق على الصفوف أو الأعمدة أن الارتفاع أو العرض الحالي يحتاج إلى التغيير لعرض البيانات. عادةً، يقوم المستخدمون بضبط ارتفاعات الصفوف وعرض الأعمدة في بيئة WYSIWYG باستخدام Microsoft Excel. ولكن مع Aspose.Cells يمكن للمطورين تنفيذ هذه العمليات في وقت التشغيل.

{{% /alert %}} 
##  **العمل مع الصفوف**
###  **ضبط ارتفاع الصف**
 Aspose.Cells يوفر فئة،[دفتر العمل](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) الذي يمثل ملف Excel Microsoft. ال[دفتر العمل](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) يحتوي الفصل على أ[مجموعة أوراق العمل](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)الذي يسمح بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة[ورقة عمل](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) فصل. ال[ورقة عمل](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) يوفر الفصل أ[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) المجموعة التي تمثل كافة الخلايا في ورقة العمل. ال[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)توفر المجموعة عدة طرق لإدارة الصفوف أو الأعمدة في ورقة العمل. وتناقش بعض هذه أدناه بمزيد من التفصيل.
####  **تحديد ارتفاع الصف**
 من الممكن ضبط ارتفاع صف واحد عن طريق استدعاء[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) المجموعة[SetRowHeight](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setrowheight/) طريقة. ال[SetRowHeight](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setrowheight/)تأخذ الطريقة المعلمات التالية كما يلي:

- *فهرس الصف**، فهرس الصف الذي تقوم بتغيير ارتفاعه.
- *ارتفاع الصف**، ارتفاع الصف الذي سيتم تطبيقه على الصف.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingHeightOfRow-new.cpp" >}}


####  **ضبط ارتفاع كافة الصفوف في ورقة العمل**
 إذا كان المطورون بحاجة إلى تعيين نفس ارتفاع الصف لجميع الصفوف في ورقة العمل، فيمكنهم القيام بذلك باستخدام[SetStandardHeight](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setstandardheight/) طريقة[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)مجموعة.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingHeightOfAllRowsInWorksheet-new.cpp" >}}
##  **العمل مع الأعمدة**
###  **تحديد عرض العمود**
 قم بتعيين عرض العمود عن طريق استدعاء[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) المجموعة[عرض_SetColumnWidth](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setcolumnwidth/) طريقة. ال[عرض_SetColumnWidth](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setcolumnwidth/)تأخذ الطريقة المعلمات التالية:

- *فهرس العمود**، فهرس العمود الذي تقوم بتغيير عرضه.
- *عرض العمود**، عرض العمود المطلوب.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingWidthOfColumn-new.cpp" >}}
###  **ضبط عرض كافة الأعمدة في ورقة العمل**
 لتعيين نفس عرض العمود لجميع الأعمدة في ورقة العمل، استخدم الأمر[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) المجموعة[SetStandardWidth](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setstandardwidth/)طريقة.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingWidthOfAllColumnsInWorksheet-new.cpp" >}}
