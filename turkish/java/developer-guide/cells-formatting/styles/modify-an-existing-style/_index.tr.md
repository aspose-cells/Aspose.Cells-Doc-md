---
title: Mevcut Stili Değiştirme
type: docs
weight: 50
url: /tr/java/modify-an-existing-style/
description: Microsoft Excel ve Aspose.Cells for Java API sı ile Excel de stilleri nasıl değiştireceğinizi öğrenin.
keywords: mevcut bir stili değiştirmek excel, mevcut bir stili değiştirmek excel java, mevcut stil excel değiştirme, mevcut stil excel java değiştirme, excelde mevcut stili değiştirme, excelde mevcut stili değiştirme java, excelde stili nasıl değiştirilir, excelde stil nasıl değiştirilir java, excelde stil nasıl değiştirilir java kullanarak, excelde mevcut stili değiştirme java, excelde mevcut stili değiştirme
---

{{% alert color="primary" %}}

Hücrelere aynı biçimlendirme seçeneklerini uygulamak için yeni bir biçimlendirme stili nesnesi oluşturun. Biçimlendirme stili nesnesi, adlandırılmış ve bir set olarak depolanan font, yazı tipi boyutu, girinti, sayı, kenarlık, desen vb. gibi biçimlendirme özelliklerinin bir kombinasyonudur. Uygulandığında, o stildeki tüm biçimlendirme uygulanır.

Ayrıca, mevcut bir stili kullanabilir, onu çalışma kitabıyla kaydedebilir ve aynı özelliklere sahip bilgiyi biçimlendirmek için kullanabilirsiniz.

Hücreler açıkça biçimlendirilmediğinde, **Normal** stili (çalışma kitabının varsayılan stili) uygulanır. Microsoft Excel, Comma, Currency ve Percent dahil olmak üzere birkaç önceden tanımlanmış stile ek olarak Normal stili de tanımlar.

Aspose.Cells, bu stillerin herhangi birini veya kendi istediğiniz özelliklere sahip herhangi bir stilini değiştirmenize olanak tanır.

{{% /alert %}}

## **Microsoft Excel Kullanımı**

Microsoft Excel 97-2003'te bir stil güncellemek için:

1. **Format** menüsünde **Stil**'e tıklayın.
1. Değiştirmek istediğiniz stili **Stil adı** listesinden seçin.
1. **Değiştir**'e tıklayın.
1. Biçim Hücreleri iletişim kutusundaki sekmeleri kullanarak istediğiniz stil seçeneklerini seçin.
1. **Tamam**'a tıklayın.
1. **Stil içerir** altında istediğiniz stil özelliklerini belirtin.
1. Kaydetmek ve seçili aralığa uygulamak için **Tamam**'a tıklayın.

## **Aspose.Cells Kullanımı**

Aspose.Cells, mevcut bir stili güncellemek için [**Style.update**](https://reference.aspose.com/cells/java/com.aspose.cells/style#update--) yöntemi sağlar.

Dinamik olarak oluşturulmuş veya önceden tanımlanmış bir adlı stili değiştirmek için, hücre veya aralığa uygulanan stilde yapılan değişiklikleri yansıtmak için [**Style.update**](https://reference.aspose.com/cells/java/com.aspose.cells/style#update--) yöntemini çağırın.

[**Style.update**](https://reference.aspose.com/cells/java/com.aspose.cells/style#update--) yöntemi, Stil iletişim kutusundaki **Tamam** düğmesine benzer: mevcut bir stile değişiklikler yaptıktan sonra değişiklikleri uygulamak için çağrı yapın. Zaten bir hücre aralığına bir stil uyguladıysanız, stile öznitelikleri değiştirin ve yöntemi çağırın; bu hücrelerin biçimi otomatik olarak güncellenir.

### **Stil Oluşturma ve Değiştirme**

Bu örnek, bir stil nesnesi oluşturur, hücre aralığına uygular ve stil nesnesini değiştirir. Değişiklikler otomatik olarak hücreye ve uygulanan aralığa uygulanır.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatingStyle-CreatingStyle.java" >}}

### **Mevcut Bir Stili Değiştirmek**

Bu örnek, zaten bir diziye uygulanmış olan bir stil olan Yüzde'nin bulunduğu basit bir şablon Excel dosyasını kullanır. Örnek:

1. İlgili stili alır,
1. Stil nesnesi oluşturur ve
1. Stil biçimlendirmesini değiştirir.

Değişiklikler otomatik olarak uygulanan aralığa uygulanır.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ModifyExistingStyle-ModifyExistingStyle.java" >}}
