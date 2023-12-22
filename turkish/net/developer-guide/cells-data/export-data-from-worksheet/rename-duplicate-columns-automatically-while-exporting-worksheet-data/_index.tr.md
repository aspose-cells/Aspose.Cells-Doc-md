---
title: Çalışma sayfası verilerini dışa aktarırken yinelenen sütunları otomatik olarak yeniden adlandırın
type: docs
weight: 250
url: /tr/net/rename-duplicate-columns-automatically-while-exporting-worksheet-data/
description: Aspose.Cells for .NET API numaralı telefondan çalışma sayfası verilerini dışa aktarırken yinelenen sütunları otomatik olarak nasıl yeniden adlandıracağınızı öğrenin.
keywords: Rename duplicate columns while exporting worksheet data, Rename duplicate columns automatically while exporting  data to DataTable
---
##  **Olası Kullanım Senaryoları**

 Bazen kullanıcı, verileri çalışma sayfasından veri tablosuna aktarırken yinelenen sütunlar sorunuyla karşı karşıya kalır. DataTable'da yinelenen sütunlar bulunamayacağından, çalışma sayfası verilerini veri tablosuna aktarabilmeniz için yinelenen sütunların yeniden adlandırılması gerekir. Aspose.Cells, belirlediğiniz stratejiye göre yinelenen sütunları otomatik olarak yeniden adlandırabilir.[**ExportTableOptions.RenameStrategy**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/renamestrategy) mülk. Eğer belirtirseniz[**Yeniden AdlandırStrateji**](https://reference.aspose.com/cells/net/aspose.cells/renamestrategy) .Digit, sütunlar sütun1, sütun2, sütun3 vb. gibi yeniden adlandırılacaktır ve belirtirseniz[**Yeniden AdlandırStrateji**](https://reference.aspose.com/cells/net/aspose.cells/renamestrategy).Harf, ardından sütunlar sütunA, sütunB, sütunC vb. gibi yeniden adlandırılacaktır.

##  **Çalışma sayfası verilerini dışa aktarırken yinelenen sütunları otomatik olarak yeniden adlandırın**

Aşağıdaki örnek kod, çalışma sayfasının ilk üç sütununa bazı veriler ekler ancak tüm sütunlar aynı adı taşır; yani *Kişiler*. Daha sonra belirterek çalışma sayfasındaki verileri veri tablosuna aktarır.[**Yeniden AdlandırStrateji**](https://reference.aspose.com/cells/net/aspose.cells/renamestrategy).Mektup stratejisi. Daha sonra Aspose.Cells tarafından oluşturulan veri tablosunun sütun adlarını yazdırır. Aşağıdaki ekran görüntüsü, görselleştiricide dışa aktarılan verileri içeren veri tablosunu gösterir. Gördüğünüz gibi yinelenen sütunlar KişilerA, KişilerB vb. olarak yeniden adlandırıldı.

![yapılacak şey:image_alt_text](rename-duplicate-columns-automatically-while-exporting-worksheet-data_1.png)

##  **Basit kod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-RenameDuplicateColumnsAutomaticallyWhileExportingWorksheetData.cs" >}}

##  **Konsol Çıkışı**

Referans olması açısından yukarıdaki örnek kodun konsol çıktısını burada bulabilirsiniz.

{{< highlight "java" >}}

People

PeopleA

PeopleB

{{< /highlight >}}
