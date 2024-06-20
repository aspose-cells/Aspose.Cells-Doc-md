---
title: Excel Dosyası Yüklenirken Uyarıları Al
type: docs
weight: 60
url: /tr/java/get-warnings-while-loading-excel-file/
---

## **Olası Kullanım Senaryoları**

Bazen kullanıcı, biraz bozuk ancak yüklenebilir bir çalışma kitabını yüklemeye çalışır. Bu durumda, Aspose.Cells çalışma kitabını yüklerken uyarılar fırlatır. Bu uyarıları yakalamak için [**IWarningCallback**](https://reference.aspose.com/cells/java/com.aspose.cells/IWarningCallback) arayüzünü uygulayarak ve [**LoadOptions.WarningCallback**](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#WarningCallback) özelliğini ayarlayarak bunları yakalayabilirsiniz.

## **Excel Dosyası Yüklenirken Uyarıları Al**

Aşağıdaki örnek kod, excel dosyasını yüklerken uyarıları nasıl alacağını açıklar. Kod, yüklenirken [**DuplicateDefinedName**](https://reference.aspose.com/cells/java/com.aspose.cells/warningtype#DUPLICATE_DEFINED_NAME) uyarısı fırlatan [örnek excel dosyasını](sampleDuplicateDefinedName.xlsx) yükler. Bu uyarı daha sonra [**IWarningCallback.Warning()**](https://reference.aspose.com/cells/java/com.aspose.cells/iwarningcallback#warning(com.aspose.cells.WarningInfo)) yöntemi ile yakalanır ve konsolda uyarı mesajlarını yazdırır. Kod daha sonra çalışma kitabını [çıktı excel dosyası](outputDuplicateDefinedName.xlsx) olarak kaydeder. Eğer örnek excel dosyasını MS Excel'de açarsanız, size bu uyarıyı gösterecektir. Daha iyi anlamak için aşağıdaki kodun konsol çıktısını da kontrol edin.

![todo:image_alt_text](get-warnings-while-loading-excel-file_1.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-WarningCallback-WarningCallback.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-GetWarningLoadingAnExcel-GetWarningLoadingAnExcel.java" >}}

## **Konsol Çıktısı**

Yukarıdaki kodun, verilen [örnek excel dosyası](sampleDuplicateDefinedName.xlsx) ile çalıştırıldığında konsol çıktısı şöyledir.

{{< highlight java >}}

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Introduction!$D$16:$D$17

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Panel!$B$228

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:'Queries '!$D$14:$D$16

{{< /highlight >}}
