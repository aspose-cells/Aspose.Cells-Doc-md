---
title: Çalışma Sayfalarında Koşullu Biçimlendirme Uygula
description: Çalışma sayfalarında koşullu biçimlendirmeyi uygulamak için C#'deki Aspose.Cells kitaplığı nasıl kullanılır? Bu kriterleri ayarlayarak hücrelerin nasıl görüneceği ve görüneceği üzerinde daha fazla kontrole sahip olursunuz.
keywords: Aspose.Cells, Conditional Formatting, C#, Worksheet, Formatting
type: docs
weight: 130
url: /tr/net/apply-conditional-formatting-in-worksheets/
---
{{% alert color="primary" %}}

Bu makale, çalışma sayfasındaki bir hücre aralığına koşullu biçimlendirmenin nasıl ekleneceğine ilişkin ayrıntılı bir anlayış sağlamak üzere tasarlanmıştır.

Koşullu biçimlendirme, Microsoft Excel'de, bir dizi hücreye biçim uygulamanıza ve bu biçimlendirmenin hücrenin değerine veya formül değerine bağlı olarak değişmesine olanak tanıyan gelişmiş bir özelliktir. Örneğin, bir hücrenin arka planı negatif bir değeri vurgulamak için kırmızı olabilir veya pozitif bir değeri vurgulamak için metin rengi yeşil olabilir. Hücrenin değeri format koşulunu karşıladığında format uygulanır. Hücrenin değeri format koşulunu karşılamıyorsa hücrenin varsayılan formatı kullanılır.

Microsoft Ofis Otomasyonu ile koşullu biçimlendirme uygulamak mümkündür ancak bunun dezavantajları vardır. Bunun çeşitli nedenleri ve sorunları vardır: örneğin güvenlik, kararlılık, ölçeklenebilirlik ve hız. Başka bir çözüm bulmanın ana nedeni, Microsoft'in kendisinin yazılım çözümleri için Ofis Otomasyonu'na şiddetle karşı çıkmasını önermesidir.

Bu makalede, bir konsol uygulamasının nasıl oluşturulacağı, Aspose.Cells API numaralı telefonu kullanarak birkaç basit kod satırıyla hücrelere koşullu biçimlendirmenin nasıl ekleneceği gösterilmektedir.

{{% /alert %}}

##  **Cell Değerine Dayalı Koşullu Biçimlendirmeyi Uygulamak için Aspose.Cells'i Kullanma**

1. *Aspose.Cells'i indirin ve yükleyin**.
 1. Aspose.Cells for .NET'i indirin.
1. Geliştirme bilgisayarınıza yükleyin.
 Tüm Aspose bileşenleri kurulduğunda değerlendirme modunda çalışır. Değerlendirme modunun zaman sınırı yoktur ve yalnızca üretilen belgelere filigranlar enjekte eder.
1. *Bir proje oluşturun**.
 Visual Studio.NET'i başlatın ve yeni bir konsol uygulaması oluşturun. Bu örnek bir C# konsol uygulaması oluşturur ancak siz VB.NET'i de kullanabilirsiniz.
1. *Referans ekleyin**.
 Projenize Aspose.Cells'e bir referans ekleyin, örneğin ….\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll'ye bir referans ekleyin
1. *Hücre değerine göre koşullu biçimlendirme uygulayın.
Görevi gerçekleştirmek için kullanılan kod aşağıdadır. Hücreye koşullu biçimlendirme uyguluyorum.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ApplyConditionalFormatting-ApplyConditionalFormattingCellValue-1.cs" >}}

Yukarıdaki kod çalıştırıldığında çıktı dosyasının (output.xls) ilk çalışma sayfasındaki “A1” hücresine koşullu biçimlendirme uygulanır. A1'e uygulanan koşullu biçimlendirme hücre değerine bağlıdır. A1 hücresinin değeri 50 ile 100 arasında ise uygulanan koşullu biçimlendirmeden dolayı arka plan rengi kırmızı olur.

##  **Formüle Dayalı Koşullu Biçimlendirmeyi Uygulamak için Aspose.Cells'i Kullanma**

1. Formüle bağlı olarak koşullu biçimlendirme uygulama (Kod Parçacığı)
 Görevi gerçekleştirmek için gereken kod aşağıdadır. B3'e koşullu biçimlendirme uygular.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ApplyConditionalFormatting-ApplyConditionalFormattingFormula-1.cs" >}}

Yukarıdaki kod çalıştırıldığında çıktı dosyasının (output.xls) ilk çalışma sayfasındaki “B3” hücresine koşullu biçimlendirme uygulanır. Uygulanan koşullu biçimlendirme, “B3” değerini B1 ve B2 toplamı olarak hesaplayan formüle bağlıdır.
