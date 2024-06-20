---
title: Çalışma kitabı yüklenirken VBA Projesini filtrele
type: docs
weight: 140
url: /tr/net/filter-vba-project-while-loading-a-workbook/
---

## **C#’de Bir Excel çalışma kitabını yüklerken VBA Projesini filtrele**

.xlsm/.xslb dosyalarının bazılarının aşırı miktarda makroya (veya çok uzun makrolara) sahip olduğu bilinmektedir. Aspose.Cells, bu tür çalışma kitaplarını açarken bu (meta) veriyi koşulsuz olarak yükleyecektir. Bu tür gereksiz içeriği atlayarak gerçekten sadece birçok çalışma kitabının sayfa adlarını çıkarmak istediğinizde bu kontrolü yine de yapmanız gerekebilir. Bu filtre, yeni bir seçenek olan  [**LoadDataFilterOptions.VBA**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions) tanıtarak sağlanmıştır.

## **Örnek Kod**

Aşağıdaki örnek kod, yalnızca VBA'nın filtrelenerek bir çalışma kitabı yükler. Bu özelliği test etmek için kullanılabilecek bir örnek dosyayı aşağıdaki bağlantıdan indirebilirsiniz:

[sampleMacroEnabledWorkbook.xlsm](79527938.xlsm)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FilterVBAMacrosWhileLoadingWorkbook-1.cs" >}}
