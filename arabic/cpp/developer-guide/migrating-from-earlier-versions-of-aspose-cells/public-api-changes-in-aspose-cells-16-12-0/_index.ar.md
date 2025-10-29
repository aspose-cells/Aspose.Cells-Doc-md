---
title: التغييرات العامة في واجهة برمجة التطبيقات العامة في Aspose.Cells 16.12.0
type: docs
weight: 10
url: /ar/cpp/public-api-changes-in-aspose-cells-16-12-0/
---

{{% alert color="primary" %}} 

يصف هذا المستند التغييرات في واجهة برمجة التطبيقات لـ Aspose.Cells من الإصدار 16.11.0 إلى 16.12.0 التي قد تكون مهمة لمطوري الوحدات/التطبيقات. وتشمل ليس فقط الطرق العامة الجديدة والمحدثة، والفئات المضافة والمحذوفة وما إلى ذلك، ولكن أيضًا وصفًا لأي تغييرات في السلوك خلف الكواليس في Aspose.Cells.

{{% /alert %}} 
## **واجهات برمجة التطبيقات الجديدة**
### **دعم جداول البيانات الدورانية**
يدعم الإصدار الثاني من Aspose.Cells for C++ إنشاء وكذلك تلاعب جداول البيانات الدورانية. Aspose.Cells for C++ توفر فئة IPivotTable التي تمثل كائن جدول بيانات دوراني في حين أن IPivotTableCollection تمثل مجموعة من جداول البيانات الدورانية. يمكن الوصول إلى IPivotTableCollection عبر كائن IWorksheet ويمكن إضافة جدول بيانات دوراني جديد إلى المجموعة باستخدام طريقة IPivotTableCollection.Add.

توضح قصاصة الكود التالية مدى سهولة استخدام Aspose.Cells for C++ API لـ [إنشاء جداول البيانات الدورانية من البداية](/cells/ar/cpp/create-pivot-table/).

**C++**

{{< highlight csharp >}}

 //Load the sample excel file

intrusive_ptr<IWorkbook> wb = Factory::CreateIWorkbook();

//Access first worksheet

intrusive_ptr<IWorksheet> ws = wb->GetIWorksheets()->GetObjectByIndex(0);

//Add source data for pivot table

intrusive_ptr<String> str = new String("Fruit");

ws->GetICells()->GetObjectByIndex(new String("A1"))->PutValue(str);

str = new String("Quantity");

ws->GetICells()->GetObjectByIndex(new String("B1"))->PutValue(str);

str = new String("Price");

ws->GetICells()->GetObjectByIndex(new String("C1"))->PutValue(str);

str = new String("Apple");

ws->GetICells()->GetObjectByIndex(new String("A2"))->PutValue(str);

str = new String("Orange");

ws->GetICells()->GetObjectByIndex(new String("A3"))->PutValue(str);

ws->GetICells()->GetObjectByIndex(new String("B2"))->PutValue(3);

ws->GetICells()->GetObjectByIndex(new String("B3"))->PutValue(4);

ws->GetICells()->GetObjectByIndex(new String("C2"))->PutValue(2);

ws->GetICells()->GetObjectByIndex(new String("C3"))->PutValue(1);

//Add pivot table

int idx = ws->GetIPivotTables()->Add(new String("A1:C3"), new String("E5"), new String("MyPivotTable"));

//Access created pivot table

intrusive_ptr<IPivotTable> pt = ws->GetIPivotTables()->GetObjectByIndex(idx);

//Manipulate pivot table rows, columns and data fields

pt->AddFieldToArea(PivotFieldType_Row, pt->GetIBaseFields()->GetObjectByIndex(0));

pt->AddFieldToArea(PivotFieldType_Data, pt->GetIBaseFields()->GetObjectByIndex(1));

pt->AddFieldToArea(PivotFieldType_Data, pt->GetIBaseFields()->GetObjectByIndex(2));

pt->AddFieldToArea(PivotFieldType_Column, pt->GetIDataField());

//Set pivot table style

pt->SetPivotTableStyleType(PivotTableStyleType_PivotTableStyleMedium9);

//Save the output excel file

wb->Save(outputPath);

{{< /highlight >}}

