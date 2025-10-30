---
title: Golang ile C++ üzerinden Hücreye Resim Nasıl Eklenir
linktitle: Hücreye Resim Ekleme Nasıl Yapılır
type: docs
weight: 130
url: /tr/go-cpp/how-to-insert-picture-in-cell/
description: Aspose.Cells kullanarak C++ ile hücreye nasıl resim ekleneceğini öğrenin.
keywords: Hücreye Resim Eklemeyi, Hücreler Üzerine Resim Eklemeyi, Hücreye Resim Koymayı, Hücreler Üzerine Resim Koymayı, Resmi Hücreye Koymayı, Resmi Hücreler Üzerine Koymayı, Hücrede Resim Nasıl Yerleştirilir, Hücreler Üzerine Resim Nasıl Yerleştirilir, Resim Yerleştirmenin Arasında Geçiş Yapmayı, Hücre İçinde Yerleştirme ve Hücreler Üzerine Resim Arasında Geçiş Yapmayı
---

## **Olası Kullanım Senaryoları**
Resim, çalışma sayfanıza parlaklık katar ve içeriğin görsel bir temsilini sağlar. Ayrıca veriyi anlamanızı kolaylaştırır ve içgörüler elde etmenize yardımcı olur. Excel'de yıllardır resimleri kullanabiliyor olsanız da, Excel yakın zamanda resimlerin gerçek hücre değerleri olmasını sağlayan özelliği etkinleştirdi. Çizimin düzeni değiştirildiğinde bile, yine de veriye bağlı kalır. Bunu tablolarınızda kullanabilir, sıralayabilir, filtreleyebilir, formüllerde dahil edebilir ve daha fazlasını yapabilirsiniz!

## **Excel Kullanarak Hücreye Resim Ekleme**
Excel'de bir hücreye resim eklemek için şu adımları izleyin:

1. Ekle sekmesine gidin ve Resimler seçeneğine tıklayın.
2. **Hücreye Yerleştir**'i seçin. **Resim Ekleme Yerinden** açılır menüsünden aşağıdaki kaynaklardan birini seçin (**Bu Cihaz**, **Stok Resimler** ve **Çevrimiçi Resimler**). Bu Cihaz, cihazınızdan resim eklemek için. Stok Resimler, stok resimlerden resim eklemek için. Çevrimiçi Resimler, webden resim eklemek için.
<br>
<img src="1.png" width=60% />
3. Resmi seçin ve bir hücreye resim ekleyin.
<br>
<img src="8.png" width=60% />

## **Excel Kullanarak Hücrelerin Üzerine Resim Ekleme**
Excel'de hücrelerin üzerine resim eklemek için şu adımları izleyin:

1. Ekle sekmesine gidin ve Resimler seçeneğine tıklayın.
2. **Hücrelerin Üzerine Yerleştir**'i seçin. **Resim Ekleme Yerinden** açılır menüsünden aşağıdaki kaynaklardan birini seçin (**Bu Cihaz**, **Stok Resimler** ve **Çevrimiçi Resimler**). Bu Cihaz, cihazınızdan resim eklemek için. Stok Resimler, stok resimlerden resim eklemek için. Çevrimiçi Resimler, webden resim eklemek için.
<br>
<img src="2.png" width=60% />
3. Resmi seçin ve hücrelerin üzerine resim ekleyin.
<br>
<img src="3.png" width=60% />

## **Hücredeki Resimden Hücrelerin Üzerindeki Resimlere Nasıl Geçilir**
Kolayca **Hücredeki Resimden Hücrelerin Üzerindeki Resimlere** geçebilirsiniz. Lütfen şu adımları izleyin:
1. Hücreye sağ tıklayın ve **Hücredeki Resim** > **Hücrelerin Üzerine Yerleştir** seçeneğini seçin. 
<br>
<img src="4.png" width=60% />
2. Değiştirdikten sonra sonuç aşağıdaki gibidir:
<br>
<img src="5.png" width=60% />

## **Hücrelerin Üzerindeki Resimden Hücredeki Resime Nasıl Geçilir**
Kolayca **Hücrelerin Üzerindeki Resimden Hücredeki Resime** geçebilirsiniz. Lütfen şu adımları izleyin:
1. Resme sağ tıklayın ve **Hücre içine Yerleştir** seçeneğini seçin. 
<br>
<img src="6.png" width=60% />
2. Değiştirdikten sonra sonuç aşağıdaki gibidir:
<br>
<img src="7.png" width=60% />

## **C++ Kullanarak Hücreye Resim Nasıl Eklenir**
Aspose.Cells kullanarak hücreye resim ekleme. Lütfen aşağıdaki örnek kodu görün. Örnek kodu yürüttükten sonra, bir resim hücreye eklenecektir.
1. Bir Çalışma Kitabı nesnesi oluşturun. 
2. Resmi yerleştirmek istediğiniz hücreyi alın.
3. Cell.EmbeddedImage özelliğini ayarlayın. 
4. Son olarak, çalışma kitabını [çıktı XLSX](out.xlsx) formatında kaydeder. 

## **Örnek Kod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-HowToPlaceImageToCell.go" >}}
