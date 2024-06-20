---
title: Çalışma Sayfasına Veri İçe Aktarma
type: docs
weight: 170
url: /tr/net/import-data-into-worksheet/
description: Aspose.Cells for .NET API si aracılığıyla çalışma sayfasına nasıl veri aktarılacağını öğrenin.
keywords: C# ile Çalışma Sayfasına Veri İçe Aktarma, ICellsDataTable arayüzü ile Excel e veri aktarma, Diziden veri aktarma, ArrayList ten veri aktarma, Özel Nesnelerden veri aktarma, Birleştirilmiş alana özel nesnelerden veri aktarma, DataTable den veri aktarma, Dinamik nesne kaynağı olarak veri aktarma, Veri sütunundan veri aktarma, DataView den veri aktarma, DataGrid den veri aktarma, GridView den veri aktarma, HTML biçimli veri aktarma, JSON verilerinden veri aktarma
---

{{% alert color="primary" %}}

Bu makale, geliştiricilerin Aspose.Cells üzerinden erişebilecekleri bazı veri aktarma tekniklerini tartışmaktadır.

{{% /alert %}}

## **Çalışma Sayfasına Veri İçe Aktarma Nasıl Yapılır**

Aspose.Cells ile bir Excel dosyasını açtığınızda, dosyadaki tüm veriler otomatik olarak içe aktarılır. Aspose.Cells ayrıca diğer veri kaynaklarından da veri içe aktarabilir.

