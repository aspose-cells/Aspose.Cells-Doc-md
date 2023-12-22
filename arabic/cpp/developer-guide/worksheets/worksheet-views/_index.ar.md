---
title: طرق عرض ورقة العمل
type: docs
weight: 40
url: /ar/cpp/worksheet-views/
---
##  **معاينة فاصل الصفحة**
يمكن عرض كافة أوراق العمل في وضعين:

- العرض العادي.
- معاينة فاصل الصفحة.

طريقة العرض العادية هي طريقة العرض الافتراضية لورقة العمل. معاينة فاصل الصفحات هي طريقة عرض تحرير تعرض ورقة العمل أثناء طباعتها. تعرض معاينة فاصل الصفحات البيانات التي سيتم نقلها في كل صفحة حتى تتمكن من ضبط منطقة الطباعة وفواصل الصفحات. يمكن للمطورين باستخدام Aspose.Cells تمكين أوضاع العرض العادي أو معاينة فاصل الصفحات.
###  **التحكم في أوضاع العرض**
 Aspose.Cells يوفر فئة[دفتر العمل](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) الذي يمثل ملف Excel Microsoft. ال[دفتر العمل](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) يحتوي الفصل على أ[أوراق عمل](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)مجموعة تسمح بالوصول إلى كل ورقة عمل في ملف Excel.

يتم تمثيل ورقة العمل بواسطة[ورقة عمل](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)فصل. ال[ورقة عمل](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) يوفر الفصل مجموعة واسعة من الأساليب لإدارة أوراق العمل. لتمكين أوضاع المعاينة العادية أو فاصل الصفحات، استخدم[SetIsPageBreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setispagebreakpreview/) طريقة[ورقة عمل](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) فصل.[IsPageBreakPreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/ispagebreakpreview/) تُرجع قيمة منطقية، مما يعني أنه يمكنها تخزين قيمة منطقية فقط**حقيقي** أو**خطأ شنيع** قيمة.
####  **تمكين العرض العادي**
قم بتعيين ورقة العمل على العرض العادي عن طريق تعيين[SetIsPageBreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setispagebreakpreview/)طريقة[ورقة عمل](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)فئة إلى *خطأ**.
####  **تمكين معاينة فاصل الصفحات**
قم بتعيين أي ورقة عمل لمعاينة فاصل الصفحات عن طريق تعيين[SetIsPageBreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setispagebreakpreview/)طريقة[ورقة عمل](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)فئة إلى * صحيح **. يؤدي القيام بذلك إلى تحويل ورقة العمل من العرض العادي إلى معاينة فاصل الصفحات.

ويرد أدناه مثال كامل يوضح كيفية استخدام[SetIsPageBreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setispagebreakpreview/)طريقة لتمكين وضع معاينة فاصل الصفحات لورقة العمل الأولى لملف Excel.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-EnablingPageBreakPreview-new.cpp" >}}
##  **عامل التكبير**
###  **باستخدام Microsoft اكسل**
Microsoft يوفر Excel ميزة تسمح للمستخدمين بتحديد تكبير/تصغير ورقة العمل أو عامل القياس. تساعد هذه الميزة المستخدمين على رؤية محتويات ورقة العمل بطرق عرض أصغر أو أكبر. يمكن للمستخدمين ضبط عامل التكبير على أي قيمة.
###  **Aspose.Cells وعامل التكبير**
 Aspose.Cells يسمح أيضًا للمطورين بضبط عامل تكبير ورقة العمل. Aspose.Cells يوفر فئة[دفتر العمل](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) الذي يمثل ملف Excel Microsoft. ال[دفتر العمل](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) يحتوي الفصل على أ[أوراق عمل](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)مجموعة تسمح بالوصول إلى كل ورقة عمل في ملف Excel.

يتم تمثيل ورقة العمل بواسطة[ورقة عمل](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) فصل. ال[ورقة عمل](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)يوفر الفصل مجموعة واسعة من الأساليب لإدارة أوراق العمل. لتعيين عامل التكبير/التصغير لورقة العمل، استخدم[SetZoom](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setzoom/) طريقة[ورقة عمل](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) فصل. يتم تعيين عامل التكبير/التصغير عن طريق تعيين قيمة رقمية (عدد صحيح) للقيمة[SetZoom](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setzoom/)طريقة.

