---
title: Aspose.Cells 16.12.0 daki Genel API Değişiklikleri
type: docs
weight: 10
url: /tr/go-cpp/public-api-changes-in-aspose-cells-16-12-0/
---

{{% alert color="primary" %}} 

Bu belge, 16.11.0'dan 16.12.0'a Aspose.Cells API'sindeki değişiklikleri modül/uygulama geliştiricilerinin ilgisini çekebilecek değişiklikleri açıklar. Sadece yeni ve güncellenmiş genel yöntemleri, eklendikçe ve kaldırılan sınıfları vb. değil, aynı zamanda Aspose.Cells'in arka planda olan değişikliklerini de açıklar.

{{% /alert %}} 
## **Eklenen API'lar**
### **Pivot Tabloları Desteği**
Aspose.Cells for C++'in ikinci sürümü, Pivot Tablolarının oluşturulmasını ve manipüle edilmesini destekler. Aspose.Cells for C++, Bir Pivot Tablo nesnesini temsil eden IPivotTable sınıfını sağlar, IPivotTableCollection ise Pivot Tablolarının bir koleksiyonunu temsil eder. IPivotTableCollection, IWorksheet nesnesi üzerinden erişilebilir ve yeni bir Pivot Tablosu koleksiyona eklenirken IPivotTableCollection.Add yöntemi kullanılır.

Aşağıdaki kod örneği, Aspose.Cells for C++ API'sini kullanarak [sıfırdan Pivot Tabloları oluşturmanın](/cells/tr/cpp/create-pivot-table/) ne kadar kolay olduğunu göstermektedir.

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

Yeni Pivot Tabloları oluşturmanın yanı sıra, Aspose.Cells for C++ API'leri mevcut Pivot Tablolarını manipüle etmeyi de destekler. API şu anda Pivot Tablosunun kaynak aralığındaki veriyi değiştirmeyi ve ardından yenilemeyi destekler. Pivot Tablosu istenen şekilde manipüle edildikten sonra, güncellenmiş veri kaynağına karşı Pivot Tablosunu yenilemek için IPivotTable.RefreshData ve IPivotTable.CalculateData yöntemlerini kullanmak en iyisidir.

Aşağıdaki kod örneği, Aspose.Cells for C++ API'sini kullanarak [mevcut bir Pivot Tabloyu manipüle etmeyi](/cells/tr/cpp/manipulate-pivot-table/) göstermektedir.

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
### **Koşullu Biçimlendirme Kuralları Desteği**
Aspose.Cells for C++ şimdi, IFormatCondition sınıfını açığa çıkararak çalışma sayfasına koşullu biçimlendirme kuralları eklemeyi sağlar. Söz konusu sınıf, uygulama gereksinimlerine göre koşullu biçimlendirme kurallarını [uygulamak için](/cells/tr/cpp/apply-conditional-formatting-in-worksheet/) aşağıdaki yöntemleri sağlar.

- IFormatCondition.GetIAboveAverage
- IFormatCondition.GetIColorScale
- IFormatCondition.GetIDataBar
- IFormatCondition.GetIIconSet
- IFormatCondition.GetITop10

Aşağıdaki örnek kod, A1 ve B2 hücrelerindeki Bir Hücre Değeri türünde bir koşullu biçimlendirme kuralı eklemenin nasıl yapıldığını göstermektedir.

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
### **Köprü Bağlantısı Desteği**
Aspose.Cells for C++ şimdi [çalışma sayfası hücrelerine köprü bağlantısı eklemeyi](/cells/tr/cpp/add-hyperlinks-to-the-cells/) destekler. Bu özelliği sağlamak için Aspose.Cells for C++ 16.12.0, IHyperlinkCollection sınıfını açığa çıkarmıştır. Söz konusu sınıf, IWorksheet nesnesi üzerinden erişilebilirken, bir köprü bağlantısı IHyperlinkCollection.Add yöntemi kullanılarak koleksiyona eklenebilir, aşağıdaki gibi gösterilmiştir.

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
### **Belge Özellikleri Desteği**
Excel uygulaması, aşağıda listelenen 2 tür belge özelliğini destekler.

- Sistem tanımlı (dahili) özellikler: Dahili özellikler, belge başlığı, yazar adı, belge istatistikleri gibi belge hakkında genel bilgiler içerir.
- Kullanıcı tanımlı (özel) özellikler: Son kullanıcı tarafından ad-değer çifti biçiminde tanımlanan özel özellikler.

Aspose.Cells for C++, [yerleşik ve özel belge özelliklerini](/cells/tr/cpp/managing-document-properties/) yönetme konusunda destek sunar. Aspose.Cells’in IWorkbook sınıfı bir Excel dosyasını temsil eder. Yerleşik belge özelliklerine erişmek için IWorkbook.GetBuiltInDocumentProperties kullanılırken, özel belge özelliklerine erişmek için IWorkbook.GetCustomDocumentProperties yöntemi kullanılır.

