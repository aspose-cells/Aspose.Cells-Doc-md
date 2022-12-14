---
title: Çalışma Sayfasının İletişim Sayfası olup olmadığını bulun
type: docs
weight: 100
url: /tr/java/find-if-the-worksheet-is-dialog-sheet/
---
## **Olası Kullanım Senaryoları**

İletişim Sayfası, bir iletişim kutusu içeren sayfanın eski bir biçimidir. Böyle bir sayfa, bu ekran görüntüsünde gösterildiği gibi Microsoft Excel örneğin 2003'ün eski bir sürümü tarafından eklenebilir. Daha yeni sürümlerde VBA ile de eklenebilir, örneğin Microsoft Excel 2016.

![yapılacaklar:resim_alternatif_Metin](find-if-the-worksheet-is-dialog-sheet_1.png)

Sayfanın bir diyalog sayfası mı yoksa başka türde bir sayfa mı olduğunu bulabilirsiniz.[**Çalışma Sayfası.Türü**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Type)Aspose.Cells tarafından sağlanan özellik. Numaralandırma değeri döndürürse[**SheetType.DIALOG**](https://reference.aspose.com/cells/java/com.aspose.cells/sheettype#DIALOG), o zaman bir diyalog sayfasıyla uğraşıyorsunuz demektir.

## **Çalışma Sayfasının İletişim Sayfası olup olmadığını bulun**

Aşağıdaki örnek kod,[örnek excel dosyası](64716841.xlsx)bir iletişim sayfası içerir. kontrol eder[**Çalışma Sayfası.Türü**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Type)mülkiyet onunla karşılaştırır[**SheetType.DIALOG**](https://reference.aspose.com/cells/java/com.aspose.cells/sheettype#DIALOG)ve ardından mesajı yazdırır. Lütfen daha fazla yardım için aşağıda verilen örnek kodun konsol çıktısına bakın.

## **Basit kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Worksheets-FindIfWorksheetIsDialogSheet.java" >}}

## **Konsol Çıkışı**

{{< highlight "java" >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}
