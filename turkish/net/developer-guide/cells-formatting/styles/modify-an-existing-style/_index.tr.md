---
title: Mevcut Bir Stili Değiştirin
description: Aspose.Cells, kullanıcıların mevcut hücre stillerini değiştirmesine olanak tanıyan, elektronik tablo dosyalarıyla çalışmaya yönelik bir .NET kitaplığıdır. Bu makalede, kullanıcıların hücrelerin görünümünü ihtiyaç duydukları şekilde değiştirebilmeleri için Aspose.Cells kitaplığıyla mevcut bir hücre stilinin nasıl değiştirileceği anlatılacaktır.
keywords: Modify existing styles, customize the look and feel of your application, guides, tutorials, help documentation, development documentation, API references, sample code, downloads, support.
type: docs
weight: 90
url: /tr/net/modify-an-existing-style/
---
{{% alert color="primary" %}}

Hücrelere aynı biçimlendirme seçeneklerini uygulamak için yeni bir biçimlendirme stili nesnesi oluşturun. Biçimlendirme stili nesnesi, yazı tipi, yazı tipi boyutu, girinti, sayı, kenarlık, desenler vb. gibi biçimlendirme özelliklerinin bir küme olarak adlandırılıp saklanan birleşimidir. Uygulandığında o stildeki tüm formatlama uygulanır.

Ayrıca mevcut bir stili kullanabilir, onu çalışma kitabıyla birlikte kaydedebilir ve bilgileri aynı niteliklerle biçimlendirmek için kullanabilirsiniz.

 Hücreler açıkça biçimlendirilmediğinde,**Normal** stil (çalışma kitabının varsayılan stili) uygulanır. Microsoft Excel, Normal stile ek olarak Virgül, Para Birimi ve Yüzde dahil çeşitli stilleri önceden tanımlar.

Aspose.Cells, bu stillerden herhangi birini veya tanımladığınız herhangi bir stili istediğiniz özelliklerle değiştirmenize olanak sağlar.

{{% /alert %}}

##  **Microsoft Excel'i kullanma**

Microsoft Excel 97-2003'te bir stili güncellemek için:

1.  Üzerinde**Biçim** menüsünde *Stil**'i tıklayın.
1.  Değiştirmek istediğiniz stili seçin.**Stil adı** liste.
1. *Değiştir**'i tıklayın.
1. Biçim Cells iletişim kutusundaki sekmeleri kullanarak istediğiniz stil seçeneklerini seçin.
1. *Tamam**'ı tıklayın.
1. *Stil içerir** altında istediğiniz stil özelliklerini belirtin.
1.  Tıklamak**OK** Stili kaydetmek ve seçilen aralığa uygulamak için.

##  **Aspose.Cells'i kullanma**

 Aşağıdaki örnekler nasıl kullanılacağını göstermektedir[**Stil.Güncelleme**](https://reference.aspose.com/cells/net/aspose.cells/style/methods/update)yöntem.

###  **Stil Oluşturma ve Değiştirme**

 Bu örnek bir oluşturur[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style) nesneyi bir dizi hücreye uygular ve[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style)nesne. Değişiklikler hücreye ve stilin uygulandığı aralığa otomatik olarak uygulanır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ModifyExistingStyle-ModifyThroughStyleObject-1.cs" >}}

###  **Mevcut Bir Stili Değiştirme**

Bu örnekte, Yüzde adı verilen bir stilin bir aralığa zaten uygulanmış olduğu basit bir şablon Excel dosyası kullanılmaktadır. Örnek:

1. tarzı alır,
1. bir stil nesnesi yaratır ve
1. stil formatını değiştirir.

Değişiklikler, stilin uygulandığı aralığa otomatik olarak uygulanır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ModifyExistingStyle-ModifyThroughSampleExcelFile-1.cs" >}}
