---
title: Genel API Aspose.Cells 17.1.0'daki değişiklikler
type: docs
weight: 20
url: /tr/cpp/public-api-changes-in-aspose-cells-17-1-0/
---
{{% alert color="primary" %}} 

Bu belge, modül/uygulama geliştiricilerinin ilgisini çekebilecek 16.12.0 sürümünden 17.1.0 sürümüne Aspose.Cells API değişikliklerini açıklamaktadır. Yalnızca yeni ve güncellenmiş genel yöntemleri, eklenen ve kaldırılan sınıfları vb. değil, aynı zamanda Aspose.Cells'deki perde arkasındaki davranış değişikliklerinin açıklamasını da içerir.

{{% /alert %}} 
## **Eklenen API'ler**
### **Adlandırılmış Aralıklar için Destek**
 Aspose.Cells for C++ artık Adlandırılmış Aralıkların oluşturulmasını ve değiştirilmesini destekliyor. Aşağıdaki kod parçacığı, Aspose.Cells for C++ API'i kullanmanın ne kadar basit olduğunu gösterir.[adlandırılmış aralıklar oluştur](/cells/tr/cpp/create-named-range-in-a-workbook/).

**C++**

{{< highlight "csharp" >}}

 //Path of your directory where you want to read or write files from

StringPtr dirPath = new String("D:\\Downloads\\");

//Path of output excel file

StringPtr outCreateNamedRange = (new String(dirPath))->Append(new String("outCreateNamedRange.xlsx"));

//Create a workbook

intrusive_ptr<IWorkbook> wb = Factory::CreateIWorkbook();

//Access first worksheet

intrusive_ptr<IWorksheet> ws = wb->GetIWorksheets()->GetObjectByIndex(0);

//Create a range

intrusive_ptr<IRange> rng = ws->GetICells()->CreateIRange((intrusive_ptr<String>)new String("A5:C10"));

//Set its name to make it named range

rng->SetName((intrusive_ptr<String>)new String("MyNamedRange"));

//Read the named range created above from names collection

intrusive_ptr<IName> nm = wb->GetIWorksheets()->GetINames()->GetObjectByIndex(0);

//Print its FullText and RefersTo properties

printf("Full Text: %s\n", nm->GetFullText()->charValue());

printf("Refers To: %s\n", nm->GetRefersTo()->charValue());

//Save the workbook in xlsx format

wb->Save(outCreateNamedRange, SaveFormat_Xlsx);

{{< /highlight >}}

 Aspose.Cells for C++ API'leri, yeni Adlandırılmış Aralıklar oluşturmanın yanı sıra mevcut Adlandırılmış Aralıkları değiştirmeyi de destekler. Aşağıdaki kod parçacığı, Aspose.Cells for C++ API'i kullanır.[varolan bir adlandırılmış aralığı manipüle etmek](/cells/tr/cpp/manipulate-named-range-in-a-workbook/).

**C++**

{{< highlight "csharp" >}}

 //Path of your directory where you want to read or write files from

StringPtr dirPath = new String("D:\\Downloads\\");

//Path of source excel file

StringPtr srcManipulateRange = (new String(dirPath))->Append(new String("srcManipulateRange.xlsx"));

//Path of output excel file

StringPtr outManipulateRange = (new String(dirPath))->Append(new String("outManipulateRange.xlsx"));

//Create a workbook

intrusive_ptr<IWorkbook> wb = Factory::CreateIWorkbook(srcManipulateRange);

//Read the named range created above from names collection

intrusive_ptr<IName> nm = wb->GetIWorksheets()->GetINames()->GetObjectByIndex(0);

//Print its FullText and RefersTo properties

printf("Full Text: %s\n", nm->GetFullText()->charValue());

printf("Refers To: %s\n", nm->GetRefersTo()->charValue());

//Manipulate the RefersTo property of NamedRange

nm->SetRefersTo((intrusive_ptr<String>)new String("=Sheet1!$D$5:$J$10"));

//Save the workbook in xlsx format

wb->Save(outManipulateRange, SaveFormat_Xlsx);

