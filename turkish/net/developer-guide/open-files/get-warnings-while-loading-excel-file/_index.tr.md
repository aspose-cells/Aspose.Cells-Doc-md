---
title: Excel Dosyasını Yüklerken Uyarılar Alın
type: docs
weight: 110
url: /tr/net/get-warnings-while-loading-excel-file/
---
## **Olası Kullanım Senaryoları**

Bazen kullanıcı, biraz bozuk ancak yüklenebilir olan çalışma kitabını yüklemeye çalışır. Böyle bir durumda Aspose.Cells çalışma kitabını yüklerken uyarı veriyor. Bu uyarıları uygulayarak yakalayabilirsiniz.**[IWarningCallback](https://reference.aspose.com/cells/net/aspose.cells/iwarningcallback)** arayüz ve ayar**[LoadOptions.WarningCallback](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/warningcallback)**Emlak.

## **Excel Dosyasını Yüklerken Uyarılar Alın**

 Aşağıdaki örnek kod, excel dosyası yüklenirken uyarıların nasıl alınacağını açıklar. Kod şunu yükler:[örnek excel dosyası](sampleDuplicateDefinedName.xlsx) hangi atar**[DuplicateDefinedName](https://reference.aspose.com/cells/net/aspose.cells/warningtype)** yükleme uyarısı. Bu uyarı daha sonra tarafından yakalanır**[IWarningCallback.Warning()](https://reference.aspose.com/cells/net/aspose.cells/iwarningcallback/methods/warning)** konsoldaki uyarı mesajlarını yazdıran yöntem. Kod daha sonra çalışma kitabını şu şekilde kaydeder:[çıktı excel dosyası](outputDuplicateDefinedName.xlsx)Örnek excel dosyasını Microsoft Excel'de açarsanız bu ekran görüntüsündeki gibi size bu uyarıyı da verecektir. Lütfen daha iyi anlamak için aşağıda verilen kodun konsol çıktısını da kontrol edin.

![yapılacaklar:resim_alternatif_metin](get-warnings-while-loading-excel-file_1.png)

## **Basit kod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-GetWarningsWhileLoadingExcelFile.cs" >}}

## **Konsol Çıkışı**

 Sağlanan ile çalıştırıldığında yukarıdaki kodun konsol çıktısı aşağıdadır.[örnek excel dosyası](sampleDuplicateDefinedName.xlsx).

{{< highlight "java" >}}

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Introduction!$D$16:$D$17

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Panel!$B$228

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:'Queries '!$D$14:$D$16

{{< /highlight >}}
