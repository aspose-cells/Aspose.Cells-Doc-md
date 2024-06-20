---
title: Çalışma Sayfasının Diyaloğu Sayfa Olup Olmadığını Bulma
type: docs
weight: 70
url: /tr/python-java/find-if-the-worksheet-is-dialog-sheet/
---

## **Olası Kullanım Senaryoları**
Diyalog Sayfa, bir diyaloğu içeren eski bir sayfa formatıdır. Bu tür bir sayfa, Microsoft Excel'in eski sürümlerine örneğin 2003'te ekrandaki gibi gösterildiği gibi eklenebilir. Ayrıca, VBA ile Microsoft Excel 2016 gibi yeni sürümlerde de eklenebilir.

![todo:image_alt_text](DialogSheet.png)
## **Çalışma Sayfasının Diyaloğu Sayfa Olup Olmadığını Bulma**
Aspose.Cells for Python via Java, çalışma sayfasının bir diyaloğu sayfa olup olmadığını kontrol etme yeteneği sağlar. Bunun için [Worksheet.Type](https://reference.aspose.com/cells/python/asposecells.api/worksheet#Type) özelliğini sağlar. Eğer [Worksheet.Type](https://reference.aspose.com/cells/python/asposecells.api/worksheet#Type) özelliği, [SheetType.DIALOG](https://reference.aspose.com/cells/python/asposecells.api/sheettype#DIALOG) numaralandırma değerini döndürürse, o zaman bir diyaloğu sayfa ile uğraştığınız anlamına gelir.

Aşağıdaki kod parçası, diyaloğu sayfa için kontrol edilmesini gösterir. Kod tarafından üretilen konsol çıktısı referans için verilmiştir.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-FindIfWorksheetIsDialogSheet.py" >}}
## **Konsol Çıktısı**
{{< highlight java >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}
