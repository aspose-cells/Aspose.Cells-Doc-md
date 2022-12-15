---
title: Genel API Aspose.Cells 16.12.0'daki değişiklikler
type: docs
weight: 10
url: /tr/cpp/public-api-changes-in-aspose-cells-16-12-0/
---
{{% alert color="primary" %}} 

Bu belge, modül/uygulama geliştiricilerinin ilgisini çekebilecek 16.11.0 sürümünden 16.12.0 sürümüne Aspose.Cells API değişikliklerini açıklamaktadır. Yalnızca yeni ve güncellenmiş genel yöntemleri, eklenen ve kaldırılan sınıfları vb. değil, aynı zamanda Aspose.Cells'deki perde arkasındaki davranış değişikliklerinin açıklamasını da içerir.

{{% /alert %}} 
## **Eklenen API'ler**
### **Pivot Tablolar için Destek**
Aspose.Cells for C++'in ikinci sürümü, Pivot Tabloların oluşturulmasını ve değiştirilmesini destekler. Aspose.Cells for C++, bir Pivot Tablo nesnesini temsil eden IPivotTable sınıfını sağlarken IPivotTableCollection, bir Pivot Tablo koleksiyonunu temsil eder. IPivotTableCollection'a IWorksheet nesnesi aracılığıyla erişilebilir ve IPivotTableCollection.Add yöntemi kullanılırken koleksiyona yeni bir Pivot Tablo eklenebilir.

 Aşağıdaki kod parçacığı, Aspose.Cells for C++ API'i kullanmanın ne kadar basit olduğunu gösterir.[sıfırdan Pivot Tablolar oluşturun](/cells/tr/cpp/create-pivot-table/).

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

Aspose.Cells for C++ API'leri, yeni Pivot Tablolar oluşturmanın yanı sıra mevcut Pivot Tabloları değiştirmeyi de destekler. API şu anda Pivot Tablonun kaynak aralığındaki verileri değiştirmeyi ve ardından yenilemeyi desteklemektedir. Pivot Tablo istendiği gibi değiştirildikten sonra, Pivot Tabloyu güncellenmiş veri kaynağına göre yenilemek için IPivotTable.RefreshData ve IPivotTable.CalculateData yöntemlerini kullanmak en iyisidir.

Aşağıdaki kod parçacığı, Aspose.Cells for C++ API'i kullanır.[mevcut bir Pivot Tabloyu manipüle etme](/cells/tr/cpp/manipulate-pivot-table/).

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
### **Koşullu Biçimlendirme Kuralları Desteği**
 Aspose.Cells for C++ artık IFormatCondition sınıfını göstererek çalışma sayfasına koşullu biçimlendirme kuralları ekleme yeteneği sağlıyor. Yukarıda belirtilen sınıf ayrıca aşağıdaki yöntemleri sağlar:[koşullu biçimlendirme kurallarını uygula](/cells/tr/cpp/apply-conditional-formatting-in-worksheet/) uygulama gereksinimlerine göre.

- IFormatCondition.GetIAboveAverage
- IFormatCondition.GetIColorScale
- IFormatCondition.GetIDataBar
- IFormatCondition.GetIIconSet
- IFormatCondition.GetITop10

Aşağıdaki örnek kod, A1 ve B2 hücrelerinde Cell Değer türünde bir koşullu biçimlendirme kuralının nasıl ekleneceğini gösterir.

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
### **Köprüler için Destek**
 Aspose.Cells for C++ şimdi destekliyor[çalışma sayfası hücrelerine köprüler ekleme](/cells/tr/cpp/add-hyperlinks-to-the-cells/)Bu özelliği sağlamak için, Aspose.Cells for C++ 16.12.0, IWorksheet nesnesi aracılığıyla erişilebilen IHyperlinkCollection sınıfını kullanıma sunmuştur, ancak aşağıda gösterildiği gibi IHyperlinkCollection.Add yöntemi kullanılırken koleksiyona bir hiper bağlantı eklenebilir.

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
### **Belge Özellikleri Desteği**
Excel uygulaması, aşağıda listelenen 2 tür belge özelliğini destekler.

