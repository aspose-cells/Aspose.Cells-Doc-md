---
title: Çalışma kitabı yüklenirken VBA Projesini filtrele
type: docs
weight: 140
url: /tr/python-net/filter-vba-project-while-loading-a-workbook/
---

## **Python'da Excel çalışma kitabını yüklerken VBA Projesini filtreleyin**

Bazı .xlsm/.xslb dosyalarında çok büyük miktarda makro (veya çok, çok uzun makrolar) bulunur. Aspose.Cells for Python via .NET, böyle çalışma kitaplarını açarken bu (meta) veriyi zorunlu olarak yükler. Bu, gerçekten ihtiyacınız olan sayfa isimlerini çıkarmak için [**LoadDataFilterOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/loaddatafilteroptions) kullanarak kontrol edebilirsiniz, böylece gereksiz içerikleri atlayabilirsiniz. Bu filtre, yeni bir seçenek olan [**LoadDataFilterOptions.VBA**](https://reference.aspose.com/cells/python-net/aspose.cells/loaddatafilteroptions/) ile sağlanır.

## **Örnek Kod**

Aşağıdaki örnek kod, yalnızca VBA'nın filtrelenerek bir çalışma kitabı yükler. Bu özelliği test etmek için kullanılabilecek bir örnek dosyayı aşağıdaki bağlantıdan indirebilirsiniz:

[sampleMacroEnabledWorkbook.xlsm](79527938.xlsm)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "VBAProject-FilterVBAMacrosWhileLoadingWorkbook-1.py" >}}