بالإضافة إلى إنشاء جداول بيانات دورانية جديدة ، تدعم APIs Aspose.Cells for C++ أيضًا تلاعب جداول البيانات الدورانية الحالية. تدعم الواجهة البرمجية حاليًا تغيير البيانات في نطاق المصدر لجدول البيانات الدوراني ثم تحديثه. بمجرد أن تم تلاعب جدول البيانات الدوراني كما هو مطلوب ، من الأفضل استخدام طرق IPivotTable.RefreshData و IPivotTable.CalculateData لتحديث جدول البيانات الدوراني ضد مصدر البيانات المحدث.

يستخدم القصاصة البرمجية التالية واجهة برمجة التطبيقات Aspose.Cells for C++ API لـ [تلاعب جدول بيانات دوراني موجود](/cells/ar/cpp/manipulate-pivot-table/).

**C++**

{{< highlight csharp >}}

 //Load the sample excel file

intrusive_ptr wb = Factory::CreateIWorkbook(samplePath);

//Access first worksheet

intrusive_ptr ws = wb->GetIWorksheets()->GetObjectByIndex(0);

//Change value of cell B3 which is inside the source data of pivot table

intrusive_ptr str = new String("Cup");

ws->GetICells()->GetObjectByIndex(new String("B3"))->PutValue(str);

//Get the value of cell H8 before refreshing pivot table

intrusive_ptr val = ws->GetICells()->GetObjectByIndex(new String("H8"))->GetStringValue();

printf("Before refreshing Pivot Table value of cell H8: %s\r\n%", val->charValue());

//Access pivot table, refresh and calculate it

intrusive_ptr pt = ws->GetIPivotTables()->GetObjectByIndex(0);

pt->RefreshData();

pt->CalculateData();

//Get the value of cell H8 after refreshing pivot table

val = ws->GetICells()->GetObjectByIndex(new String("H8"))->GetStringValue();

printf("After refreshing Pivot Table value of cell H8: %s\r\n%", val->charValue());

//Save the output excel file

wb->Save(outputPath);

{{< /highlight >}}
### **دعم قواعد التنسيق المشروط**
توفر Aspose.Cells for C++ الآن القدرة على إضافة قواعد التنسيق المشروط إلى ورقة العمل من خلال فتح فئة IFormatCondition. توفر الفئة المذكورة أيضًا الطرق التالية لـ [تطبيق قواعد التنسيق المشروط](/cells/ar/cpp/apply-conditional-formatting-in-worksheet/) وفقًا لمتطلبات التطبيق.

- IFormatCondition.GetIAboveAverage
- IFormatCondition.GetIColorScale
- IFormatCondition.GetIDataBar
- IFormatCondition.GetIIconSet
- IFormatCondition.GetITop10

يوضح الكود النموذجي التالي كيفية إضافة قاعدة تنسيق مشروط من نوع قيمة الخلية على الخلايا A1 و B2.

**C++**

{{< highlight csharp >}}

 //Create an empty workbook

intrusive_ptr wb = Factory::CreateIWorkbook();

//Access first worksheet

intrusive_ptr ws = wb->GetIWorksheets()->GetObjectByIndex(0);

//Adds an empty conditional formatting

int idx = ws->GetIConditionalFormattings()->Add();

intrusive_ptr fcs = ws->GetIConditionalFormattings()->GetObjectByIndex(idx);

//Set the conditional format range

intrusive_ptr ca = ICellArea::CreateICellArea(new String("A1"), new String("A1"));

fcs->AddArea(ca);

ca = ICellArea::CreateICellArea(new String("B2"), new String("B2"));

fcs->AddArea(ca);

//Add condition and set the background color

idx = fcs->AddCondition(FormatConditionType_CellValue, OperatorType_Between, new String("=A2"), new String("100"));

intrusive_ptr fc = fcs->GetObjectByIndex(idx);

fc->GetIStyle()->SetBackgroundColor(Color::GetRed());

//User friendly message to test the output excel file.

StringPtr msgStr = new String("Red color in cells A1 and B2 is because of Conditional Formatting.");

ws->GetICells()->GetObjectByIndex(new String("A10"))->PutValue(msgStr);

//Save the output excel file

wb->Save(outputPath);

