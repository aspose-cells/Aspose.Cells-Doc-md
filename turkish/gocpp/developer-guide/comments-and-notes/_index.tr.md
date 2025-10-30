---
title: Golang ile C++ kullanarak Yorumlar ve Notlar ile yönetin
linktitle: Yorumlar ve Notlar
type: docs
weight: 128
url: /tr/go-cpp/comments-and-notes/
description: Aspose.Cells for C++ ile yorum veya notlar ekleyip yönetme
keywords: yorum ekle, not ekle
---

## **Giriş**

Yorumlar, hücrelere ek bilgi eklemek için kullanılır. Aspose.Cells, hücrelere yorum eklemek için iki yöntem sağlar. İlk yöntem, tasarımcı dosyasında manuel olarak yorumlar oluşturmaktır. Bu yorumlar daha sonra Aspose.Cells kullanılarak içe aktarılır. İkinci yöntem, Aspose.Cells API'sını kullanarak çalışma zamanında yorum eklemektir. Bu konu, Aspose.Cells API'sını kullanarak hücrelere yorum eklemeyi tartışmaktadır. Yorumları biçimlendirmek de açıklanacaktır.

## **Yorum Ekleme**

Yorum koleksiyonunun Add metodu (encapsulated in the CommentAttribute object) çağrılarak bir hücreye yorum eklenir. Yeni CommentAttribute nesnesine, yorum dizinine geçilerek ulaşılabilir. CommentAttribute nesnesine erişildikten sonra, yorum notunu Customize edebilirsiniz.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CommentsAndNotes.go" >}}
## **Yorum Biçimlendirme**

Yorumların görünümünü yükseklik, genişlik ve yazı tipi ayarlarıyla biçimlendirmek de mümkündür.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CommentsAndNotes-1.go" >}}
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

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CommentsAndNotes-2.go" >}}
## **Gelişmiş Konular**
- [Yorumun Yazı Yönünü Değiştirme](/cells/tr/cpp/change-text-direction-of-the-comment/)
- [Yorum Yazı Tipi Rengini Nasıl Değiştirilir](/cells/tr/cpp/how-to-change-the-comment-font-color/)
- [Yorum arka planını nasıl ayarlarım](/cells/tr/cpp/how-to-set-comment-background/)
- [İz bırakan Yorumlar](/cells/tr/cpp/threaded-comments/)