Aşağıdaki örnek kod mevcut bir örnek elektronik tablo yükler ve Başlık, Konu gibi yerleşik belge özelliklerini ve MyCustom1 adlı özel özelliği okur.

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
### **Liste Nesnelerini Destekleme**
Bir Excel tablosu, herhangi bir sayıda satır ve sütun içeren bir hücre matrisidir, aynı tablo Aspose.Cells for C++ API'lerinde bir Liste Nesnesi olarak adlandırılır. Aspose::Cells::Tables ad alanı, Liste Nesneleri ile ilgili işlemleri yapan gerekli tüm sınıfları içerir. En önemli sınıflar IListObject ve IListObjectCollection'dır, bunlar List Nesnelerini [oluşturmak ve biçimlendirmek](/cells/tr/cpp/create-and-format-table/) gibi işlemlere izin verir.

Aşağıdaki örnek kod örnek elektronik tablo dosyasını yükler ve ardından A1:H10 aralığında bir Liste Nesnesi (tablo) oluşturur, ardından toplamı göstermek için çeşitli yöntemlerini kullanır.

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
### **Satır ve Sütun Gruplama Desteği**
Aspose.Cells for C++ API'si, verilen bir çalışma sayfasındaki tüm hücrelerin koleksiyonu olan ICells sınıfını kullanarak satırları ve sütunları gruplamak için GroupRows ve GroupColumns yöntemlerini sunar.