Aspose.Cells, Microsoft Excel dosyasını temsil eden bir sınıf olan [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sağlar. [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfı, bir Excel dosyasındaki her çalışma sayfasına erişime izin veren bir [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) koleksiyonunu içerir. Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfı ile temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfı bir [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) koleksiyonu sağlar. [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) koleksiyonu, farklı veri kaynaklarından veri içe aktarmak için kullanışlı yöntemler sağlar. Bu makale, bu yöntemlerin nasıl kullanılabileceğini açıklar.

## **ICellsDataTable arayüzü ile Excel'e veri aktarma işlemi nasıl yapılır**
Çeşitli veri kaynaklarını sarmak için [ICellsDataTable](https://reference.aspose.com/cells/net/aspose.cells/icellsdatatable) ı uygulayın, ardından [Cells.ImportData()](https://reference.aspose.com/cells/net/aspose.cells/cells/importdata/#importdata) yöntemini kullanarak verileri Excel çalışma sayfasına aktarın.
### **Örnek Kod**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "ImportICellsDataTableIntoWorksheet.cs" >}}

*CustomerDataSource*, *Customer*, ve *CustomerList* sınıflarının uygulaması aşağıda verilmiştir

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-ICellsDataTableDataSourceForWorkbookDesigner-2.cs" >}}


## **Diziden Excel'e Veri Aktarma**

Bir diziden elektronik tabloya veri aktarmak için, [**ImportArray**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importarray/index) koleksiyonunun [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) yöntemini çağırın. [**ImportArray**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importarray/index) yönteminin birçok aşırı yüklenmiş sürümü vardır, ancak tipik bir aşırı yüklenmenin aşağıdaki parametreleri alır:

- **Dizi**, içeriği aktardığınız dizi nesnesi.
- **Satır numarası**, verilerin aktarılacağı ilk hücrenin satır numarası.
- **Sütun numarası**, verilerin aktarılacağı ilk hücrenin sütun numarası.
- **Dikey mi**, verinin dikey olarak mı yoksa yatay olarak mı aktarılacağını belirten bir Boolean değeri.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromArray-1.cs" >}}

## **ArrayList'ten Excel'e Veri Aktarma**

*ArrayList* daki verileri elektronik tablolara aktarmak için, [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) koleksiyonunun [**ImportArrayList**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importarraylist) yöntemini çağırın. ImportArray yöntemi aşağıdaki parametreleri alır:

- **Array list**, içeriği aktardığınız *ArrayList* nesnesini temsil eder.
- **Satır numarası**, verilerin aktarılacağı ilk hücrenin satır numarasını temsil eder.
- **Sütun numarası**, verilerin aktarılacağı ilk hücrenin sütun numarasını temsil eder.
- **Dikey mi**, verinin dikey olarak mı yoksa yatay olarak mı aktarılacağını belirten bir Boolean değeri.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromArrayList-1.cs" >}}

## **Özel Nesnelerden Excel'e Veri Aktarma**

Nesne koleksiyonundan bir çalışma sayfasına veri aktarmak için [**ImportCustomObjects**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importcustomobjects/index) kullanın. İstenen nesnelerin listeni yönteme sağlayarak istediğiniz nesne listesini görüntüleyin.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromCustomObject-1.cs" >}}

## **Özel Nesnelerden Excel'e Veri Aktarma ve Birleştirilmiş Alanı Kontrol Etme**

Birleştirilmiş hücreler içeren bir çalışma sayfasından nesne koleksiyonundan veri aktarmak için [**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/checkmergedcells) özelliğini kullanın. Excel şablonunda birleştirilmiş hücreler varsa, [**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/checkmergedcells) özelliğinin değerini true olarak ayarlayın. İstenen nesne listesini göstermek için yönteme [**ImportTableOptions**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions) nesnesini ve sütun/özelliklerin listesini sağlayın. Aşağıdaki kod örneği, özel nesnelerden birleştirilmiş hücrelere veri aktarmak için [**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/checkmergedcells) özelliğinin kullanımını gösterir. Referans için lütfen ekteki [kaynak Excel](90112033.xlsx) dosyasını ve [çıktı Excel](90112034.xlsx) dosyasını inceleyin.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportCustomObjectsToMergedArea-1.cs" >}}

## **DataTable'dan Excel'e Veri Aktarma**

*DataTable* dan veri aktarmak için, [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) koleksiyonunun [**ImportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatatable/index) yöntemini çağırın. [**ImportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatatable/index) yönteminin birçok aşırı yüklenmiş sürümü vardır, ancak tipik bir aşırı yüklenmenin aşağıdaki parametreleri alır:

- **Data table**, içeriği aktardığınız *DataTable* nesnesi.
- **Alan adı gösterilir mi**, *DataTable* sütunlarının çalışma sayfasına birinci satır olarak aktarılıp aktarılmayacağını belirler.
- **Başlangıç hücresi**, *DataTable* içeriğini nereden aktarılacağını temsil eder (örneğin "A1").

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataTable-1.cs" >}}

## **Dinamik nesne olarak veri kaynağından Excel'e Veri Aktarma**

Aspose.Cells, dinamik nesnelerle çalışmak için özellikler sağlar. Özelliklerin nesnelere dinamik olarak eklenmesine yardımcı olur. Özellikler nesneye eklenir eklenmez, Aspose.Cells ilk girişi şablon olarak kabul eder ve geri kalanı buna göre işler. Bu, bir dinamik özellik yalnızca ilk öğeye eklenirse ve diğer nesnelere eklenmezse, Aspose.Cells'ın tüm öğelerin aynı olması gerektiğini düşünmesi anlamına gelir.

Bu örnekte, başlangıçta yalnızca iki değişken içeren bir şablon model kullanılmaktadır. Bu Liste Listesi dinamik nesnelerin Liste'sine dönüştürülmüştür. Daha sonra buna bazı ek alan eklenir ve Son olarak Bildirime yüklenir. Excel, yalnızca şablon XLSX dosyasındaki değerleri alır. Bu şablon çalışma kitabı, ayrıca parametreler içeren Zeki İşaretçiler kullanır. Parametreler, bilgilerin nasıl düzenlendiğini değiştirmenize olanak tanır. Zeki İşaretçi hakkındaki ayrıntılar aşağıdaki makaleden elde edilebilir: 

[Akıllı İşaretçiler Kullanarak](/cells/tr/net/using-smart-markers/)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDynamicDataTable-1.cs" >}}

## **Excel'e DataColumn Nasıl İçe Aktarılır**

Bir *DataTable* ya da *DataView* nesnesi bir veya daha fazla sütundan oluşur. Geliştiriciler, *DataTable* ya da *DataView*'in herhangi bir Sütun/Sütunlar'ından veri içe aktarabilirler. *[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)* koleksiyonunun *[**ImportData**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index)* yöntemini çağırarak *DataTable* ya da *DataView* içeriğini içe aktarabilirler. *[**ImportData**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index)* yöntemi, *[**ImportTableOptions**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions)* türünde bir parametre alır. *[**ImportTableOptions**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions)* sınıfı, bir dizi sütun indeksini kabul eden *[**ColumnIndexes**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/columnindexes)* özelliği sağlar.

Aşağıdaki örnek kod, seçici sütunları içe aktarmak için *[**ImportTableOptions.ColumnIndexes**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/columnindexes)* kullanımını göstermektedir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataColumn-1.cs" >}}

## **Excel'e DataView Nasıl İçe Aktarılır**

*DataView*'den veri içe aktarmak için, *[**ImportData**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index)* koleksiyonunun *[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)* yöntemini çağırın. *[**ImportData**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index)* yönteminin birçok aşırı yüklenmiş sürümü bulunmaktadır ancak DataView için tipik bir aşırı yüklemenin aldığı parametreler şunlardır:

- **DataView:** İçeriği içe aktarmak istediğiniz *DataView* nesnesi.
- **İlk Satır:** Verinin içe aktarılacağı ilk hücrenin satır numarası.
- **İlk Sütun:** Verinin içe aktarılacağı ilk hücrenin sütun numarası.
- **ImportTableOptions:** İçe aktarma seçenekleri.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataView-1.cs" >}}

## **DataGrid Nasıl Excel'e İçe Aktarılır**

*DataGrid*'den veri içe aktarmak mümkündür, *[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)* koleksiyonunun *[**ImportDataGrid**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatagrid/index)* yöntemini çağırarak. *[**ImportDataGrid**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatagrid/index)* yönteminin birçok aşırı yüklenmiş sürümü bulunmaktadır ancak tipik bir aşırı yüklemenin aldığı parametreler şunlardır:

- **Data grid**, içerik içe aktardığınız *DataGrid* nesnesi.
- **Satır Numarası**, verinin içe aktarılacağı ilk hücrenin satır numarası.
- **Sütun Numarası**, verinin içe aktarılacağı ilk hücrenin sütun numarası.
- **Satırlar Ekle**, veriyi sığdırmak için çalışma sayfasına ekstra satır eklenip eklenmeyeceğini belirten Boolean özelliği.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataGrid-1.cs" >}}

## **GridView Nasıl Excel'e İçe Aktarılır**

*GridView* kontrolünden veri içe aktarmak için, *[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)* koleksiyonunun *[**ImportGridView**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importgridview)* yöntemini çağırın.

Aspose.Cells, veriyi elektronik tabloya içe aktarırken HTML biçimli değerleri dikkate almamıza olanak tanır. Verileri içe aktarırken HTML ayrıştırması etkinleştirildiğinde, Aspose.Cells HTML'i karşılık gelen hücre biçimlemesine dönüştürür.

## **HTML Biçimli Veriler Nasıl Excel'e İçe Aktarılır**

Aspose.Cells, dış veri kaynaklarından veri içe aktarmak için çok kullanışlı yöntemler sağlayan bir [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) sınıfı sağlar. Bu makale, veri içe aktarırken HTML biçimli metni ayrıştırma ve HTML'i biçimli hücre değerlerine dönüştürme işlemlerini göstermektedir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportHtmlFormattedData-1.cs" >}}

## **JSON'dan Excel'e Veri İçe Aktarma**

Aspose.Cells, JSON işleme için bir [**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) sınıfı sağlar. [**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) sınıfı, JSON verisini içe aktarmak için bir [**ImportData**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility/methods/importdata) yöntemine sahiptir. Aspose.Cells ayrıca, JSON düzeni seçeneklerini temsil eden bir [**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions) sınıfı sağlar. [**ImportData**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility/methods/importdata) yöntemi, bir parametre olarak [**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions) kabul eder. [**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions) sınıfı aşağıdaki özellikleri sağlar.

- [**ArrayAsTable**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/arrayastable): Array içindeki öğenin tablo olarak işlenip işlenmeyeceğini belirtir.
- [**ConvertNumericOrDate**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/convertnumericordate): JSON içindeki dizenin sayısal veya tarihsel bir değere dönüştürülüp dönüştürülmeyeceğini alır veya ayarlar.
- [**DateFormat**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/dateformat): Tarih değerinin biçimlendirilmesini alır ve ayarlar.
- [**IgnoreArrayTitle**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignorearraytitle): Nesnenin özelliği bir dizi ise başlığın dikkate alınıp alınmayacağını belirtir.
- [**IgnoreNull**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignorenull): null değerinin dikkate alınıp alınmayacağını belirler.
- [**IgnoreObjectTitle**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignoreobjecttitle): Nesnenin özelliği bir nesne ise başlığın dikkate alınıp alınmayacağını belirtir.
- [**NumberFormat**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/numberformat): Sayısal değerin biçimlendirmesini alır ve ayarlar.
- [**TitleStyle**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/titlestyle): Başlık stilini alır ve ayarlar.

Aşağıda verilen örnek kod, JSON verilerini içe aktarmak için [**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) ve [**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions) sınıflarının kullanımını göstermektedir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromJson-1.cs" >}}

## **Gelişmiş Konular**
- [Çalışma Sayfasına Veri İçeri Aktarırken Formül Alanlarını Belirt](/cells/tr/net/specify-formula-fields-while-importing-data-to-worksheet/)
- [Hücreler Veri Tablosu Satırlarını Eklerken İlk Satırı Aşağıya Kaydırma](/cells/tr/net/shift-first-row-down-when-inserting-cells-data-table-rows/)