{{< /highlight >}}
### **دعم الروابط التشعبية**
يدعم الإصدار Aspose.Cells for C++ الآن [إضافة الروابط التشعبية لخلايا جدول البيانات](/cells/ar/cpp/add-hyperlinks-to-the-cells/). ومن أجل توفير هذه الميزة، قام الإصدار 16.12.0 من Aspose.Cells for C++ بتعريض فئة IHyperlinkCollection التي يمكن الوصول إليها عبر كائن IWorksheet، حيث يمكن إضافة رابط تشعبي إلى المجموعة باستخدام طريقة IHyperlinkCollection.Add كما هو موضح أدناه.

**C++**

{{< highlight csharp >}}

 //Create a new workbook

intrusive_ptr wb = Factory::CreateIWorkbook();

//Get the first worksheet

intrusive_ptr wsc = wb->GetIWorksheets();

intrusive_ptr ws = wsc->GetObjectByIndex(0);

//Add hyperlink in cell C7 and make use of its various methods

intrusive_ptr hypLnks = ws->GetIHyperlinks();

int idx = hypLnks->Add(new String("C7"), 1, 1, new String("http://www.aspose.com/"));

intrusive_ptr lnk = hypLnks->GetObjectByIndex(idx);

lnk->SetTextToDisplay(new String("Aspose"));

lnk->SetScreenTip(new String("Link to Aspose Website"));

//Save the workbook in xlsx format

wb->Save(dirPath->Append(new String("output.xlsx")), SaveFormat_Xlsx);

{{< /highlight >}}
### **دعم خصائص المستند**
تدعم تطبيق Excel نوعين من خصائص المستند كما هو مدرج أدناه.

- الخصائص المعرفة مسبقاً (المضمنة): تحتوي الخصائص المضمنة على معلومات عامة حول المستند مثل عنوان المستند، اسم الكاتب، إحصاءات المستند وغيرها.
- الخصائص المعرفة بواسطة المستخدم (المخصصة): تحددها الخصائص المخصصة التي يقوم المستخدم بتعريفها في شكل زوج اسم قيمة.

يدعم الإصدار Aspose.Cells for C++ [إدارة كل من أنواع خصائص المستند، المضمنة والمخصصة](/cells/ar/cpp/managing-document-properties/). فئة IWorkbook في Aspose.Cells تمثل ملف Excel. من أجل الوصول إلى خصائص المستند المضمنة، استخدم طريقة IWorkbook.GetBuiltInDocumentProperties بينما يمكن الوصول إلى خصائص المستند المخصصة باستخدام طريقة IWorkbook.GetCustomDocumentProperties.

الكود النموذجي التالي يحمل جدول بيانات عينة موجود مسبقًا ويقرأ خصائص المستند المضمنة مثل العنوان والموضوع والخصائص المخصصة بالاسم MyCustom1.

**C++**

{{< highlight csharp >}}

 //Load the sample excel file

intrusive_ptr wb = Factory::CreateIWorkbook(samplePath);

//Read built-in title and subject properties

StringPtr strTitle = wb->GetIBuiltInDocumentProperties()->GetTitle();

StringPtr strSubject = wb->GetIBuiltInDocumentProperties()->GetSubject();

printf("Title: %s\r\n", strTitle->charValue());

printf("Subject: %s\r\n", strSubject->charValue());

printf("\r\n");

//Modify built-in title and subject properties

strTitle = new String("Aspose.Cells New Title");

strSubject = new String("Aspose.Cells New Subject");

wb->GetIBuiltInDocumentProperties()->SetTitle(strTitle);

wb->GetIBuiltInDocumentProperties()->SetSubject(strSubject);

//Read the custom property

StringPtr strCustomPropName = new String("MyCustom1");

StringPtr strCustomPropValue = wb->GetICustomDocumentProperties()->GetObjectByIndex(strCustomPropName)->ToString();

printf("MyCustom1: %s\r\n", strCustomPropValue->charValue());

//Add a new custom property

strCustomPropName = new String("MyCustom5");

strCustomPropValue = new String("This is my custom five.");

wb->GetICustomDocumentProperties()->AddIDocumentProperty(strCustomPropName, strCustomPropValue);

//Save the output excel file

wb->Save(outputPath);

{{< /highlight >}}
### **دعم لجداول البيانات**
يعتبر جدول Excel مصفوفة من الخلايا تحتوي على عدد من الصفوف والأعمدة، في حين يشار إلى نفس الجدول بأنه كائن قائمة في واجهات برمجة التطبيقات (APIs) لـ Aspose.Cells for C++. فضاء الاسم Aspose::Cells::Tables يحتوي على جميع الفئات الضرورية التي تتعامل مع العمليات المتعلقة بجداول البيانات. من بين أبرز الفئات تذكير فئات IListObject وIListObjectCollection والتي تسمح بـ [إنشاء وتنسيق جداول البيانات](/cells/ar/cpp/create-and-format-table/) وغيرها.

