---
title: Çalışma kitabı yüklerken VBA Projesini filtreleme
type: docs
weight: 70
url: /tr/java/filter-vba-project-while-loading-a-workbook/
---
## **Olası Kullanım Senaryoları**
Bazı .xlsm/.xslb dosyalarında çok büyük miktarda makro (veya çok, çok uzun makrolar) bulunur. Aspose.Cells, bu tür çalışma kitaplarını açarken bu (meta) verileri koşulsuz olarak yükleyecektir. Gerçekten yalnızca çok sayıda çalışma kitabı için sayfa adlarını ayıklamanız gerektiğinde, bu tür gereksiz içeriği atlamanız gerektiğinde, bunu LoadDataFilterOptions üzerinden kontrol etmeniz gerekebilir. Bu filtre, LoadDataFilterOptions.VBA adlı yeni seçeneğin tanıtılmasıyla sağlanır.
## **Basit kod**
Aşağıdaki örnek kod, yalnızca VBA'nın filtreleneceği bir çalışma kitabı yükler. Bu özelliği test etmek için örnek dosya aşağıdaki bağlantıdan indirilebilir:

[sampleMacroEnabledWorkbook.xlsm](79527951.xlsm)

// Yükleme seçeneklerini ayarlayın, VBA'yı yüklemek istemiyoruz
LoadOptions loadOptions = yeni LoadOptions(LoadFormat.AUTO);
loadOptions.setLoadFilter(yeni LoadFilter(LoadDataFilterOptions.ALL & ~LoadDataFilterOptions.VBA));

// Yükleme seçeneklerini kullanarak örnek excel dosyasından çalışma kitabı nesnesi oluşturun
Çalışma kitabı kitabı = yeni Çalışma Kitabı(srcDir + "sampleMacroEnabledWorkbook.xlsm", loadOptions);

// Çıktıyı pdf formatında kaydet
book.save(outDir + "OutputSampleMacroEnabledWorkbook.xlsm", SaveFormat.XLSM);
