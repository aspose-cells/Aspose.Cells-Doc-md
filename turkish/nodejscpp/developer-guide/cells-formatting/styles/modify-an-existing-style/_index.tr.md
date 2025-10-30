---
title: Mevcut Stili Değiştirme
linktitle: Mevcut Stili Değiştirme
description: Aspose.Cells, elektronik tablo dosyalarıyla çalışma imkanı sunan Node.js kütüphanesidir. Bu makale, var olan hücre stillerini değiştirmeyi ve istenildiği gibi hücrelerin görünümünü düzenlemeyi anlatacaktır.
keywords: Mevcut stilleri değiştirin, uygulamanın görünümünü özelleştirin, kılavuzlar, öğreticiler, yardım belgeleri, geliştirme belgeleri, API referansları, örnek kodlar, indirmeler, destek.
type: docs
weight: 90
url: /tr/nodejs-cpp/modify-an-existing-style/
---

{{% alert color="primary" %}}

Aynı biçimlendirme seçeneklerini hücrelere uygulamak için yeni bir biçimlendirme stili nesnesi oluşturun. Bir biçimlendirme stili nesnesi, yazı tipi, yazı tipi boyutu, girinti, sayı, kenar, desen vb. gibi biçimlendirme özelliklerinin bir kombinasyonudur, adlandırılır ve bir küme olarak saklanır. Uygulandığında, bu stildeki tüm biçimlendirme uygulanır.

Ayrıca var olan bir stili kullanabilir, çalışma kitabı ile kaydedebilir ve aynı özelliklere sahip bilgileri biçimlendirmek için kullanabilirsiniz.

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

## **Aspose.Cells for Node.js via C++ kullanımıyla**

Aşağıdaki örnekler [**Style.update()**](https://reference.aspose.com/cells/nodejs-cpp/style/#update--) metodunun nasıl kullanılacağını gösterir.

### **Stil Oluşturma ve Değiştirme**

Bu örnek, bir [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) nesnesi oluşturur, onu bir hücre aralığına uygular ve [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) nesnesini değiştirir. Yapılan değişiklikler otomatik olarak hücreye ve stili uygulanan aralığa yansıtılır.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Styles-CreateAndModifyStyle.js" >}}


### **Mevcut Bir Stili Değiştirmek**

Bu örnek, zaten bir diziye uygulanmış olan bir stil olan Yüzde'nin bulunduğu basit bir şablon Excel dosyasını kullanır. Örnek:

1. İlgili stili alır,
1. Stil nesnesi oluşturur ve
1. Stil biçimlendirmesini değiştirir.

Değişiklikler otomatik olarak uygulanan aralığa uygulanır.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Styles-ModifyExistingStyle.js" >}}


{{< app/cells/assistant language="nodejs-cpp" >}}