Aşağıdaki kod örneği, yukarıda bahsedilen her iki yöntemin basit kullanım senaryosunu göstermektedir.

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
### **Tema Desteği**
Aspose.Cells for C++ API'leri artık Excel uygulamasının sunduğu temaları kullanmak ve değiştirmek için destek sunmaktadır.
#### **Özel Tema Renklerini Uygulama Yeteneği**
Aşağıdaki kod parçası, elektronik tablo için [özel renklerle yeni bir tema oluşturmaya](/cells/tr/cpp/apply-custom-theme-colors-of-the-workbook-using-array-of-colors/) çalışmaktadır.

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
#### **Tema Renklerinin Değiştirilmesi Desteği**
Aşağıdaki örnek kod, elektronik tablonun tema renklerini [okuma ve değiştirme](/cells/tr/cpp/apply-custom-theme-colors-of-the-workbook-using-array-of-colors/) işlemini göstermektedir. Örnek kod mevcut bir elektronik tabloyu yükler, Accent1-Accent6 gibi temanın renklerini okur ve kaydetmeden önce renkleri değiştirir.

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
#### **Tema Kodlarının Kopyalanabilme Yeteneği**
Aşağıdaki örnek kod, bir elektronik tablodan diğerine [tema kopyalamayı](/cells/tr/cpp/copy-theme-from-one-workbook-to-another/) nasıl gerçekleştireceğinizi göstermektedir, bu durum birden fazla elektronik tabloya yerleşik veya özel temalar uygulamada kullanışlı olabilir.

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
## **Adı Değişen API'lar**
Aspose.Cells for C++ 16.12.0 sürümüyle, arabirimleri birleştirilmiş tutabilmek için birkaç yöntemi yeniden adlandırdık. Yeniden adlandırılan tüm API'lerin listesi aşağıdaki gibidir.
#### **ICell::SetStyle yönteminin adı ICell::SetIStyle olarak değiştirildi**
#### **ICell::SetCharacters yönteminin adı ICell::SetIFontSettings olarak değiştirildi**
#### **ICellsColor::SetThemeColor yönteminin adı ICellsColor::SetIThemeColor olarak değiştirildi**
#### **ICells::SetStyle yönteminin adı ICells::SetIStyle olarak değiştirildi**
#### **ICellsHelper::GetDPI_i yönteminin adı ICellsHelper::GetDPI olarak değiştirildi**
#### **ICellsHelper::SetDPI_i yönteminin adı ICellsHelper::SetDPI olarak değiştirildi**
#### **ICellsHelper::GetVersion_i yönteminin adı ICellsHelper::GetVersion olarak değiştirildi**
#### **ICellsHelper::IsProtectedByRMS_i yönteminin adı ICellsHelper::IsProtectedByRMS olarak değiştirildi**
#### **ICellsHelper::IsProtectedByRMS_i yönteminin adı ICellsHelper::IsProtectedByRMS olarak değiştirildi**
#### **ICellsHelper::CellNameToIndex_i yönteminin adı ICellsHelper::CellNameToIndex olarak değiştirildi**
#### **ICellsHelper::CellIndexToName_i yönteminin adı ICellsHelper::CellIndexToName olarak değiştirildi**
#### **ICellsHelper::ColumnIndexToName_i yönteminin adı ICellsHelper::ColumnIndexToName olarak değiştirildi**
#### **ICellsHelper::ColumnNameToIndex_i metodu ICellsHelper::ColumnNameToIndex olarak yeniden adlandırıldı**
#### **ICellsHelper::RowIndexToName_i metodu ICellsHelper::RowIndexToName olarak yeniden adlandırıldı**
#### **ICellsHelper::RowNameToIndex_i metodu ICellsHelper::RowNameToIndex olarak yeniden adlandırıldı**
#### **ICellsHelper::ConvertR1C1FormulaToA1_i metodu ICellsHelper::ConvertR1C1FormulaToA1 olarak yeniden adlandırıldı**
#### **ICellsHelper::ConvertA1FormulaToR1C1_i metodu ICellsHelper::ConvertA1FormulaToR1C1 olarak yeniden adlandırıldı**
#### **ICellsHelper::GetDateTimeFromDouble_i metodu ICellsHelper::GetDateTimeFromDouble olarak yeniden adlandırıldı**
#### **ICellsHelper::GetDoubleFromDateTime_i metodu ICellsHelper::GetDoubleFromDateTime olarak yeniden adlandırıldı**
#### **ICellsHelper::DetectLoadFormat_i metodu ICellsHelper::DetectLoadFormat olarak yeniden adlandırıldı**
#### **ICellsHelper::DetectFileFormat_i metodu ICellsHelper::DetectFileFormat olarak yeniden adlandırıldı**
#### **ICellsHelper::GetFontDir_i metodu ICellsHelper::GetFontDir olarak yeniden adlandırıldı**
#### **ICellsHelper::SetFontDir_i metodu ICellsHelper::SetFontDir olarak yeniden adlandırıldı**
#### **ICellsHelper::GetFontDirs_i metodu ICellsHelper::GetFontDirs olarak yeniden adlandırıldı**
#### **ICellsHelper::SetFontDirs_i metodu ICellsHelper::SetFontDirs olarak yeniden adlandırıldı**
#### **ICellsHelper::GetFontFiles_i metodu ICellsHelper::GetFontFiles olarak yeniden adlandırıldı**
#### **ICellsHelper::SetFontFiles_i metodu ICellsHelper::SetFontFiles olarak yeniden adlandırıldı**
#### **ICellsHelper::GetStartupPath_i metodu ICellsHelper::GetStartupPath olarak yeniden adlandırıldı**
#### **ICellsHelper::SetStartupPath_i metodu ICellsHelper::SetStartupPath olarak yeniden adlandırıldı**
#### **ICellsHelper::GetAltStartPath_i metodu ICellsHelper::GetAltStartPath olarak yeniden adlandırıldı**
#### **ICellsHelper::SetAltStartPath_i metodu ICellsHelper::SetAltStartPath olarak yeniden adlandırıldı**
#### **ICellsHelper::GetLibraryPath_i metodu ICellsHelper::GetLibraryPath olarak yeniden adlandırıldı**
#### **ICellsHelper::SetLibraryPath_i metodu ICellsHelper::SetLibraryPath olarak yeniden adlandırıldı**
#### **ICellsHelper::GetUsedColors_i metodu ICellsHelper::GetUsedColors olarak yeniden adlandırıldı**
#### **ICellsHelper::AddAddInFunction_i metodu ICellsHelper::AddAddInFunction olarak yeniden adlandırıldı**
#### **ICellsHelper::MergeFiles_i metodu ICellsHelper::MergeFiles olarak yeniden adlandırıldı**
#### **IColumnCollection::GetByIndex_i metodu IColumnCollection::GetIColumn olarak yeniden adlandırıldı**
#### **IFileFormatUtil::DetectFileFormat_i metodu IFileFormatUtil::DetectFileFormat olarak yeniden adlandırıldı**
#### **IFileFormatUtil::ExtensionToSaveFormat_i metodu IFileFormatUtil::ExtensionToSaveFormat olarak yeniden adlandırıldı**
#### **IFileFormatUtil::IsTemplateFormat_i metodu IFileFormatUtil::IsTemplateFormat olarak yeniden adlandırıldı**
#### **IFileFormatUtil::LoadFormatToExtension_i metodu IFileFormatUtil::LoadFormatToExtension olarak yeniden adlandırıldı**
#### **IFileFormatUtil::LoadFormatToSaveFormat_i metodu IFileFormatUtil::LoadFormatToSaveFormat olarak yeniden adlandırıldı**
#### **IFileFormatUtil::SaveFormatToExtension_i metodu IFileFormatUtil::SaveFormatToExtension olarak yeniden adlandırıldı**
#### **IFileFormatUtil::SaveFormatToLoadFormat_i metodu IFileFormatUtil::SaveFormatToLoadFormat olarak yeniden adlandırıldı**
#### **IRange::SetStyle metodu IRange::SetIStyle olarak yeniden adlandırıldı**
#### **IFindOptions::SetRange metodu IFindOptions::SetIRange olarak yeniden adlandırıldı**
#### **ILoadOptions::SetLoadDataOptions metodu ILoadOptions::SetILoadDataOptions olarak yeniden adlandırıldı**
#### **IWorkbook::SetSettings metodu IWorkbook::SetISettings olarak yeniden adlandırıldı**
#### **IWorkbook::SetDefaultStyle metodu IWorkbook::SetDefaultIStyle olarak yeniden adlandırıldı**
