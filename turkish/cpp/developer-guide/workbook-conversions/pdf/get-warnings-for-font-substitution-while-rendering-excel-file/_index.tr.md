---
title: Excel Dosyasını İşleme Sırasında Font Yedekleme Uyarıları Almak (C++)
linktitle: Yedekleme Uyarıları Almak
type: docs
weight: 230
url: /tr/cpp/get-warnings-for-font-substitution-while-rendering-excel-file/
description: Aspose.Cells kullanarak, Excel dosyalarını PDF ye dönüştürürken font yedekleme uyarılarını nasıl alacağınızı öğrenin.
---

{{% alert color="primary" %}}

Bazen, bir Microsoft Excel dosyasını PDF'e render ederken, Aspose.Cells fontları değiştirir. Aspose.Cells, geliştiricilerin hangi belirli fontun değiştirildiğini bildiren bir uyarı ile ilgili bir özellik sağlar. Bu, bir Aspose.Cells tarafından render edilmiş PDF'nin orijinal Microsoft Excel dosyasından farklı görünmesinin nedenini belirlemenize ve uygun işlemleri almanıza yardımcı olabilecek faydalı bir özelliktir. Örneğin, eksik fontları yükleyerek render sonuçlarının aynı görünmesini sağlamak gibi.

{{% /alert %}}

Excel dosyalarını PDF'ye dönüştürürken yazı tipi değiştirme uyarıları almak için, `IWarningCallback` arayüzünü uygulayın ve uyguladığınız arayüz ile `PdfSaveOptions.WarningCallback` özelliğini ayarlayın.

Aşağıdaki ekran görüntüsü, aşağıdaki kodda kullanacağımız kaynak Excel dosyasını göstermektedir. A6 ve A7 hücrelerinde, Microsoft Excel tarafından düzgün bir şekilde render edilmeyen fontlarda bazı metinler bulunmaktadır.

|**Tüm fontlar düzgün bir şekilde render edilmiyor**|
| :- |
|![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_1.png)|

Aspose.Cells, A6 ve A7 hücrelerindeki yazı tiplerini aşağıda gösterildiği gibi uygun yazı tipleriyle değiştirecektir.

|**Değiştirilen fontlar**|
| :- |
|![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_2.png)|

## **Kaynak Dosya ve Çıktı PDF'sini İndir**
Aşağıdaki bağlantılardan kaynak Excel dosyasını ve çıktı PDF'sini indirebilirsiniz:

- [source.xlsx](5112611.xlsx)
- [output.pdf](5112616.pdf)

## **Kod**
Aşağıdaki kod `IWarningCallback`'i uyguluyor ve `PdfSaveOptions.WarningCallback` özelliğini uygulanan arayüz ile ayarlıyor. Artık, herhangi bir hücrede herhangi bir yazı tipi değiştirilirse, Aspose.Cells bu uyarıyı `WarningCallback.Warning()` metodunda tetikler.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

class GetWarningsForFontSubstitution : public IWarningCallback
{
public:
    void Warning(WarningInfo& info) override
    {
        if (info.GetType() == ExceptionType::FontSubstitution)
        {
            std::cout << "WARNING INFO: " << info.GetDescription().ToUtf8() << std::endl;
        }
    }

    static void Run()
    {
        U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
        U16String outDir(u"..\\Data\\02_OutputDirectory\\");
        Workbook workbook(srcDir + u"source.xlsx");
        PdfSaveOptions options;
        auto callback = std::make_shared<GetWarningsForFontSubstitution>();
        options.SetWarningCallback(callback.get());
        workbook.Save(outDir + u"output_out.pdf", options);
        std::cout << "PDF saved successfully with font substitution warnings!" << std::endl;
    }
};

int main()
{
    Aspose::Cells::Startup();
    GetWarningsForFontSubstitution::Run();
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Çıktı**
Kaynak Excel dosyasının PDF olarak dönüştürülmesinden sonra uyarılar şu şekilde hata ayıklama konsoluna çıktı verilir:

{{< highlight java >}}
WARNING INFO: Font substitution: Font [ Athene Logos; Regular ] has been substituted in Cell [ A6 ] in Sheet [ Sheet1 ].
WARNING INFO: Font substitution: Font [ B Traffic; Regular ] has been substituted in Cell [ A7 ] in Sheet [ Sheet1 ].
{{< /highlight >}}

{{% alert color="primary" %}}

Eğer elektronik tablonuz formüller içeriyorsa, PDF formatına dönüştürmeden hemen önce `Workbook.CalculateFormula` metodunu çağırmanız en iyisidir. Bu, formüle bağlı değerlerin yeniden hesaplanmasını sağlar ve PDF'de doğru değerler gösterilir.

{{% /alert %}}
