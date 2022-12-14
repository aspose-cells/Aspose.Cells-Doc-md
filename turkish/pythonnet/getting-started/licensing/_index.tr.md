---
title: lisanslama
type: docs
weight: 21
url: /tr/python-net/licensing/
---
{{% alert color="primary" %}}

 Aspose.Cells Python değerlendirme sürümünü .Net üzerinden kolayca indirebilirsiniz.[indirme sayfası](https://pypi.org/project/aspose-cells-python/) @ Pypi depoları. Değerlendirme sürümü, bileşenin lisanslı sürümüyle kesinlikle aynı yetenekleri sağlar. Ayrıca, bir lisans satın aldığınızda ve lisansı uygulamak için birkaç satır kod eklediğinizde, değerlendirme sürümü kolayca lisanslanır.

{{% /alert %}}

## **Değerlendirme Sürümü Sınırlamaları**

.Net ürünü aracılığıyla Aspose.Cells Python değerlendirme sürümü (lisans belirtilmeden) tam ürün işlevselliği sağlar, ancak bir programda 100 dosya ve değerlendirme filigranlı fazladan bir çalışma sayfası açmakla sınırlıdır.

Sınırlamalar aşağıda gösterilmiştir:

- **Açılan Dosya Sayısı** (Aspose.Cells Python .Net üzerinden)
Programınızı çalıştırırken .Net kütüphanesi üzerinden Aspose.Cells Python kullanarak sadece 100 Excel dosyasını açabilirsiniz. Uygulamanız bu sayıyı aşarsa bir istisna atılır.


Ayrıca kütüphane aracılığıyla Aspose.Cells Python kullanılarak oluşturulan excel dosyasında değerlendirme filigranlı bir çalışma sayfası her zaman aktif çalışma sayfası olarak görünecektir. Yalnızca lisanslı sürümde, aktif çalışma sayfasını diğer çalışma sayfalarına ayarlayabilirsiniz. Aspose.Cells Python üzerinden alınan PDF veya resim dosyası çıktısında, belgenin/resmin üst kısmına bir değerlendirme filigranı yapıştırılır.

{{% alert color="primary" %}}

 Aspose.Cells Python üzerinden değerlendirmesiz versiyon sınırlaması ile test etmek isterseniz ayrıca talepte bulunabilirsiniz.[30 Günlük Geçici Lisans](https://purchase.aspose.com/temporary-license).

{{% /alert %}}

## **Bileşen aracılığıyla Aspose.Cells Python'de bir Lisansın Uygulanması**

Lisans, ürün adı, lisanslandığı geliştirici sayısı, abonelik bitiş tarihi gibi ayrıntıları içeren düz metin bir XML dosyasıdır. Dosya dijital olarak imzalanmıştır, bu nedenle dosyayı değiştirmeyin. Dosyaya yanlışlıkla fazladan bir satır eklenmesi bile onu geçersiz kılacaktır. Değerlendirme sınırlamasını önlemek istiyorsanız, Aspose.Cells Python'i kullanmadan önce bir lisans ayarlamanız gerekir. Uygulama (veya süreç) başına yalnızca bir kez lisans ayarlamak gerekir. Lisans bir dosyadan yüklenebilir.

Aspose.Cells Python aracılığıyla, açık yol konumlarında lisansı bulmaya çalışır.

Dosyadan lisans uygulamak için iki yaygın yöntem vardır.

### **Diskten Lisans Uygulama**

Lisans belirlemenin en kolay yolu, lisans dosyasını açık yola koymaktır.

{{< highlight "csharp" >}}

 //Instantiate an instance of license and set the license file through its path

license = License();
 //For Windows
license.set_license("D:\Aspose.Cells.lic");
 //For Linux or MacOS
license.set_license("/home/yourusername/Aspose.Cells.lic"); 
{{< /highlight >}}

{{% alert color="primary" %}}

seti aradığınızda_lisans yöntemi, lisans adı, lisans dosyanızın adı ile aynı olmalıdır. Örneğin, lisans dosyası adını **Aspose.Cells.lic.xml** olarak değiştirebilirsiniz. Ardından, kodunuzda, set için değiştirilmiş lisans adını (**Aspose.Cells.lic.xml**) kullanmalısınız._lisans yöntemi.

{{% /alert %}}


