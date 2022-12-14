---
title: Çalışma kitabı yüklerken VBA Projesini filtreleme
type: docs
weight: 140
url: /tr/net/filter-vba-project-while-loading-a-workbook/
---
## **C#'de bir Excel çalışma kitabı yüklenirken VBA Projesini filtreleyin**

Bazı .xlsm/.xslb dosyalarında çok büyük miktarda makro (veya çok, çok uzun makrolar) bulunur. Aspose.Cells, bu tür çalışma kitaplarını açarken bu (meta) verileri koşulsuz olarak yükleyecektir. Yine de bunu kontrol etmeniz gerekebilir[**LoadDataFilterOptions**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions) çok sayıda çalışma kitabı için gerçekten yalnızca sayfa adlarını ayıklamanız gerektiğinde, böylece bu tür gereksiz içeriği atlarsınız. Bu filtre yeni bir seçenek getirilerek sağlanır,[**LoadDataFilterOptions.VBA**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions).

## **Basit kod**

Aşağıdaki örnek kod, yalnızca VBA'nın filtreleneceği bir çalışma kitabı yükler. Bu özelliği test etmek için örnek bir dosya aşağıdaki bağlantıdan indirilebilir:

[sampleMacroEnabledWorkbook.xlsm](79527938.xlsm)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FilterVBAMacrosWhileLoadingWorkbook-1.cs" >}}
