---
title: Çalışma Kitaplarında Koşullu Biçimlendirme Uygulama
description: Python da Aspose.Cells for Python via .NET kütüphanesini kullanarak iş sayfalarına koşullu biçimlendirme uygulama. Bu kriterleri ayarlayarak, hücrelerin görünümüne ve görünüşüne daha fazla kontrol sahibi olursunuz.
keywords: Aspose.Cells, Koşullu Biçimlendirme, Python, Çalışma Sayfası, Biçimlendirme
type: docs
weight: 130
url: /tr/python-net/apply-conditional-formatting-in-worksheets/
---

{{% alert color="primary" %}}

Bu makale, bir çalışma sayfasındaki hücre aralığına koşullu biçimlendirme eklemenin detaylı bir anlayışını sağlamak amacıyla tasarlanmıştır.

Koşullu biçimlendirme, Microsoft Excel'de gelişmiş bir özelliktir ve bir hücrenin değerine veya bir formülün değerine bağlı olarak biçimlendirme uygulamanıza olanak tanır. Örneğin, bir hücrenin arka planı, negatif bir değeri vurgulamak için kırmızı olabilir veya pozitif bir değer için metin rengi yeşil olabilir. Hücrenin değeri biçim koşulunu karşıladığında, biçim uygulanır. Hücrenin değeri biçim koşulunu karşılamadığında, hücrenin varsayılan biçimlendirmesi kullanılır.

Microsoft Office Automation ile koşullu biçimlendirme uygulamak mümkündür ancak bunun dezavantajları vardır. Örneğin, güvenlik, istikrar, ölçeklenebilirlik ve hız gibi çeşitli nedenler ve sorunlar bulunmaktadır. Başka bir çözüm bulma ana nedeni, Microsoft'un kendisinin yazılım çözümleri için Office Automation'a kesinlikle karşı çıkmasıdır.

Bu makale, Aspose.Cells API kullanarak birkaç basit kod satırıyla hücrelere koşullu biçimlendirme eklemeyi göstermektedir.

{{% /alert %}}

## **Hücre Değerine Bağlı Olarak Koşullu Biçimlendirme Uygulamak İçin Aspose.Cells Kullanma**

1. **Aspose.Cells'ı İndirin ve Kurun**.
   1. Aspose.Cells for Python via .NET'i indirin.
1. Geliştirme bilgisayarınıza kurun.
   Kurulduğunda, tüm Aspose bileşenleri değerlendirme modunda çalışır. Değerlendirme modunun süresiz bir sınırlaması yoktur ve yalnızca üretilen belgelere filigran enjekte eder.
1. **Bir proje oluşturun.**
   Visual Studio.NET'i başlatın ve yeni bir konsol uygulaması oluşturun. Bu örnek bir Python konsol uygulaması oluşturur, ancak VB.NET de kullanabilirsiniz.
1. **Referanslar Ekleyin**.
   Projenize Aspose.Cells referansı ekleyin.
1. *Hücre Değerine Bağlı Olarak Koşullu Biçimlendirme Uygulayın.
   Aşağıda verilen kod, görevi gerçekleştirmek için kullanılan koddur. Bir hücreye koşullu biçimlendirme uygularım.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ApplyConditionalFormattingCellValue-1.py" >}}

Yukarıdaki kod çalıştırıldığında, koşullu biçimlendirme çıktı dosyasının ilk çalışsayfasındaki “A1” hücresine uygulanır (çıktı.xls). A1 hücresinin değerine bağlı olarak uygulanan koşullu biçimlendirme. Eğer A1'in değeri 50 ile 100 arasında ise, arka plan rengi koşullu biçimlendirme nedeniyle kırmızı olur.

## **Aspose.Cells Kullanarak Formül Değerine Bağlı Olarak Koşullu Biçimlendirme Uygulama**

1. Formül Uygun Olarak Koşullu Biçimlendirme Uygulama (Kod Parçası)
   Aşağıda verilen kod, görevi gerçekleştirmek için kullanılan koddur. B3'e koşullu biçimlendirme uygular.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ApplyConditionalFormattingFormula-1.py" >}}

Yukarıdaki kod çalıştırıldığında, koşullu biçimlendirme çıktı dosyasının ilk çalışsayfasındaki “B3” hücresine uygulanır (çıktı.xls). Uygulanan koşullu biçimlendirme, “B1” ve “B2”nin değerinin toplamını hesaplayan formülün sonucuna bağlıdır.

{{< app/cells/assistant language="python-net" >}}
