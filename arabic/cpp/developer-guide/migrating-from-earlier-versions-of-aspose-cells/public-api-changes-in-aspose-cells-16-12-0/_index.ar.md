---
title: عام API تغييرات في Aspose.Cells 16.12.0
type: docs
weight: 10
url: /ar/cpp/public-api-changes-in-aspose-cells-16-12-0/
---
{{% alert color="primary" %}} 

يصف هذا المستند التغييرات التي تم إجراؤها على Aspose.Cells API من الإصدار 16.11.0 إلى 16.12.0 والتي قد تهم مطوري الوحدة / التطبيق. لا يشمل فقط الأساليب العامة الجديدة والمحدثة ، والفئات المضافة والمحذوفة وما إلى ذلك ، بل يشمل أيضًا وصفًا لأي تغييرات في السلوك خلف الكواليس في Aspose.Cells.

{{% /alert %}} 
## **تمت إضافة واجهات برمجة التطبيقات**
### **دعم الجداول المحورية**
يدعم الإصدار الثاني من Aspose.Cells لـ C++ الإنشاء بالإضافة إلى معالجة الجداول المحورية. يوفر Aspose.Cells لـ C++ فئة IPivotTable التي تمثل كائن Pivot Table بينما تمثل IPivotTableCollection مجموعة من الجداول المحورية. يمكن الوصول إلى IPivotTableCollection عبر كائن IWorksheet ويمكن إضافة جدول Pivot Table جديد إلى المجموعة أثناء استخدام أسلوب IPivotTableCollection.Add.

 يوضح مقتطف الشفرة التالي مدى سهولة استخدام Aspose.Cells لـ C++ API[إنشاء جداول محورية من البداية](/cells/ar/cpp/create-pivot-table/).

**C++**

{{< highlight "csharp" >}}

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

إلى جانب إنشاء جداول محورية جديدة ، تدعم Aspose.Cells لواجهات برمجة التطبيقات C++ أيضًا معالجة الجداول المحورية الموجودة. يدعم API حاليًا تغيير البيانات في النطاق المصدر للجدول المحوري ثم تحديثه. بمجرد معالجة Pivot Table كما هو مطلوب ، من الأفضل استخدام أساليب IPivotTable.RefreshData و IPivotTable.CalculateData لتحديث Pivot Table مقابل مصدر البيانات المحدث.

 يستخدم مقتطف الكود التالي Aspose.Cells لـ C++ API إلى[معالجة جدول محوري موجود](/cells/ar/cpp/manipulate-pivot-table/).

**C++**

{{< highlight "csharp" >}}

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
### **دعم قواعد التنسيق الشرطي**
 يوفر Aspose.Cells لـ C++ الآن إمكانية إضافة قواعد التنسيق الشرطي إلى ورقة العمل عن طريق عرض فئة IFormatCondition. توفر الفئة المذكورة أعلاه كذلك الطرق التالية لـ[تطبيق قواعد التنسيق الشرطي](/cells/ar/cpp/apply-conditional-formatting-in-worksheet/) حسب متطلبات التطبيق.

- IFormatCondition.GetIAboveAverage
- IFormatCondition.GetIColorScale
- IFormatCondition.GetIDataBar
- IFormatCondition.GetIIconSet
- IFormatCondition.GetITop10

يوضح نموذج التعليمات البرمجية التالي كيفية إضافة قاعدة تنسيق شرطي من النوع Cell القيمة على الخلايا A1 و B2.

**C++**

{{< highlight "csharp" >}}

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
### **دعم الارتباطات التشعبية**
 Aspose.Cells لـ C++ يدعم الآن[إضافة ارتباطات تشعبية إلى خلايا ورقة العمل](/cells/ar/cpp/add-hyperlinks-to-the-cells/). من أجل توفير هذه الميزة ، كشف Aspose.Cells لـ C++ 16.12.0 فئة IHyperlinkCollection التي يمكن الوصول إليها عبر كائن IWorksheet بينما يمكن إضافة ارتباط تشعبي إلى المجموعة أثناء استخدام طريقة IHyperlinkCollection.Add كما هو موضح أدناه.

**C++**

{{< highlight "csharp" >}}

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
يدعم تطبيق Excel نوعين من خصائص المستند كما هو موضح أدناه.