{{< /highlight >}}
### **ICells::LinkToXmlMap Yöntemi Eklendi**
ICells sınıfına, bir XML eşlemesini bağlamada yararlı olan LinkToXmlMap yöntemi eklendi.
### **ICells::ImportCSV Yöntemi Eklendi**
Bir çalışma sayfasının hücrelerine bir CSV dosyasını içe aktarmak için yararlı olan ImportCSV yöntemi ICells sınıfına eklenmiştir.
### **ICells::ImportTwoDimensionArray Yöntemi Eklendi**
GetIProtectedRangeCollection yöntemi, iki boyutlu bir veri dizisini bir çalışma sayfasına aktarmak için yararlı olan ICells sınıfına eklenmiştir.
### **IWorksheet::GetIProtectedRangeCollection Yöntemi Eklendi**
GetIProtectedRangeCollection yöntemi, IProtectedRange nesnelerinin koleksiyonunun alınmasında yararlı olan IWorksheet sınıfına eklendi.
### **IWorksheet::GetIProtectedRangeCollection Yöntemi Eklendi**
Çalışma sayfasından düzenleme aralığı koleksiyonunun alınmasında kullanışlı olan GetIProtectedRangeCollection yöntemi, IWorksheet sınıfına eklenmiştir.
### **IWorkbookSettings::ClearPivottables Yöntemi Eklendi**
ClearPivottables yöntemi, belirli bir elektronik tablodan tüm Pivot Tabloları temizlemede yararlı olan IWorkbookSettings sınıfına eklenmiştir.
### **IWorksheetCollection::CreateIRange Yöntemi Eklendi**
IWorksheetCollection sınıfına, hücre referanslarını dize biçiminde ileterek IRange nesnesinin oluşturulmasında yararlı olan CreateIRange yöntemi eklendi.
### **IExternalLink::IsVisible Yöntemi Eklendi**
IsVisible yöntemi, Excel uygulamasında harici bir bağlantının görünürlük durumunu alır.
### **GetScaleCrop & SetScaleCrop Yöntemleri Eklendi**
Aspose.Cells for C++ 17.1.0, GetScaleCrop & SetScaleCrop yöntemlerini IBuiltInDocumentPropertyCollection sınıfına maruz bıraktı. Bu yöntemler, belge küçük resminin görüntüleme modunu belirten ScaleCrop özelliğini almak veya ayarlamak için kullanışlıdır.
### **GetLinksUpToDate & SetLinksUpToDate Yöntemleri Eklendi**
Aspose.Cells for C++ 17.1.0, GetLinksUpToDate & SetLinksUpToDate yöntemlerini IBuiltInDocumentPropertyCollection sınıfına maruz bıraktı. Bu yöntemler, bir belgedeki köprülerin güncel olup olmadığını gösteren LinkUpToDate özelliğini almak veya ayarlamak için kullanışlıdır.
### **GetAbsolutePath & SetAbsolutePath Yöntemleri Eklendi**
Aspose.Cells for C++ 17.1.0, GetAbsolutePath & SetAbsolutePath yöntemlerini IWorkbook sınıfına gösterdi. Bu yöntemler, yalnızca harici bağlantılar için kullanılabilen dosyanın mutlak yolunu almak veya ayarlamak için kullanışlıdır.
### **GetFormula & SetFormula Yöntemleri Eklendi**
Aspose.Cells for C++'in bu sürümü, IListColumn sınıfı için GetFormula & SetFormula yöntemlerini kullanıma sunmuştur. Bu yöntemler, bir liste sütununun formülünü almak veya ayarlamak için kullanışlıdır.
### **GetCheckCompatibility & SetCheckCompatibility Yöntemleri Eklendi**
Aspose.Cells for C++'in bu sürümü, IWorkbookSettings sınıfı için GetCheckCompatibility & GetCheckCompatibility yöntemlerini kullanıma sunmuştur. Bu yöntemler, çalışma kitabını kaydederken API'in uyumluluğu denetlemesi gerekip gerekmediğini gösteren uyumluluk denetimi özelliğini almak veya ayarlamak için kullanışlıdır. Varsayılan değer true'dur ve uygulama gereksinimi uyumluluğu kontrol etmek değilse false olarak ayarlanabilir.
### **GetILightCellsDataHandler & SetILightCellsDataHandler Yöntemleri Eklendi**
Aspose.Cells for C++ şimdi ILoadOptions sınıfı için GetILightCellsDataHandler & SetILightCellsDataHandler yöntemlerini kullanıma sundu. Bu yöntemler, şablon dosyasını okurken hücre verilerini işlemek için veri işleyiciyi belirtir.
### **GetCultureInfo & SetCultureInfo Yöntemleri Eklendi**
Aspose.Cells for C++, ILoadOptions sınıfı için GetCultureInfo & SetCultureInfo yöntemlerini kullanıma sundu. Bu yöntemler, dosya yüklenirken sistem kültürü bilgisini alabilir veya ayarlayabilir.
## **Kaldırılan API'ler**
### **Kaldırılan ICells::MaxDataRowInColumn Yöntemi**
Bunun yerine ICells::GetLastDataRow yöntemini kullanmanız önerilir.
### **Kaldırılan ICell::GetConditionalIStyle Yöntemi**
Bunun yerine ICell::GetIConditionalFormattingResult yöntemini kullanmanız önerilir.
### **Kaldırılan IPageSetup::GetDraft & SetDraft Yöntemleri**
Bunun yerine IPageSetup::GetPrintDraft & IPageSetup::SetPrintDraft yöntemlerinin kullanılması önerilir.

{{% alert color="primary" %}} 

Aspose.Cells for C++ 17.1.0 sürümüyle, kullanılmayan ve dolayısıyla gereksiz görülen birkaç yöntemi kaldırdık. İşte tüm bu tür yöntemlerin listesi.

- IPaneCollection::GetAcitvePaneType & SetAcitvePaneType Yöntemleri
- IRange::ToString Yöntem
- IRow::Equals Yöntemi
- IWorkbook::SetISettings Yöntem
- ICell::ToString() Yöntem
- ICell::Equals(ObjectPtr) Yöntem
- ICell::GetHashCode Yöntem
- IWorksheet::ToString Yöntem

{{% /alert %}}
