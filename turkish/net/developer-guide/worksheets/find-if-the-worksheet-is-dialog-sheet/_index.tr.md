---
title: Çalışma Sayfasının İletişim Sayfası olup olmadığını bulun
type: docs
weight: 90
url: /tr/net/find-if-the-worksheet-is-dialog-sheet/
---
## **Olası Kullanım Senaryoları**

İletişim Sayfası, bir iletişim kutusu içeren eski bir sayfa biçimidir. Bu tür bir sayfa, bu ekran görüntüsünde gösterildiği gibi Microsoft Excel'in eski bir sürümü, örneğin 2003 tarafından eklenebilir. Daha yeni sürümlerde VBA ile de eklenebilir, örneğin Microsoft Excel 2016.

![yapılacaklar:resim_alternatif_metin](find-if-the-worksheet-is-dialog-sheet_1.png)

Sayfanın bir diyalog sayfası mı yoksa başka türde bir sayfa mı olduğunu bulabilirsiniz.[**Çalışma Sayfası.Türü**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/type)Aspose.Cells tarafından sağlanan özellik. Numaralandırma değeri döndürürse[**SheetType.Dialog**](https://reference.aspose.com/cells/net/aspose.cells/sheettype), o zaman diyalog sayfasıyla uğraşıyorsunuz demektir.

## **Çalışma Sayfasının İletişim Sayfası olup olmadığını bulun**

 Aşağıdaki örnek kod,[örnek excel dosyası](64716820.xlsx) bir iletişim sayfası içerir. kontrol eder[**Çalışma Sayfası.Türü**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/type)mülkiyet onunla karşılaştırır[**SheetType.Dialog**](https://reference.aspose.com/cells/net/aspose.cells/sheettype) ve ardından mesajı yazdırır. Lütfen daha fazla yardım için aşağıda verilen örnek kodun konsol çıktısına bakın.

## **Basit kod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Worksheets-FindIfWorksheetIsDialogSheet.cs" >}}

## **Konsol Çıkışı**

{{< highlight "java" >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}
