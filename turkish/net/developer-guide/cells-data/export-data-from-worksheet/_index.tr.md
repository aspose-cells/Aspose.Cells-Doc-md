---
title: .NET te Çalışma Sayfasından Veri Aktar
linktitle: Çalışma sayfasından veri aktarımı veya içe/dışa aktarımı nasıl yapılacağını açıklayan bu makalede C# kullanılarak veri datatable a aktarma veya oradan alma işlemleri anlatılır.
type: docs
weight: 180
url: /tr/net/export-data-from-worksheet/
description: C# ta Çalışma Sayfasından Veri Aktarımı, C# İçin Veri DataTable a Aktarım, Güçlü Yazılım Tipli Veri İçeren Sütunlar, Güçsüz Yazılım Tipli Veri İçeren Sütunlar, Kolon Adını Atlayacak Bayrakla Veri Aralığını Aktarma, Başlık İle Veri Aralığını Aktarma.
keywords: C# da Çalışma Sayfasından Veri Aktarımı, C# da Veriyi DataTable e Aktarı, Güçlü Tipli Veri İçeren Sütunlar, Güçsüz Tipli Veri İçeren Sütunlar, Sütun Adını Atlamak İçin Bayrakla Birlikte Aralık Aktarma, Başlık İle Aralık Aktarımı Nasıl Yapılır?
---

## Genel Bakış

Bu makale, C# kullanarak Çalışma Sayfası verilerinizi DataTable'a nasıl aktarılacağını açıklar. Aşağıdaki konuları kapsar

