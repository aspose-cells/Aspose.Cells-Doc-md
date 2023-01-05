---
title: Aspose.Cells for Java 8.3.2 ملاحظات الإصدار
type: docs
weight: 90
url: /ar/java/aspose-cells-for-java-8-3-2-release-notes/
---
{{% alert color="primary" %}} 

 تحتوي هذه الصفحة على ملاحظات الإصدار لـ[Aspose.Cells for Java 8.3.2](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-8.3.2/)

{{% /alert %}} 

\1) Aspose.Cells 


الميزات الرئيسية

تم إصدار تغييرات الأرشيف لـ JDK المدعومة

من الآن فصاعدًا ، نقدم ملف Jar واحدًا فقط لـ 1.6 وما فوق في الأرشيف.

تحسينات وتغييرات أخرى

ميزات جديدة

(CELLSJAVA-41144) - القدرة على حذف النمط من StyleCollection عند حفظ HTML
(CELLSJAVA-41127) - تحديد فواصل مخصصة لمصنف كامل
(CELLSJAVA-41143) - حدد اسم المهمة / المستند عند الطباعة باستخدام Aspose.Cells

التحسينات

(CELLSJAVA-41145) - الجيل الذكي لـ CSS أثناء تصدير جداول البيانات إلى HTML
(CELLSJAVA-41177) - Cell.setHtmlString لا يعمل عند استخدام "<s><span style="color:#ff00ff;">S2</span></s>"
(CELLSJAVA-41162) - أضف دلائل الخطوط الافتراضية لنظامي التشغيل Mac و Linux في قائمة البحث عن الخطوط

أداء

(CELLSJAVA-41119) - توقف صورة Chart.to لفترة غير محددة

البق

(CELLSJAVA-41165) - لا يتم تحديث PivotChart بعد تحديث البيانات المصدر وتقديم جدول البيانات إلى PDF
(CELLSJAVA-41156) - تتسبب Chart.refreshPivotData في تحويل التواريخ في محور المخطط إلى أرقام أثناء تحويل جدول البيانات إلى PDF
(CELLSJAVA-41154) - يظهر صف إضافي في إخراج HTML أثناء لصق النطاق باستخدام PasteType.ALL
(CELLSJAVA-41151) - سلوك غريب فيما يتعلق بالتنسيق في تقرير PivotTable الناتج عند استخدام وبدون استخدام سطر الكود الذي يتوافق مع استرداد نطاق الصف
(CELLSJAVA-41150) - FormatCondition غير مدعومة فيما يتعلق بتنسيق Numbers عند التقديم إلى تنسيق ملف HTML
(CELLSJAVA-41146) - عرض غير صحيح للحدود أثناء تحويل جدول البيانات إلى HTML
(CELLSJAVA-41134) - لا يتم تحميل XLSB2007TestNewS.xlsb ويحافظ على زيادة استهلاك الذاكرة
(CELLSJAVA-41129) - تظهر خطوط إضافية عند عرض الإخراج HTML في Chrome
(CELLSJAVA-41122) - فتح المالية وادخارها_بيان - تصريح_إدخال_نقل_Withdata.xlsb يجعلها تالفة
(CELLSJAVA-41098) - يزيل الجدول المحوري التحديث تنسيق Pivot Table عند التحويل إلى PDF
(CELLSJAVA-41157) - MemorySetting.MEMORY_PREFERENCE يتسبب في تلف XLS
(CELLSJAVA-41149) - عرض غير صحيح للوقت عند تحويل جدول البيانات إلى PDF
(CELLSJAVA-41148) - عثر Excel على محتوى غير قابل للقراءة ... خطأ عند فتح المصنف وحفظه
(CELLSJAVA-41141) - لم يتم ضبط Cell باستخدام طريقة ListObject.putCellValue ()
(CELLSJAVA-41140) - تمديد الجدول لا ينسخ الصيغة إلى صفوف جديدة
(CELLSJAVA-41166) - XPS لا يمكن للمشاهد فتح Aspose.Cells ولدت XPS
(CELLSJAVA-41163) - يؤدي تصدير SVG إلى إنشاء ملف غير صالح
(CELLSJAVA-41153) - يقوم Shape.toImage بتخزين الصورة بتنسيق BMP بدلاً من SVG للأشكال الأخرى غير المخطط
(CELLSJAVA-41137) - مشكلة تتعلق بتعيين قيم نطاق خلايا datalabels
(CELLSJAVA-41128) - لا يتم عرض الرسوم البيانية بشكل جيد عند إعادة حفظ الملف XLSX
(CELLSJAVA-41125) - تحتوي صورة المخطط على ضوضاء عند تحويلها بدقة أقل
(CELLSJAVA-40928) - لا يتم عرض النص الصيني في عناوين فئة المخطط بشكل صحيح
(CELLSJAVA-41158) - مشكلة في تنسيق البيانات في تقرير PivotTable
(CELLSJAVA-41159) - مشكلة في حساب بيانات الجدول المحوري
(CELLSJAVA-41175) - لا يتم عرض سلسلة خطوط الاتجاه في وسيلة الإيضاح

استثناءات

(CELLSJAVA-41164) - java.lang.NullPointerException في Cells. ابحث
(CELLSJAVA-41131) - الحفظ في PDF تتعطل وتتعطل مشكلة الذاكرة مع الملف المصدر XLSB

API العام والتغييرات غير المتوافقة مع الإصدارات السابقة

فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for Java. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.

 يضيف WorkbookSettings.NumberDecimalSeparator ، و NumberGroupSeparator
 الحصول على / تعيين الفواصل المستخدمة لتنسيق / تحليل القيم الرقمية.

