---
title: Excel Dosyasını İşlerken Yazı Tipi Değiştirme Uyarıları Alın
type: docs
weight: 230
url: /tr/net/get-warnings-for-font-substitution-while-rendering-excel-file/
---
{{% alert color="primary" %}} 

Bazen, bir Microsoft Excel dosyasını PDF olarak işlerken yazı tiplerini Aspose.Cells değiştirir. Aspose.Cells, geliştiricilerin hangi yazı tipinin değiştirildiğini bir uyarı vererek bilmelerini sağlayan bir özellik sağlar. Bu, Aspose.Cells'in işlenen PDF'in orijinal Microsoft Excel dosyasından neden farklı göründüğünü belirlemenize yardımcı olabilecek kullanışlı bir özelliktir, böylece uygun işlemleri yapabilirsiniz. Örneğin, oluşturma sonuçlarının aynı görünmesi için eksik yazı tiplerini yüklemek.

{{% /alert %}} 

Excel dosyalarını PDF olarak işlerken yazı tipi değiştirme uyarıları almak için IWarningCallback arabirimini uygulayın ve uygulanan arabiriminizle PdfSaveOptions.WarningCallback özelliğini ayarlayın.

Aşağıdaki ekran görüntüsü, aşağıdaki kodda kullanacağımız bir kaynak Excel dosyasını göstermektedir. Microsoft Excel tarafından iyi işlenmeyen yazı tiplerinde A6 ve A7 hücrelerinde bazı metinler var.

|**Tüm yazı tipleri doğru şekilde oluşturulmaz**|
|:- |
|![yapılacaklar:resim_alternatif_metin](get-warnings-for-font-substitution-while-rendering-excel-file_1.png)|
Aspose.Cells, A6 ve A7 hücrelerindeki yazı tiplerini aşağıda gösterildiği gibi uygun yazı tipleriyle değiştirecektir.

|**Değiştirilen yazı tipleri**|
|:- |
|![yapılacaklar:resim_alternatif_metin](get-warnings-for-font-substitution-while-rendering-excel-file_2.png)|
## **Kaynak Dosyayı ve Çıktıyı İndirin PDF**
Kaynak Excel dosyasını ve PDF çıktısını aşağıdaki linklerden indirebilirsiniz.

- [kaynak.xlsx](5112611.xlsx)
- [çıktı.pdf](5112616.pdf)
## **kod**
Aşağıdaki kod, IWarningCallback'i uygular ve uygulanan arabirimle PdfSaveOptions.WarningCallback özelliğini ayarlar. Artık, herhangi bir hücrede herhangi bir yazı tipi değiştirildiğinde, Aspose.Cells, WarningCallback.Warning() yöntemi içinde bir uyarı tetikleyecektir.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-GetWarningsForFontSubstitution-1.cs" >}}
## **Çıktı**
Kaynak Excel dosyasını PDF'e dönüştürdükten sonra, uyarılar şu şekilde hata ayıklama konsoluna gönderilir:

{{< highlight "java" >}}

 WARNING INFO: Font substitution: Font [ Athene Logos; Regular ]has been substituted in Cell [ A6 ]in Sheet [ Sheet1 ].

WARNING INFO: Font substitution: Font [ B Traffic; Regular ]has been substituted in Cell [ A7 ]in Sheet [ Sheet1 ].

{{< /highlight >}}

{{% alert color="primary" %}} 

Elektronik tablonuz formüller içeriyorsa, elektronik tabloyu PDF biçimine dönüştürmeden hemen önce Workbook.CalculateFormula yöntemini çağırmak en iyisidir. Bunu yapmak, formüle bağlı değerlerin yeniden hesaplanmasını ve PDF'de doğru değerlerin oluşturulmasını sağlar.

{{% /alert %}}
