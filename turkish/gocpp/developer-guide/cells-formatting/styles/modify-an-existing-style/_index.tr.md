---
title: Mevcut bir Stili Golang ile C++ kullanarak düzenle
description: Aspose.Cells, kullanıcıların mevcut hücre stillerini değiştirmelerine olanak tanıyan, elektronik tablo dosyalarıyla çalışmak için C++ kütüphanesidir. Bu makale, kullanıcıların hücrelerin görünümünü ihtiyaçlarına göre değiştirebilmeleri için Aspose.Cells kütüphanesi ile mevcut hücre stilini nasıl değiştireceklerini tanıtacaktır.
keywords: Mevcut stilleri değiştirin, uygulamanın görünümünü özelleştirin, kılavuzlar, öğreticiler, yardım belgeleri, geliştirme belgeleri, API referansları, örnek kodlar, indirmeler, destek.
type: docs
weight: 90
url: /tr/go-cpp/modify-an-existing-style/
---

{{% alert color="primary" %}}

Aynı biçimlendirme seçeneklerini hücrelere uygulamak için yeni bir biçimlendirme stili nesnesi oluşturun. Bir biçimlendirme stili nesnesi, yazı tipi, yazı tipi boyutu, girinti, sayı, kenar, desen vb. gibi biçimlendirme özelliklerinin bir kombinasyonudur, adlandırılır ve bir küme olarak saklanır. Uygulandığında, bu stildeki tüm biçimlendirme uygulanır.

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

Aşağıdaki örnekler [**Style.Update**](https://reference.aspose.com/cells/go-cpp/style/update/) metodunun nasıl kullanılacağını gösterir.

### **Stil Oluşturma ve Değiştirme**

Bu örnek, bir [**Style**](https://reference.aspose.com/cells/go-cpp/style/) nesnesi oluşturur, onu bir hücre aralığına uygular ve [**Style**](https://reference.aspose.com/cells/go-cpp/style/) nesnesini değiştirir. Yapılan değişiklikler, otomatik olarak hücreye ve stilin uygulandığı aralığa yansıtılır.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ModifyAnExistingStyle.go" >}}
### **Mevcut Bir Stili Değiştirmek**

Bu örnek, zaten bir diziye uygulanmış olan bir stil olan Yüzde'nin bulunduğu basit bir şablon Excel dosyasını kullanır. Örnek:

1. İlgili stili alır,
1. Stil nesnesi oluşturur ve
1. Stil biçimlendirmesini değiştirir.

Değişiklikler otomatik olarak uygulanan aralığa uygulanır.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ModifyAnExistingStyle-1.go" >}}