- Sistem tanımlı (yerleşik) özellikler: Yerleşik özellikler, belge hakkında belge başlığı, yazar adı, belge istatistikleri vb. gibi genel bilgileri içerir.
- Kullanıcı tanımlı (özel) özellikler: Son kullanıcı tarafından ad değer çifti şeklinde tanımlanan özel özellikler.

 Aspose.Cells for C++ destekler[Yerleşik ve özel olmak üzere her iki belge özelliğini yönetme](/cells/tr/cpp/managing-document-properties/)Aspose.Cells' IWorkbook sınıfı bir Excel dosyasını temsil eder. Yerleşik belge özelliklerine erişmek için IWorkbook.GetBuiltInDocumentProperties kullanın, özel belge özelliklerine ise IWorkbook.GetCustomDocumentProperties yöntemi kullanılırken erişilebilir.

Aşağıdaki örnek kod, varolan bir örnek elektronik tabloyu yükler ve MyCustom1 adıyla Başlık, Konu ve özel özellik gibi yerleşik belge özelliklerini okur.

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
### **ListObjects için destek**
 Bir Excel tablosu, herhangi bir sayıda satır ve sütun içeren bir hücre matrisidir, oysa aynı tablo, Aspose.Cells for C++ API'lerinde Liste Nesnesi olarak anılır. Aspose::Cells::Tables ad alanı, Liste Nesneleriyle ilgili işlemlerle ilgilenen tüm gerekli sınıfları içerir. En çok bahsetmeye değer sınıflar, izin veren IListObject ve IListObjectCollection'dır.[Liste Nesneleri oluşturma ve biçimlendirme](/cells/tr/cpp/create-and-format-table/) ve benzeri.

Aşağıdaki örnek kod, örnek elektronik tablo dosyasını yükler ve ardından A1:H10 aralığında bir Liste Nesnesi (tablo) oluşturur, ardından alt toplamı göstermek için bunun çeşitli yöntemlerinden yararlanır.

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
### **Satır ve Sütun Gruplandırma Desteği**
 Aspose.Cells for C++ API, temel olarak belirli bir çalışma sayfasındaki tüm hücrelerin toplanması olan ICells sınıfını kullanırken satırları ve sütunları gruplandırmak için kullanılabilir. ICells sınıfı, GroupRows ve GroupColumns yöntemlerini sunar.[grup satırları ve sütunları](/cells/tr/cpp/group-rows-and-columns-of-worksheet/) sırasıyla.

