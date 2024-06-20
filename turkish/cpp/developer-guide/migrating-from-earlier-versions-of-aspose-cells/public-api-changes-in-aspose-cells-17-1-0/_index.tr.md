---
title: Aspose.Cells 17.1.0 da Genel API Değişiklikleri
type: docs
weight: 20
url: /tr/cpp/public-api-changes-in-aspose-cells-17-1-0/
---

{{% alert color="primary" %}} 

Bu belge, sürüm 16.12.0'den 17.1.0'a Aspose.Cells API'sindeki değişiklikleri açıklar ve modül/uygulama geliştiricileri için ilgi çekebilecek değişiklikleri içerir. Yalnızca yeni ve güncellenmiş genel yöntemler, eklenen ve kaldırılan sınıflar vb. değil, aynı zamanda Aspose.Cells'in arka planda davranışında herhangi bir değişikliğin açıklamasını içerir.

{{% /alert %}} 
## **Eklenen API'lar**
### **İsimlendirilmiş Aralıkları Destekleme**
Aspose.Cells for C++ artık İsimlendirilmiş Aralıkların oluşturulmasını ve manipülasyonunu destekler. Aşağıdaki kod örneği, Aspose.Cells for C++ API'sini [ele almak için ne kadar basit olduğunu](/cells/tr/cpp/create-named-range-in-a-workbook/) gösterir.

**C++**

{{< highlight csharp >}}

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

Yeni İsimlendirilmiş Aralıklar oluşturmanın ötesinde, Aspose.Cells for C++ API'leri mevcut İsimlendirilmiş Aralıkları manipüle etmeyi de destekler. Aşağıdaki kod örneği, Aspose.Cells for C++ API'sini [mevcut bir isimlendirilmiş aralığı ele almak](/cells/tr/cpp/manipulate-named-range-in-a-workbook/) için kullanır.

**C++**

