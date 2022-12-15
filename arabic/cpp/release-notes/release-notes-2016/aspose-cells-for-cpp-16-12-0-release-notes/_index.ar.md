---
title: Aspose.Cells لملاحظات إصدار CPP 16.12.0
type: docs
weight: 10
url: /ar/cpp/aspose-cells-for-cpp-16-12-0-release-notes/
---
|**مفتاح**|**ملخص**|**فئة**|
|:- |:- |:- |
|CELLSPORTINGC-432|تطبيق التنسيق الشرطي على الخلايا|ميزة جديدة|
|CELLSPORTINGC-433|قراءة / كتابة خصائص المستند المخصصة|ميزة جديدة|
|CELLSPORTINGC-434|قراءة / كتابة خصائص المستند المضمنة|ميزة جديدة|
|CELLSPORTINGC-435|أضف ارتباطات تشعبية إلى الخلايا|ميزة جديدة|
|CELLSPORTINGC-436|دعم مواضيع MS Excel|ميزة جديدة|
|CELLSPORTINGC-437|إضافة ومعالجة جداول PivotTables في جدول البيانات|ميزة جديدة|
|CELLSPORTINGC-438|قم بتجميع الصفوف والأعمدة في ورقة العمل|ميزة جديدة|
|CELLSPORTINGC-439|أضف كائن جدول / قائمة إلى ورقة العمل|ميزة جديدة|
|CELLSPORTINGC-426|مشكلة الترخيص مع Aspose.Cells for C++ واجهات برمجة التطبيقات|حشرة|
|CELLSPORTINGC-425|تحسين أداء حفظ ملفات XLS|تحسين|
### **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**
فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for C++. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.
#### **يعيد تسمية طريقة ICell :: SetStyle إلى ICell :: SetIStyle**
#### **يعيد تسمية طريقة ICell :: SetCharacters إلى ICell :: SetIFontSettings**
#### **إعادة تسمية طريقة ICellsColor :: SetThemeColor إلى ICellsColor :: SetIThemeColor**
#### **يعيد تسمية طريقة ICells :: SetStyle إلى ICells :: SetIStyle**
#### **يعيد تسمية طريقة ICellsHelper :: GetDPI_i إلى ICellsHelper :: GetDPI**
#### **يعيد تسمية طريقة ICellsHelper :: SetDPI_i إلى ICellsHelper :: SetDPI**
#### **يعيد تسمية طريقة ICellsHelper :: GetVersion_i إلى ICellsHelper :: GetVersion**
#### **يعيد تسمية طريقة ICellsHelper :: IsProtectedByRMS_i إلى ICellsHelper :: IsProtectedByRMS**
#### **يعيد تسمية طريقة ICellsHelper :: IsProtectedByRMS_i إلى ICellsHelper :: IsProtectedByRMS**
#### **إعادة تسمية طريقة ICellsHelper :: CellNameToIndex_i إلى ICellsHelper :: CellNameToIndex**
#### **إعادة تسمية طريقة ICellsHelper :: CellIndexToName_i إلى ICellsHelper :: CellIndexToName**
#### **إعادة تسمية طريقة ICellsHelper :: ColumnIndexToName_i إلى ICellsHelper :: ColumnIndexToName**
#### **يعيد تسمية طريقة ICellsHelper :: ColumnNameToIndex_i إلى ICellsHelper :: ColumnNameToIndex**
#### **إعادة تسمية طريقة ICellsHelper :: RowIndexToName_i إلى ICellsHelper :: RowIndexToName**
#### **إعادة تسمية طريقة ICellsHelper :: RowNameToIndex_i إلى ICellsHelper :: RowNameToIndex**
#### **إعادة تسمية طريقة ICellsHelper :: ConvertR1C1FormulaToA1_i إلى ICellsHelper :: ConvertR1C1FormulaToA1**
#### **إعادة تسمية طريقة ICellsHelper :: ConvertA1FormulaToR1C1_i إلى ICellsHelper :: ConvertA1FormulaToR1C1**
#### **يعيد تسمية طريقة ICellsHelper :: GetDateTimeFromDouble_i إلى ICellsHelper :: GetDateTimeFromDouble**
#### **يعيد تسمية طريقة ICellsHelper :: GetDoubleFromDateTime_i إلى ICellsHelper :: GetDoubleFromDateTime**
#### **يعيد تسمية طريقة ICellsHelper :: DetectLoadFormat_i إلى ICellsHelper :: DetectLoadFormat**
#### **إعادة تسمية طريقة ICellsHelper :: DetectFileFormat_i إلى ICellsHelper :: DetectFileFormat**
#### **يعيد تسمية طريقة ICellsHelper :: GetFontDir_i إلى ICellsHelper :: GetFontDir**
#### **يعيد تسمية طريقة ICellsHelper :: SetFontDir_i إلى ICellsHelper :: SetFontDir**
#### **يعيد تسمية طريقة ICellsHelper :: GetFontDirs_i إلى ICellsHelper :: GetFontDirs**
#### **يعيد تسمية طريقة ICellsHelper :: SetFontDirs_i إلى ICellsHelper :: SetFontDirs**
#### **يعيد تسمية طريقة ICellsHelper :: GetFontFiles_i إلى ICellsHelper :: GetFontFiles**
#### **يعيد تسمية طريقة ICellsHelper :: SetFontFiles_i إلى ICellsHelper :: SetFontFiles**
#### **يعيد تسمية طريقة ICellsHelper :: GetStartupPath_i إلى ICellsHelper :: GetStartupPath**
#### **يعيد تسمية طريقة ICellsHelper :: SetStartupPath_i إلى ICellsHelper :: SetStartupPath**
#### **إعادة تسمية طريقة ICellsHelper :: GetAltStartPath_i إلى ICellsHelper :: GetAltStartPath**
#### **يعيد تسمية طريقة ICellsHelper :: SetAltStartPath_i إلى ICellsHelper :: SetAltStartPath**
#### **يعيد تسمية طريقة ICellsHelper :: GetLibraryPath_i إلى ICellsHelper :: GetLibraryPath**
#### **يعيد تسمية طريقة ICellsHelper :: SetLibraryPath_i إلى ICellsHelper :: SetLibraryPath**
#### **يعيد تسمية طريقة ICellsHelper :: GetUsedColors_i إلى ICellsHelper :: GetUsedColors**
#### **يعيد تسمية طريقة ICellsHelper :: AddAddInFunction_i إلى ICellsHelper :: AddAddInFunction**
#### **يعيد تسمية طريقة ICellsHelper :: MergeFiles_i إلى ICellsHelper :: MergeFiles**
#### **إعادة تسمية طريقة IColumnCollection :: GetByIndex_i إلى IColumnCollection :: GetIColumn**
#### **إعادة تسمية طريقة IFileFormatUtil :: DetectFileFormat_i إلى IFileFormatUtil :: DetectFileFormat**
#### **إعادة تسمية أسلوب IFileFormatUtil :: ExtensionToSaveFormat_i إلى IFileFormatUtil :: ExtensionToSaveFormat**
#### **إعادة تسمية طريقة IFileFormatUtil :: IsTemplateFormat_i إلى IFileFormatUtil :: IsTemplateFormat**
#### **إعادة تسمية أسلوب IFileFormatUtil :: LoadFormatToExtension_i إلى IFileFormatUtil :: LoadFormatToExtension**
#### **إعادة تسمية أسلوب IFileFormatUtil :: LoadFormatToSaveFormat_i إلى IFileFormatUtil :: LoadFormatToSaveFormat**
#### **إعادة تسمية طريقة IFileFormatUtil :: SaveFormatToExtension_i إلى IFileFormatUtil :: SaveFormatToExtension**
#### **إعادة تسمية طريقة IFileFormatUtil :: SaveFormatToLoadFormat_i إلى IFileFormatUtil :: SaveFormatToLoadFormat**
#### **يعيد تسمية طريقة IRange :: SetStyle إلى IRange :: SetIStyle**
#### **يعيد تسمية أسلوب IFindOptions :: SetRange إلى IFindOptions :: SetIRange**
#### **يعيد تسمية طريقة ILoadOptions :: SetLoadDataOptions إلى ILoadOptions :: SetILoadDataOptions**
#### **يعيد تسمية طريقة IWorkbook :: SetSettings إلى IWorkbook :: SetISettings**
#### **يعيد تسمية طريقة IWorkbook :: SetDefaultStyle إلى SetDefaultIStyle**
