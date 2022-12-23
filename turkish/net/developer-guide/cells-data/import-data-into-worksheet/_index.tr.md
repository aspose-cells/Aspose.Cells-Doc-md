---
title: Verileri Çalışma Sayfasına Aktarın
type: docs
weight: 170
url: /tr/net/import-data-into-worksheet/
---
{{% alert color="primary" %}}

Bu makalede, geliştiricilerin Aspose.Cells aracılığıyla erişebildiği bazı veri içe aktarma teknikleri açıklanmaktadır.

{{% /alert %}}

## **Verileri Çalışma Sayfasına Aktarın**

Aspose.Cells ile bir Excel dosyasını açtığınızda, dosyadaki tüm veriler otomatik olarak içe aktarılır. Aspose.Cells, diğer veri kaynaklarından da veri alabilir.

Aspose.Cells bir sağlar[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook)Microsoft Excel dosyasını temsil eden sınıf. bu[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook)sınıf bir içerir[**çalışma sayfaları**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)bir Excel dosyasındaki her çalışma sayfasına erişim sağlayan koleksiyon. Bir çalışma sayfası şununla temsil edilir:[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf. bu[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf bir sağlar[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)Toplamak.[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)toplama, farklı veri kaynaklarından veri almak için yararlı yöntemler sağlar. Bu makalede, bu yöntemlerin nasıl kullanılabileceği açıklanmaktadır.

## **ICellsDataTable arabirimiyle verileri Excel'e aktarma**
 Uygulamak[ICellsDataTable](https://reference.aspose.com/cells/net/aspose.cells/icellsdatatable) çeşitli veri kaynaklarınızı sarmak için kullanın, ardından[Cells.ImportData()](https://reference.aspose.com/cells/net/aspose.cells/cells/importdata/#importdata) verileri Excel çalışma sayfasına aktarmak için.
### **Basit kod**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "ImportICellsDataTableIntoWorksheet.cs" >}}

uygulanması*Müşteri Veri Kaynağı*, *Müşteri*, ve*Müşteri listesi* sınıflar aşağıda verilmiştir

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-ICellsDataTableDataSourceForWorkbookDesigner-2.cs" >}}


## **Diziden İçe Aktarma**

 Bir diziden elektronik tabloya veri aktarmak için[**İçe Aktarma Dizisi**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importarray/index) yöntemi[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Toplamak. Programın aşırı yüklenmiş birçok versiyonu vardır.[**İçe Aktarma Dizisi**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importarray/index)yöntem ancak tipik bir aşırı yükleme aşağıdaki parametreleri alır:

- **Dizi**, içeriği içe aktardığınız dizi nesnesi.
- **Satır numarası**verilerin içe aktarılacağı ilk hücrenin satır numarası.
- **sütun numarası**, verilerin içe aktarılacağı ilk hücrenin sütun numarası.
- **dikey mi**, verilerin dikey mi yoksa yatay olarak mı içe aktarılacağını belirten bir Boole değeri.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromArray-1.cs" >}}

## **ArrayList'ten içe aktarma**

 Verileri içe aktarmak için bir*Dizi Listesi* çalışma sayfalarına[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) koleksiyonun[**ImportArrayList**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importarraylist)yöntem. ImportArray yöntemi aşağıdaki parametreleri alır:

- **dizi listesi** , temsil etmek*Dizi Listesi*içe aktardığınız nesne.
- **Satır numarası**, verilerin içe aktarılacağı ilk hücrenin satır numarasını temsil eder.
- **sütun numarası**, verilerin içe aktarılacağı ilk hücrenin sütun numarasını temsil eder.
- **dikey mi**, verilerin dikey mi yoksa yatay olarak mı içe aktarılacağını belirten bir Boole değeri.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromArrayList-1.cs" >}}

## **Özel Nesnelerden İçe Aktarma**

 Bir nesne koleksiyonundan bir çalışma sayfasına veri aktarmak için şunu kullanın:[**Özel Nesneleri İçe Aktar**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importcustomobjects/index). İstediğiniz nesne listesini görüntülemek için yönteme bir sütun/özellikler listesi sağlayın.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromCustomObject-1.cs" >}}

## **Özel Nesnelerden birleştirilmiş alana içe aktarma**

Nesne koleksiyonundan birleştirilmiş hücreler içeren bir çalışma sayfasına veri aktarmak için şunu kullanın:[**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/checkmergedcells) Emlak. Excel şablonunda birleştirilmiş hücreler varsa, değerini ayarlayın.[**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/checkmergedcells)özellik doğru. Geç[**ImportTableOptions**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions) istediğiniz nesne listesini görüntülemek için yönteme sütunlar/özellikler listesiyle birlikte nesne. Aşağıdaki kod örneği, kullanımını gösterir[**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/checkmergedcells) Özel Nesnelerden birleştirilmiş hücrelere veri aktarmak için özellik. Lütfen eke bakın[kaynak Excel](90112033.xlsx) dosya ve[Excel çıktısı](90112034.xlsx) referans için dosya.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportCustomObjectsToMergedArea-1.cs" >}}

## **DataTable'dan içe aktarma**

 Verileri içe aktarmak için bir*Veri tablosu* , ara[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) koleksiyonun[**ImportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatatable/index) yöntem. Programın aşırı yüklenmiş birçok versiyonu vardır.[**ImportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatatable/index)yöntem ancak tipik bir aşırı yükleme aşağıdaki parametreleri alır:

- **Veri tablosu** ,*Veri tablosu* İçeriği içe aktardığınız nesne.
- **alan adı gösteriliyor mu** , adlarının olup olmadığını belirtir*Veri tablosu*sütunlar çalışma sayfasına ilk satır olarak aktarılmalı veya alınmamalıdır.
- **Hücreyi başlat** , içeriğin içe aktarılacağı başlangıç hücresinin adını (örneğin "A1") temsil eder.*Veri tablosu*.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataTable-1.cs" >}}

## **Dinamik nesneden veri kaynağı olarak içe aktarma**

Aspose.Cells, dinamik nesnelerle veri kaynağı olarak çalışmak için özellikler sağlar. Özelliklerin nesnelere dinamik olarak eklendiği veri kaynağının kullanılmasına yardımcı olur. Özellikler nesneye eklendikten sonra, Aspose.Cells ilk girişi şablon olarak kabul eder ve gerisini buna göre işler. Bu, bazı dinamik özelliklerin yalnızca ilk öğeye eklenmesi ve diğer nesnelere eklenmemesi anlamına gelir, Aspose.Cells, koleksiyondaki tüm öğelerin aynı olması gerektiğini düşünür.

Bu örnekte, başlangıçta yalnızca iki değişken içeren bir şablon model kullanılmıştır. Bu Liste, dinamik nesnelerin Listesine dönüştürülür. Sonra içine bazı ek alanlar eklenir ve son olarak çalışma kitabına yüklenir. Çalışma kitabı yalnızca şablon XLSX dosyasındaki değerleri seçer. Bu şablon çalışma kitabı, parametreleri de içeren Akıllı İşaretleyiciler kullanır. Parametreler, bilgilerin düzenlenme şeklini değiştirmenize olanak tanır. Akıllı İşaretleyicilerle ilgili ayrıntılar aşağıdaki makaleden edinilebilir:

[Akıllı İşaretleyicileri Kullanma](/cells/tr/net/using-smart-markers/)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDynamicDataTable-1.cs" >}}

## **DataColumn'dan içe aktarma (.NET)**

A*Veri tablosu*veya*Veri görünümü*nesne bir veya daha fazla sütundan oluşur. Geliştiriciler ayrıca herhangi bir Sütundan/Sütunlardan veri alabilir.*Veri tablosu*veya*Veri görünümü*arayarak[**Verileri İçe Aktar**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index) yöntemi[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)Toplamak. bu[**Verileri İçe Aktar**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index)yöntem, türde bir parametre kabul eder[**ImportTableOptions**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions). bu[**ImportTableOptions**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions) sınıf bir sağlar[**Sütun Dizinleri**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/columnindexes)bir dizi sütun dizini kabul eden özellik.

Aşağıda verilen örnek kod,[**ImportTableOptions.ColumnIndexes**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/columnindexes) Seçici sütunları içe aktarmak için.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataColumn-1.cs" >}}

## **DataView'dan içe aktarma (.NET)**

 Verileri içe aktarmak için bir*Veri görünümü* , ara[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) koleksiyonun[**Verileri İçe Aktar**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index) yöntem. Programın aşırı yüklenmiş birçok versiyonu vardır.[**Verileri İçe Aktar**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index)yöntem ancak DataView için olan aşağıdaki parametreleri alır:

- **Veri görünümü:** bu*Veri görünümü*İçeriği aktarmak üzere olduğunuz nesne.
- **İlk sıra:**verilerin içe aktarılacağı ilk hücrenin satır numarası.
- **İlk sütun:**verilerin içe aktarılacağı ilk hücrenin sütun numarası.
- **ImportTableOptions:**İçe aktarma seçenekleri.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataView-1.cs" >}}

## **DataGrid'den içe aktarma (.NET)**

 Bir dosyadan veri almak mümkündür.*Veri şebekesi* arayarak[**ImportDataGrid**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatagrid/index) yöntemi[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Toplamak. Programın aşırı yüklenmiş birçok versiyonu vardır.[**ImportDataGrid**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatagrid/index)yöntem ancak tipik bir aşırı yükleme aşağıdaki parametreleri alır:

- **Veri şebekesi** ,*Veri şebekesi*İçeriği içe aktardığınız nesne.
- **Satır numarası**verilerin içe aktarılacağı ilk hücrenin satır numarası.
- **Sütun Numarası**, verilerin içe aktarılacağı ilk hücrenin sütun numarası.
- **Satır Ekle**, verileri sığdırmak için çalışma sayfasına fazladan satır eklenip eklenmeyeceğini gösteren bir Boolean özelliği.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataGrid-1.cs" >}}

## **GridView'dan içe aktarma**

 Verileri içe aktarmak için bir*Izgara Görünümü* kontrol, çağrı[**Grid Görünümünü İçe Aktar**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importgridview) yöntemi[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)Toplamak.

Aspose.Cells, elektronik tabloya veri aktarırken HTML biçimlendirilmiş değerlerine uymamızı sağlar. Verileri içe aktarırken HTML ayrıştırma etkinleştirildiğinde, Aspose.Cells, HTML'i karşılık gelen hücre biçimlendirmesine dönüştürür.

## **HTML biçimlendirilmiş verileri içe aktarma**

 Aspose.Cells bir sağlar[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)dış veri kaynaklarından veri almak için çok kullanışlı yöntemler sağlayan sınıf. Bu makale, verileri içe aktarırken HTML biçimlendirilmiş metnin nasıl ayrıştırılacağını ve HTML'in biçimlendirilmiş hücre değerlerine dönüştürülmesini gösterir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportHtmlFormattedData-1.cs" >}}

## **JSON'den Verileri İçe Aktarma**

Aspose.Cells bir sağlar[**Json Yardımcı Programı**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) işleme sınıfı JSON.[**Json Yardımcı Programı**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) sınıfın bir[**Verileri İçe Aktar**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility/methods/importdata) JSON verilerini içe aktarma yöntemi. Aspose.Cells ayrıca bir[**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions) JSON düzeninin seçeneklerini temsil eden sınıf. bu[**Verileri İçe Aktar**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility/methods/importdata)yöntem kabul eder[**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)parametre olarak. bu[**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)sınıf aşağıdaki özellikleri sağlar.

- [**DiziAsTablosu**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/arrayastable): Dizide tablo olarak işlenip işlenmeyeceğini belirtir.
- [**NümerikOrTarihi Dönüştür**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/convertnumericordate): JSON'deki dizenin sayısala mı yoksa tarihe mi dönüştürüleceğini gösteren bir değer alır veya ayarlar.
- [**Tarih formatı**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/dateformat): Tarih değerinin biçimini alır ve ayarlar.
- [**Dizi Başlığını Yoksay**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignorearraytitle): Nesnenin özelliği bir dizi ise, başlığın göz ardı edilip edilmeyeceğini belirtir
- [**YoksayNull**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignorenull): Boş değerin göz ardı edilip edilmeyeceğini gösterir.
- [**Nesne Başlığını Yoksay**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignoreobjecttitle): Nesnenin özelliği bir nesne ise, başlığın göz ardı edilip edilmeyeceğini belirtir.
- [**Sayı Biçimi**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/numberformat): Sayısal değerin biçimini alır ve ayarlar.
- [**BaşlıkStil**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/titlestyle): Başlığın stilini alır ve ayarlar.

Aşağıda verilen örnek kod,[**Json Yardımcı Programı**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) ve[**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions) JSON verilerini içe aktarmak için sınıflar.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromJson-1.cs" >}}

## **ileri konular**
- [Verileri Çalışma Sayfasına Aktarırken Formül Alanlarını Belirtin](/cells/tr/net/specify-formula-fields-while-importing-data-to-worksheet/)
- [Cells Veri Tablosu Satırlarını eklerken İlk Satırı aşağı kaydır](/cells/tr/net/shift-first-row-down-when-inserting-cells-data-table-rows/)
