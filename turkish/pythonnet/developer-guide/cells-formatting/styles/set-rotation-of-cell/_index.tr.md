---
title: Hücrenin metnini Nasıl Döndürülür
type: docs
weight: 80
url: /tr/python-net/how-to-rotate-text-of-cell/
description: Aspose.Cells for Python via .NET API ile Cell in metnini döndürmek için C# kodu
keywords: Python ile Cell in metnini döndürme, Python ile çalışma kitabındaki Cell in metnini programatik olarak döndürme, çalışma kitabında hücre dönme açısını programatik olarak ayarlama, Python da Excel de Cell in metnini nasıl döndüreceğinizi öğrenin
---

## **Aspose.Cells for Python via .NET'de Cell'in Metnini Döndürmek**

Aspose.Cells for Python via .NET, geliştiricilerin Excel tabloları ile programlamalı olarak çalışmasını sağlayan güçlü bir .NET ve Java bileşenidir. Aspose.Cells for Python via .NET'de sunulan özelliklerden biri hücreleri döndürme yeteneğidir; bu, metnin yönünü özelleştirmenize ve veri görsel sunumunu geliştirmenize olanak tanır. Bu belgede, Aspose.Cells for Python via .NET kullanarak hücreleri nasıl döndüreceğinizi keşfedeceğiz.

## **Excel'de Hücrenin Metnini Döndürme**
Bir hücreyi Excel'de döndürmek için aşağıdaki adımları kullanabilirsiniz:
1. Excel'i açın ve döndürmek istediğiniz hücreyi veya hücre aralığını seçin.
1. Seçilen hücre(ler)e sağ tıklayın ve bağlam menüsünden "Hücreleri Biçimlendir"'i seçin. Alternatif olarak, Excel şeridinde "Ana Sayfa" sekmesine gidip "Hücreler" grubundaki "Biçimlamanın" açılır menüsüne tıklayıp "Hücreleri Biçimlendir"'i seçebilirsiniz.
1. "Hücreleri Biçimlendir" iletişim kutusunda, "Hizalama" sekmesine gidin.
1. "Yönlendirme" bölümünde, metni döndürebileceğiniz seçenekleri göreceksiniz. "Derece" kutusuna istenen dönme açısını doğrudan girebilirsiniz. Pozitif değerler metni saat yönünün tersine döndürür, negatif değerler ise saat yönünde döndürür.
<br>
![todo:image_alt_text](alignment.png)
1. İstenilen yönlendirmeyi seçtikten sonra, değişiklikleri uygulamak için "Tamam"'a tıklayın. Seçilen hücre(ler) artık seçtiğiniz dönme açısına veya yönlendirmeye göre dönecektir.

## **Aspose.Cells for Python via .NET API kullanarak hücre metnini döndürme nasıl yapılır**

[**Style.rotation_angle**](https://reference.aspose.com/cells/python-net/aspose.cells/style/rotation_angle) özelliği hücreleri döndürmeyi kolaylaştırır. Aspose.Cells for Python via .NET'de hücreleri döndürmek için aşağıdaki adımları izlemelisiniz:
1. Excel Çalışma Kitabını Yükle
<br>
İlk olarak, Aspose.Cells for Python via .NET kullanarak Excel çalışma kitabını yüklemeniz gerekir. Var olan bir Excel dosyasını açmak veya yeni bir tane oluşturmak için Workbook sınıfını kullanabilirsiniz. 

1. Çalışma Sayfasına Eriş
<br>
Çalışma kitabı yüklendikten sonra, hücreleri döndürmek istediğiniz çalışma sayfasına erişmeniz gerekir. Çalışma sayfasına endeksine veya adına göre erişebilirsiniz. 

1. Hücrenin metnini döndür
<br>
Artık çalışma sayfasına erişiminiz olduğuna göre, istenen hücrelerin Stil objesini değiştirerek hücreleri döndürebilirsiniz. Stil objesi, dönme dahil çeşitli biçimlendirme seçeneklerini belirlemenizi sağlar. 

1. Çalışma Kitabını Kaydet
<br>
Hücreleri döndürdükten sonra, değiştirilmiş çalışma kitabını Save metodunu kullanarak bir dosyaya veya akıma geri kaydedebilirsiniz.

## **Python Örnek Kodu**

Lütfen aşağıdaki kodu inceleyin, bir çalışma kitabı nesnesi oluşturur ve çeşitli hücreler için farklı döndürme açıları belirler. Ekran görüntüsü, örnek kodun çalıştırılmasından sonra elde edilen sonucu gösterir.
<br>
<img src="rotation.png" width=80% />



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-Cells-rotate-text.py" >}}

