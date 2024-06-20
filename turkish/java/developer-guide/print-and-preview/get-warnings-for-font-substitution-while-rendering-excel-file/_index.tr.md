---
title: Excel Dosyasını Rendelerken Yazı Tiplerinin Yerine Kullanılacak Uyarıları Alma
type: docs
weight: 120
url: /tr/java/get-warnings-for-font-substitution-while-rendering-excel-file/
---

{{% alert color="primary" %}}

Bazen Microsoft Excel dosyalarını PDF'e dönüştürürken, Aspose.Cells yazı tiplerini değiştirir. Aspose.Cells, belirli bir yazı tipinin değiştirildiğini bildiren bir uyarı göndererek geliştiricilere bu bilgiyi sağlar. Bu, Aspose.Cells tarafından rendelenmiş PDF'nin gerçek Excel dosyasından farklı görünmesinin nedenini belirlemenize ve uygun eylemleri almanıza yardımcı olan yararlı bir özelliktir. Örneğin, eksik yazı tiplerini yükleyerek rendeleme sonuçlarının aynı görünmesini sağlayabilirsiniz.

Excel dosyasını PDF'e dönüştürürken yazı tipleri yerine kullanılan uyarıları almak istiyorsanız, IWarningCallback arabirimini uygulayın ve PdfSaveOptions.setWarningCallback() yöntemini uyguladığınız arabirimle ayarlayın.

{{% /alert %}}

Aşağıdaki ekran görüntüsü, aşağıdaki kodda kullanılan kaynak Excel dosyasını göstermektedir. A6 ve A7 hücrelerinde Microsoft Excel tarafından iyi bir şekilde işlenmeyen yazı tiplerine sahip metinler bulunmaktadır.

![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_1.png)

Aspose.Cells, A6 ve A7 hücrelerindeki yazı tiplerini aşağıda gösterildiği gibi uygun yazı tipleriyle değiştirecektir.

![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_2.png)

## **Kaynak Dosya ve Çıktı PDF'sini İndir**

Kaynak Excel dosyasını ve çıktı PDF'sini aşağıdaki bağlantılardan indirebilirsiniz

- [source.xlsx](5472700.xlsx)
- [output.pdf](5472699.pdf)

Aşağıdaki kod, [**IWarningCallback**](https://reference.aspose.com/cells/java/com.aspose.cells/IWarningCallback) öğesini uygular ve [**PdfSaveOptions.setWarningCallback()**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#WarningCallback) yöntemini uyguladığı arabirimle. Artık herhangi bir hücrede herhangi bir yazı tipi değiştirildiğinde, Aspose.Cells, WarningCallback.warning() yöntemi içinde bir uyarı gönderecektir.

{{< highlight java >}}

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

Kaynak dosya dönüştürüldükten sonra, aşağıdaki uyarılar hata ayıklama konsoluna çıktı verir:

{{< highlight java >}}

WARNING INFO: Font substitution: Font [ Athene Logos; Regular ] has been substituted in Cell [ A6 ] in Sheet [ Sheet1 ].

WARNING INFO: Font substitution: Font [ B Traffic; Regular ] has been substituted in Cell [ A7 ] in Sheet [ Sheet1 ].

{{< /highlight >}}

{{% alert color="primary" %}}

Eğer elektronik tablonuz formüller içeriyorsa, elektronik tabloyu PDF formatına dönüştürmeden hemen önce Workbook.calculateFormula metodunu çağırmak en iyisidir. Bu sayede formül bağımlı değerler tekrar hesaplanacak ve PDF'de doğru değerler görüntülenecektir. 

{{% /alert %}}
