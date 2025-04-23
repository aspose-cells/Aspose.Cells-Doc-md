---
title: Excel Dosyası Yüklenirken Uyarıları Al
type: docs
weight: 110
url: /tr/net/get-warnings-while-loading-excel-file/
---

## **Olası Kullanım Senaryoları**

Bazen kullanıcı, biraz bozuk ancak yüklenebilir bir çalışma kitabını yüklemeye çalışır. Bu durumda, Aspose.Cells çalışma kitabını yüklerken uyarılar fırlatır. Bu uyarıları yakalamak için [**IWarningCallback**](https://reference.aspose.com/cells/net/aspose.cells/iwarningcallback) arayüzünü uygulayarak ve [**LoadOptions.WarningCallback**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/warningcallback) özelliğini ayarlayarak bunları yakalayabilirsiniz.

## **Excel Dosyası Yüklenirken Uyarıları Al**

Aşağıdaki örnek kod, excel dosyasını yüklerken uyarıları nasıl alacağını açıklar. Kod, yüklenirken [**DuplicateDefinedName**](https://reference.aspose.com/cells/net/aspose.cells/warningtype) uyarısı fırlatan [örnek excel dosyasını](sampleDuplicateDefinedName.xlsx) yükler. Bu uyarı daha sonra [**IWarningCallback.Warning()**](https://reference.aspose.com/cells/net/aspose.cells/iwarningcallback/methods/warning) yöntemi ile yakalanır ve konsolda uyarı mesajlarını yazdırır. Kod daha sonra çalışma kitabını [çıktı excel dosyası](outputDuplicateDefinedName.xlsx) olarak kaydeder. Eğer örnek excel dosyasını MS Excel'de açarsanız, size bu uyarıyı gösterecektir. Daha iyi anlamak için aşağıdaki kodun konsol çıktısını da kontrol edin.

![todo:image_alt_text](get-warnings-while-loading-excel-file_1.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-GetWarningsWhileLoadingExcelFile.cs" >}}

## **Konsol Çıktısı**

Yukarıdaki kodun, verilen [örnek excel dosyası](sampleDuplicateDefinedName.xlsx) ile çalıştırıldığında konsol çıktısı şöyledir.

{{< highlight java >}}

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Introduction!$D$16:$D$17

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Panel!$B$228

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:'Queries '!$D$14:$D$16

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
