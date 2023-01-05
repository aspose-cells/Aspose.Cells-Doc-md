---
title: Mevcut Bir Stili Değiştirin
type: docs
weight: 90
url: /tr/net/modify-an-existing-style/
---
{{% alert color="primary" %}}

Aynı biçimlendirme seçeneklerini hücrelere uygulamak için yeni bir biçimlendirme stili nesnesi oluşturun. Biçimlendirme stili nesnesi, bir küme olarak adlandırılan ve depolanan yazı tipi, yazı tipi boyutu, girinti, sayı, kenarlık, desenler vb. gibi biçimlendirme özelliklerinin bir kombinasyonudur. Uygulandığında, o stildeki biçimlendirmenin tümü uygulanır.

Ayrıca mevcut bir stili kullanabilir, çalışma kitabıyla kaydedebilir ve bilgileri aynı özniteliklerle biçimlendirmek için kullanabilirsiniz.

 Hücreler açıkça biçimlendirilmediğinde,**Normal** stili (çalışma kitabının varsayılan stili) uygulanır. Microsoft Excel, Normal stile ek olarak Virgül, Para Birimi ve Yüzde dahil olmak üzere çeşitli stilleri önceden tanımlar.

Aspose.Cells, bu stillerden herhangi birini veya istediğiniz niteliklerle tanımladığınız diğer stilleri değiştirmenize izin verir.

{{% /alert %}}

## **Microsoft Excel'i kullanma**

Microsoft Excel 97-2003'te bir stili güncellemek için:

1.  Üzerinde**Biçim** menü, tıklayın**stil**.
1.  bölümünden değiştirmek istediğiniz stili seçin.**Stil adı** liste.
1.  Tıklamak**Değiştir**.
1. Biçim Cells iletişim kutusundaki sekmeleri kullanarak istediğiniz stil seçeneklerini seçin.
1.  Tıklamak**Tamam**.
1.  Altında**Stil içerir**, istediğiniz stil özelliklerini belirtin.
1.  Tıklamak**Tamam** stili kaydetmek ve seçilen aralığa uygulamak için.

## **Aspose.Cells'i kullanma**

 Aşağıdaki örnekler nasıl kullanılacağını göstermektedir[**Stil.Güncelleme**](https://reference.aspose.com/cells/net/aspose.cells/style/methods/update)yöntem.

### **Stil Oluşturma ve Değiştirme**

 Bu örnek bir oluşturur[**stil**](https://reference.aspose.com/cells/net/aspose.cells/style) nesne, onu bir hücre aralığına uygular ve değiştirir[**stil**](https://reference.aspose.com/cells/net/aspose.cells/style)nesne. Değişiklikler hücreye ve stilin uygulandığı aralığa otomatik olarak uygulanır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ModifyExistingStyle-ModifyThroughStyleObject-1.cs" >}}

### **Mevcut Bir Stili Değiştirmek**

Bu örnek, bir aralığa Yüzde adlı bir stilin zaten uygulanmış olduğu basit bir şablon Excel dosyası kullanır. Örnek:

1. tarzı alır,
1. bir stil nesnesi oluşturur ve
1. stil biçimlendirmesini değiştirir.

Değişiklikler, stilin uygulandığı aralığa otomatik olarak uygulanır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ModifyExistingStyle-ModifyThroughSampleExcelFile-1.cs" >}}
