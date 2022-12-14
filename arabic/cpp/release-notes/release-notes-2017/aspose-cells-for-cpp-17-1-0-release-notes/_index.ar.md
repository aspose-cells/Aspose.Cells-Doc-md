---
title: Aspose.Cells لملاحظات إصدار CPP 17.1.0
type: docs
weight: 40
url: /ar/cpp/aspose-cells-for-cpp-17-1-0-release-notes/
---
|**مفتاح**|**ملخص**|**فئة**|
|:- |:- |:- |
|CELLSCPP-35|قراءة / كتابة تنسيق ملف XLSM|ميزة جديدة|
|CELLSCPP-36|قراءة / كتابة تنسيق ملف CSV|ميزة جديدة|
|CELLSCPP-37|قراءة / كتابة تنسيق ملف XLSB|ميزة جديدة|
|CELLSCPP-38|إنشاء النطاقات المسماة والتعامل معها|ميزة جديدة|
|CELLSCPP-39|قراءة / كتابة تنسيق ملف محدد بعلامات جدولة|ميزة جديدة|
### **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**
فيما يلي قائمة بأية تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells لـ C++. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.
#### **يزيل طريقة IPageSetup :: GetDraft () / SetDraft ()**
استخدم طريقة IPageSetup :: GetPrintDraft () / SetPrintDraft () بدلاً من ذلك.
#### **يزيل طريقة ICell :: GetConditionalIStyle ()**
استخدم ICell :: GetIConditionalFormattingResult () بدلاً من ذلك.
#### **يزيل طريقة ICells :: MaxDataRowInColumn ()**
استخدم ICells :: GetLastDataRow () بدلاً من ذلك.
#### **يحذف أسلوب IPaneCollection :: GetAcitvePaneType () / SetAcitvePaneType ()**
غير ضروري ، محذوف.
#### **يحذف طريقة IRange :: ToString ()**
غير ضروري ، محذوف.
#### **يحذف طريقة IRow :: Equals ()**
غير ضروري ، محذوف.
#### **يحذف طريقة IWorkbook :: SetISettings ()**
غير ضروري ، محذوف.
#### **يحذف طريقة ICell :: ToString ()**
غير ضروري ، محذوف.
#### **يحذف طريقة ICell :: Equals (ObjectPtr)**
غير ضروري ، محذوف.
#### **يحذف طريقة ICell :: GetHashCode ()**
غير ضروري ، محذوف.
#### **يحذف طريقة IWorksheet :: ToString ()**
غير ضروري ، محذوف.
#### **يضيف طريقة IBuiltInDocumentPropertyCollection :: GetScaleCrop () / SetScaleCrop ()**
يشير إلى وضع عرض مصغر المستند.
#### **يضيف طريقة IBuiltInDocumentPropertyCollection :: GetLinksUpToDate () / SetLinksUpToDate ()**
يشير إلى ما إذا كانت الارتباطات التشعبية في مستند محدثة أم لا.
#### **يضيف طريقة IExternalLink :: IsVisible ()**
يشير إلى ما إذا كان هذا الارتباط الخارجي مرئيًا في MS Excel.
#### **يضيف طريقة IListColumn :: GetFormula () / SetFormula ()**
الحصول على صيغة عمود القائمة وتعيينها.
#### **يضيف أسلوب IWorkbook :: GetAbsolutePath () / SetAbsolutePath ()**
الحصول على المسار المطلق للملف وتعيينه ، ويستخدم فقط للارتباطات الخارجية.
#### **يضيف طريقة IWorkbookSettings :: GetCheckCompatibility () / SetCheckCompatibility ()**
يشير إلى ما إذا كان التحقق من التوافق عند حفظ المصنف ، القيمة الافتراضية صحيحة.
#### **يضيف طريقة IWorksheetCollection :: CreateIRange ()**
يقوم بإنشاء IRange ، كائن من عنوان النطاق.
#### **يضيف طريقة IWorkbookSettings :: ClearPivottables ()**
مسح الجداول المحورية من جدول البيانات.
#### **يضيف طريقة ILoadOptions :: GetCultureInfo / SetCultureInfo ()**
يحصل على معلومات ثقافة النظام وقت تحميل الملف.
#### **يضيف طريقة ILoadOptions :: GetILightCellsDataHandler () / SetILightCellsDataHandler ()**
يشير إلى معالج البيانات لمعالجة بيانات الخلايا عند قراءة ملف القالب.
#### **يضيف طريقة IWorksheet :: GetIProtectedRangeCollection ()**
يحصل على مجموعة نطاق التحرير المسموح بها في ورقة العمل.
#### **يضيف طريقة IWorksheet :: Dispose ()**
يتخلص من ورقة العمل.
#### **يضيف طريقة ICells :: ImportTwoDimensionArray ()**
يستورد صفيفًا ثنائي الأبعاد من البيانات في ورقة عمل
#### **يضيف طريقة ICells :: ImportCSV ()**
يستورد ملف CSV إلى الخلايا.
#### **يضيف طريقة ICells :: LinkToXmlMap ()**
روابط لخريطة xml.