- الخصائص المحددة من قبل النظام (المضمنة): تحتوي الخصائص المضمنة على معلومات عامة حول المستند مثل عنوان المستند واسم المؤلف وإحصائيات المستند وما إلى ذلك.
- الخصائص المعرفة من قبل المستخدم (المخصصة): الخصائص المخصصة التي يحددها المستخدم النهائي في شكل زوج قيمة الاسم.

Aspose.Cells لدعم C++[إدارة كلا النوعين من خصائص المستندات المضمنة والمخصصة](/cells/ar/cpp/managing-document-properties/). Aspose.Cells 'فئة IWorkbook تمثل ملف Excel. من أجل الوصول إلى خصائص المستند المضمنة ، استخدم IWorkbook.GetBuiltInDocumentProperties بينما يمكن الوصول إلى خصائص المستند المخصصة أثناء استخدام أسلوب IWorkbook.GetCustomDocumentProperties.

يقوم نموذج التعليمات البرمجية التالي بتحميل نموذج جدول بيانات موجود ويقرأ خصائص المستند المضمنة مثل العنوان والموضوع والخصائص المخصصة حسب الاسم MyCustom1.

**C++**

{{< highlight "csharp" >}}

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
### **دعم ListObjects**
 جدول Excel هو مصفوفة من الخلايا تحتوي على أي عدد من الصفوف والأعمدة بينما يشار إلى نفس الجدول على أنه كائن قائمة في Aspose.Cells لواجهات برمجة التطبيقات C++. تحتوي مساحة الاسم Aspose :: Cells :: Tables على كافة الفئات الضرورية التي تتعامل مع العمليات المتعلقة بكائنات القائمة. أكثر الفئات الجديرة بالذكر هي IListObject و IListObjectCollection التي تسمح بذلك[إنشاء وتنسيق قائمة كائنات](/cells/ar/cpp/create-and-format-table/) وهلم جرا.

يقوم نموذج التعليمات البرمجية التالي بتحميل نموذج ملف جدول البيانات ثم يقوم بإنشاء "كائن قائمة" (جدول) في نطاق A1: H10 ، ثم استخدم طرقه المختلفة لإظهار الإجمالي الفرعي.

**C++**

{{< highlight "csharp" >}}

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
### **دعم تجميع الصف والعمود**
 يمكن استخدام Aspose.Cells لـ C++ API لتجميع الصفوف والأعمدة أثناء استخدام فئة ICells والتي تمثل أساسًا مجموعة كل الخلايا في ورقة عمل معينة. تقدم فئة ICells أساليب GroupRows و GroupColumns من أجل[مجموعة الصفوف والأعمدة](/cells/ar/cpp/group-rows-and-columns-of-worksheet/) على التوالى.

يوضح مقتطف الشفرة التالي سيناريو الاستخدام البسيط للطريقتين المذكورتين أعلاه.

**C++**

{{< highlight "csharp" >}}

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
### **دعم الثيمات**
Aspose.Cells لـ C++ APIs تدعم الآن استخدام ومعالجة السمات التي يقدمها تطبيق Excel.
#### **القدرة على تطبيق ألوان السمة المخصصة**
 يحاول المقتطف التالي[قم بإنشاء نسق جديد بألوان مخصصة](/cells/ar/cpp/apply-custom-theme-colors-of-the-workbook-using-array-of-colors/) للمصنف.

**C++**

{{< highlight "csharp" >}}

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
#### **دعم معالجة ألوان النسق**
يوضح نموذج التعليمات البرمجية التالي كيفية[قراءة وتعديل ألوان نسق المصنف](/cells/ar/cpp/apply-custom-theme-colors-of-the-workbook-using-array-of-colors/). يقوم نموذج التعليمات البرمجية بتحميل جدول بيانات موجود ، وقراءة ألوان السمات الخاصة به ، مثل Accent1-Accent6 ، وتعديل الألوان قبل حفظ جدول البيانات.

**C++**

