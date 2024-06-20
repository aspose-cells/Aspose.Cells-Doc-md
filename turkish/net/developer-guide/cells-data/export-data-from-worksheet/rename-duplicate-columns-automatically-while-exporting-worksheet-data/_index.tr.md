---
title: Çalışsayede veriyi aktarırken yinelenen sütunları otomatik olarak yeniden adlandır
type: docs
weight: 250
url: /tr/net/rename-duplicate-columns-automatically-while-exporting-worksheet-data/
description: Aspose.Cells for .NET API aracılığıyla Çalışsayede Veriyi Aktarırken Otomatik Olarak Yinelenen Sütunları Yeniden Adlandırmayı Öğrenin.
keywords: Excel çalışsayesinden veriyi data table a aktarırken yinelenen sütunları yeniden adlandırın, Otomatik olarak yenilenen sütunları data table a aktarırken yeniden adlandırın
---

## **Olası Kullanım Senaryoları**

Kullanıcı bazen çalışsayedeki veriyi data table'a aktarırken yinelenen sütunlar problemiyle karşılaşır. DataTable yinelenen sütunlara sahip olamaz, bu nedenle çalışsayedeki veriyi data table'a aktarmadan önce yinelenen sütunların adı değiştirilmelidir. Aspose.Cells, [**ExportTableOptions.RenameStrategy**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/renamestrategy) özelliği ile belirttiğiniz stratejiye göre yinelenen sütunları otomatik olarak yeniden adlandırabilir. [**RenameStrategy**](https://reference.aspose.com/cells/net/aspose.cells/renamestrategy).Digit belirtirseniz, sütunlar column1, column2, column3 vb. gibi adlandırılacak ve [**RenameStrategy**](https://reference.aspose.com/cells/net/aspose.cells/renamestrategy).Letter belirtirseniz sütunlar columnA, columnB, columnC vb. olarak yeniden adlandırılacaktır.

## **Çalışma sayfası verileri dışa aktarılırken tekrarlanan sütunları otomatik olarak yeniden adlandırma**

Aşağıdaki örnek kod, çalışsayenin ilk üç sütununa bazı veriler ekler, ancak tüm sütunlar aynı adı yani *Kişiler* adını taşır. Daha sonra, [**RenameStrategy**](https://reference.aspose.com/cells/net/aspose.cells/renamestrategy).Letter stratejisini belirterek çalışsayedeki veriyi data table'e aktarır. Ardından, Aspose.Cells tarafından oluşturulan data table'ın sütun adlarını yazdırır. Aşağıdaki ekran görüntüsü, görselleştirmeli olarak veri tablosundaki aktarılmış veriyi gösterir. Görebileceğiniz gibi, yinelenen sütunlar PeopleA, PeopleB vb. şeklinde yeniden adlandırılmıştır.

![todo:image_alt_text](rename-duplicate-columns-automatically-while-exporting-worksheet-data_1.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-RenameDuplicateColumnsAutomaticallyWhileExportingWorksheetData.cs" >}}

## **Konsol Çıktısı**

Yukarıdaki örnek kodun konsol çıktısı aşağıda verilmiştir.

{{< highlight java >}}

People

PeopleA

PeopleB

{{< /highlight >}}
