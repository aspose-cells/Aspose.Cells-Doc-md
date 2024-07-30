---
title: Çalışma Sayfasının Diyaloğu Sayfa Olup Olmadığını Bulma
type: docs
weight: 90
url: /tr/python-net/find-if-the-worksheet-is-dialog-sheet/
description: Diyalog Sayfası, eski bir sayfa biçimidir. Bu makale, Aspose.Cells for Python via .NET Kütüphanesini kullanarak Excel çalışma sayfasının programlı olarak bir Diyalog Sayfası olup olmadığını belirleme talimatlarını ve örnek kodları sağlar.
keywords: Python Excel Kütüphanesi, Python da excel çalışma sayfası diyalog türü bulma, python da çalışma sayfası diyalogu.
---

## **Olası Kullanım Senaryoları**

Diyalog Sayfa, içinde bir diyalog kutusu bulunan eski bir sayfa formatıdır. Bu tür bir sayfa, Microsoft Excel'in eski bir sürümü olan örneğin 2003'ün bir görüntüsünde gösterildiği gibi eklenebilir. Ayrıca, Microsoft Excel 2016 gibi yeni sürümlerde VBA ile de eklenebilir.

![todo:image_alt_text](find-if-the-worksheet-is-dialog-sheet_1.png)

Aspose.Cells for Python via .NET tarafından sağlanan [**Worksheet.type**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/type/) özelliği ile çalışma sayfasının bir diyalog sayfa olup olmadığını bulabilirsiniz. Eğer numaralandırma değeri [**SheetType.DIALOG**](https://reference.aspose.com/cells/python-net/aspose.cells/sheettype/) dönerse, bu durumda bir diyalog sayfa ile uğraştığınızı gösterir.

## **Çalışma Sayfasının Diyaloğu Sayfa Olup Olmadığını Bulma**

Aşağıdaki örnek kod, diyalog sayfası içeren [örnek Excel dosyasını](64716820.xlsx) yükler. Daha sonra [**Worksheet.type**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/type/) özelliğini kontrol eder, [**SheetType.DIALOG**](https://reference.aspose.com/cells/python-net/aspose.cells/sheettype/) ile karşılaştırır ve ardından iletiyi yazdırır. Daha fazla yardım için lütfen aşağıdaki örnek kodun konsol çıktısına bakınız.

## **Örnek Kod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-FindIfWorksheetIsDialogSheet.py" >}}

## **Konsol Çıktısı**

{{< highlight java >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}
