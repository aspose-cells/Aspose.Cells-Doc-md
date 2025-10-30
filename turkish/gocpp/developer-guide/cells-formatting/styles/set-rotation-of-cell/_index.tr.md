---
title: Hücrenin Yazısını Golang ile C++ kullanarak Nasıl Döndürürüz
linktitle: Hücrenin metnini Nasıl Döndürülür
type: docs
weight: 80
url: /tr/go-cpp/how-to-rotate-text-of-cell/
description: C++ kodu ile Aspose.Cells for C++ API kullanarak Hücre yazısını döndürme
keywords: c++ ile Hücre yazısını döndürme, C++ ile çalışma kitabında hücreyi programlı olarak döndürme, çalışma kitabında hücre döndürme açısını programlı ayarlama, excel de Hücre yazısını C++ ile nasıl döndürülür
---

## **Aspose.Cells'te Hücrenin Metnini Döndür**

Aspose.Cells, programcıların Excel elektronik tabloları ile programlı olarak çalışmasına olanak sağlayan güçlü bir C++ bileşenidir. Aspose.Cells'in sunduğu özelliklerden biri, hücreleri döndürme yeteneğidir; bu, yazı yönünü özelleştirmenize ve verilerinizin görsel sunumunu geliştirmeye yardımcı olur. Bu belgede, Aspose.Cells kullanarak hücreleri nasıl döndüreceğinizi keşfedeceğiz.

## **Excel'de Hücrenin Metnini Döndürme**
Bir hücreyi Excel'de döndürmek için aşağıdaki adımları kullanabilirsiniz:
1. Excel'i açın ve döndürmek istediğiniz hücreyi veya hücre aralığını seçin.
1. Seçilen hücre(ler)e sağ tıklayın ve bağlam menüsünden "Hücreleri Biçimlendir"'i seçin. Alternatif olarak, Excel şeridinde "Ana Sayfa" sekmesine gidip "Hücreler" grubundaki "Biçimlamanın" açılır menüsüne tıklayıp "Hücreleri Biçimlendir"'i seçebilirsiniz.
1. "Hücreleri Biçimlendir" iletişim kutusunda, "Hizalama" sekmesine gidin.
1. "Yönlendirme" bölümünde, metni döndürebileceğiniz seçenekleri göreceksiniz. "Derece" kutusuna istenen dönme açısını doğrudan girebilirsiniz. Pozitif değerler metni saat yönünün tersine döndürür, negatif değerler ise saat yönünde döndürür.
<br>
![todo:image_alt_text](alignment.png)
1. İstenilen yönlendirmeyi seçtikten sonra, değişiklikleri uygulamak için "Tamam"'a tıklayın. Seçilen hücre(ler) artık seçtiğiniz dönme açısına veya yönlendirmeye göre dönecektir.

## **Aspose.Cells API kullanarak Hücrenin Metnini Döndürme**

[**Style.GetRotationAngle()**](https://reference.aspose.com/cells/go-cpp/style/getrotationangle/) özelliği hücreleri döndürmeyi kolaylaştırır. Aspose.Cells'te hücreleri döndürmek için şu adımları izlemeniz gerekir:
1. Excel Çalışma Kitabını Yükle
<br>
İlk olarak, mevcut bir Excel dosyasını açmak veya yeni bir tane oluşturmak için Workbook sınıfını kullanarak Excel çalışma kitabını yüklemeniz gerekir. 

1. Çalışma Sayfasına Eriş
<br>
Çalışma kitabı yüklendikten sonra, hücreleri döndürmek istediğiniz çalışma sayfasına erişmeniz gerekir. Çalışma sayfasına endeksine veya adına göre erişebilirsiniz. 

1. Hücrenin metnini döndür
<br>
Artık çalışma sayfasına erişiminiz olduğuna göre, istenen hücrelerin Stil objesini değiştirerek hücreleri döndürebilirsiniz. Stil objesi, dönme dahil çeşitli biçimlendirme seçeneklerini belirlemenizi sağlar. 

1. Çalışma Kitabını Kaydet
<br>
Hücreleri döndürdükten sonra, değiştirilmiş çalışma kitabını Save metodunu kullanarak bir dosyaya veya akıma geri kaydedebilirsiniz.

## **C++ Örnek Kodu**

Lütfen aşağıdaki kodu inceleyin, bir çalışma kitabı nesnesi oluşturur ve çeşitli hücreler için farklı döndürme açıları belirler. Ekran görüntüsü, örnek kodun çalıştırılmasından sonra elde edilen sonucu gösterir.
<br>
<img src="rotation.png" width=80% />

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SetRotationOfCell.go" >}}