Aşağıdaki kod parçacığı, yukarıda belirtilen her iki yöntemin de basit kullanım senaryosunu göstermektedir.

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
### **Tema Desteği**
Aspose.Cells for C++ API'ler artık Excel uygulamasının sunduğu temaları kullanmayı ve değiştirmeyi destekliyor.
#### **Özel Tema Renklerini Uygulama Yeteneği**
 Aşağıdaki parçacığı çalışır[özel renklerle yeni bir tema oluşturun](/cells/tr/cpp/apply-custom-theme-colors-of-the-workbook-using-array-of-colors/) çalışma kitabı için.

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
#### **Tema Renklerinin Manipülasyonu İçin Destek**
 Aşağıdaki örnek kod, nasıl yapılacağını gösterir[çalışma kitabının tema renklerini okuma ve değiştirme](/cells/tr/cpp/apply-custom-theme-colors-of-the-workbook-using-array-of-colors/). Örnek kod, mevcut bir elektronik tabloyu yükler, tema renklerini okur, yani Accent1-Accent6 ve elektronik tabloyu kaydetmeden önce renkleri değiştirir.

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
#### **Çalışma Kitapları Arasında Tema Kopyalama Yeteneği**
 Aşağıdaki örnek kod, nasıl yapılacağını gösterir[temayı bir çalışma kitabından diğerine kopyala](/cells/tr/cpp/copy-theme-from-one-workbook-to-another/)Bu, birden çok e-tabloya yerleşik veya özel temalar uygularken yararlı olabilir.

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
## **Yeniden adlandırılan API'ler**
Aspose.Cells for C++ 16.12.0 sürümüyle, arayüzleri bir arada tutmak için birkaç yöntemi yeniden adlandırdık. Yeniden adlandırılan tüm API'lerin listesi aşağıdaki gibidir.
#### **ICell::SetStyle yöntemi ICell::SetIStyle olarak yeniden adlandırıldı**
#### **ICell::SetCharacters yöntemi ICell::SetIFontSettings olarak yeniden adlandırıldı**
#### **ICellsColor::SetThemeColor yöntemi ICellsColor::SetIThemeColor olarak yeniden adlandırıldı**
#### **ICells::SetStyle yöntemi ICells::SetIStyle olarak yeniden adlandırıldı**
#### **ICellsHelper::GetDPI_i yöntemi ICellsHelper::GetDPI olarak yeniden adlandırıldı**
#### **ICellsHelper::SetDPI_i yöntemi ICellsHelper::SetDPI olarak yeniden adlandırıldı**
#### **ICellsHelper::GetVersion_i yöntemi ICellsHelper::GetVersion olarak yeniden adlandırıldı**
#### **ICellsHelper::IsProtectedByRMS_i yöntemi ICellsHelper::IsProtectedByRMS olarak yeniden adlandırıldı**
#### **ICellsHelper::IsProtectedByRMS_i yöntemi ICellsHelper::IsProtectedByRMS olarak yeniden adlandırıldı**
#### **ICellsHelper::CellNameToIndex_i yöntemi ICellsHelper::CellNameToIndex olarak yeniden adlandırıldı**
#### **ICellsHelper::CellIndexToName_i yöntemi ICellsHelper::CellIndexToName olarak yeniden adlandırıldı**
#### **ICellsHelper::ColumnIndexToName_i yöntemi ICellsHelper::ColumnIndexToName olarak yeniden adlandırıldı**
#### **ICellsHelper::ColumnNameToIndex_i yöntemi ICellsHelper::ColumnNameToIndex olarak yeniden adlandırıldı**
#### **ICellsHelper::RowIndexToName_i yöntemi ICellsHelper::RowIndexToName olarak yeniden adlandırıldı**
#### **ICellsHelper::RowNameToIndex_i yöntemi ICellsHelper::RowNameToIndex olarak yeniden adlandırıldı**
#### **ICellsHelper::ConvertR1C1FormulaToA1_i yöntemi ICellsHelper::ConvertR1C1FormulaToA1 olarak yeniden adlandırıldı**
#### **ICellsHelper::ConvertA1FormulaToR1C1_i yöntemi ICellsHelper::ConvertA1FormulaToR1C1 olarak yeniden adlandırıldı**
#### **ICellsHelper::GetDateTimeFromDouble_i yöntemi ICellsHelper::GetDateTimeFromDouble olarak yeniden adlandırıldı**
#### **ICellsHelper::GetDoubleFromDateTime_i yöntemi ICellsHelper::GetDoubleFromDateTime olarak yeniden adlandırıldı**
#### **ICellsHelper::DetectLoadFormat_i yöntemi ICellsHelper::DetectLoadFormat olarak yeniden adlandırıldı**
#### **ICellsHelper::DetectFileFormat_i yöntemi ICellsHelper::DetectFileFormat olarak yeniden adlandırıldı**
#### **ICellsHelper::GetFontDir_i yöntemi ICellsHelper::GetFontDir olarak yeniden adlandırıldı**
#### **ICellsHelper::SetFontDir_i yöntemi ICellsHelper::SetFontDir olarak yeniden adlandırıldı**
#### **ICellsHelper::GetFontDirs_i yöntemi ICellsHelper::GetFontDirs olarak yeniden adlandırıldı**
#### **ICellsHelper::SetFontDirs_i yöntemi ICellsHelper::SetFontDirs olarak yeniden adlandırıldı**
#### **ICellsHelper::GetFontFiles_i yöntemi ICellsHelper::GetFontFiles olarak yeniden adlandırıldı**
#### **ICellsHelper::SetFontFiles_i yöntemi ICellsHelper::SetFontFiles olarak yeniden adlandırıldı**
#### **ICellsHelper::GetStartupPath_i yöntemi ICellsHelper::GetStartupPath olarak yeniden adlandırıldı**
#### **ICellsHelper::SetStartupPath_i yöntemi ICellsHelper::SetStartupPath olarak yeniden adlandırıldı**
#### **ICellsHelper::GetAltStartPath_i yöntemi ICellsHelper::GetAltStartPath olarak yeniden adlandırıldı**
#### **ICellsHelper::SetAltStartPath_i yöntemi ICellsHelper::SetAltStartPath olarak yeniden adlandırıldı**
#### **ICellsHelper::GetLibraryPath_i yöntemi ICellsHelper::GetLibraryPath olarak yeniden adlandırıldı**
#### **ICellsHelper::SetLibraryPath_i yöntemi ICellsHelper::SetLibraryPath olarak yeniden adlandırıldı**
#### **ICellsHelper::GetUsedColors_i yöntemi ICellsHelper::GetUsedColors olarak yeniden adlandırıldı**
#### **ICellsHelper::AddAddInFunction_i yöntemi ICellsHelper::AddAddInFunction olarak yeniden adlandırıldı**
#### **ICellsHelper::MergeFiles_i yöntemi ICellsHelper::MergeFiles olarak yeniden adlandırıldı**
#### **IColumnCollection::GetByIndex_i yöntemi IColumnCollection::GetIColumn olarak yeniden adlandırıldı**
#### **IFileFormatUtil::DetectFileFormat_i yöntemi, IFileFormatUtil::DetectFileFormat olarak yeniden adlandırıldı**
#### **IFileFormatUtil::ExtensionToSaveFormat_i yöntemi, IFileFormatUtil::ExtensionToSaveFormat olarak yeniden adlandırıldı**
#### **IFileFormatUtil::IsTemplateFormat_i yöntemi, IFileFormatUtil::IsTemplateFormat olarak yeniden adlandırıldı**
#### **IFileFormatUtil::LoadFormatToExtension_i yöntemi, IFileFormatUtil::LoadFormatToExtension olarak yeniden adlandırıldı**
#### **IFileFormatUtil::LoadFormatToSaveFormat_i yöntemi, IFileFormatUtil::LoadFormatToSaveFormat olarak yeniden adlandırıldı**
#### **IFileFormatUtil::SaveFormatToExtension_i yöntemi, IFileFormatUtil::SaveFormatToExtension olarak yeniden adlandırıldı**
#### **IFileFormatUtil::SaveFormatToLoadFormat_i yöntemi, IFileFormatUtil::SaveFormatToLoadFormat olarak yeniden adlandırıldı**
#### **IRange::SetStyle yöntemi IRange::SetIStyle olarak yeniden adlandırıldı**
#### **IFindOptions::SetRange yöntemi, IFindOptions::SetIRange olarak yeniden adlandırıldı**
#### **ILoadOptions::SetLoadDataOptions yöntemi, ILoadOptions::SetILoadDataOptions olarak yeniden adlandırıldı**
#### **IWorkbook::SetSettings yöntemi, IWorkbook::SetISettings olarak yeniden adlandırıldı**
#### **IWorkbook::SetDefaultStyle yöntemi, IWorkbook::SetDefaultIStyle olarak yeniden adlandırıldı**
