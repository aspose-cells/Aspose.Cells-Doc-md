---
title: Bir çalışma kitabı yüklenirken VBA Projesini filtreleme Golang ile C++ kullanarak nasıl yapılır
linktitle: Çalışma kitabı yüklenirken VBA Projesini filtrele
type: docs
weight: 140
url: /tr/go-cpp/filter-vba-project-while-loading-a-workbook/
description: Aspose.Cells kullanarak Golang ile C++ aracılığıyla Excel çalışma kitabı yüklenirken VBA projelerini nasıl filtreleyeceğinizi öğrenin.
---

## **Excel dosyası yüklerken VBA Projesini C++ ile filtreleme**

Bazı .xlsm/.xlsb dosyalarında aşırı büyük makrolar (veya çok uzun makrolar) bulunabilir. Aspose.Cells, bu tür çalışma kitapları açılırken bu (meta) verileri kayıtsız şartsız yükler. Ancak, yalnızca çok sayıda çalışma sayfası ismi çıkarmak istiyorsanız, ve bu gereksiz içeriği atlamak istiyorsanız, bu filtreyi [**LoadDataFilterOptions**](https://reference.aspose.com/cells/go-cpp/loaddatafilteroptions) kullanarak kontrol edebilirsiniz. Bu yeni seçenek, [**LoadDataFilterOptions.VBA**](https://reference.aspose.com/cells/go-cpp/loaddatafilteroptions) ile eklenmiştir.

## **Örnek Kod**

Aşağıdaki örnek kod, yalnızca VBA'nın filtrelenerek bir çalışma kitabı yükler. Bu özelliği test etmek için kullanılabilecek bir örnek dosyayı aşağıdaki bağlantıdan indirebilirsiniz:

[sampleMacroEnabledWorkbook.xlsm](79527938.xlsm)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FilterVbaProjectWhileLoadingAWorkbook.go" >}}
