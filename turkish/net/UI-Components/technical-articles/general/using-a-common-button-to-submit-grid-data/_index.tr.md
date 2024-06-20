---
title: Grid Verisini Göndermek İçin Ortak Bir Düğmeyi Kullanma
type: docs
weight: 20
url: /tr/net/aspose-cells-gridweb/using-a-common-button-to-submit-grid-data/
keywords: GridWeb, gönder, düğme, özel
description: Bu makale, GridWeb de gönder düğmesinin kullanımını açıklar.
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb, **Gönder** ve **Kaydet** gibi bazı yerleşik komut düğmelerini sağlar. İlgili görevleri gerçekleştirmek için bu düğmeleri kullanın.

Bu makale, yalnızca GridWeb'in yerleşik **Kaydet** komut düğmesini tıklamakla değil, aynı zamanda ortak bir ASP.NET Düğmesi (Web Kontrolü) tıklanarak sunucuya veri gönderme yöntemini gösterir. Bu makalenin amacı Aspose.Cells.GridWeb'in esnekliğini göstermektir. Ayrıca, bu makale aynı zamanda istemci tarafında kullanılacak Aspose.Cells.GridWeb tarafından sunulan özel işlevleri de kullanır.

{{% /alert %}} 
## **ASP.NET Düğmesi Kullanarak Grid Verisini Gönderme**
Aspose.Cells.GridWeb, üç yerleşik düğme (**Gönder**, **Kaydet** ve **Geri Al**) sağlar. GridWeb'de düzenleme yaptıktan sonra, bir kullanıcı, verileri sunucuya göndermek için sekme çubuğundaki **Gönder** veya **Kaydet** düğmesini tıklayabilir. Kullanıcı bir Sayfa Sekmesine tıklarsa, GridWeb kontrolü, yerleşik komut düğmelerinin göreviyle aynı görevi gerçekleştirir. Aspose.Cells.GridWeb ayrıca bu işlevselliğin ortak bir ASP.NET Düğme denetimine de eklenmesini destekler, ancak uygulamaya ekstra kod eklemeniz gerekir.
### **1. Bir Test Uygulaması Oluşturma**
Visual Studio.NET IDE'nizi açın ve yeni bir ASP.NET Web Uygulaması projesi oluşturun. Uygulama oluşturulduktan sonra, projenize varsayılan WebForm1.aspx sayfası eklenir. Web Form'unuzda Toolbox'tan GridWeb kontrolünü sürükleyip bırakın. GridWeb kontrolünü Toolbox'ta bulamıyorsanız daha fazla bilgi için şu sayfaya bakın: [Visual Studio.NET ile Aspose.Cells Grid Kontrollerini Entegre Etme](/cells/tr/net/integrate-aspose-cells-grid-controls-with-visual-studio-net/). GridWeb kontrolü Web Form'unuza eklendikten sonra, Toolbox'tan bir Düğme web kontrolünü de Web Form'unuza ekleyin.
### **2. Page_Load Olayına Kod Eklemek**
Şimdi, Web Form'unun tasarım görünümünde Web Form'a çift tıklayarak Page_Load olayına kod eklemek zamanı geldi ve VS.NET IDE otomatik olarak sizi Page_Load olay işleyicisine götürecektir. Burada, Düğme'nin Özellikler koleksiyonunu, OnClick olayını geçersiz kılmak için kullanmanız gerekir.

{{% alert color="primary" %}} 

ASP.NET Düğme denetimi bir sunucu taraflı denetimdir. Tıklanıldığında, sunucu taraflı bir olay tetiklenir, ancak eğer bu Düğme denetimini istemci taraflıda (genellikle javascript kullanarak) bazı kodları çalıştırmak için kullanmak istiyorsanız, tıklanma özniteliğini Page_Load olayı altında değiştirmeniz gerekir. Aspose.Cells.GridWeb, istemci tarafında GridWeb kontrolü ile ilgilenmek için javascript'te çağırılabilen bazı işlevler sağlar. Aşağıdaki örnekte, GridWeb'in istemci tarafında kullanılan güncellemeData ve tüm verileri doğrulama gibi işlevleri kullanmış bulunmaktayız.

{{% /alert %}} 
#### **Kod Örneği**


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-UsingCommonSubmitButton.aspx-UsingCommonSubmitButton.cs" >}}
### **3. Uygulamayı Çalıştırma**
Şimdi, uygulamanızı derlemek ve çalıştırmak için Ctrl+F5 tuşuna basarak yeni bir tarayıcı penceresinde sayfa açılacaktır. GridWeb'e bazı değerler ekleyelim ve Sunucuya Rozet Veri Gönder düğmesine basın ve GridWeb verilerini güncellemek ve doğrulamak için postback'i göreceksiniz.
## **Sonuç**
{{% alert color="primary" %}} 

Aspose.Cells.GridWeb, sunucu veya istemci tarafından GridWeb kontrolleriyle çalışma konusunda büyük esneklik sunar. Geliştiriciler, müşterilerine daha iyi çözümler sunmak için farklı senaryolarda GridWeb kontrolünü kullanma seçeneklerine sahiptir.

{{% /alert %}}
