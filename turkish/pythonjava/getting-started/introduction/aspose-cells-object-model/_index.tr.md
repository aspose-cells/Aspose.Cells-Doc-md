---
title: Aspose.Cells Nesne Modeli
type: docs
weight: 20
url: /tr/python-java/aspose-cells-object-model/
---

{{% alert color="primary" %}}

Aspose.Cells Nesne Modeli, Aspose.Cells sınıf kitaplığındaki nesneler arasındaki yapısal ilişkiler hakkında bilgi sağlar.

{{% /alert %}}

Aspose.Cells nesne modelinin en üst düzey yapısı aşağıdaki şekilde hiyerarşik bir şekilde gösterilmiştir.

|**Aspose.Cells Nesne Modeli Üst Düzey Yapısı**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_1.png)|
Yukarıdaki şekilden görebileceğiniz gibi, nesne modelinin kökü Workbook nesnesidir. Giriş amaçlı aşağıda belirli nesnelerin kısa bir açıklaması verilmiştir.

## **WorksheetCollection/Worksheet**

Workbook nesnesi, bir elektronik tablodaki tüm Worksheet nesnelerinin koleksiyonunu temsil eden WorksheetCollection'ı içerir.

|**Çalışsayfaları ve Çalışsayı nesneleri**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_2.png)|

## **Cells/Cell**

Her Worksheet nesnesi, bir çalışma sayfasındaki tüm Hücre nesnelerinin koleksiyonunu temsil eden bir Cells nesnesini içerir.

|**Hücreler & Hücre nesneleri**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_3.png)|
Hücre nesnesini kullanarak, tek bir hücrenin değerini, stili, formülü ve diğer özelliklerini almak ve ayarlamak mümkündür.

## **ChartCollection/Chart**

Charts nesnesi, bir Çalışsayfada bulunan tüm Grafik nesnelerinin bir koleksiyonunu temsil eder. Her Grafik nesnesi, grafik oluşturmak ve yönetmek için birlikte çalışan birkaç başka nesneden oluşur. Aspose.Cells'te Grafik yapısı aşağıdaki diyagramda gösterilmektedir:

|**Grafik Nesne Modeli**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_4.png)|

## **CommentCollection/Comment**

Her Worksheet nesnesi ayrıca, bir çalışma sayfasındaki tüm Yorum nesnelerinin bir koleksiyonunu temsil eden bir Yorumlar nesnesini içerir.

|**Yorumlar & Yorum nesneleri**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_5.png)|
Yorum nesnesi, çalışma sayfasındaki belirtilen herhangi bir hücreye yorum eklemek için kullanılır.

## **HorizontalPageBreakCollection/HorizontalPageBreak**

Her Worksheet nesnesi ayrıca, çalışma sayfasındaki tüm YataySayfaKırıkları nesnelerinin bir koleksiyonunu temsil eden bir HorizontalPageBreakCollection'ı içerir.

|**YataySayfaKırıkları & YataySayfaKırığı nesneleri**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_6.png)|
Bir YataySayfaKırığı nesnesi, çalışma sayfasında yatay bir sayfa kırığı oluşturmak için kullanılır.

## **HyperlinkCollection/Hyperlink**

Bir Çalışma Sayfası nesnesi ayrıca, çalışma sayfasındaki tüm Hyperlink nesnelerinin bir koleksiyonunu temsil eden bir HyperlinkCollection'ı içerir.

|**Bağlantılar & Bağlantı nesneleri**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_7.png)|
Bir Hyperlink objesi elektronik tabloda bir bağlantıyı temsil eder. Geliştiriciler, Hyperlink objesini kullanarak bağlantı adresini ve diğer ilgili özellikleri ayarlayabilirler.

## **PictureCollection/Picture**

Her Worksheet objesi, elektronik tablodaki tüm Resim objelerini temsil eden bir ResimKoleksiyonu nesnesi içerir, aşağıda gösterildiği gibi:

|**Resimler ve Resim objeleri**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_8.png)|
Bir Resim objesi elektronik tabloda bir resmi temsil eder. Resim objesi kullanılarak, geliştiriciler sadece resimleri elektronik tablolara ekleyemezler, aynı zamanda bu resimleri herhangi bir konuma yerleştirebilirler. Resimlerin sınırlarını veya diğer özelliklerini ayarlamak da mümkündür.

## **VerticalPageBreakCollection/VerticalPageBreak**

Her Worksheet objesi, elektronik tablodaki tüm DikeySayfaKırıkKoleksiyonunu temsil eden bir DikeySayfaKırıkKoleksiyonu nesnesi içerir, aşağıda gösterildiği gibi:

|**VPageBreaks ve VPageBreak objeleri**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_9.png)|
Bir DikeySayfaKırık objesi, elektronik tabloda dikey bir sayfa kırığı oluşturmak için kullanılır.
