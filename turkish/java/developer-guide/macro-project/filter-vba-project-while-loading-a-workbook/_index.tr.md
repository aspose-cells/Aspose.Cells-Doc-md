---
title: Çalışma kitabı yüklenirken VBA Projesini filtrele
type: docs
weight: 70
url: /tr/java/filter-vba-project-while-loading-a-workbook/
---

## **Olası Kullanım Senaryoları**
Bazı .xlsm/.xslb dosyalarında son derece fazla miktarda makro (veya çok, çok uzun makrolar) bulunmaktadır. Aspose.Cells, bu tür çalışma kitaplarını açarken bu (meta) verileri koşulsuz olarak yükleyecektir. Böyle geniş bir işlem kitabının sayfa adlarını çıkarmak için gerçekten yalnızca bu tür gereksiz içeriği atlamak istediğinizde, LoadDataFilterOptions ile bunu kontrol etmeniz gerekebilir. Bu filtre, yeni seçenek LoadDataFilterOptions.VBA'yı tanıtarak sağlanır.
## **Örnek Kod**
Aşağıdaki örnek kod, yalnızca VBA'yı filtreleyecek şekilde bir çalışma kitabı yükler. Bu özelliği test etmek için örnek dosyayı aşağıdaki bağlantıdan indirebilirsiniz:

[sampleMacroEnabledWorkbook.xlsm](79527951.xlsm)

// Yükleme seçeneklerini ayarlayın, VBA'yı yüklemek istemiyoruz
LoadOptions loadOptions = new LoadOptions(LoadFormat.AUTO);
loadOptions.setLoadFilter(new LoadFilter(LoadDataFilterOptions.ALL & ~LoadDataFilterOptions.VBA));

// Yükleme seçeneklerini kullanarak örnek excel dosyasından çalışma kitabı nesnesi oluşturun
Workbook book = new Workbook(srcDir + "sampleMacroEnabledWorkbook.xlsm", loadOptions);

// Çıktıyı pdf formatında kaydedin
book.save(outDir + "OutputSampleMacroEnabledWorkbook.xlsm", SaveFormat.XLSM);
{{< app/cells/assistant language="java" >}}
