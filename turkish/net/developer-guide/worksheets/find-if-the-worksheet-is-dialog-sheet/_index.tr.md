---
title: Çalışma Sayfasının Diyaloğu Sayfa Olup Olmadığını Bulma
type: docs
weight: 90
url: /tr/net/find-if-the-worksheet-is-dialog-sheet/
description: Diyalog Sayfa eski bir sayfa formatıdır. Bu makale, bir Excel çalışma sayfasının programlı olarak bir Diyalog Sayfa olup olmadığını belirleme hakkında talimatlar ve örnek kodlar sunar ve bunun için C# API veya .NET Kitaplığı kullanabilirsiniz.
keywords: c# ile excel çalışma sayfası diyalog türünü bulma
---

## **Olası Kullanım Senaryoları**

Diyalog Sayfa, içinde bir diyalog kutusu bulunan eski bir sayfa formatıdır. Bu tür bir sayfa, Microsoft Excel'in eski bir sürümü olan örneğin 2003'ün bir görüntüsünde gösterildiği gibi eklenebilir. Ayrıca, Microsoft Excel 2016 gibi yeni sürümlerde VBA ile de eklenebilir.

![todo:image_alt_text](find-if-the-worksheet-is-dialog-sheet_1.png)

Sayfanın bir diyalog sayfa olup olmadığını [**Worksheet.Type**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/type) özelliği tarafından sağlanan numaralandırma değeri [**SheetType.Dialog**](https://reference.aspose.com/cells/net/aspose.cells/sheettype) karşılaştırarak ve ardından mesajı yazdırarak belirleyebilirsiniz. Daha fazla yardım için aşağıdaki örnek koddaki örnek Excel dosyasının konsol çıktısına bakınız.

## **Çalışma Sayfasının Diyaloğu Sayfa Olup Olmadığını Bulma**

Aşağıdaki örnek kod, diyalog sayfası içeren [örnek Excel dosyasını](64716820.xlsx) yükler. Daha sonra [**Worksheet.Type**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/type) özelliğini kontrol eder, [**SheetType.Dialog**](https://reference.aspose.com/cells/net/aspose.cells/sheettype) ile karşılaştırır ve ardından iletiyi yazdırır. Daha fazla yardım için lütfen aşağıdaki örnek kodun konsol çıktısına bakınız.

## **Örnek Kod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Worksheets-FindIfWorksheetIsDialogSheet.cs" >}}

## **Konsol Çıktısı**

{{< highlight java >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}
