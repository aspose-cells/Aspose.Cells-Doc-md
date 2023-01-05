---
title: Yorumları ve Notları Yönetin
linktitle: Yorumlar ve Notlar
type: docs
weight: 128
url: /tr/java/comments-and-notes/
description: Java için Aspose.Cells ile yorumları veya notları ekleyin ve yönetin.
keywords: insert comments, insert notes
---
## **Giriş**

Yorumlar, hücrelere ek bilgi eklemek için kullanılır. Aspose.Cells, hücrelere yorum eklemek için iki yöntem sağlar. İlki, bir tasarımcı dosyasında manuel olarak yorumlar oluşturmaktır. Bu yorumlar daha sonra Aspose.Cells kullanılarak içe aktarılır. İkincisi, çalışma zamanında Aspose.Cells API kullanılarak yorum eklemektir. Bu konuda, Aspose.Cells API kullanılarak hücrelere yorum eklenmesi ele alınmaktadır. Yorumların biçimlendirilmesi de açıklanacaktır.

## **Yorum Ekleme**

 öğesini çağırarak bir hücreye yorum ekleyin.[**Yorumlar**](https://reference.aspose.com/cells/java/com.aspose.cells/CommentCollection) koleksiyonun**Eklemek** yöntem (kapsüllenmiş[**Çalışma kağıdı**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) nesne). Yeni[**Yorum Yap**](https://reference.aspose.com/cells/java/com.aspose.cells/Comment) nesneden erişilebilir.[**Yorumlar**](https://reference.aspose.com/cells/java/com.aspose.cells/CommentCollection) yorum dizinini geçirerek koleksiyon. eriştikten sonra[**Yorum Yap**](https://reference.aspose.com/cells/java/com.aspose.cells/Comment) kullanarak yorum notunu özelleştirin.[**Yorum Yap**](https://reference.aspose.com/cells/java/com.aspose.cells/Comment) nesnenin[**Not**](https://reference.aspose.com/cells/java/com.aspose.cells/comment#Note)Emlak.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "AddingComment-1.java" >}}

## **Yorum Biçimlendirme**

Yükseklik, genişlik ve yazı tipi ayarlarını yapılandırarak yorumların görünümünü biçimlendirmek de mümkündür.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "CommentFormatting-1.java" >}}

## **Yoruma Resim Ekleyin**

Microsoft Excel 2007 ile, bir hücre yorumunun arka planı olarak bir görüntüye sahip olmak da mümkündür. Excel 2007'de bu, aşağıdaki adımlar izlenerek gerçekleştirilir. (Zaten bir hücre yorumu eklediğinizi varsayarlar.)

1. Açıklamayı içeren hücreye sağ tıklayın.
1.  Seçme**Yorumları Göster/Gizle**, ve yorumdaki tüm metni temizleyin.
1. Seçmek için yorumun kenarlığına tıklayın.
1.  Seçme**Biçim** , o zamanlar**Yorum Yap**.
1.  Üzerinde**Renkler ve Çizgiler** sekmesini genişletin**Renk** liste.
1.  Tıklamak**Dolgu Efektleri**.
1.  Üzerinde**Resim** sekme, tıklayın**Resim Seç**.
1. Resmi bulun ve seçin.
1.  Tıklamak**Tamam** tüm diyaloglar kapanana kadar.

Aspose.Cells de bu özelliği sağlıyor. Aşağıda, sıfırdan bir XLSX dosyası oluşturan ve "A1" hücresine arka planı resim olarak ayarlanmış bir yorum ekleyen bir kod örneği verilmiştir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "AddImageToComment-1.java" >}}

## **ileri konular**
- [Yorumun Metin Yönünü Değiştirme](/cells/tr/java/change-text-direction-of-the-comment/)
- [Yorum Yazı Tipi Rengi nasıl değiştirilir?](/cells/tr/java/how-to-change-the-comment-font-color/)
- [Yorum arka planı nasıl ayarlanır?](/cells/tr/java/how-to-set-comment-background/)
- [Zincirleme Yorumlar](/cells/tr/java/threaded-comments/)