_Biçim_: **Excel**
- [C# Excel'den DataTable'a](#csharp-excel-to-datatable)
- [C# Excel'i DataTable'a Dönüştür](#csharp-convert-excel-to-datatable)
- [C# Excel'i DataTable'a İçe Aktar](#csharp-import-excel-to-datatable)
- [C# Excel'den DataTable'a Aktar](#csharp-export-to-datatable-from-excel)

_Biçim_: **XLS**
- [C# XLS'ten DataTable'a](#csharp-xls-to-datatable)
- [C# XLS'i DataTable'a Dönüştür](#csharp-convert-xls-to-datatable)
- [C# XLS'i DataTable'a İçe Aktar](#csharp-import-xls-to-datatable)
- [C# XLS'ten DataTable'a Aktar](#csharp-export-to-datatable-from-xls)

_Biçim_: **XLSX**
- [C# XLSX'ten DataTable'a](#csharp-xlsx-to-datatable)
- [C# XLSX'i DataTable'a Dönüştür](#csharp-convert-xlsx-to-datatable)
- [C# XLSX'i DataTable'a İçe Aktar](#csharp-import-xlsx-to-datatable)
- [C# XLSX'ten DataTable'a Aktar](#csharp-export-to-datatable-from-xlsx)

_Biçim_: **ODS**
- [C# ODS'ten DataTable'a](#csharp-ods-to-datatable)
- [C# ODS'i DataTable'a Dönüştür](#csharp-convert-ods-to-datatable)
- [C# ODS'i DataTable'a İçe Aktar](#csharp-import-ods-to-datatable)
- [C# ODS'ten DataTable'a Aktar](#csharp-export-to-datatable-from-ods)

## **C# Kullanarak Excel Verilerini Aktarma**

{{% alert color="primary" %}}

Bu makale, geliştiricilerin Aspose.Cells aracılığıyla erişimine sahip oldukları bazı veri aktarma tekniklerini ele almaktadır.

{{% /alert %}}

## **Çalışma Sayfasından Veri Aktarımı Nasıl Yapılır**

Aspose.Cells, kullanıcılarına sadece dış veri kaynaklarından çalışma sayfalarına veri aktarmakla kalmaz, aynı zamanda çalışma sayfası verilerini bir [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)'ye aktarmalarına da olanak tanır. [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)'nin ADO.NET'in bir parçası olduğunu ve veriyi tutmak için kullanıldığını biliyoruz. Veri bir [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)'ye depolandığında, kullanıcı gereksinimlerine göre herhangi bir şekilde kullanılabilir. Geliştiriciler, bu veriyi (bir [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)'de depolanan veri) istiyorlarsa doğrudan bir veritabanına da saklayabilirler. Bu nedenle, çalışma sayfası verilerini bir [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)'ye aktarmak, geliştiricilerin çalışma sayfası verisini manipüle etmelerini kolaylaştırır.

## **Aspose.Cells Kullanarak DataTable'a Veri Aktarma**

Geliştiriciler, çalışma sayfası verilerini bir [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) nesnesine çağırarak ya da [**ExportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index) veya [**ExportDataTableAsString**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatableasstring/index) yöntemlerini [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) sınıfının kullanarak kolayca aktarabilirler. Her iki yöntem de farklı senaryolarda kullanılır, bu senaryolar aşağıda daha detaylı bir şekilde tartışılmaktadır.

## **Güçlü-Tiplendirilmiş Veri İçeren Sütunlar**

Çalışma sayfası verilerini sıralı satır ve sütunlar olarak depoladığını biliyoruz. Bir çalışma sayfasının sütunlarında bulunan tüm değerler güçlü bir şekilde yazılmışsa (bu, bir sütundaki tüm değerlerin aynı veri türüne sahip olması anlamına gelir), o zaman çalışma sayfası içeriğini bir [**ExportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index)'ne [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) sınıfının [**ExportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index) yöntemini çağırarak aktarabiliriz. [**ExportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index) yöntemi, çalışma sayfası verilerini [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) nesnesi olarak aktarmak için aşağıdaki parametreleri alır:

- **Satır numarası**, İlk hücre verisinin dışa aktarılacağı satır numarası.
- **Sütun numarası**, Verinin dışa aktarılacağı ilk hücrenin sütun numarası.
- **Satır sayısı**, dışa aktarılacak satır sayısı.
- **Sütun sayısı**, dışa aktarılacak sütun sayısı.
- **Sütun adlarını dışa aktar**, İlk çalışma sayfasının verisinin [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) sütun adları olarak dışa aktarılıp aktarılmayacağını gösteren bir Boolean özelliği.

_Adımlar: Verileri DataTable'a Dışa Aktarma_

- <a name="csharp-excel-to-datatable" id="csharp-excel-to-datatable"><strong><em>Adımlar:</em> Excel to DataTable in C#</strong></a>
  - <a name="csharp-xls-to-datatable" id="csharp-xls-to-datatable"><strong><em>Adımlar:</em> XLS to DataTable in C#</strong></a>
  - <a name="csharp-xlsx-to-datatable" id="csharp-xlsx-to-datatable"><strong><em>Adımlar:</em> XLSX to DataTable in C#</strong></a>
  - <a name="csharp-ods-to-datatable" id="csharp-ods-to-datatable"><strong><em>Adımlar:</em> ODS to DataTable in C#</strong></a>
- <a name="csharp-convert-excel-to-datatable" id="csharp-convert-excel-to-datatable"><strong><em>Adımlar:</em> Convert Excel to DataTable in C#</strong></a>
  - <a name="csharp-convert-xls-to-datatable" id="csharp-convert-xls-to-datatable"><strong><em>Adımlar:</em> Convert XLS to DataTable in C#</strong></a>
  - <a name="csharp-convert-xlsx-to-datatable" id="csharp-convert-xlsx-to-datatable"><strong><em>Adımlar:</em> Convert XLSX to DataTable in C#</strong></a>
  - <a name="csharp-convert-ods-to-datatable" id="csharp-convert-ods-to-datatable"><strong><em>Adımlar:</em> Convert ODS to DataTable in C#</strong></a>
- <a name="csharp-import-excel-to-datatable" id="csharp-import-excel-to-datatable"><strong><em>Adımlar:</em> Import Excel to DataTable in C#</strong></a>
  - <a name="csharp-import-xls-to-datatable" id="csharp-import-xls-to-datatable"><strong><em>Adımlar:</em> Import XLS to DataTable in C#</strong></a>
  - <a name="csharp-import-xlsx-to-datatable" id="csharp-import-xlsx-to-datatable"><strong><em>Adımlar:</em> Import XLSX to DataTable in C#</strong></a>
  - <a name="csharp-import-ods-to-datatable" id="csharp-import-ods-to-datatable"><strong><em>Adımlar:</em> Import ODS to DataTable in C#</strong></a>
- <a name="csharp-export-to-datatable-from-excel" id="csharp-export-to-datatable-from-excel"><strong><em>Adımlar:</em> Export to DataTable from Excel in C#</strong></a>
  - <a name="csharp-export-to-datatable-from-xls" id="csharp-export-to-datatable-from-xls"><strong><em>Adımlar:</em> Export to DataTable from XLS in C#</strong></a>
  - <a name="csharp-export-to-datatable-from-xlsx" id="csharp-export-to-datatable-from-xlsx"><strong><em>Adımlar:</em> Export to DataTable from XLSX in C#</strong></a>
  - <a name="csharp-export-to-datatable-from-ods" id="csharp-export-to-datatable-from-ods"><strong><em>Adımlar:</em> Export to DataTable from ODS in C#</strong></a>

_Kod Adımları:_

1. Excel dosyanızı [Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook/) nesnesinde yükleyin.
   - [Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook/) nesnesi XLS, XLSX, XLSM, ODS vb. Excel dosyası biçimlerini yükleyebilir.
3. Excel dosyasındaki ilk [Worksheet](https://reference.aspose.com/cells/net/aspose.cells/worksheet/)'e erişin.
4. 1. **DataTable**'ın 1. hücresinden başlayarak 7 satır ve 2 sütun gibi dışa aktarım alanını seçin.
5. Veriyi DataTable'a dışa aktarmak için [ExportDataTable](https://reference.aspose.com/cells/net/aspose.cells/cells/exportdatatable/) yöntemini kullanın.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-ExportColumnContainingStronglyTypedData-1.cs" >}}

## **Güçlü-Tiplendirilmemiş Veri İçeren Sütunlar**

Bir çalışma sayfasındaki sütunlardaki tüm değerler güçlü bir türde değilse (bu, bir sütundaki değerlerin farklı veri tiplerine sahip olabileceği anlamına gelir), o zaman çalışma sayfası içeriğini [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) sınıfının [**ExportDataTableAsString**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatableasstring/index) yöntemini çağırarak dışa aktarabiliriz. [**ExportDataTableAsString**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatableasstring/index) yöntemi, çalışma sayfası verilerini bir [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) nesnesi olarak dışa aktarmak için aynı parametre setini alır. [**ExportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index) yöntemi.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-ExportColumnContainingNonStronglyTypedData-1.cs" >}}

## **Başlık ile Aralığı Dışa Aktarma Nasıl**

Bir aralıktan veri, dışa aktarılmak istenilen [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) yerine taşınabilir. Dışa aktarılan veride başlık satırının atlanmasına olanak tanıyan bir bayrak bulunmaktadır. Aşağıdaki kod, [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) için veri aralığını dışa aktarır ve içinde [**ExportColumnName**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/exportcolumnname) bayrağı bulunan [**ExportTableOptions**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions) argümanını içerir. Başlık bilgisi varsa, değer **true** olarak ayarlanır, bu nedenle veriye dahil edilmez ve başlık yoksa ve tüm satırların veri olarak kabul edilmesi gerekiyorsa, **false** olarak ayarlanır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-ExportRangeWithFlagToSkipColumnHeader-1.cs" >}}

## **Gelişmiş Konular**
- [Herhangi bir Biçimlendirme Olmadan Excel Verilerini DataTable'a Dışa Aktar](/cells/tr/net/export-excel-data-to-datatable-without-any-formatting/)
- [Hücrelerin HTML Dize Değerini DataTable'a Dışa Aktar](/cells/tr/net/export-html-string-value-of-the-cells-to-the-datatable/)
- [Çalışma Sayfasından Görünen Satırların Verilerini Dışa Aktar](/cells/tr/net/export-visible-rows-data-from-worksheet/)
- [Gizli Sütunları Dikkate Almadan Çalışma Sayfası Verilerini Data Table'a Dışa Aktarma](/cells/tr/net/ignore-hidden-columns-while-exporting-worksheet-data-to-data-table/)
- [Çalışma sayfası verileri dışa aktarılırken tekrarlanan sütunları otomatik olarak yeniden adlandırma](/cells/tr/net/rename-duplicate-columns-automatically-while-exporting-worksheet-data/)
