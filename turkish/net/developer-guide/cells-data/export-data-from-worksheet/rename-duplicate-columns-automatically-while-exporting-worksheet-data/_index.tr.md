---
title: Çalışma sayfası verilerini dışa aktarırken yinelenen sütunları otomatik olarak yeniden adlandırın
type: docs
weight: 250
url: /tr/net/rename-duplicate-columns-automatically-while-exporting-worksheet-data/
---
## **Olası Kullanım Senaryoları**

Bazen kullanıcı, verileri çalışma sayfasından veri tablosuna aktarırken yinelenen sütun sorunuyla karşılaşır. DataTable'ın yinelenen sütunları olamaz, bu nedenle çalışma sayfası verilerini veri tablosuna aktarabilmeniz için yinelenen sütunların yeniden adlandırılması gerekir. Aspose.Cells, yinelenen sütunları sizin tarafınızdan belirtilen stratejiye göre otomatik olarak yeniden adlandırabilir.[**ExportTableOptions.RenameStrategy**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/renamestrategy) Emlak. eğer belirtirsen[**Stratejiyi Yeniden Adlandır**](https://reference.aspose.com/cells/net/aspose.cells/renamestrategy) .Digit, sütunlar sütun1, sütun2, sütun3 gibi yeniden adlandırılacak ve belirtirseniz[**Stratejiyi Yeniden Adlandır**](https://reference.aspose.com/cells/net/aspose.cells/renamestrategy).Letter, sütunlar sütunA, sütunB, sütunC gibi yeniden adlandırılacaktır.

## **Çalışma sayfası verilerini dışa aktarırken yinelenen sütunları otomatik olarak yeniden adlandırın**

 Aşağıdaki örnek kod, çalışma sayfasının ilk üç sütununa bazı veriler ekler, ancak tüm sütunların adı aynıdır;*İnsanlar* . Ardından, çalışma sayfasındaki verileri belirterek veri tablosuna aktarır.[**Stratejiyi Yeniden Adlandır**](https://reference.aspose.com/cells/net/aspose.cells/renamestrategy).Harf stratejisi. Ardından, Aspose.Cells tarafından oluşturulan veri tablosunun sütun adlarını yazdırır. Aşağıdaki ekran görüntüsü, görselleştiricide dışa aktarılan verilerle birlikte veri tablosunu gösterir. Gördüğünüz gibi, yinelenen sütunlar PeopleA, PeopleB vb. olarak yeniden adlandırıldı.

![yapılacaklar:resim_alternatif_metin](rename-duplicate-columns-automatically-while-exporting-worksheet-data_1.png)

## **Basit kod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-RenameDuplicateColumnsAutomaticallyWhileExportingWorksheetData.cs" >}}

## **Konsol Çıkışı**

İşte referans için yukarıdaki örnek kodun konsol çıktısı.

{{< highlight "java" >}}

People

PeopleA

PeopleB

{{< /highlight >}}