الكود النموذجي التالي يقوم بتحميل ملف جدول بيانات عينة ثم يقوم بإنشاء كائن قائمة (جدول) في نطاق A1:H10، ثم يستخدم طرقه المختلفة لإظهار الإجمالي الفرعي.

**C++**

{{< highlight csharp >}}

 //Load the sample excel file

intrusive_ptr<IWorkbook> wb = Factory::CreateIWorkbook(samplePath);

//Access first worksheet

intrusive_ptr<IWorksheet> ws = wb->GetIWorksheets()->GetObjectByIndex(0);

//Add table i.e. list object

int idx = ws->GetIListObjects()->Add(new String("A1"), new String("H10"), true);

//Access the newly added list object

intrusive_ptr<IListObject> lo = ws->GetIListObjects()->GetObjectByIndex(idx);

//Make use of its display methods

lo->SetShowHeaderRow(true);

lo->SetShowTableStyleColumnStripes(true);

lo->SetShowTotals(true);

//Set its style

lo->SetTableStyleType(TableStyleType_TableStyleLight12);

//Set total functions of 3rd, 4th and 5th columns

lo->GetIListColumns()->GetObjectByIndex(2)->SetTotalsCalculation(TotalsCalculation_Min);

lo->GetIListColumns()->GetObjectByIndex(3)->SetTotalsCalculation(TotalsCalculation_Max);

lo->GetIListColumns()->GetObjectByIndex(4)->SetTotalsCalculation(TotalsCalculation_Count);

//Save the output excel file

wb->Save(outputPath);

{{< /highlight >}}
### **الدعم لتجميع الصفوف والأعمدة**
يمكن استخدام واجهات برمجة التطبيقات (APIs) لـ Aspose.Cells for C++ لتجميع الصفوف والأعمدة باستخدام فئة ICells والتي تمثل في الأساس مجموعة جميع الخلايا في الورقة العمل المعطاة. تقدم فئة ICells طرق GroupRows وGroupColumns من أجل [تجميع الصفوف والأعمدة](/cells/ar/cpp/group-rows-and-columns-of-worksheet/) على التوالي.

الكود المقتطف التالي يوضح سيناريو الاستخدام البسيط لكل من الطرق المذكورة سابقًا.

**C++**

{{< highlight csharp >}}

 //Create an empty workbook

intrusive_ptr wb = Factory::CreateIWorkbook();

//Add worksheet for grouping rows

intrusive_ptr grpRows = wb->GetIWorksheets()->GetObjectByIndex(0);

grpRows->SetName(new String("GroupRows"));

//Add worksheet for grouping columns

int idx = wb->GetIWorksheets()->Add();

intrusive_ptr grpCols = wb->GetIWorksheets()->GetObjectByIndex(idx);

grpCols->SetName(new String("GroupColumns"));

//Add sample values in both worksheets

for (int i = 0; i<50; i++)

{

	intrusive_ptr str = new String("Text");

	grpRows->GetICells()->GetObjectByIndex(i, 0)->PutValue(str);

	grpCols->GetICells()->GetObjectByIndex(0, i)->PutValue(str);

}

//Grouping rows at first level

grpRows->GetICells()->GroupRows(0, 10);

grpRows->GetICells()->GroupRows(12, 22);

grpRows->GetICells()->GroupRows(24, 34);

//Grouping rows at second level

grpRows->GetICells()->GroupRows(2, 8);

grpRows->GetICells()->GroupRows(14, 20);

grpRows->GetICells()->GroupRows(28, 30);

//Grouping rows at third level

grpRows->GetICells()->GroupRows(5, 7);

//Grouping columns at first level

grpCols->GetICells()->GroupColumns(0, 10);

grpCols->GetICells()->GroupColumns(12, 22);

grpCols->GetICells()->GroupColumns(24, 34);

//Grouping columns at second level

grpCols->GetICells()->GroupColumns(2, 8);

grpCols->GetICells()->GroupColumns(14, 20);

grpCols->GetICells()->GroupColumns(28, 30);

