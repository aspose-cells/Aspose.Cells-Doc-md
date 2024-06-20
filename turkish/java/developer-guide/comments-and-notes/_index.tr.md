---
title: Yorumları ve Notları Yönetme
linktitle: Yorumlar ve Notlar
type: docs
weight: 128
url: /tr/java/comments-and-notes/
description: Aspose.Cells for Java ile yorumları veya notları ekleyin ve yönetin.
keywords: yorum ekle, not ekle
---

## **Giriş**

Yorumlar, hücrelere ek bilgi eklemek için kullanılır. Aspose.Cells, hücrelere yorum eklemek için iki yöntem sağlar. İlk yöntem, tasarımcı dosyasında manuel olarak yorumlar oluşturmaktır. Bu yorumlar daha sonra Aspose.Cells kullanılarak içe aktarılır. İkinci yöntem, Aspose.Cells API'sını kullanarak çalışma zamanında yorum eklemektir. Bu konu, Aspose.Cells API'sını kullanarak hücrelere yorum eklemeyi tartışmaktadır. Yorumları biçimlendirmek de açıklanacaktır.

## **Yorum Ekleme**

Yeni bir yorum notunu [**Comments**](https://reference.aspose.com/cells/java/com.aspose.cells/CommentCollection) koleksiyonundan alarak [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) nesnesine kapsüllenen [**Comments**](https://reference.aspose.com/cells/java/com.aspose.cells/CommentCollection) koleksiyonunun **Ekle** yöntemini çağırarak bir hücreye yorum ekleyin. Yeni [**Comment**](https://reference.aspose.com/cells/java/com.aspose.cells/Comment) nesnesi, yorum endeksini geçirerek [**Comments**](https://reference.aspose.com/cells/java/com.aspose.cells/CommentCollection) koleksiyonundan erişilebilir. [**Comment**](https://reference.aspose.com/cells/java/com.aspose.cells/Comment) nesnesine erişme sonrasında, [**Comment**](https://reference.aspose.com/cells/java/com.aspose.cells/Comment) nesnesinin [**Note**](https://reference.aspose.com/cells/java/com.aspose.cells/comment#Note) özelliğini kullanarak yorum notunu özelleştirin.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "AddingComment-1.java" >}}

## **Yorum Biçimlendirme**

Yorumların görünümünü yükseklik, genişlik ve yazı tipi ayarlarıyla biçimlendirmek de mümkündür.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "CommentFormatting-1.java" >}}

## **Yoruma Resim Ekle**

Microsoft Excel 2007 ile, bir hücre yorumuna arka plan olarak bir resim eklemek de mümkündür. Excel 2007'de bunu aşağıdaki adımları takip ederek başarabilirsiniz. (Zaten bir hücre yorumu eklediğinizi varsayarlar.)

1. Yorum içeren hücreye sağ tıklayın.
1. **Yorumları Göster/Gizle**'yi seçin ve yorumdan herhangi bir metni temizleyin.
1. Yorumun kenarına tıklayın.
1. **Biçim**, ardından **Yorum**'u seçin.
1. **Renk ve Çizgiler** sekmesinde, **Renk** listesini genişletin.
1. **Dolgu Efektleri**'ni tıklayın.
1. **Resim** sekmesinde, **Resim Seç**'i tıklayın.
1. Resmi bulun ve seçin.
1. Tüm iletiler kapatılıncaya kadar **Tamam**'ı tıklayın.

Aspose.Cells ayrıca bu özelliği sağlar. Aşağıda, sıfırdan XLSX dosyası oluşturan ve "A1" hücresine resimli bir arka plan ekleyen bir kod örneği bulunmaktadır.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "AddImageToComment-1.java" >}}

## **Gelişmiş Konular**
- [Yorumun Yazı Yönünü Değiştirme](/cells/tr/java/change-text-direction-of-the-comment/)
- [Yorum Yazı Tipi Rengini Nasıl Değiştirilir](/cells/tr/java/how-to-change-the-comment-font-color/)
- [Yorum arka planını nasıl ayarlarım](/cells/tr/java/how-to-set-comment-background/)
- [İz bırakan Yorumlar](/cells/tr/java/threaded-comments/)

