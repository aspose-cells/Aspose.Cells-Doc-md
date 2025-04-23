---
title: Mevcut Stili Değiştirme
description: Aspose.Cells, kullanıcıların mevcut hücre stillerini değiştirmelerine olanak tanıyan bir Python kütüphanesidir. Bu makale, Aspose.Cells for Python via .NET kütüphanesi kullanılarak mevcut bir hücre stilinin nasıl değiştirileceğini tanıtacak ve böylece kullanıcıların hücrelerin görünümünü ihtiyaçlarına göre değiştirmelerine olanak sağlayacaktır.
keywords: Mevcut stilleri değiştirin, uygulamanın görünümünü özelleştirin, kılavuzlar, öğreticiler, yardım belgeleri, geliştirme belgeleri, API referansları, örnek kodlar, indirmeler, destek.
type: docs
weight: 90
url: /tr/python-net/modify-an-existing-style/
---

{{% alert color="primary" %}}

Aynı biçimlendirme seçeneklerini hücrelere uygulamak için yeni bir biçimlendirme stili nesnesi oluşturun. Bir biçimlendirme stili nesnesi, yazı tipi, yazı tipi boyutu, girinti, sayı, kenar, desen vb. gibi biçimlendirme özelliklerinin bir kombinasyonudur, adlandırılır ve bir küme olarak saklanır. Uygulandığında, bu stildeki tüm biçimlendirme uygulanır.

Ayrıca var olan bir stili kullanabilir, çalışma kitabı ile kaydedebilir ve aynı özelliklere sahip bilgileri biçimlendirmek için kullanabilirsiniz.

Hücreler açıkça biçimlendirilmediğinde, **Normal** stili (çalışma kitabının varsayılan stili) uygulanır. Microsoft Excel, Comma, Currency ve Percent dahil olmak üzere birkaç önceden tanımlanmış stile ek olarak Normal stili de tanımlar.

Aspose.Cells for Python via .NET, istediğiniz özellikler ile herhangi bir stil veya bu stilleri değiştirme imkanı sağlar.

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

## **Aspose.Cells for Python via .NET Kullanılarak**

Aşağıdaki örnekler, [**Style.update**](https://reference.aspose.com/cells/python-net/aspose.cells/style/update) yöntemini nasıl kullanacağınızı gösterir.

### **Stil Oluşturma ve Değiştirme**

Bu örnek, bir [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) nesnesi oluşturur, hücrelerin bir aralığına uygular ve [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) nesnesini değiştirir. Değişiklikler otomatik olarak hücreye ve uygulandığı aralığa uygulanır.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ModifyThroughStyleObject-1.py" >}}

### **Mevcut Bir Stili Değiştirmek**

Bu örnek, zaten bir diziye uygulanmış olan bir stil olan Yüzde'nin bulunduğu basit bir şablon Excel dosyasını kullanır. Örnek:

1. İlgili stili alır,
1. Stil nesnesi oluşturur ve
1. Stil biçimlendirmesini değiştirir.

Değişiklikler otomatik olarak uygulanan aralığa uygulanır.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ModifyThroughSampleExcelFile-1.py" >}}