//Grouping columns at third level

grpCols->GetICells()->GroupColumns(5, 7);

//Save the output excel file

wb->Save(outputPath);

{{< /highlight >}}
### **الدعم للسمات**
تدعم الآن واجهات برمجة التطبيقات برقم Aspose.Cells for C++ استخدام وتلاعب السمات المقدمة من تطبيق Excel.
#### **القدرة على تطبيق ألوان السمة المخصصة**
يحاول المقتطف التالي [إنشاء سمة جديدة بألوان مخصصة](/cells/ar/cpp/apply-custom-theme-colors-of-the-workbook-using-array-of-colors/) لدفتر العمل.

**C++**

{{< highlight csharp >}}

 //Create a workbook

intrusive_ptr<IWorkbook> wb = Factory::CreateIWorkbook();

//Create array of custom theme colors

intrusive_ptr<Array1D<Color*>> clrs = new Array1D<Color*>(12);

//Background1

clrs->SetValue(Color::GetRed(), 0);

//Text1

clrs->SetValue(Color::GetRed(), 1);

//Background2

clrs->SetValue(Color::GetRed(), 2);

//Text2

clrs->SetValue(Color::GetRed(), 3);

//Accent1

clrs->SetValue(Color::GetRed(), 4);

//Accent2

clrs->SetValue(Color::GetGreen(), 5);

//Accent3

clrs->SetValue(Color::GetGreen(), 6);

//Accent4

clrs->SetValue(Color::GetGreen(), 7);

//Accent5

clrs->SetValue(Color::GetGreen(), 8);

//Accent6

clrs->SetValue(Color::GetBlue(), 9);

//Hyperlink

clrs->SetValue(Color::GetBlue(), 10);

//Followed Hyperlink

clrs->SetValue(Color::GetBlue(), 11);

//Apply custom theme colors on workbook

wb->CustomTheme(new String("AnyTheme"), clrs);

//Save the workbook

wb->Save(outputPath);

{{< /highlight >}}
#### **دعم تلاعب ألوان السمة**
يعرض الكود النموذجي التالي كيفية [قراءة وتعديل ألوان السمة لدفتر العمل](/cells/ar/cpp/apply-custom-theme-colors-of-the-workbook-using-array-of-colors/). يحمل الكود النموذجي جدول بيانات موجودًا، يقرأ ألوان السمة الخاصة به وهي Accent1-Accent6، ويعدل الألوان قبل حفظ جدول البيانات.

**C++**

{{< highlight csharp >}}

 //Load the sample excel file

intrusive_ptr<IWorkbook> wb = Factory::CreateIWorkbook(samplePath);

//Read these theme colors i.e. Accent1 till Accent6

intrusive_ptr<Color> clr_Accent1 = wb->GetThemeColor(ThemeColorType_Accent1);

intrusive_ptr<Color> clr_Accent2 = wb->GetThemeColor(ThemeColorType_Accent2);

intrusive_ptr<Color> clr_Accent3 = wb->GetThemeColor(ThemeColorType_Accent3);

intrusive_ptr<Color> clr_Accent4 = wb->GetThemeColor(ThemeColorType_Accent4);

intrusive_ptr<Color> clr_Accent5 = wb->GetThemeColor(ThemeColorType_Accent5);

intrusive_ptr<Color> clr_Accent6 = wb->GetThemeColor(ThemeColorType_Accent6);

//Print all of them. ffff00 means Yellow

printf("Accent1: %x\r\n", clr_Accent1->ToArgb());

printf("Accent2: %x\r\n", clr_Accent2->ToArgb());

printf("Accent3: %x\r\n", clr_Accent3->ToArgb());

printf("Accent4: %x\r\n", clr_Accent4->ToArgb());

printf("Accent5: %x\r\n", clr_Accent5->ToArgb());

printf("Accent6: %x\r\n", clr_Accent6->ToArgb());

//Set all of them to Red

wb->SetThemeColor(ThemeColorType_Accent1, Color::GetRed());

wb->SetThemeColor(ThemeColorType_Accent2, Color::GetRed());

wb->SetThemeColor(ThemeColorType_Accent3, Color::GetRed());

wb->SetThemeColor(ThemeColorType_Accent4, Color::GetRed());

wb->SetThemeColor(ThemeColorType_Accent5, Color::GetRed());