ويرد أدناه مثال كامل يوضح كيفية استخدام[SetZoom](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setzoom/)طريقة لتعيين عامل التكبير في ورقة العمل الأولى لملف Excel.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-ZoomFactor-new.cpp" >}}
##  **أجزاء التجميد**
###  **باستخدام Microsoft اكسل**
تجميد الأجزاء هي ميزة يوفرها Microsoft Excel. تسمح لك أجزاء التجميد بتحديد البيانات لتظل مرئية عند التمرير في ورقة العمل.
###  **Aspose.Cells وتجميد الألواح**
 Aspose.Cells يسمح أيضًا للمطورين بتطبيق أجزاء التجميد على أوراق العمل في وقت التشغيل. Aspose.Cells يوفر فئة[دفتر العمل](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) الذي يمثل ملف Excel Microsoft. ال[دفتر العمل](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) يحتوي الفصل على أ[أوراق عمل](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)مجموعة تسمح بالوصول إلى كل ورقة عمل في ملف Excel.

يتم تمثيل ورقة العمل بواسطة[ورقة عمل](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) فصل. ال[ورقة عمل](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)يوفر الفصل مجموعة واسعة من الأساليب لإدارة أوراق العمل. لتكوين أجزاء التجميد، اتصل بـ[أجزاء التجميد](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/)طريقة[ورقة عمل](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) فصل. ال[أجزاء التجميد](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/)تأخذ الطريقة المعلمات التالية:

- *الصف**، فهرس صف الخلية التي سيبدأ التجميد منها.
- *العمود**، فهرس عمود الخلية التي سيبدأ التجميد منها.
- *الصفوف المجمدة**، عدد الصفوف المرئية في الجزء العلوي.
- *الأعمدة المجمدة**، عدد الأعمدة المرئية في الجزء الأيمن

 ويرد أدناه مثال كامل يوضح كيفية استخدام[أجزاء التجميد](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/)طريقة لتجميد الصفوف والأعمدة (بدءًا من C4، ممثلة بالصف الرابع والعمود الثالث، حيث تبدأ الصفوف والأعمدة من الفهرس 0) لورقة العمل الأولى لملف Excel.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-FreezePanes-new.cpp" >}}
##  **تقسيم الأجزاء**
إذا كنت بحاجة إلى تقسيم الشاشة للحصول على طريقتي عرض مختلفتين في نفس ورقة العمل، فقم بتقسيم الأجزاء. Microsoft يقدم برنامج Excel ميزة مفيدة جدًا تتيح لك عرض أكثر من نسخة من ورقة العمل الخاصة بك، كما تتيح لك إمكانية التمرير خلال كل جزء من ورقة العمل بشكل مستقل: الأجزاء المقسمة.

تعمل الأجزاء في وقت واحد. إذا قمت بإجراء تغيير في أحدهما، فسيظهر التغيير في الوقت نفسه في الآخر. Aspose.Cells يوفر ميزة الأجزاء المقسمة للمستخدمين.
###  **تطبيق وإزالة الأجزاء المقسمة**
####  **تقسيم الأجزاء**
 Aspose.Cells يوفر فئة[دفتر العمل](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) الذي يمثل ملف Excel Microsoft. ال[دفتر العمل](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)يوفر class مجموعة واسعة من الأساليب لإدارة ملف Excel. لتنفيذ طرق العرض المقسمة، استخدم[ينقسم](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/split/) طريقة[ورقة عمل](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) فصل. لإزالة الأجزاء المقسمة، استخدم[إزالة سبليت](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/removesplit/)طريقة.

في المثال، نستخدم ملف قالب بسيط يتم تحميله، ثم يتم تطبيق ميزة تعيين الأجزاء المقسمة على خلية في ورقة العمل الأولى. يتم حفظ الملف المحدث.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-SplitPanes-new.cpp" >}}
####  **إزالة الأجزاء**
 قم بإزالة الأجزاء المقسمة باستخدام[إزالة سبليت](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/removesplit/)طريقة.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-RemovingPanes-new.cpp" >}}
