---
title: .NET'deki Çalışma Sayfasından Verileri Dışa Aktar
linktitle: Çalışma Sayfasından Verileri Dışa Aktarma
type: docs
weight: 180
url: /tr/net/export-data-from-worksheet/
description: Bu makalede, C# kullanılarak çalışma sayfasındaki verilerin nasıl veri tablosuna aktarılacağı veya alınacağı açıklanmaktadır.
---
## genel bakış

Bu makale, Çalışma Sayfası verilerinizi C# kullanarak DataTable'a nasıl aktaracağınızı açıklar. Aşağıdaki konuları kapsar.

_Biçim_: **excel**
- [C# Excel'den DataTable'a](#csharp-excel-to-datatable)
- [C# Excel'i DataTable'a Dönüştür](#csharp-convert-excel-to-datatable)
- [C# Excel'i DataTable'a Aktar](#csharp-import-excel-to-datatable)
- [C# Excel'den DataTable'a Aktar](#csharp-export-to-datatable-from-excel)

_Biçim_: **XLS**
- [C# XLS'den DataTable'a](#csharp-xls-to-datatable)
- [C# XLS'yi DataTable'a Dönüştür](#csharp-convert-xls-to-datatable)
- [C# XLS'yi DataTable'a Aktar](#csharp-import-xls-to-datatable)
- [C# XLS'den DataTable'a Aktar](#csharp-export-to-datatable-from-xls)

_Biçim_: **XLSX**
- [C# XLSX'ten DataTable'a](#csharp-xlsx-to-datatable)
- [C# XLSX'i DataTable'a Dönüştür](#csharp-convert-xlsx-to-datatable)
- [C# XLSX'i DataTable'a Aktar](#csharp-import-xlsx-to-datatable)
- [C# XLSX'ten DataTable'a Aktar](#csharp-export-to-datatable-from-xlsx)

_Biçim_: **ODS**
- [C# ODS'den DataTable'a](#csharp-ods-to-datatable)
- [C# ODS'yi DataTable'a Dönüştür](#csharp-convert-ods-to-datatable)
- [C# ODS'yi DataTable'a Aktar](#csharp-import-ods-to-datatable)
- [C# ODS'den DataTable'a Aktar](#csharp-export-to-datatable-from-ods)

## **C# Excel Verilerini Dışa Aktar**

{{% alert color="primary" %}}

Bu makalede, geliştiricilerin Aspose.Cells aracılığıyla erişebildiği bazı veri dışa aktarma teknikleri ele alınmaktadır.

{{% /alert %}}

## **Çalışma Sayfasından Verileri Dışa Aktarma**

 Aspose.Cells, kullanıcılarının yalnızca harici veri kaynaklarından çalışma sayfalarına veri almalarını kolaylaştırmakla kalmaz, aynı zamanda çalışma sayfası verilerini bir[**Veri tablosu**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) . bildiğimiz gibi[**Veri tablosu**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) ADO.NET'in bir parçasıdır ve verileri tutmak için kullanılır. Veriler bir kez depolandığında[**Veri tablosu**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) , kullanıcıların gereksinimlerine göre herhangi bir şekilde kullanılabilir. Geliştiriciler ayrıca bu verileri (içinde depolanan) depolayabilir.[**Veri tablosu**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) ) isterlerse doğrudan bir veritabanına. Dolayısıyla, çalışma sayfası verilerini bir bilgisayara aktarılırsa, geliştiricilerin bunları manipüle etmesinin daha kolay hale geldiğini görebiliriz.[**Veri tablosu**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8).

## **Aspose.Cells Kullanarak Verileri DataTable'a Aktarma**

Geliştiriciler, çalışma sayfası verilerini kolayca dışa aktarabilir.[**Veri tablosu**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) birini çağırarak nesne[**ExportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index) veya[**ExportDataTableAsString**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatableasstring/index) yöntemi[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)sınıf. Her iki yöntem de aşağıda daha ayrıntılı olarak tartışılan farklı senaryolarda kullanılmaktadır.

## **Kesinlikle Yazılmış Verileri İçeren Sütunlar**

 Bir elektronik tablonun verileri bir dizi satır ve sütun olarak sakladığını biliyoruz. Bir çalışma sayfasının sütunlarındaki tüm değerler kesin olarak yazılmışsa (bu, bir sütundaki tüm değerlerin aynı veri türüne sahip olması gerektiği anlamına gelir), o zaman çalışma sayfasının içeriğini çağırarak dışa aktarabiliriz.[**ExportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index) yöntemi[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) sınıf.[**ExportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index) yöntem, çalışma sayfası verilerini şu şekilde dışa aktarmak için aşağıdaki parametreleri alır:[**Veri tablosu**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)nesne:

- **Satır numarası**, verinin dışa aktarılacağı ilk hücrenin satır numarası.
- **sütun numarası**, verilerin dışa aktarılacağı ilk hücrenin sütun numarası.
- **Satır sayısı**, dışa aktarılacak satır sayısı.
- **Sütun sayısı**, dışa aktarılacak sütun sayısı.
- **Sütun adlarını dışa aktar** çalışma sayfasının ilk satırındaki verilerin, çalışma sayfasının sütun adları olarak dışa aktarılıp aktarılmayacağını belirten bir Boolean özelliğidir.[**Veri tablosu**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)ya da değil.

_Adımlar: Verileri DataTable'a Aktarma_

- <a name="csharp-excel-to-datatable" id="csharp-excel-to-datatable"><strong><em>Adımlar:</em> C#'de Excel'den DataTable'a</strong></a>
  - <a name="csharp-xls-to-datatable" id="csharp-xls-to-datatable"><strong><em>Adımlar:</em> C#'de XLS'den DataTable'a</strong></a>
  - <a name="csharp-xlsx-to-datatable" id="csharp-xlsx-to-datatable"><strong><em>Adımlar:</em> C#'de XLSX'ten DataTable'a</strong></a>
  - <a name="csharp-ods-to-datatable" id="csharp-ods-to-datatable"><strong><em>Adımlar:</em> C#'de ODS'den DataTable'a</strong></a>
- <a name="csharp-convert-excel-to-datatable" id="csharp-convert-excel-to-datatable"><strong><em>Adımlar:</em> C#'de Excel'i DataTable'a dönüştürün</strong></a>
  - <a name="csharp-convert-xls-to-datatable" id="csharp-convert-xls-to-datatable"><strong><em>Adımlar:</em> C#'de XLS'yi DataTable'a dönüştürün</strong></a>
  - <a name="csharp-convert-xlsx-to-datatable" id="csharp-convert-xlsx-to-datatable"><strong><em>Adımlar:</em> C#'de XLSX'i DataTable'a dönüştürün</strong></a>
  - <a name="csharp-convert-ods-to-datatable" id="csharp-convert-ods-to-datatable"><strong><em>Adımlar:</em> C#'de ODS'yi DataTable'a dönüştürün</strong></a>
- <a name="csharp-import-excel-to-datatable" id="csharp-import-excel-to-datatable"><strong><em>Adımlar:</em> C#'de Excel'i DataTable'a aktarın</strong></a>
  - <a name="csharp-import-xls-to-datatable" id="csharp-import-xls-to-datatable"><strong><em>Adımlar:</em> C#'de XLS'yi DataTable'a aktarın</strong></a>
  - <a name="csharp-import-xlsx-to-datatable" id="csharp-import-xlsx-to-datatable"><strong><em>Adımlar:</em> C#'de XLSX'i DataTable'a aktarın</strong></a>
  - <a name="csharp-import-ods-to-datatable" id="csharp-import-ods-to-datatable"><strong><em>Adımlar:</em> C#'de ODS'yi DataTable'a aktarın</strong></a>
- <a name="csharp-export-to-datatable-from-excel" id="csharp-export-to-datatable-from-excel"><strong><em>Adımlar:</em> C#'de Excel'den DataTable'a Aktar</strong></a>
  - <a name="csharp-export-to-datatable-from-xls" id="csharp-export-to-datatable-from-xls"><strong><em>Adımlar:</em> C#'de XLS'den DataTable'a aktarın</strong></a>
  - <a name="csharp-export-to-datatable-from-xlsx" id="csharp-export-to-datatable-from-xlsx"><strong><em>Adımlar:</em> C#'de XLSX'ten DataTable'a aktarın</strong></a>
  - <a name="csharp-export-to-datatable-from-ods" id="csharp-export-to-datatable-from-ods"><strong><em>Adımlar:</em> C#'de ODS'den DataTable'a aktarın</strong></a>

_Kod Adımları:_

1.  Excel dosyanızı içine yükleyin[Çalışma kitabı](https://reference.aspose.com/cells/net/aspose.cells/workbook/) nesne.
   - [Çalışma kitabı](https://reference.aspose.com/cells/net/aspose.cells/workbook/)nesne, XLS, XLSX, XLSM, ODS vb. gibi Excel dosya biçimlerini yükleyebilir.
 3. İlkine erişin[Çalışma kağıdı](https://reference.aspose.com/cells/net/aspose.cells/worksheet/) Excel dosyasında.
 4. Dışa aktarma alanınızı seçin, örneğin 1. hücreden başlayarak 7 satır ve 2 sütun**Veri tablosu**.
 5. Kullanım[ExportDataTable](https://reference.aspose.com/cells/net/aspose.cells/cells/exportdatatable/) verileri DataTable'a aktarma yöntemi.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-ExportColumnContainingStronglyTypedData-1.cs" >}}

## **Kesinlikle Yazılmamış Veriler İçeren Sütunlar**

 Bir çalışma sayfasının sütunlarındaki tüm değerler kesin olarak yazılmamışsa (bu, bir sütundaki değerlerin farklı veri türlerine sahip olabileceği anlamına gelir), o zaman çalışma sayfasının içeriğini çağırarak dışarı aktarabiliriz.[**ExportDataTableAsString**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatableasstring/index) yöntemi[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) sınıf.[**ExportDataTableAsString**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatableasstring/index)yöntemi ile aynı parametre kümesini alır.[**ExportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index)çalışma sayfası verilerini dışa aktarma yöntemi[**Veri tablosu**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)nesne.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-ExportColumnContainingNonStronglyTypedData-1.cs" >}}

## **Sütun adını atlamak için Bayraklı Aralığı Dışa Aktar**

 Bir aralıktaki veriler şuraya aktarılabilir:[**Veri tablosu**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) dışa aktarılan verilerde başlık satırını atlamak için bir bayrağın mevcut olduğu yer. Aşağıdaki kod, bir dizi veriyi dışa aktarır:[**Veri tablosu**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) bir tartışma ile[**Dışa Aktarma Tablosu Seçenekleri**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions) içeren[**Dışa Aktarma SütunuAdı**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/exportcolumnname) bayrak. ayarlandı**doğru**başlık bilgisi varsa, bu nedenle verilere dahil edilmeyecek ve**yanlış** başlık yoksa ve tüm satırlar veri olarak kabul edilecekse.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-ExportRangeWithFlagToSkipColumnHeader-1.cs" >}}

## **ileri konular**
- [Excel Verilerini Formatlamadan DataTable'a Aktarın](/cells/tr/net/export-excel-data-to-datatable-without-any-formatting/)
- [Cells'in HTML Dizesi Değerini DataTable'a Aktarın](/cells/tr/net/export-html-string-value-of-the-cells-to-the-datatable/)
- [Görünür Satır Verilerini Çalışma Sayfasından Dışa Aktarma](/cells/tr/net/export-visible-rows-data-from-worksheet/)
- [Çalışma Sayfası Verilerini Veri Tablosuna Aktarırken Gizli Sütunları Yoksay](/cells/tr/net/ignore-hidden-columns-while-exporting-worksheet-data-to-data-table/)
- [Çalışma sayfası verilerini dışa aktarırken yinelenen sütunları otomatik olarak yeniden adlandırın](/cells/tr/net/rename-duplicate-columns-automatically-while-exporting-worksheet-data/)