wb->SetThemeColor(ThemeColorType_Accent6, Color::GetRed());

//Reading one of them after modifying, it will be ff0000 which means Red

printf("\r\nReading one of them after modifying, it will be ff0000 which means Red\r\n\r\n");

clr_Accent6 = wb->GetThemeColor(ThemeColorType_Accent6);

printf("Accent6: %x\r\n", (clr_Accent6->ToArgb())&0xffffff);

//Save the output excel file

wb->Save(outputPath);

{{< /highlight >}}
#### **القدرة على نسخ السمات عبر دفاتر العمل**
يعرض الكود النموذجي التالي كيفية [نسخ السمة من دفتر عمل إلى آخر](/cells/ar/cpp/copy-theme-from-one-workbook-to-another/)، مما يمكن أن يكون مفيدًا في تطبيق السمات المضمنة أو المخصصة على جداول بيانات متعددة.

**C++**

{{< highlight csharp >}}

 //Read excel file that has Damask theme applied on it

intrusive_ptr<IWorkbook> damask = Factory::CreateIWorkbook(damaskPath);

//Read your sample excel file

intrusive_ptr<IWorkbook> wb = Factory::CreateIWorkbook(samplePath);

//Copy theme from source file

wb->CopyTheme(damask);

//Save the workbook in xlsx format

wb->Save(outputPath, SaveFormat_Xlsx);

