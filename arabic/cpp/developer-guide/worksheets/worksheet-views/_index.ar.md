---
title: طرق عرض ورقة العمل
type: docs
weight: 40
url: /ar/cpp/worksheet-views/
---
## **معاينة فاصل الصفحة**
يمكن عرض جميع أوراق العمل في وضعين:

- العرض العادي.
- معاينة فاصل الصفحة.

طريقة العرض "عادي" هي طريقة العرض الافتراضية لورقة العمل. معاينة فاصل الصفحة هي طريقة عرض تحرير تعرض ورقة عمل كما ستتم طباعتها. تُظهر معاينة فاصل الصفحة البيانات التي سيتم نقلها على كل صفحة حتى تتمكن من ضبط منطقة الطباعة وفواصل الصفحات. باستخدام Aspose.Cells يمكن للمطورين تمكين العرض العادي أو أوضاع معاينة فاصل الصفحة.
### **التحكم في أوضاع العرض**
 Aspose.Cells يوفر فئة[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) الذي يمثل ملف إكسل Microsoft. ال[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) فئة تحتوي على[أوراق عمل](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)مجموعة تسمح بالوصول إلى كل ورقة عمل في ملف Excel.

 يتم تمثيل ورقة العمل بواسطة[IWorksheet](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)صف دراسي. ال[IWorksheet](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) يوفر class مجموعة واسعة من الأساليب لإدارة أوراق العمل. لتمكين أوضاع المعاينة العادية أو أوضاع معاينة فاصل الصفحة ، استخدم ملف[IsPageBreakPreview](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#aa1af81cfb7635232c7f839192b442892) طريقة[IWorksheet](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) صف دراسي.[IsPageBreakPreview](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#aa1af81cfb7635232c7f839192b442892) تُرجع قيمة منطقية ، مما يعني أنه يمكنها فقط تخزين ملف**حقيقي** أو**خاطئة** القيمة.
#### **تمكين العرض العادي**
قم بتعيين ورقة عمل إلى العرض العادي عن طريق تعيين ملف[IsPageBreakPreview](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#aa1af81cfb7635232c7f839192b442892)طريقة[IWorksheet](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) الفئة الى**خاطئة**.
#### **تمكين معاينة فاصل الصفحة**
قم بتعيين أي ورقة عمل لمعاينة فاصل الصفحة عن طريق تعيين ملف[IsPageBreakPreview](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#aa1af81cfb7635232c7f839192b442892)طريقة[IWorksheet](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) الفئة الى**حقيقي**يؤدي القيام بذلك إلى تبديل ورقة العمل من العرض العادي إلى معاينة فاصل الصفحة.

 ويرد أدناه مثال كامل يوضح كيفية استخدام[IsPageBreakPreview](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#aa1af81cfb7635232c7f839192b442892)طريقة لتمكين وضع معاينة فاصل الصفحة لورقة العمل الأولى لملف Excel.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-EnablingPageBreakPreview.cpp" >}}
## **عامل التكبير**
### **باستخدام Microsoft إكسل**
يوفر Microsoft Excel ميزة تتيح للمستخدمين تعيين تكبير / تصغير ورقة العمل أو عامل التحجيم. تساعد هذه الميزة المستخدمين على رؤية محتويات ورقة العمل في طرق عرض أصغر أو أكبر. يمكن للمستخدمين ضبط عامل التكبير / التصغير على أي قيمة.
### **Aspose.Cells & عامل التكبير**
 يسمح Aspose.Cells أيضًا للمطورين بتعيين عامل تكبير ورقة العمل. Aspose.Cells يوفر فئة[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) الذي يمثل ملف إكسل Microsoft. ال[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) فئة تحتوي على[أوراق عمل](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)مجموعة تسمح بالوصول إلى كل ورقة عمل في ملف Excel.

 يتم تمثيل ورقة العمل بواسطة[IWorksheet](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) صف دراسي. ال[IWorksheet](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)يوفر class مجموعة واسعة من الأساليب لإدارة أوراق العمل. لتعيين عامل التكبير / التصغير الخاص بورقة العمل ، استخدم ملف[تكبير](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#ad94669a93a4324b3a4b7f9582df5b0ec) طريقة[IWorksheet](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) class يتم تعيين عامل التكبير / التصغير عن طريق تعيين قيمة رقمية (عدد صحيح) لملف[تكبير](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#ad94669a93a4324b3a4b7f9582df5b0ec)طريقة.

 ويرد أدناه مثال كامل يوضح كيفية استخدام[تكبير](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#ad94669a93a4324b3a4b7f9582df5b0ec)طريقة لتعيين عامل التكبير / التصغير لورقة العمل الأولى من ملف Excel.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-ZoomFactor.cpp" >}}
## **أجزاء التجميد**
### **باستخدام Microsoft إكسل**
ألواح التجميد هي ميزة يوفرها Microsoft Excel. تسمح لك أجزاء التجميد بتحديد البيانات لتظل مرئية عند التمرير في ورقة العمل.
### **Aspose.Cells & تجميد الأجزاء**
 يسمح Aspose.Cells أيضًا للمطورين بتطبيق ألواح التجميد على أوراق العمل في وقت التشغيل. Aspose.Cells يوفر فئة[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) يمثل ملف Excel Microsoft. ال[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) فئة تحتوي على[أوراق عمل](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)مجموعة تسمح بالوصول إلى كل ورقة عمل في ملف Excel.

 يتم تمثيل ورقة العمل بواسطة[IWorksheet](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) صف دراسي. ال[IWorksheet](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)يوفر class مجموعة واسعة من الأساليب لإدارة أوراق العمل. لتكوين أجزاء التجميد ، اتصل بـ[أجزاء التجميد](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#ac4f68dfe9ac219fb8de6d6824ec1aa22)طريقة[IWorksheet](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) صف دراسي. ال[أجزاء التجميد](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#ac4f68dfe9ac219fb8de6d6824ec1aa22)تأخذ الطريقة المعلمات التالية:

- **صف**، فهرس صف الخلية الذي سيبدأ التجميد منه.
- **عمودي**، فهرس العمود الخاص بالخلية التي سيبدأ التجميد منها.
- **صفوف مجمدة**، عدد الصفوف المرئية في الجزء العلوي.
- **أعمدة مجمدة**، عدد الأعمدة المرئية في الجزء الأيمن

 ويرد أدناه مثال كامل يوضح كيفية استخدام ملف[أجزاء التجميد](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#ac4f68dfe9ac219fb8de6d6824ec1aa22)طريقة لتجميد الصفوف والأعمدة (بدءًا من C4 ، ممثلة بالصف الرابع والعمود الثالث ، حيث تبدأ الصفوف والأعمدة من فهرس 0) من ورقة العمل الأولى من ملف Excel.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-FreezePanes.cpp" >}}
## **تقسيم الأجزاء**
إذا كنت بحاجة إلى تقسيم الشاشة للحصول على عرضين مختلفين في نفس ورقة العمل ، فقم بتقسيم الألواح. يوفر Microsoft Excel ميزة مفيدة للغاية تتيح لك عرض أكثر من نسخة واحدة من ورقة العمل الخاصة بك ، ولتتمكن من التمرير عبر كل جزء من ورقة العمل بشكل مستقل: تقسيم الأجزاء.

تعمل الأجزاء في وقت واحد. إذا قمت بإجراء تغيير في أحدهما ، فسيظهر التغيير في الآخر في نفس الوقت. يوفر Aspose.Cells ميزة الأجزاء المنقسمة للمستخدمين.
### **تطبيق وإزالة الأجزاء المنقسمة**
#### **تقسيم الأجزاء**
 Aspose.Cells يوفر فئة[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) الذي يمثل ملف إكسل Microsoft. ال[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)توفر class مجموعة واسعة من الطرق لإدارة ملف Excel. لتنفيذ طرق العرض المقسمة ، استخدم ملف[انشق، مزق](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#a0e581a3a9528a767c57008521ee02b6f) طريقة[IWorksheet](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) صف دراسي. لإزالة الأجزاء المنقسمة ، استخدم ملف[RemoveSplit](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#a5b554108c91f686e906400c26248eee5)طريقة.

في المثال ، نستخدم ملف قالب بسيط يتم تحميله ، ثم يتم تطبيق ميزة تقسيم الأجزاء المحددة على خلية في ورقة العمل الأولى. يتم حفظ الملف المحدث.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-SplitPanes.cpp" >}}
#### **إزالة الأجزاء**
 قم بإزالة الأجزاء المنقسمة باستخدام[RemoveSplit](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#a5b554108c91f686e906400c26248eee5)طريقة.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-RemovingPanes.cpp" >}}
