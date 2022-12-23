---
title: Excel Dosyasını İşlerken Yazı Tipi Değiştirme Uyarıları Alın
type: docs
weight: 120
url: /tr/java/get-warnings-for-font-substitution-while-rendering-excel-file/
---
{{% alert color="primary" %}}

Bazen, Microsoft Excel dosyalarını PDF olarak işlerken, Aspose.Cells yazı tiplerini değiştirir. Aspose.Cells, geliştiricilerin belirli bir yazı tipinin bir uyarı tetikleyerek değiştirildiğini bilmesini sağlayan bir özellik sağlar. Bu, Aspose.Cells'in işlenen PDF'den neden farklı olduğunu belirlemenize yardımcı olabilecek kullanışlı bir özelliktir ve ardından uygun işlemleri yapabilirsiniz. Örneğin, oluşturma sonuçlarının aynı görünmesi için eksik yazı tiplerini yükleyebilirsiniz.

Bir Excel dosyasını PDF olarak işlerken yazı tipi değiştirme uyarılarını almak istiyorsanız, IWarningCallback arabirimini uygulayın ve uyguladığınız arabirimle PdfSaveOptions.setWarningCallback() yöntemini ayarlayın.

{{% /alert %}}

Aşağıdaki ekran görüntüsü, aşağıdaki kodda kullanılan kaynak Excel dosyasını göstermektedir. Microsoft Excel tarafından iyi işlenmeyen yazı tiplerinde A6 ve A7 hücrelerinde bazı metinler var.

![yapılacaklar:resim_alternatif_metin](get-warnings-for-font-substitution-while-rendering-excel-file_1.png)

Aspose.Cells, A6 ve A7 hücrelerindeki yazı tiplerini aşağıda gösterildiği gibi uygun yazı tipleriyle değiştirecektir.

![yapılacaklar:resim_alternatif_metin](get-warnings-for-font-substitution-while-rendering-excel-file_2.png)

## **Kaynak Dosyayı ve Çıktıyı İndirin PDF**

Kaynak Excel dosyasını ve PDF çıktısını aşağıdaki linklerden indirebilirsiniz.

- [kaynak.xlsx](5472700.xlsx)
- [çıktı.pdf](5472699.pdf)

 Aşağıdaki kod uygular[**IUyarıGeri Arama**](https://reference.aspose.com/cells/java/com.aspose.cells/IWarningCallback) ve ayarla[**PdfSaveOptions.setWarningCallback()**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#WarningCallback) Uygulanan arayüz ile yöntem. Artık, herhangi bir hücrede herhangi bir yazı tipi değiştirildiğinde, Aspose.Cells, WarningCallback.warning() yöntemi içinde bir uyarı tetikleyecektir.

{{< highlight "java" >}}

 public class WarningCallback implements IWarningCallback {

    @Override

    public void warning(WarningInfo info) {

        if(info.getWarningType() == WarningType.FONT_SUBSTITUTION)

        {

            System.out.println("WARNING INFO: " + info.getDescription());

        }

    }

}

//........

//........

static void Run() throws Exception

{

    Workbook workbook = new Workbook("source.xlsx");

    PdfSaveOptions options = new PdfSaveOptions();

    options.setWarningCallback(new WarningCallback());

    workbook.save("output.pdf", options);

}

{{< /highlight >}}

## **Uyarı Çıktısı**

Kaynak dosyayı dönüştürdükten sonra hata ayıklama konsoluna aşağıdaki uyarılar gönderilir:

{{< highlight "java" >}}

WARNING INFO: Font substitution: Font [ Athene Logos; Regular ]has been substituted in Cell [ A6 ]in Sheet [ Sheet1 ].

WARNING INFO: Font substitution: Font [ B Traffic; Regular ]has been substituted in Cell [ A7 ]in Sheet [ Sheet1 ].

{{< /highlight >}}

{{% alert color="primary" %}}

 E-tablonuz formüller içeriyorsa, e-tabloyu PDF biçimine dönüştürmeden hemen önce Workbook.calculateFormula yöntemini çağırmak en iyisidir. Bunu yapmak, formüle bağlı değerlerin yeniden hesaplanmasını ve PDF'de doğru değerlerin oluşturulmasını sağlar.

{{% /alert %}}