{{< highlight "csharp" >}}

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
#### **القدرة على نسخ المظاهر عبر المصنفات**
يوضح نموذج التعليمات البرمجية التالي كيفية[نسخ النسق من مصنف إلى آخر](/cells/ar/cpp/copy-theme-from-one-workbook-to-another/)، والتي يمكن أن تكون مفيدة في تطبيق سمات مضمنة أو مخصصة على جداول بيانات متعددة.

**C++**

{{< highlight "csharp" >}}

 //Read excel file that has Damask theme applied on it

intrusive_ptr<IWorkbook> damask = Factory::CreateIWorkbook(damaskPath);

//Read your sample excel file

intrusive_ptr<IWorkbook> wb = Factory::CreateIWorkbook(samplePath);

//Copy theme from source file

wb->CopyTheme(damask);

//Save the workbook in xlsx format

wb->Save(outputPath, SaveFormat_Xlsx);

{{< /highlight >}}
## **إعادة تسمية واجهات برمجة التطبيقات**
مع إصدار Aspose.Cells لـ C++ 16.12.0 ، قمنا بإعادة تسمية بعض الطرق من أجل الحفاظ على توحيد الواجهات. قائمة جميع واجهات برمجة التطبيقات المعاد تسميتها كما يلي.
#### **تمت إعادة تسمية طريقة ICell :: SetStyle إلى ICell :: SetIStyle**
#### **تمت إعادة تسمية طريقة ICell :: SetCharacters إلى ICell :: SetIFontSettings**
#### **تمت إعادة تسمية طريقة ICellsColor :: SetThemeColor إلى ICellsColor :: SetIThemeColor**
#### **تمت إعادة تسمية طريقة ICells :: SetStyle إلى ICells :: SetIStyle**
#### **تمت إعادة تسمية طريقة ICellsHelper :: GetDPI_i إلى ICellsHelper :: GetDPI**
#### **تمت إعادة تسمية طريقة ICellsHelper :: SetDPI_i إلى ICellsHelper :: SetDPI**
#### **تمت إعادة تسمية طريقة ICellsHelper :: GetVersion_i إلى ICellsHelper :: GetVersion**
#### **تمت إعادة تسمية طريقة ICellsHelper :: IsProtectedByRMS_i إلى ICellsHelper :: IsProtectedByRMS**
#### **تمت إعادة تسمية طريقة ICellsHelper :: IsProtectedByRMS_i إلى ICellsHelper :: IsProtectedByRMS**
#### **تمت إعادة تسمية طريقة ICellsHelper :: CellNameToIndex_i إلى طريقة ICellsHelper :: CellNameToIndex**
#### **تمت إعادة تسمية طريقة ICellsHelper :: CellIndexToName_i إلى طريقة ICellsHelper :: CellIndexToName**
#### **تمت إعادة تسمية طريقة ICellsHelper :: ColumnIndexToName_i إلى طريقة ICellsHelper :: ColumnIndexToName**
#### **تمت إعادة تسمية طريقة ICellsHelper :: ColumnNameToIndex_i إلى طريقة ICellsHelper :: ColumnNameToIndex**
#### **تمت إعادة تسمية طريقة ICellsHelper :: RowIndexToName_i إلى طريقة ICellsHelper :: RowIndexToName**
#### **تمت إعادة تسمية طريقة ICellsHelper :: RowNameToIndex_i إلى طريقة ICellsHelper :: RowNameToIndex**
#### **تمت إعادة تسمية ICellsHelper :: ConvertR1C1FormulaToA1_i طريقة إلى ICellsHelper :: ConvertR1C1FormulaToA1**
#### **تمت إعادة تسمية ICellsHelper :: ConvertA1FormulaToR1C1_i طريقة إلى ICellsHelper :: ConvertA1FormulaToR1C1**
#### **تمت إعادة تسمية طريقة ICellsHelper :: GetDateTimeFromDouble_i إلى طريقة ICellsHelper :: GetDateTimeFromDouble**
#### **تمت إعادة تسمية طريقة ICellsHelper :: GetDoubleFromDateTime_i إلى طريقة ICellsHelper :: GetDoubleFromDateTime**
#### **تمت إعادة تسمية طريقة ICellsHelper :: DetectLoadFormat_i إلى ICellsHelper :: DetectLoadFormat**
#### **تمت إعادة تسمية طريقة ICellsHelper :: DetectFileFormat_i إلى ICellsHelper :: DetectFileFormat**
#### **تمت إعادة تسمية طريقة ICellsHelper :: GetFontDir_i إلى ICellsHelper :: GetFontDir**
#### **تمت إعادة تسمية طريقة ICellsHelper :: SetFontDir_i إلى ICellsHelper :: SetFontDir**
#### **تمت إعادة تسمية طريقة ICellsHelper :: GetFontDirs_i إلى ICellsHelper :: GetFontDirs**
#### **تمت إعادة تسمية طريقة ICellsHelper :: SetFontDirs_i إلى ICellsHelper :: SetFontDirs**
#### **تمت إعادة تسمية طريقة ICellsHelper :: GetFontFiles_i إلى ICellsHelper :: GetFontFiles**
#### **تمت إعادة تسمية طريقة ICellsHelper :: SetFontFiles_i إلى ICellsHelper :: SetFontFiles**
#### **تمت إعادة تسمية طريقة ICellsHelper :: GetStartupPath_i إلى ICellsHelper :: GetStartupPath**
#### **تمت إعادة تسمية طريقة ICellsHelper :: SetStartupPath_i إلى ICellsHelper :: SetStartupPath**
#### **تمت إعادة تسمية طريقة ICellsHelper :: GetAltStartPath_i إلى ICellsHelper :: GetAltStartPath**
#### **تمت إعادة تسمية طريقة ICellsHelper :: SetAltStartPath_i إلى ICellsHelper :: SetAltStartPath**
#### **تمت إعادة تسمية طريقة ICellsHelper :: GetLibraryPath_i إلى ICellsHelper :: GetLibraryPath**
#### **تمت إعادة تسمية طريقة ICellsHelper :: SetLibraryPath_i إلى ICellsHelper :: SetLibraryPath**
#### **تمت إعادة تسمية طريقة ICellsHelper :: GetUsedColors_i إلى ICellsHelper :: GetUsedColors**
#### **تمت إعادة تسمية طريقة ICellsHelper :: AddAddInFunction_i إلى ICellsHelper :: AddAddInFunction**
#### **تمت إعادة تسمية طريقة ICellsHelper :: MergeFiles_i إلى ICellsHelper :: MergeFiles**
#### **تمت إعادة تسمية طريقة IColumnCollection :: GetByIndex_i إلى IColumnCollection :: GetIColumn**
#### **تمت إعادة تسمية طريقة IFileFormatUtil :: DetectFileFormat_i إلى IFileFormatUtil :: DetectFileFormat**
#### **تمت إعادة تسمية IFileFormatUtil :: ExtensionToSaveFormat_i طريقة IFileFormatUtil :: ExtensionToSaveFormat**
#### **تمت إعادة تسمية طريقة IFileFormatUtil :: IsTemplateFormat_i إلى IFileFormatUtil :: IsTemplateFormat**
#### **تمت إعادة تسمية أسلوب IFileFormatUtil :: LoadFormatToExtension_i إلى IFileFormatUtil :: LoadFormatToExtension**
#### **تمت إعادة تسمية أسلوب IFileFormatUtil :: LoadFormatToSaveFormat_i إلى IFileFormatUtil :: LoadFormatToSaveFormat**
#### **تمت إعادة تسمية طريقة IFileFormatUtil :: SaveFormatToExtension_i إلى IFileFormatUtil :: SaveFormatToExtension**
#### **تمت إعادة تسمية طريقة IFileFormatUtil :: SaveFormatToLoadFormat_i إلى IFileFormatUtil :: SaveFormatToLoadFormat**
#### **تمت إعادة تسمية طريقة IRange :: SetStyle إلى IRange :: SetIStyle**
#### **تمت إعادة تسمية طريقة IFindOptions :: SetRange إلى IFindOptions :: SetIRange**
#### **تمت إعادة تسمية طريقة ILoadOptions :: SetLoadDataOptions إلى ILoadOptions :: SetILoadDataOptions**
#### **تمت إعادة تسمية طريقة IWorkbook :: SetSettings إلى IWorkbook :: SetISettings**
#### **تمت إعادة تسمية طريقة IWorkbook :: SetDefaultStyle إلى IWorkbook :: SetDefaultIStyle**