{{< highlight csharp >}}

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
### **ICells::LinkToXmlMap Metodu Eklendi**
LinkToXmlMap metodu, bir XML haritasını bağlamak için yararlı olan ICells sınıfına eklenmiştir.
### **ICells::ImportCSV Metodu Eklendi**
ImportCSV metodu, bir CSV dosyasının bir çalışma sayfasının hücrelerine aktarılmasında kullanışlı olan ICells sınıfına eklenmiştir.
### **ICells::ImportTwoDimensionArray Metodu Eklendi**
IProtectedRangeCollection'nin  olan GetIProtectedRangeCollection metodu, bir çalışma sayfasına iki boyutlu bir veri dizisinin aktarılmasında kullanışlıdır.
### **IWorksheet::GetIProtectedRangeCollection Metodu Eklendi**
GetIProtectedRangeCollection metodu, bir IWorksheet sınıfına eklendi ve çalışma sayfasındaki IProtectedRange nesnelerinin koleksiyonunu almakta kullanışlıdır.
### **IWorksheet::GetIProtectedRangeCollection Metodu Eklendi**
GetIProtectedRangeCollection metodu, bir IWorksheet sınıfına eklendi ve çalışma sayfasından düzenleme aralığı koleksiyonunu alma işlevine sahiptir.
### **IWorkbookSettings::ClearPivottables Metodu Eklendi**
ClearPivottables metodu, bir IWorkbookSettings sınıfına eklendi ve belirli bir elektronik tablodan tüm Pivottable'ların temizlenmesinde kullanışlıdır.
### **IWorksheetCollection::CreateIRange Metodu Eklendi**
CreateIRange metodu, bir IWorksheetCollection sınıfına eklenmiş olup, hücre referanslarını dize formatında geçerek IRange nesnesini oluşturmada kullanışlıdır.
### **IExternalLink::IsVisible Metodu Eklendi**
IsVisible metodu, bir dış bağlantının Excel uygulamasında görünürlük durumunu alır.
### **GetScaleCrop ve SetScaleCrop Metotları Eklendi**
Aspose.Cells for C++ 17.1.0, IBuiltInDocumentPropertyCollection sınıfına GetScaleCrop ve SetScaleCrop yöntemlerini açığa çıkardı. Bu yöntemler, belgenin küçük resminin görüntüleme modunu gösteren ScaleCrop özelliğini almak veya ayarlamak için kullanışlıdır.
### **GetLinksUpToDate ve SetLinksUpToDate Yöntemleri Eklendi**
Aspose.Cells for C++ 17.1.0, IBuiltInDocumentPropertyCollection sınıfına GetLinksUpToDate ve SetLinksUpToDate yöntemlerini açığa çıkardı. Bu yöntemler, belgedeki bağlantıların güncel olup olmadığını gösteren LinkUpToDate özelliğini almak veya ayarlamak için kullanışlıdır.
### **GetAbsolutePath ve SetAbsolutePath Yöntemleri Eklendi**
Aspose.Cells for C++ 17.1.0, IWorkbook sınıfına GetAbsolutePath ve SetAbsolutePath yöntemlerini açığa çıkardı. Bu yöntemler, yalnızca dış bağlantılar için kullanılabilecek olan dosyanın mutlak yolunu almak veya ayarlamak için kullanışlıdır.
### **GetFormula ve SetFormula Yöntemleri Eklendi**
Bu sürümde Aspose.Cells for C++, IListColumn sınıfı için GetFormula ve SetFormula yöntemlerini açığa çıkardı. Bu yöntemler, listedeki sütunun formülünü almak veya ayarlamak için kullanışlıdır.
### **GetCheckCompatibility ve SetCheckCompatibility Yöntemleri Eklendi**
Bu sürümde Aspose.Cells for C++, IWorkbookSettings sınıfı için GetCheckCompatibility ve GetCheckCompatibility yöntemlerini açığa çıkardı. Bu yöntemler, çalışma kitabını kaydederken API'nın uyumluluğu kontrol etmesi gerekip gerekmediğini gösteren uyumluluk kontrol özelliğini almak veya ayarlamak için kullanışlıdır. Varsayılan değer true'dur ve gereksinim durumunda uyumluluğu kontrol etmemesi için false olarak ayarlanabilir.
### **GetILightCellsDataHandler ve SetILightCellsDataHandler Yöntemleri Eklendi**
Aspose.Cells for C++ artık ILoadOptions sınıfı için GetILightCellsDataHandler ve SetILightCellsDataHandler yöntemlerini ortaya çıkardı. Bu yöntemler, şablon dosyasını okurken hücre verilerini işlemek için veri işleyiciyi belirtir.
### **GetCultureInfo ve SetCultureInfo Yöntemleri Eklendi**
Aspose.Cells for C++, ILoadOptions sınıfı için GetCultureInfo ve SetCultureInfo yöntemlerini açığa çıkardı. Bu yöntemler, dosya yükleme sırasındaki sistem kültür bilgisini almak veya ayarlamak için kullanılır.
## **Removed APIs**
### **ICells::MaxDataRowInColumn Yöntemi Kaldırıldı**
Icells::GetLastDataRow yönteminin kullanılması önerilir.
### **ICell::GetConditionalIStyle Yöntemi Kaldırıldı**
ICell::GetIConditionalFormattingResult yönteminin kullanılması önerilir.
### **IPageSetup::GetDraft ve SetDraft Yöntemleri Kaldırıldı**
IPageSetup::GetPrintDraft ve IPageSetup::SetPrintDraft yöntemlerinin kullanılması önerilir.

{{% alert color="primary" %}} 

Aspose.Cells for C++ 17.1.0 ile, kullanılmayan ve gereksiz görülen birkaç yöntem kaldırıldı. İşte böyle yöntemlerin tüm listesi.

- IPaneCollection::GetAcitvePaneType ve SetAcitvePaneType Yöntemleri
- IRange::ToString Yöntemi
- IRow::Equals Yöntemi
- IWorkbook::SetISettings Yöntemi
- ICell::ToString() Yöntemi
- ICell::Equals(ObjectPtr) Yöntemi
- ICell::GetHashCode Yöntemi
- IWorksheet::ToString Yöntemi

{{% /alert %}}
