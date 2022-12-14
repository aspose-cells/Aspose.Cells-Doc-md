---
title: Çalışma Sayfalarında Koşullu Biçimlendirme Uygula
type: docs
weight: 130
url: /tr/net/apply-conditional-formatting-in-worksheets/
---
{{% alert color="primary" %}}

Bu makale, bir çalışma sayfasındaki bir dizi hücreye koşullu biçimlendirmenin nasıl ekleneceğine ilişkin ayrıntılı bir anlayış sağlamak için tasarlanmıştır.

Koşullu biçimlendirme, Microsoft Excel'de bulunan ve bir hücre aralığına biçimler uygulamanıza ve bu biçimlendirmenin hücrenin değerine veya bir formülün değerine bağlı olarak değişmesini sağlayan gelişmiş bir özelliktir. Örneğin, bir hücrenin arka planı negatif bir değeri vurgulamak için kırmızı olabilir veya pozitif bir değer için metin rengi yeşil olabilir. Hücrenin değeri biçim koşulunu karşıladığında biçim uygulanır. Hücrenin değeri biçim koşulunu karşılamıyorsa, hücrenin varsayılan biçimlendirmesi kullanılır.

Microsoft Office Otomasyonu ile koşullu biçimlendirme uygulamak mümkündür, ancak bunun dezavantajları vardır. İlgili birkaç neden ve sorun vardır: örneğin, güvenlik, kararlılık, ölçeklenebilirlik ve hız. Başka bir çözüm bulmanın ana nedeni, Microsoft'in kendisinin yazılım çözümleri için Office Otomasyonu'nu şiddetle önermesidir.

Bu makale, bir konsol uygulamasının nasıl oluşturulacağını, Aspose.Cells API'i kullanarak en basit birkaç kod satırıyla hücrelere koşullu biçimlendirme eklemeyi gösterir.

{{% /alert %}}

## **Cell Değerine Göre Koşullu Biçimlendirmeyi Uygulamak için Aspose.Cells'i Kullanma**

1. **İndirin ve yükleyin Aspose.Cells**.
 1. İndir Aspose.Cells for .NET.
1. Geliştirme bilgisayarınıza kurun.
Tüm Aspose bileşenleri kurulduğunda değerlendirme modunda çalışır. Değerlendirme modunun zaman sınırı yoktur ve yalnızca üretilen belgelere filigran ekler.
1. **proje oluştur**.
 Visual Studio.NET'i başlatın ve yeni bir konsol uygulaması oluşturun. Bu örnek, bir C# konsol uygulaması oluşturur, ancak VB.NET'i de kullanabilirsiniz.
1. **referans ekle**.
 Projenize Aspose.Cells'e bir referans ekleyin, örneğin ….\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll'ye bir referans ekleyin
1. *Hücre değerine göre koşullu biçimlendirme uygulayın.
 Görevi gerçekleştirmek için kullanılan kod aşağıdadır. Bir hücreye koşullu biçimlendirme uyguluyorum.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ApplyConditionalFormatting-ApplyConditionalFormattingCellValue-1.cs" >}}

Yukarıdaki kod yürütüldüğünde, çıktı dosyasının (output.xls) ilk çalışma sayfasındaki "A1" hücresine koşullu biçimlendirme uygulanır. A1'e uygulanan koşullu biçimlendirme, hücre değerine bağlıdır. A1'in hücre değeri 50 ile 100 arasındaysa, uygulanan koşullu biçimlendirme nedeniyle arka plan rengi kırmızıdır.

## **Formüle Dayalı Koşullu Biçimlendirmeyi Uygulamak için Aspose.Cells'i Kullanma**

1. Formüle bağlı olarak koşullu biçimlendirme uygulama (Kod Parçacığı)
 Görevi gerçekleştirmek için kod aşağıdadır. B3'te koşullu biçimlendirme uygular.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ApplyConditionalFormatting-ApplyConditionalFormattingFormula-1.cs" >}}

Yukarıdaki kod yürütüldüğünde, çıktı dosyasının (output.xls) ilk çalışma sayfasındaki "B3" hücresine koşullu biçimlendirme uygulanır. Uygulanan koşullu biçimlendirme, “B3” değerini B1 ve B2'nin toplamı olarak hesaplayan formüle bağlıdır.