{{< /highlight >}}
## **تغيير أسماء الواجهات البرمجية**
مع إصدار 16.12.0 من Aspose.Cells for C++، لقد قمنا بإعادة تسمية بعض الأساليب للحفاظ على توحيد الواجهات. قائمة جميع واجهات برمجة التطبيقات المعاد تسميتها هي كالتالي.
#### **إعادة تسمية طريقة ICell::SetStyle إلى ICell::SetIStyle**
#### **إعادة تسمية طريقة ICell::SetCharacters إلى ICell::SetIFontSettings**
#### **إعادة تسمية طريقة ICellsColor::SetThemeColor إلى ICellsColor::SetIThemeColor**
#### **إعادة تسمية طريقة ICells::SetStyle إلى ICells::SetIStyle**
#### **إعادة تسمية طريقة ICellsHelper::GetDPI_i إلى ICellsHelper::GetDPI**
#### **إعادة تسمية طريقة ICellsHelper::SetDPI_i إلى ICellsHelper::SetDPI**
#### **إعادة تسمية طريقة ICellsHelper::GetVersion_i إلى ICellsHelper::GetVersion**
#### **قم بإعادة تسمية طريقة ICellsHelper::IsProtectedByRMS_i إلى ICellsHelper::IsProtectedByRMS**
#### **قم بإعادة تسمية طريقة ICellsHelper::IsProtectedByRMS_i إلى ICellsHelper::IsProtectedByRMS**
#### **قم بإعادة تسمية طريقة ICellsHelper::CellNameToIndex_i إلى ICellsHelper::CellNameToIndex**
#### **قم بإعادة تسمية طريقة ICellsHelper::CellIndexToName_i إلى ICellsHelper::CellIndexToName**
#### **قم بإعادة تسمية طريقة ICellsHelper::ColumnIndexToName_i إلى ICellsHelper::ColumnIndexToName**
#### **قم بإعادة تسمية طريقة ICellsHelper::ColumnNameToIndex_i إلى ICellsHelper::ColumnNameToIndex**
#### **قم بإعادة تسمية طريقة ICellsHelper::RowIndexToName_i إلى ICellsHelper::RowIndexToName**
#### **قم بإعادة تسمية طريقة ICellsHelper::RowNameToIndex_i إلى ICellsHelper::RowNameToIndex**
#### **قم بإعادة تسمية طريقة ICellsHelper::ConvertR1C1FormulaToA1_i إلى ICellsHelper::ConvertR1C1FormulaToA1**
#### **قم بإعادة تسمية طريقة ICellsHelper::ConvertA1FormulaToR1C1_i إلى ICellsHelper::ConvertA1FormulaToR1C1**
#### **قم بإعادة تسمية طريقة ICellsHelper::GetDateTimeFromDouble_i إلى ICellsHelper::GetDateTimeFromDouble**
#### **قم بإعادة تسمية طريقة ICellsHelper::GetDoubleFromDateTime_i إلى ICellsHelper::GetDoubleFromDateTime**
#### **قم بإعادة تسمية طريقة ICellsHelper::DetectLoadFormat_i إلى ICellsHelper::DetectLoadFormat**
#### **قم بإعادة تسمية طريقة ICellsHelper::DetectFileFormat_i إلى ICellsHelper::DetectFileFormat**
#### **قم بإعادة تسمية طريقة ICellsHelper::GetFontDir_i إلى ICellsHelper::GetFontDir**
#### **قم بإعادة تسمية طريقة ICellsHelper::SetFontDir_i إلى ICellsHelper::SetFontDir**
#### **قم بإعادة تسمية طريقة ICellsHelper::GetFontDirs_i إلى ICellsHelper::GetFontDirs**
#### **قم بإعادة تسمية طريقة ICellsHelper::SetFontDirs_i إلى ICellsHelper::SetFontDirs**
#### **قم بإعادة تسمية طريقة ICellsHelper::GetFontFiles_i إلى ICellsHelper::GetFontFiles**
#### **قم بإعادة تسمية طريقة ICellsHelper::SetFontFiles_i إلى ICellsHelper::SetFontFiles**
#### **قم بإعادة تسمية طريقة ICellsHelper::GetStartupPath_i إلى ICellsHelper::GetStartupPath**
#### **قام بتغيير اسم طريقة ICellsHelper::SetStartupPath_i إلى ICellsHelper::SetStartupPath**
#### **قام بتغيير اسم طريقة ICellsHelper::GetAltStartPath_i إلى ICellsHelper::GetAltStartPath**
#### **قام بتغيير اسم طريقة ICellsHelper::SetAltStartPath_i إلى ICellsHelper::SetAltStartPath**
#### **قام بتغيير اسم طريقة ICellsHelper::GetLibraryPath_i إلى ICellsHelper::GetLibraryPath**
#### **قام بتغيير اسم طريقة ICellsHelper::SetLibraryPath_i إلى ICellsHelper::SetLibraryPath**
#### **قام بتغيير اسم طريقة ICellsHelper::GetUsedColors_i إلى ICellsHelper::GetUsedColors**
#### **قام بتغيير اسم طريقة ICellsHelper::AddAddInFunction_i إلى ICellsHelper::AddAddInFunction**
#### **قام بتغيير اسم طريقة ICellsHelper::MergeFiles_i إلى ICellsHelper::MergeFiles**
#### **قام بتغيير اسم طريقة IColumnCollection::GetByIndex_i إلى IColumnCollection::GetIColumn**
#### **قام بتغيير اسم طريقة IFileFormatUtil::DetectFileFormat_i إلى IFileFormatUtil::DetectFileFormat**
#### **قام بتغيير اسم طريقة IFileFormatUtil::ExtensionToSaveFormat_i إلى IFileFormatUtil::ExtensionToSaveFormat**
#### **قام بتغيير اسم طريقة IFileFormatUtil::IsTemplateFormat_i إلى IFileFormatUtil::IsTemplateFormat**
#### **قام بتغيير اسم طريقة IFileFormatUtil::LoadFormatToExtension_i إلى IFileFormatUtil::LoadFormatToExtension**
#### **قام بتغيير اسم طريقة IFileFormatUtil::LoadFormatToSaveFormat_i إلى IFileFormatUtil::LoadFormatToSaveFormat**
#### **قام بتغيير اسم طريقة IFileFormatUtil::SaveFormatToExtension_i إلى IFileFormatUtil::SaveFormatToExtension**
#### **قام بتغيير اسم طريقة IFileFormatUtil::SaveFormatToLoadFormat_i إلى IFileFormatUtil::SaveFormatToLoadFormat**
#### **قام بتغيير اسم طريقة IRange::SetStyle إلى IRange::SetIStyle**
#### **قام بتغيير اسم طريقة IFindOptions::SetRange إلى IFindOptions::SetIRange**
#### **قام بتغيير اسم طريقة ILoadOptions::SetLoadDataOptions إلى ILoadOptions::SetILoadDataOptions**
#### **قام بتغيير اسم طريقة IWorkbook::SetSettings إلى IWorkbook::SetISettings**
#### **تمت إعادة تسمية الطريقة IWorkbook::SetDefaultStyle إلى IWorkbook::SetDefaultIStyle**
{{< app/cells/assistant language="cpp" >}}
