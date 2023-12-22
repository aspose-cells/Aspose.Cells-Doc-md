---
title: .NET'deki Çalışma Sayfasından Verileri Dışa Aktar
linktitle: Verileri Çalışma Sayfasından Dışa Aktarma
type: docs
weight: 180
url: /tr/net/export-data-from-worksheet/
description: Bu makalede, C# kullanılarak çalışma sayfasındaki verilerin veri tablosuna nasıl aktarılacağı veya içe aktarılacağı açıklanmaktadır.
keywords: C# Export Data from Worksheet, C# Export Data to DataTable, Columns Containing Strongly Typed Data, Columns Containing Non-Strongly Typed Data, C# Export Range with flag to skip column name
---
##  Genel Bakış

Bu makalede Çalışma Sayfası verilerinizin C#'i kullanarak DataTable'a nasıl aktarılacağı açıklanmaktadır. Aşağıdaki konuları kapsar.

 _Biçim_:**excel**
- [C# Excel'den DataTable'a](#csharp-excel-to-datatable)
- [C# Excel'i DataTable'a dönüştürün](#csharp-convert-excel-to-datatable)
- [C# Excel'i DataTable'a aktar](#csharp-import-excel-to-datatable)
- [C# Excel'den DataTable'a aktarın](#csharp-export-to-datatable-from-excel)

 _Biçim_:**XLS**
- [C# XLS'den DataTable'a](#csharp-xls-to-datatable)
- [C# XLS'i DataTable'a dönüştürün](#csharp-convert-xls-to-datatable)
- [C# XLS'i DataTable'a aktar](#csharp-import-xls-to-datatable)
- [C# XLS'den DataTable'a aktar](#csharp-export-to-datatable-from-xls)

 _Biçim_:**XLSX**
- [C# XLSX'den DataTable'a](#csharp-xlsx-to-datatable)
- [C# XLSX'i DataTable'a dönüştürün](#csharp-convert-xlsx-to-datatable)
- [C# XLSX'i DataTable'a aktar](#csharp-import-xlsx-to-datatable)
- [C# XLSX'den DataTable'a aktar](#csharp-export-to-datatable-from-xlsx)

 _Biçim_:**ODS**
- [C# ODS'den DataTable'a](#csharp-ods-to-datatable)
- [C# ODS'i DataTable'a dönüştürün](#csharp-convert-ods-to-datatable)
- [C# ODS'i DataTable'a aktar](#csharp-import-ods-to-datatable)
- [C# ODS'den DataTable'a aktar](#csharp-export-to-datatable-from-ods)

##  **C# Kullanarak Excel Verilerini Dışa Aktarma**

{{% alert color="primary" %}}

Bu makalede, geliştiricilerin Aspose.Cells aracılığıyla erişebildiği bazı veri dışa aktarma teknikleri anlatılmaktadır.

{{% /alert %}}

##  **Çalışma Sayfasından Veri Nasıl Dışa Aktarılır**

 Aspose.Cells, kullanıcılarının yalnızca harici veri kaynaklarından çalışma sayfalarına veri aktarmalarını kolaylaştırmakla kalmaz, aynı zamanda çalışma sayfası verilerini bir[**Veri tablosu**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) . Bunu bildiğimize göre[**Veri tablosu**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) ADO.NET'in bir parçasıdır ve verileri tutmak için kullanılır. Veriler bir yerde saklandıktan sonra[**Veri tablosu**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) Kullanıcıların gereksinimlerine göre istenilen şekilde kullanılabilir. Geliştiriciler ayrıca bu verileri de saklayabilir ([**Veri tablosu**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) ) isterlerse doğrudan bir veritabanına. Dolayısıyla, çalışma sayfası verilerinin bir bilgisayara aktarılması durumunda geliştiricilerin bunları işlemesinin daha kolay hale geldiğini görebiliriz.[**Veri tablosu**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8).

##  **Aspose.Cells Kullanarak Verileri DataTable'a Dışa Aktarma**

 Geliştiriciler çalışma sayfası verilerini kolayca bir[**Veri tablosu**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) ikisini de arayarak nesne[**Veri Tablosunu Dışa Aktar**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index) veya[**ExportDataTableAsString**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatableasstring/index) yöntemi[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)sınıf. Her iki yöntem de aşağıda daha ayrıntılı olarak ele alınan farklı senaryolarda kullanılır.

##  **Kesinlikle Yazılan Verileri İçeren Sütunlar**

 Bir e-tablonun verileri bir dizi satır ve sütun halinde sakladığını biliyoruz. Bir çalışma sayfasının sütunlarındaki tüm değerler kesin olarak yazılmışsa (bu, bir sütundaki tüm değerlerin aynı veri türüne sahip olması gerektiği anlamına gelir), o zaman çalışma sayfasının içeriğini şu komutu çağırarak dışa aktarabiliriz:[**Veri Tablosunu Dışa Aktar**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index) yöntemi[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) sınıf.[**Veri Tablosunu Dışa Aktar**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index) yöntem, çalışma sayfası verilerini şu şekilde dışa aktarmak için aşağıdaki parametreleri alır:[**Veri tablosu**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)nesne:

- *Satır numarası**, dışa aktarılacak ilk hücre verisinin satır numarasıdır.
- *Sütun numarası**, verilerin dışa aktarılacağı ilk hücrenin sütun numarası.
- *Satır sayısı**, dışa aktarılacak satır sayısı.
- *Sütun sayısı**, dışa aktarılacak sütun sayısı.
- *Sütun adlarını dışa aktar**; çalışma sayfasının ilk satırındaki verilerin sütun adları olarak dışa aktarılıp aktarılmayacağını belirten bir Boolean özelliği.[**Veri tablosu**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)ya da değil.

_Adımlar: Verileri DataTable'a Aktarma_

- <a name="csharp-excel-to-datatable" id="csharp-excel-to-datatable"><strong><em>Adımlar:</em> C#'de Excel'den DataTable'a</strong></a>
  - <a name="csharp-xls-to-datatable" id="csharp-xls-to-datatable"><strong><em>Adımlar:</em> XLS'den C#'deki DataTable'a</strong></a>
  - <a name="csharp-xlsx-to-datatable" id="csharp-xlsx-to-datatable"><strong><em>Adımlar:</em> XLSX'den C#'deki DataTable'a</strong></a>
  - <a name="csharp-ods-to-datatable" id="csharp-ods-to-datatable"><strong><em>Adımlar:</em> ODS'den C#'deki DataTable'a</strong></a>
- <a name="csharp-convert-excel-to-datatable" id="csharp-convert-excel-to-datatable"><strong><em>Adımlar:</em> C#'de Excel'i DataTable'a dönüştürün</strong></a>
  - <a name="csharp-convert-xls-to-datatable" id="csharp-convert-xls-to-datatable"><strong><em>Adımlar:</em> XLS'i C#'deki DataTable'a dönüştürün</strong></a>
  - <a name="csharp-convert-xlsx-to-datatable" id="csharp-convert-xlsx-to-datatable"><strong><em>Adımlar:</em> XLSX'i C#'deki DataTable'a dönüştürün</strong></a>
  - <a name="csharp-convert-ods-to-datatable" id="csharp-convert-ods-to-datatable"><strong><em>Adımlar:</em> ODS'i C#'deki DataTable'a dönüştürün</strong></a>
- <a name="csharp-import-excel-to-datatable" id="csharp-import-excel-to-datatable"><strong><em>Adımlar:</em> C#'de Excel'i DataTable'a aktarın</strong></a>
  - <a name="csharp-import-xls-to-datatable" id="csharp-import-xls-to-datatable"><strong><em>Adımlar:</em> XLS'i C#'deki DataTable'a aktarın</strong></a>
  - <a name="csharp-import-xlsx-to-datatable" id="csharp-import-xlsx-to-datatable"><strong><em>Adımlar:</em> XLSX'i C#'deki DataTable'a aktarın</strong></a>
  - <a name="csharp-import-ods-to-datatable" id="csharp-import-ods-to-datatable"><strong><em>Adımlar:</em> ODS'i C#'deki DataTable'a aktarın</strong></a>
- <a name="csharp-export-to-datatable-from-excel" id="csharp-export-to-datatable-from-excel"><strong><em>Adımlar:</em> C#'de Excel'den DataTable'a aktarın</strong></a>
  - <a name="csharp-export-to-datatable-from-xls" id="csharp-export-to-datatable-from-xls"><strong><em>Adımlar:</em> C#'de XLS'den DataTable'a aktar</strong></a>
  - <a name="csharp-export-to-datatable-from-xlsx" id="csharp-export-to-datatable-from-xlsx"><strong><em>Adımlar:</em> C#'de XLSX'den DataTable'a aktar</strong></a>
  - <a name="csharp-export-to-datatable-from-ods" id="csharp-export-to-datatable-from-ods"><strong><em>Adımlar:</em> C#'de ODS'den DataTable'a aktar</strong></a>

_Kod Adımları:_

1.  Excel dosyanızı yükleyin[Çalışma kitabı](https://reference.aspose.com/cells/net/aspose.cells/workbook/) nesne.
   - [Çalışma kitabı](https://reference.aspose.com/cells/net/aspose.cells/workbook/) nesne, örneğin XLS, XLSX, XLSM, ODS vb. Excel dosya formatlarını yükleyebilir.
 3. İlkine erişin[Çalışma kağıdı](https://reference.aspose.com/cells/net/aspose.cells/worksheet/) Excel dosyasında.
4. Dışa aktarma alanınızı seçin; örneğin *DataTable**'ın 1. hücresinden başlayarak 7 satır ve 2 sütun.
 5. Kullan[Veri Tablosunu Dışa Aktar](https://reference.aspose.com/cells/net/aspose.cells/cells/exportdatatable/) Verileri DataTable'a aktarma yöntemi.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-ExportColumnContainingStronglyTypedData-1.cs" >}}

##  **Kesin Olarak Yazılmamış Veriler İçeren Sütunlar**

 Bir çalışma sayfasının sütunlarındaki tüm değerler kesin olarak yazılmamışsa (bu, bir sütundaki değerlerin farklı veri türlerine sahip olabileceği anlamına gelir), o zaman çalışma sayfasının içeriğini şu komutu çağırarak dışa aktarabiliriz:[**ExportDataTableAsString**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatableasstring/index) yöntemi[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) sınıf.[**ExportDataTableAsString**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatableasstring/index)yöntem, yöntem ile aynı parametre kümesini alır.[**Veri Tablosunu Dışa Aktar**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index)çalışma sayfası verilerini dışa aktarma yöntemi[**Veri tablosu**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)nesne.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-ExportColumnContainingNonStronglyTypedData-1.cs" >}}

##  **Sütun adını atlamak için Aralığı bayrakla Dışa Aktarma**

 Bir aralıktaki veriler şuraya aktarılabilir:[**Veri tablosu**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) Dışa aktarılan verilerde başlık satırını atlamak için bir bayrağın mevcut olduğu yer. Aşağıdaki kod bir dizi veriyi dışa aktarır[**Veri tablosu**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) bir argümanla[**Tabloyu Dışa Aktarma Seçenekleri**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions) hangisini içerir[**Dışa Aktarılan SütunAdı**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/exportcolumnname) bayrak. Şu şekilde ayarlandı:**doğru** başlık bilgisi varsa, bu nedenle verilere dahil edilmeyecek ve şu şekilde ayarlanmayacaktır:**YANLIŞ** başlık yoksa ve tüm satırlar veri olarak kabul edilecekse.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-ExportRangeWithFlagToSkipColumnHeader-1.cs" >}}

##  **İleri konular**
- [Excel Verilerini herhangi bir Biçimlendirme olmadan DataTable'a aktarma](/cells/tr/net/export-excel-data-to-datatable-without-any-formatting/)
- [Cells'in HTML Dize Değerini DataTable'a aktarın](/cells/tr/net/export-html-string-value-of-the-cells-to-the-datatable/)
- [Görünür Satır Verilerini Çalışma Sayfasından Dışa Aktarma](/cells/tr/net/export-visible-rows-data-from-worksheet/)
- [Çalışma Sayfası Verilerini Veri Tablosuna Aktarırken Gizli Sütunları Yoksay](/cells/tr/net/ignore-hidden-columns-while-exporting-worksheet-data-to-data-table/)
- [Çalışma sayfası verilerini dışa aktarırken yinelenen sütunları otomatik olarak yeniden adlandırın](/cells/tr/net/rename-duplicate-columns-automatically-while-exporting-worksheet-data/)
