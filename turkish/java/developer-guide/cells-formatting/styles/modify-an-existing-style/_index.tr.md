---
title: Mevcut Bir Stili Değiştirin
type: docs
weight: 50
url: /tr/java/modify-an-existing-style/
description: Microsoft Excel ve Aspose.Cells for Java API ile Excel'de stilleri nasıl değiştireceğinizi öğrenin.
keywords: modify an existing style excel, modify an existing style excel java, modify existing style excel, modify existing style excel java, change existing style in excel, change existing style in excel java, how to change style in excel, how to change style in excel with java, how to change style in excel with java, how to change style in excel using java, changing existing style in excel java, changing existing style in excel
---
{{% alert color="primary" %}}

Aynı biçimlendirme seçeneklerini hücrelere uygulamak için yeni bir biçimlendirme stili nesnesi oluşturun. Biçimlendirme stili nesnesi, bir küme olarak adlandırılan ve depolanan yazı tipi, yazı tipi boyutu, girinti, sayı, kenarlık, desenler vb. gibi biçimlendirme özelliklerinin bir kombinasyonudur. Uygulandığında, o stildeki biçimlendirmenin tümü uygulanır.

Ayrıca mevcut bir stili kullanabilir, çalışma kitabıyla kaydedebilir ve aynı özniteliklere sahip bilgileri biçimlendirmek için kullanabilirsiniz.

 Hücreler açıkça biçimlendirilmediğinde,**Normal** stili (çalışma kitabının varsayılan stili) uygulanır. Microsoft Excel, Normal stile ek olarak Virgül, Para Birimi ve Yüzde dahil olmak üzere çeşitli stilleri önceden tanımlar.

Aspose.Cells, bu stillerden herhangi birini veya istediğiniz niteliklerle tanımladığınız diğer stilleri değiştirmenize izin verir.

{{% /alert %}}

## **Microsoft Excel'i kullanma**

Microsoft Excel 97-2003'te bir stili güncellemek için:

1.  Üzerinde**Biçim** menü, tıklayın**stil**.
1.  bölümünden değiştirmek istediğiniz stili seçin.**Stil adı** liste.
1.  Tıklamak**Değiştir**.
1. Biçim Cells iletişim kutusundaki sekmeleri kullanarak istediğiniz stil seçeneklerini seçin.
1.  Tıklamak**TAMAM**.
1.  Altında**Stil içerir**, istediğiniz stil özelliklerini belirtin.
1.  Tıklamak**TAMAM** stili kaydetmek ve seçilen aralığa uygulamak için.

## **Aspose.Cells'i kullanma**

 Aspose.Cells şunları sağlar:[**Stil güncellemesi**](https://reference.aspose.com/cells/java/com.aspose.cells/style#update()) mevcut bir stili güncelleme yöntemi.

 İster Aspose.Cells kullanılarak dinamik olarak oluşturulmuş ister önceden tanımlı olsun, adlandırılmış bir stili değiştirmek için[**Stil güncellemesi**](https://reference.aspose.com/cells/java/com.aspose.cells/style#update()) bir hücreye veya aralığa uygulanan stildeki değişiklikleri yansıtma yöntemi.

 bu[**Stil güncellemesi**](https://reference.aspose.com/cells/java/com.aspose.cells/style#update() ) yöntemi şu şekilde davranır:**TAMAM** Stil iletişim kutusundaki düğme: mevcut bir stilde değişiklik yaptıktan sonra, değişikliği uygulamak için arayın. Bir hücre aralığına zaten bir stil uyguladıysanız, stil niteliklerini değiştirin ve yöntemi çağırın, bu hücrelerin biçimlendirmesi otomatik olarak güncellenir.

### **Stil Oluşturma ve Değiştirme**

Bu örnek, bir stil nesnesi oluşturur, bunu bir hücre aralığına uygular ve stil nesnesini değiştirir. Değişiklikler hücreye ve stilin uygulandığı aralığa otomatik olarak uygulanır.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatingStyle-CreatingStyle.java" >}}

### **Mevcut Bir Stili Değiştirmek**

Bu örnek, bir aralığa Yüzde adlı bir stilin zaten uygulanmış olduğu basit bir şablon Excel dosyası kullanır. Örnek:

1. tarzı alır,
1. bir stil nesnesi oluşturur ve
1. stil biçimlendirmesini değiştirir.

Değişiklikler, stilin uygulandığı aralığa otomatik olarak uygulanır.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ModifyExistingStyle-ModifyExistingStyle.java" >}}
