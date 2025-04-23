---
title: Çalışma Sayfasının Diyaloğu Sayfa Olup Olmadığını Bulma
type: docs
weight: 90
url: /tr/python-net/find-if-the-worksheet-is-dialog-sheet/
description: Diyalog Sayfası, eski formatta bir sayfadır. Bu makale, Aspose.Cells for Python via .NET kütüphanesi kullanarak bir Excel çalışma sayfasının Diyalog Sayfası olup olmadığını programlı olarak belirlemeniz için talimatlar ve örnek kod sağlar.
keywords: Python Excel Kütüphanesi, Python da excel çalışma sayfası diyaloğu türü, Python da çalışma sayfası diyaloğu.
---

## **Olası Kullanım Senaryoları**

Diyalog Sayfa, içinde bir diyalog kutusu bulunan eski bir sayfa formatıdır. Bu tür bir sayfa, Microsoft Excel'in eski bir sürümü olan örneğin 2003'ün bir görüntüsünde gösterildiği gibi eklenebilir. Ayrıca, Microsoft Excel 2016 gibi yeni sürümlerde VBA ile de eklenebilir.

![todo:image_alt_text](find-if-the-worksheet-is-dialog-sheet_1.png)

Aspose.Cells for Python via .NET tarafından sağlanan [**Worksheet.type**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/type/) özelliği ile sayfanın diyalo sayfası mı yoksa başka bir tür sayfa mı olduğunu bulabilirsiniz. Eğer kutup değerini [**SheetType.DIALOG**](https://reference.aspose.com/cells/python-net/aspose.cells/sheettype/) dönerse, diyalo sayfasıyla ilgilendiğiniz anlamına gelir.

## **Çalışma Sayfasının Diyaloğu Sayfa Olup Olmadığını Bulma**

Aşağıdaki örnek kod, diyalog sayfası içeren [örnek Excel dosyasını](64716820.xlsx) yükler. Daha sonra [**Worksheet.type**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/type/) özelliğini kontrol eder, [**SheetType.DIALOG**](https://reference.aspose.com/cells/python-net/aspose.cells/sheettype/) ile karşılaştırır ve ardından iletiyi yazdırır. Daha fazla yardım için lütfen aşağıdaki örnek kodun konsol çıktısına bakınız.

## **Örnek Kod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-FindIfWorksheetIsDialogSheet.py" >}}

## **Konsol Çıktısı**

{{< highlight java >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}
