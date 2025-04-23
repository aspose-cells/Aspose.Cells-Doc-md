---
title: Çalışma Kitaplarında Koşullu Biçimlendirme Uygulama
linktitle: Çalışma Kitaplarında Koşullu Biçimlendirme Uygulama
description: Node.js de C++ kullanarak Aspose.Cells kütüphanesiyle çalışma sayfalarında hücre görünümünü daha iyi kontrol etmek için koşullu biçimlendirme uygulama.
keywords: Aspose.Cells, Koşullu Biçimlendirme, Node.js via C++, Çalışma Sayfası, Biçimlendirme
type: docs
weight: 130
url: /tr/nodejs-cpp/apply-conditional-formatting-in-worksheets/
---

{{% alert color="primary" %}}

Bu makale, bir çalışma sayfasındaki hücre aralığına koşullu biçimlendirme eklemenin detaylı bir anlayışını sağlamak amacıyla tasarlanmıştır.

Koşullu biçimlendirme, Microsoft Excel'de gelişmiş bir özelliktir ve bir hücrenin değerine veya bir formülün değerine bağlı olarak biçimlendirme uygulamanıza olanak tanır. Örneğin, bir hücrenin arka planı, negatif bir değeri vurgulamak için kırmızı olabilir veya pozitif bir değer için metin rengi yeşil olabilir. Hücrenin değeri biçim koşulunu karşıladığında, biçim uygulanır. Hücrenin değeri biçim koşulunu karşılamadığında, hücrenin varsayılan biçimlendirmesi kullanılır.

Microsoft Office Automation ile koşullu biçimlendirme uygulamak mümkündür ancak bunun dezavantajları vardır. Örneğin, güvenlik, istikrar, ölçeklenebilirlik ve hız gibi çeşitli nedenler ve sorunlar bulunmaktadır. Başka bir çözüm bulma ana nedeni, Microsoft'un kendisinin yazılım çözümleri için Office Automation'a kesinlikle karşı çıkmasıdır.

Bu makale, Aspose.Cells API kullanarak birkaç basit kod satırıyla hücrelere koşullu biçimlendirme eklemeyi göstermektedir.

{{% /alert %}}

## **Hücre Değerine Bağlı Olarak Koşullu Biçimlendirme Uygulamak İçin Aspose.Cells Kullanma**

1. **Aspose.Cells'ı İndirin ve Kurun**.
   1. Aspose.Cells for Node.js via C++'ü indirin.
1. Geliştirme bilgisayarınıza kurun.
   Kurulduğunda, tüm Aspose bileşenleri değerlendirme modunda çalışır. Değerlendirme modunun süresiz bir sınırlaması yoktur ve yalnızca üretilen belgelere filigran enjekte eder.
1. **Bir proje oluşturun.**
   Node.js projenize başlamak için başlatın. Bu örnek, bir Node.js konsol uygulaması oluşturmaktadır.
1. **Referanslar Ekleyin**.
   Projeye Aspose.Cells referansı ekleyin, örneğin paketi aşağıdaki gibi dahil ederek:
   ```javascript
   const AsposeCells = require("aspose.cells.node");
   ```
1. **Hücre değerine dayalı koşullu biçimlendirme uygula**.
   Aşağıda, görevi yerine getirmek için kullanılan kod yer almaktadır. Bu, hücre üzerinde koşullu biçimlendirme uygular.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ConditionalFormatting-ApplyToCellValue.js" >}}


Yukarıdaki kod yürütüldüğünde, çıktı dosyasının (output.xls) ilk çalışma sayfasındaki “A1” hücresine koşullu biçimlendirme uygulanır. A1 hücresine uygulanan koşullu biçimlendirme, hücre değere bağlıdır. A1 hücresinin değeri 50 ile 100 arasında ise, koşullu biçimlendirme nedeniyle arka plan rengi kırmızı olur.

## **Aspose.Cells Kullanarak Formül Değerine Bağlı Olarak Koşullu Biçimlendirme Uygulama**

1. Formül Uygun Olarak Koşullu Biçimlendirme Uygulama (Kod Parçası)
   Aşağıda verilen kod, görevi gerçekleştirmek için kullanılan koddur. B3'e koşullu biçimlendirme uygular.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ConditionalFormatting-ApplyToFormula.js" >}}

Yukarıdaki kod yürütüldüğünde, çıktı dosyasının (output.xls) ilk çalışma sayfasındaki “B3” hücresine koşullu biçimlendirme uygulanır. Uygulanan koşullu biçimlendirme, B3 hücresinin B1 ve B2 toplamı olarak hesaplanan değere bağlıdır.
