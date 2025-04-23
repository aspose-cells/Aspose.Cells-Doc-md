---
title: Excel Dosyasını Rendelerken Yazı Tiplerinin Yerine Kullanılacak Uyarıları Alma
type: docs
weight: 230
url: /tr/net/get-warnings-for-font-substitution-while-rendering-excel-file/
---

{{% alert color="primary" %}} 

Bazen, bir Microsoft Excel dosyasını PDF'e render ederken, Aspose.Cells fontları değiştirir. Aspose.Cells, geliştiricilerin hangi belirli fontun değiştirildiğini bildiren bir uyarı ile ilgili bir özellik sağlar. Bu, bir Aspose.Cells tarafından render edilmiş PDF'nin orijinal Microsoft Excel dosyasından farklı görünmesinin nedenini belirlemenize ve uygun işlemleri almanıza yardımcı olabilecek faydalı bir özelliktir. Örneğin, eksik fontları yükleyerek render sonuçlarının aynı görünmesini sağlamak gibi.

{{% /alert %}} 

Excel dosyalarını PDF'e render ederken font değişimi için uyarıları almak için IWarningCallback arabirimini uygulayın ve PdfSaveOptions.WarningCallback özelliğini uyguladığınız arabirimle ayarlayın.

Aşağıdaki ekran görüntüsü, aşağıdaki kodda kullanacağımız kaynak Excel dosyasını göstermektedir. A6 ve A7 hücrelerinde, Microsoft Excel tarafından düzgün bir şekilde render edilmeyen fontlarda bazı metinler bulunmaktadır.

|**Tüm fontlar düzgün bir şekilde render edilmiyor**|
| :- |
|![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_1.png)|
Aspose.Cells, A6 ve A7 hücrelerindeki yazı tiplerini aşağıda gösterildiği gibi uygun yazı tipleriyle değiştirecektir.

|**Değiştirilen fontlar**|
| :- |
|![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_2.png)|
## **Kaynak Dosya ve Çıktı PDF'sini İndir**
Kaynak Excel dosyasını ve çıktı PDF'sini aşağıdaki bağlantılardan indirebilirsiniz

- [source.xlsx](5112611.xlsx)
- [output.pdf](5112616.pdf)
## **Kod**
Aşağıdaki kod, IWarningCallback'ı uygular ve PdfSaveOptions.WarningCallback özelliğini uygulanan arayüze ayarlar. Artık Aspose.Cells herhangi bir hücrede herhangi bir fontun değiştirilmesi durumunda bir uyarı oluşturur.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-GetWarningsForFontSubstitution-1.cs" >}}
## **Çıktı**
Kaynak Excel dosyasının PDF olarak dönüştürülmesinden sonra uyarılar şu şekilde hata ayıklama konsoluna çıktı verilir:

{{< highlight java >}}

 WARNING INFO: Font substitution: Font [ Athene Logos; Regular ] has been substituted in Cell [ A6 ] in Sheet [ Sheet1 ].

WARNING INFO: Font substitution: Font [ B Traffic; Regular ] has been substituted in Cell [ A7 ] in Sheet [ Sheet1 ].

{{< /highlight >}}

{{% alert color="primary" %}} 

Eğer elektronik tablonuz formüller içeriyorsa, elektronik tabloyu PDF biçimine dönüştürmeden önce en iyi işlem, Workbook.CalculateFormula yöntemini çağırmaktır. Bu işlem, formül bağımlı değerlerin yeniden hesaplanmasını sağlar ve PDF biçiminde doğru değerlerin çıktılanmasını sağlar.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
