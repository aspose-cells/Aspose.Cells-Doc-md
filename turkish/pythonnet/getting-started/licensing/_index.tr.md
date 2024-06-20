---
title: Lisanslama
type: docs
weight: 21
url: /tr/python-net/licensing/
---

{{% alert color="primary" %}}

Aspose.Cells Python'u değerlendirme sürümünü Pypi repos'indeki [indirme sayfasından](https://pypi.org/project/aspose-cells-python/) kolayca indirebilirsiniz. Değerlendirme sürümü, bileşenin lisanslı sürümüyle kesinlikle aynı yetenekleri sunar. Ayrıca, değerlendirme sürümü, lisans satın aldığınızda ve lisansı uygulamak için birkaç satır kod eklediğinizde lisanslanmış duruma gelir.

{{% /alert %}}

## **Değerlendirme Sürümü Kısıtlamaları**

Aspose.Cells Python via .Net'in değerlendirme sürümü (belirtilmiş bir lisans olmadan) tam ürün işlevselliği sağlar, ancak bir programda 100 dosya ve bir ek çalışma sayfası ile sınırlandırılmıştır.

Sınırlamalar aşağıda gösterilmiştir:

- **Açılan Dosya Sayısı** (Aspose.Cells Python via .Net)
  Programınızı çalıştırırken, Aspose.Cells Python via .Net kütüphanesini kullanarak sadece 100 Excel dosyası açabilirsiniz. Uygulamanız bu sayıyı aşarsa bir istisna fırlatılacaktır.


Ayrıca, Aspose.Cells Python via kütüphanesini kullanarak oluşturulan Excel dosyasında bir değerlendirme filigranı her zaman etkin çalışma sayfası olarak görüntülenir. Yalnızca lisanslı sürümde etkin çalışma sayfasını diğer çalışma sayfalarına ayarlayabilirsiniz. Aspose.Cells Python via tarafından oluşturulan PDF veya görüntü dosyasında, bir değerlendirme filigranı belgenin/görüntünün üst kısmına yapıştırılır.

{{% alert color="primary" %}}

Aspose.Cells Python via'nın değerlendirme sürümü sınırlamalar olmadan test etmek isterseniz, ayrıca [30 Günlük Geçici Lisans](https://purchase.aspose.com/temporary-license) talep edebilirsiniz.

{{% /alert %}}

## **Aspose.Cells Python via Bileşeninde Lisans Uygulama**

Lisans, ürün adı, lisanslanan geliştiricilerin sayısı, abonelik sona erme tarihi vb. gibi ayrıntıları içeren düz metinli bir XML dosyasıdır. Dosya dijital imzalıdır, bu yüzden dosyayı değiştirmeyin. Dosyaya yanlışlıkla bir ekstra satır aralığı eklemek bile dosyayı geçersiz kılacaktır. Aspose.Cells Python via'yi kullanmadan önce bir lisans ayarlamanız gerekmektedir. Uygulama başına (veya işlem) sadece bir kez lisans ayarlamanız gerekmektedir. Lisans, bir dosyadan yüklenebilir.

Aspose.Cells Python via dosya yolunda lisansı bulmaya çalışır.

Dosyadan lisans uygulamanın iki yaygın yöntemi bulunmaktadır.

### **Diskten Lisans Uygulama**

Bir lisansı ayarlamanın en kolay yolu, lisans dosyasını açık yola koymaktır.

{{< highlight csharp >}}

# Instantiate an instance of license and set the license file through its path

license = License();
# For Windows
license.set_license("D:\Aspose.Cells.lic");
# For Linux or MacOS
license.set_license("/home/yourusername/Aspose.Cells.lic"); 
{{< /highlight >}}

{{% alert color="primary" %}}

set_license yöntemini çağırdığınızda, lisans adı lisans dosya adınızla aynı olmalıdır. Örneğin, lisans dosya adını **Aspose.Cells.lic.xml** olarak değiştirebilirsiniz. Ardından kodunuzda, değiştirilmiş lisans adını (**Aspose.Cells.lic.xml**) set_license yöntemi için kullanmalısınız.

{{% /alert %}}


