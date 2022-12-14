---
title: Aspose.Cells Nesne Modeli
type: docs
weight: 20
url: /tr/net/aspose-cells-object-model/
---
{{% alert color="primary" %}} 

 Aspose.Cells Nesne Modeli, Aspose.Cells sınıf kitaplığının nesneleri arasındaki yapısal ilişkiler hakkında bilgi sağlar.

{{% /alert %}} 

Aspose.Cells nesne modelinin üst düzey yapısı aşağıda hiyerarşik olarak gösterilmiştir.

|**Aspose.Cells Nesne Modeli'nin üst düzey yapısı**|
|:- |
|![yapılacaklar:resim_alternatif_Metin](aspose-cells-object-model_1.png)|
Yukarıdaki şekilden de görebileceğiniz gibi, nesne modelinin kökü Workbook nesnesidir. Giriş amacıyla aşağıda nesnelerin birkaçının kısa bir açıklaması verilmiştir.
## **Çalışma SayfasıToplama/Çalışma Sayfası**
Workbook nesnesi, aşağıda gösterildiği gibi bir elektronik tablodaki tüm Worksheet nesnelerinin koleksiyonunu temsil eden WorksheetCollection'ı içerir:

|**Çalışma Sayfaları ve Çalışma Sayfası nesneleri**|
|:- |
|![yapılacaklar:resim_alternatif_Metin](aspose-cells-object-model_2.png)|
## **Cells/Cell**
Her Çalışma Sayfası nesnesi, aşağıda gösterildiği gibi bir çalışma sayfasındaki tüm Cell nesnelerinin koleksiyonunu temsil eden bir Cells nesnesi içerir:

|**Cells & Cell nesneleri**|
|:- |
|![yapılacaklar:resim_alternatif_Metin](aspose-cells-object-model_3.png)|
Tek bir hücrenin değerini, stilini, formülünü ve diğer özelliklerini almak ve ayarlamak için Cell nesnesini kullanabilirsiniz.
## **GrafikKoleksiyon/Grafik**
Charts nesnesi, bir Çalışma Sayfasındaki tüm Chart nesnelerinin bir koleksiyonunu temsil eder. Her Chart nesnesi, grafikler oluşturmak ve yönetmek için birlikte çalışan birkaç başka nesneden oluşur. Aspose.Cells'deki Grafik yapısı aşağıdaki şemada gösterilmiştir:

|**Grafiğin nesne modeli**|
|:- |
|![yapılacaklar:resim_alternatif_Metin](aspose-cells-object-model_4.png)|
## **YorumToplama/Yorum**
Her Çalışma Sayfası nesnesi, aşağıda gösterildiği gibi bir çalışma sayfasındaki tüm Yorum nesnelerinin koleksiyonunu temsil eden bir Yorumlar nesnesi de içerir:

|**Yorumlar ve Yorum nesneleri**|
|:- |
|![yapılacaklar:resim_alternatif_Metin](aspose-cells-object-model_5.png)|
Açıklama nesnesi, çalışma sayfasında belirtilen herhangi bir hücreye yorum eklemek için kullanılır.
## **HorizontalPageBreakCollection/HorizontalPageBreak**
Her Worksheet nesnesi, aşağıda gösterildiği gibi bir çalışma sayfasındaki tüm HorizontalPageBreak nesnelerinin bir koleksiyonunu temsil eden bir HorizontalPageBreakCollection içerir:

|**HPageBreaks ve HPageBreak nesneleri**|
|:- |
|![yapılacaklar:resim_alternatif_Metin](aspose-cells-object-model_6.png)|
Çalışma sayfasında yatay bir sayfa sonu oluşturmak için bir HorizontalPageBreak nesnesi kullanılır.
## **Köprü Koleksiyonu/Köprü**
Bir Worksheet nesnesi ayrıca, aşağıda gösterildiği gibi çalışma sayfasındaki tüm Hyperlink nesnelerinin bir koleksiyonunu temsil eden bir HyperlinkCollection içerir:

|**Köprüler ve Köprü nesneleri**|
|:- |
|![yapılacaklar:resim_alternatif_Metin](aspose-cells-object-model_7.png)|
Bir Köprü nesnesi, çalışma sayfasındaki bir köprüyü temsil eder. Geliştiriciler, Köprü nesnesini kullanarak köprü adresini ve diğer ilgili özellikleri ayarlayabilir.
## **ResimKoleksiyon/Resim**
Her Worksheet nesnesi, aşağıda gösterildiği gibi bir çalışma sayfasındaki tüm Picture nesnelerinin bir koleksiyonunu temsil eden bir PictureCollection nesnesi içerir:

|**Resimler ve Resim nesneleri**|
|:- |
|![yapılacaklar:resim_alternatif_Metin](aspose-cells-object-model_8.png)|
Resim nesnesi, çalışma sayfasındaki bir resmi temsil eder. Geliştiriciler, Resim nesnesini kullanarak çalışma sayfalarına sadece resim eklemekle kalmaz, aynı zamanda bu resimleri herhangi bir yere konumlandırırlar. Resimlerin kenarlıklarını veya diğer özelliklerini ayarlamak da mümkündür.
## **VerticalPageBreakCollection/DikeyPageBreak**
Her Worksheet nesnesi, aşağıda gösterildiği gibi bir çalışma sayfasındaki tüm VerticalPageBreak nesnelerinin bir koleksiyonunu temsil eden bir VerticalPageBreakCollection nesnesi içerir:

|**VPageBreaks & VPageBreak nesneleri**|
|:- |
|![yapılacaklar:resim_alternatif_Metin](aspose-cells-object-model_9.png)|
Çalışma sayfasında dikey bir sayfa sonu oluşturmak için VerticalPageBreak nesnesi kullanılır.
