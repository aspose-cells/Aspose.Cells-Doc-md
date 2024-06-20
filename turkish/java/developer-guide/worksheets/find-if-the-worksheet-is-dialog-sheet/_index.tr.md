---
title: Çalışma Sayfasının Diyaloğu Sayfa Olup Olmadığını Bulma
type: docs
weight: 100
url: /tr/java/find-if-the-worksheet-is-dialog-sheet/
---

## **Olası Kullanım Senaryoları**

Diyalog Sayfa, bir diyaloğu içeren eski bir sayfa formatıdır. Bu tür bir sayfa, Microsoft Excel'in eski sürümlerine örneğin 2003'te ekrandaki gibi gösterildiği gibi eklenebilir. Ayrıca, VBA ile Microsoft Excel 2016 gibi yeni sürümlerde de eklenebilir.

![todo:image_alt_text](find-if-the-worksheet-is-dialog-sheet_1.png)

Eğer Aspose.Cells tarafından sağlanan [**Worksheet.Type**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Type) özelliği, numaralandırma değeri [**SheetType.DIALOG**](https://reference.aspose.com/cells/java/com.aspose.cells/sheettype#DIALOG) döndürürse, o zaman, iletişim sayfası ile uğraştığınız anlamına gelir.

## **Çalışma Sayfasının Diyaloğu Sayfa Olup Olmadığını Bulma**

Aşağıdaki örnek kod, bir iletişim sayfası içeren [örnek Excel dosyasını](64716841.xlsx) yükler. [**Worksheet.Type**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Type) özelliğini kontrol eder, onu [**SheetType.DIALOG**](https://reference.aspose.com/cells/java/com.aspose.cells/sheettype#DIALOG) ile karşılaştırır ve sonra mesajı yazdırır. Daha fazla yardım için lütfen aşağıdaki örnek kodun konsol çıktısına bakın.

## **Örnek Kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Worksheets-FindIfWorksheetIsDialogSheet.java" >}}

## **Konsol Çıktısı**

{{< highlight java >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}
