---
title: Verileri Çalışma Sayfasına Aktar
type: docs
weight: 170
url: /tr/net/import-data-into-worksheet/
description: Aspose.Cells for .NET API numaralı telefondan verileri Çalışma Sayfasına nasıl aktaracağınızı öğrenin.
keywords: C# Import Data into Worksheet, Import data into Excel with ICellsDataTable interface, Import data from Array, Import Data from ArrayList, Import Data from Custom Objects, Import Data from Custom Objects to merged area, Import Data from DataTable, Import Data from dynamic object as data source, Import Data from DataColumn, Import Data from DataView, Import Data from DataGrid, Import Data from GridView, Import HTML formatted data, Import Data Data from JSON
---
{{% alert color="primary" %}}

Bu makalede, geliştiricilerin Aspose.Cells aracılığıyla erişebildiği bazı veri içe aktarma teknikleri anlatılmaktadır.

{{% /alert %}}

##  **Verileri Çalışma Sayfasına Aktarma**

Aspose.Cells numaralı Excel dosyasını açtığınızda dosyadaki tüm veriler otomatik olarak içe aktarılır. Aspose.Cells ayrıca diğer veri kaynaklarından verileri de içe aktarabilir.

Aspose.Cells şunları sağlar:[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook)Microsoft Excel dosyasını temsil eden sınıf.[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook)sınıf bir içerir[**Çalışma sayfaları**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)Bir Excel dosyasındaki her çalışma sayfasına erişime izin veren koleksiyon. Bir çalışma sayfası şu şekilde temsil edilir:[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf.[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf sağlar[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)Toplamak.[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)toplama, farklı veri kaynaklarından verileri içe aktarmak için yararlı yöntemler sağlar. Bu makalede bu yöntemlerin nasıl kullanılabileceği açıklanmaktadır.

##  **ICellsDataTable arayüzü ile verileri Excel'e aktarma**
 Uygulamak[ICellsDataTable](https://reference.aspose.com/cells/net/aspose.cells/icellsdatatable) çeşitli veri kaynaklarınızı sarmak için kullanın ve ardından[Cells.ImportData()](https://reference.aspose.com/cells/net/aspose.cells/cells/importdata/#importdata) Verileri Excel çalışma sayfasına aktarmak için.
###  **Basit kod**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "ImportICellsDataTableIntoWorksheet.cs" >}}

uygulanması*CustomerDataSource*, *Customer* ve *CustomerList* sınıflar aşağıda verilmiştir

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-ICellsDataTableDataSourceForWorkbookDesigner-2.cs" >}}


##  **Diziden Excel'e Veri Nasıl Aktarılır**

 Bir diziden bir e-tabloya veri aktarmak için[**İçe Aktarma Dizisi**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importarray/index) yöntemi[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)Toplamak. Birçok aşırı yüklenmiş sürümü vardır.[**İçe Aktarma Dizisi**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importarray/index)yöntem ancak tipik bir aşırı yük aşağıdaki parametreleri alır:

- *Array**, içeriği içe aktardığınız dizi nesnesi.
- *Satır numarası**, verilerin aktarılacağı ilk hücrenin satır numarası.
- *Sütun numarası**, verilerin aktarılacağı ilk hücrenin sütun numarası.
- *Dikeydir**, verilerin dikey mi yoksa yatay olarak mı içe aktarılacağını belirten bir Boolean değeridir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromArray-1.cs" >}}

##  **ArrayList'ten Excel'e Veri Nasıl Aktarılır**

 Verileri bir dosyadan içe aktarmak için*Dizi Listesi* çalışma sayfalarına, arayın[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Koleksiyonun[**Dizi Listesini İçe Aktar**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importarraylist)yöntem. ImportArray yöntemi aşağıdaki parametreleri alır:

-  *Dizi listesi**,*Dizi Listesi*içe aktardığınız nesne.
- *Satır numarası**, verinin aktarılacağı ilk hücrenin satır numarasını temsil eder.
- *Sütun numarası**, verinin aktarılacağı ilk hücrenin sütun numarasını temsil eder.
- *Dikeydir**, verilerin dikey mi yoksa yatay olarak mı içe aktarılacağını belirten bir Boolean değeridir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromArrayList-1.cs" >}}

##  **Özel Nesnelerden Excel'e Veri Nasıl Aktarılır**

 Bir nesne koleksiyonundan verileri bir çalışma sayfasına aktarmak için şunu kullanın:[**Özel Nesneleri İçe Aktar**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importcustomobjects/index). İstediğiniz nesne listesini görüntülemek için yönteme bir sütun/özellik listesi sağlayın.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromCustomObject-1.cs" >}}

##  **Özel Nesnelerden birleştirilmiş alana Verileri Excel'e Aktarma**

Bir nesne koleksiyonundan birleştirilmiş hücreleri içeren bir çalışma sayfasına veri aktarmak için şunu kullanın:[**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/checkmergedcells) mülk. Excel şablonunda birleştirilmiş hücreler varsa değerini ayarlayın.[**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/checkmergedcells)özellik doğru. Geç[**Tablo Seçeneklerini İçe Aktar**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions) İstediğiniz nesne listesini görüntüleme yöntemine sütun/özellik listesiyle birlikte nesne ekleyin. Aşağıdaki kod örneği kullanımını gösterir:[**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/checkmergedcells) Özel Nesnelerden birleştirilmiş hücrelere veri aktarma özelliği. Lütfen eke bakın[kaynak Excel](90112033.xlsx) dosya ve[Excel'in çıktısı](90112034.xlsx) referans için dosya.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportCustomObjectsToMergedArea-1.cs" >}}

##  **DataTable'dan Excel'e Veri Nasıl Aktarılır**

*DataTable*'dan veri aktarmak için[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Koleksiyonun[**Veri Tablosunu İçe Aktar**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatatable/index) yöntem. Birçok aşırı yüklenmiş sürümü vardır.[**Veri Tablosunu İçe Aktar**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatatable/index)yöntem ancak tipik bir aşırı yük aşağıdaki parametreleri alır:

-  *Veri tablosu**,*Veri tablosu* İçeriği içe aktardığınız nesne.
-  *Alan adı gösteriliyor mu**, alan adlarının gösterilip gösterilmeyeceğini belirtir.*Veri tablosu*sütunlar çalışma sayfasına ilk satır olarak aktarılmalı veya aktarılmamalıdır.
- *Başlangıç hücresi**, *DataTable* içeriğinin içe aktarılacağı başlangıç hücresinin adını (örneğin "A1") temsil eder.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataTable-1.cs" >}}

##  **Veri kaynağı olarak dinamik nesneden Excel'e Veri Alma**

Aspose.Cells, veri kaynağı olarak dinamik nesnelerle çalışma özellikleri sağlar. Özelliklerin nesnelere dinamik olarak eklendiği veri kaynağının kullanılmasına yardımcı olur. Özellikler nesneye eklendiğinde, Aspose.Cells ilk girişi şablon olarak kabul eder ve gerisini buna göre işler. Bu, bazı dinamik özelliklerin yalnızca ilk öğeye eklenmesi ve diğer nesnelere eklenmemesi durumunda Aspose.Cells'in koleksiyondaki tüm öğelerin aynı olması gerektiğini dikkate aldığı anlamına gelir.

Bu örnekte başlangıçta yalnızca iki değişken içeren bir şablon model kullanılmıştır. Bu Liste, Dinamik nesnelerin listesine dönüştürülür. Daha sonra içine bazı ek alanlar eklenir ve son olarak çalışma kitabına yüklenir. Çalışma kitabı yalnızca şablon XLSX dosyasındaki değerleri seçer. Bu şablon çalışma kitabı, parametreleri de içeren Akıllı İşaretleyicileri kullanır. Parametreler bilgilerin düzenlenme şeklini değiştirmenize olanak tanır. Akıllı İşaretleyiciler ile ilgili detaylı bilgiye aşağıdaki makaleden ulaşabilirsiniz:

[Akıllı İşaretleyicileri Kullanma](/cells/tr/net/using-smart-markers/)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDynamicDataTable-1.cs" >}}

##  **DataColumn'dan Excel'e Veri Alma (.NET)**

A *Veri tablosu*veya*Veri görünümü*nesne bir veya daha fazla sütundan oluşur. Geliştiriciler ayrıca herhangi bir Sütundan/Sütunundan veri aktarabilir.*Veri tablosu*veya*Veri görünümü*arayarak[**Verileri İçe Aktar**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index) yöntemi[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)Toplamak.[**Verileri İçe Aktar**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index)yöntem türünde bir parametre kabul eder[**Tablo Seçeneklerini İçe Aktar**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions).[**Tablo Seçeneklerini İçe Aktar**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions) sınıf sağlar[**Sütun Dizinleri**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/columnindexes)bir dizi sütun dizini kabul eden özellik.

Aşağıda verilen örnek kod kullanımını göstermektedir.[**ImportTableOptions.ColumnIndexes**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/columnindexes)Seçici sütunları içe aktarmak için.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataColumn-1.cs" >}}

##  **DataView'dan Excel'e Veri Alma (.NET)**

 *DataView*'dan veri aktarmak için[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Koleksiyonun[**Verileri İçe Aktar**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index) yöntem. Birçok aşırı yüklenmiş sürümü vardır.[**Verileri İçe Aktar**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index)yöntem ancak DataView için olanı aşağıdaki parametreleri alır:

- **Veri görünümü:***Veri görünümü*İçeriği içe aktarmak üzere olduğunuz nesne.
- **İlk sıra:**verilerin aktarılacağı ilk hücrenin satır numarası.
- **İlk sütun:**verilerin aktarılacağı ilk hücrenin sütun numarası.
- **İçe Aktarma Tablosu Seçenekleri:**İçe aktarma seçenekleri.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataView-1.cs" >}}

##  **DataGrid'den Excel'e Veri Alma (.NET)**

 Verileri bir dosyadan içe aktarmak mümkündür.*Veri şebekesi* arayarak[**DataGrid'i İçe Aktar**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatagrid/index) yöntemi[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)Toplamak. Birçok aşırı yüklenmiş sürümü vardır.[**DataGrid'i İçe Aktar**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatagrid/index)yöntem ancak tipik bir aşırı yük aşağıdaki parametreleri alır:

-  *Veri kılavuzu**,*Veri şebekesi*İçeriği içe aktardığınız nesne.
- *Satır Numarası**, verilerin aktarılacağı ilk hücrenin satır numarası.
- *Sütun Numarası**, verilerin aktarılacağı ilk hücrenin sütun numarası.
- *Satır Ekle**, verileri sığdırmak için çalışma sayfasına fazladan satırların eklenmesi gerekip gerekmediğini belirten bir Boolean özelliği.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataGrid-1.cs" >}}

##  **GridView'dan Excel'e Veri Nasıl Aktarılır**

 Verileri bir dosyadan içe aktarmak için*Izgara Görünümü* kontrol edin, arayın[**Grid Görünümünü İçe Aktar**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importgridview) yöntemi[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)Toplamak.

Aspose.Cells, e-tabloya veri aktarırken HTML biçimlendirilmiş değerlerine uymamıza olanak tanır. Verileri içe aktarırken HTML ayrıştırma etkinleştirildiğinde, Aspose.Cells, HTML'i karşılık gelen hücre formatına dönüştürür.

##  **HTML formatlı verileri Excel'e nasıl aktarırım**

 Aspose.Cells şunları sağlar:[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)Harici veri kaynaklarından veri içe aktarmak için çok kullanışlı yöntemler sağlayan sınıf. Bu makalede, verileri içe aktarırken HTML biçimli metnin nasıl ayrıştırılacağı ve HTML'in biçimlendirilmiş hücre değerlerine nasıl dönüştürüleceği gösterilmektedir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportHtmlFormattedData-1.cs" >}}

##  **JSON'den Excel'e Veri Nasıl Aktarılır**

Aspose.Cells şunları sağlar:[**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) JSON'in işlenmesi için sınıf.[**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) sınıf var[**Verileri İçe Aktar**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility/methods/importdata) JSON verilerini içe aktarma yöntemi. Aspose.Cells ayrıca bir de sağlar[**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions) JSON düzeninin seçeneklerini temsil eden sınıf.[**Verileri İçe Aktar**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility/methods/importdata)yöntem kabul edilir[**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)parametre olarak.[**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)class aşağıdaki özellikleri sağlar.

- [**DiziAsTablo**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/arrayastable): Dizide tablo olarak işlenip işlenmeyeceğini belirtir.
- [**ConvertNumericOrDate**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/convertnumericordate): JSON'deki dizenin sayısala mı yoksa tarihe mi dönüştürüleceğini gösteren bir değer alır veya ayarlar.
- [**Tarih formatı**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/dateformat): Tarih değerinin biçimini alır ve ayarlar.
- [**IgnoreArrayTitle**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignorearraytitle): Nesnenin özelliği bir dizi ise başlığın yoksayılıp yok sayılmayacağını belirtir
- [**YoksayNull**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignorenull): Boş değerin göz ardı edilip edilmeyeceğini belirtir.
- [**NesneBaşlığını Yoksay**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignoreobjecttitle): Nesnenin özelliği bir nesne ise başlığın göz ardı edilip edilmeyeceğini belirtir.
- [**Sayı Formatı**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/numberformat): Sayısal değerin biçimini alır ve ayarlar.
- [**BaşlıkStil**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/titlestyle): Başlığın stilini alır ve ayarlar.

Aşağıda verilen örnek kod,[**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) Ve[**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)JSON verilerini içe aktaracak sınıflar.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromJson-1.cs" >}}

##  **İleri konular**
- [Verileri Çalışma Sayfasına Aktarırken Formül Alanlarını Belirleme](/cells/tr/net/specify-formula-fields-while-importing-data-to-worksheet/)
- [Cells Veri Tablosu Satırlarını eklerken İlk Satırı aşağı kaydır](/cells/tr/net/shift-first-row-down-when-inserting-cells-data-table-rows/)