يضيف طريقة WorkbookSettings.CheckWriteProtectedPassword ()
 للتحقق مما إذا كانت كلمة المرور صحيحة ، وكتابة كلمة المرور المحمية.

 إضافة خاصية Picture.SignatureLine وفئة SignatureLine.
 يستخدم لإنشاء وقراءة إعداد خط التوقيع.

 إضافة خاصية PivotItem.Position.
 يحدد فهرس الموضع في كل عناصر PivotItems ، وليس PivotItems ضمن نفس العقدة الأصلية.

 إضافة خاصية PivotItem.PositionInSameParentNode.
 يحدد فهرس الموضع في PivotItems تحت نفس العقدة الأصلية.

 يضيف طريقة PivotItem.Move (عدد int ، bool isSameParent).
تحريك العنصر لأعلى أو لأسفل.

 يضيف طريقة Worksheet.RefreshPivotTables ().
يحدّث كل جداول PivotTables في ورقة العمل هذه.

 يضيف طريقة Workbook.GetNamedStyle (اسم السلسلة).
الحصول على النمط المسمى في تجمع أنماط المصنف حسب الاسم.

 يضيف Cells.ImportTwoDimensionArray (object ،، object، int، int، TxtLoadOptions)
يستورد صفيفًا ثنائي الأبعاد من البيانات في ورقة عمل بخيارات أكثر مرونة محددة في TxtLoadOptions.

 إضافة خاصية PageSetup.IsAutomaticPaperSize.
 يشير إلى ما إذا كان حجم الصفحة تلقائيًا.

 يضيف خصائص XpsSaveOptions.OnePagePerSheet
إذا كانت OnePagePerSheet صحيحة ، فسيتم إخراج كل محتوى ورقة واحدة إلى صفحة واحدة فقط نتيجة لذلك.

 يضيف خصائص XpsSaveOptions.PageIndex
الحصول على أو تحديد الفهرس الذي يستند إلى 0 للصفحة الأولى لحفظها.

 إضافة خصائص XpsSaveOptions.PageCount
الحصول على أو تحديد عدد الصفحات المراد حفظها.

 يضيف SheetRender.ToPrinter (سلسلة PrinterName ، int PrintPageIndex ، int PrintPageCount)
يعرض ورقة العمل للطابعة.

 يضيف WorkbookRender.ToPrinter (سلسلة PrinterName ، int PrintPageIndex ، int PrintPageCount)
يعرض المصنف إلى الطابعة.

 يضيف خصائص PdfSaveOptions.IsFontSubstitutionCharGranularity
الإشارة إلى ما إذا كان سيتم استبدال خط الحرف فقط عندما لا يكون خط الخلية متوافقًا معه.

 يضيف خاصية GridWeb.AutoRefreshChart
يشير إلى ما إذا تم تحديث صورة المخطط أثناء تحديث قيمة الخلية. الافتراضي هو الصحيح.

 يضيف أسلوب GridWeb.RefreshChartShape ()
يحدّث كل صور المخطط لورقة العمل النشطة.

 Obsoletes Workbook.SaveOptions property
يجب على المستخدمين إنشاء SaveOptions المناسبة ثم استخدام Workbook.Save () معها.

 عفا عليها الزمن فئة StyleCollection و Workbook.Styles الملكية
يجب على المستخدمين استخدام Workbook.CreateStyle () لإنشاء نمط المصنف ومعالجته بدلاً من StyleCollection.Add () واستخدام Workbook.GetNamedStyle (سلسلة) للحصول على نمط مسمى بدلاً من StyleCollectionstring.

 عفا عليها الزمن طريقة PivotItem.Move (عدد العمليات).
استخدام طريقة PivotItem.Move (عدد int ، bool isSameParent) بدلاً من ذلك.

 يحذف جميع طرق Open () و Save () القديمة من المصنف.

 يحذف طريقة Workbook.SetOleSize () القديمة.

 حذف خصائص IsProtected ، اللغة والمنطقة القديمة من المصنف.

 يحذف أساليب Workbook.LoadData () القديمة.

 يحذف طرق Open () و Save () المتقادمة من WorkbookDesigner.

حذف خصائص ReCalcOnOpen واللغة والتشفير و ConvertNumericData المتقادمة من WorkbookSettings.

 حذف خصائص HidePivotFieldList و EnableHTTPCompression و IsMinimized و IsHidden و SheetTabBarWidth القديمة في WorksheetCollection.

 يحذف WindowLeft و WindowLeftInch و WindowLeftCM و WindowTop و WindowTopInch و WindowTopCM و WindowWidth و WindowWidthInch و WindowWidthCM و WindowHeight و WindowHeightInch و WindowHeightCM وخصائص WorksheetCollection.

 يحذف طريقة DeleteName () القديمة من WorksheetCollection.

 يحذف HPageBreaks و VPageBreaks القديمة من ورقة العمل.

 حذف DisplayHTMLCrossString و ExportChartImageFormat المتقادم من HtmlSaveOptions.

 حذف خاصية ExpCellNameToXLSX القديمة الخاصة بـ SaveOptions.

 يحذف خصائص SaveOptions و SaveOptions و PdfBookmark و PdfImageCompression القديمة.

 يحذف TxtSaveOptions. خاصية AlwaysQuoted القديمة.


ملحوظة
نظرًا لأن قاعدة الكود Aspose.Cells for Java تطابق رمز إصدار .NET ذي الصلة ، فإن معظم التغييرات والتحسينات والإصلاحات المضمنة في Aspose.Cells for .NET v8.3.2 مدرجة أيضًا في Aspose.Cells for Java v8.3.2.
