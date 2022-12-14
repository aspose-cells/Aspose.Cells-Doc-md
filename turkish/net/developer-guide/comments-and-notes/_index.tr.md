---
title: Yorumları ve Notları Yönetin
linktitle: Yorumlar ve Notlar
type: docs
weight: 128
url: /tr/net/comments-and-notes/
description: .Net için Aspose.Cells ile yorumları veya notları ekleyin ve yönetin.
keywords: insert comments, insert notes
---
## **giriiş**

Yorumlar, hücrelere ek bilgi eklemek için kullanılır. Aspose.Cells, hücrelere yorum eklemek için iki yöntem sağlar. İlki, bir tasarımcı dosyasında manuel olarak yorumlar oluşturmaktır. Bu yorumlar daha sonra Aspose.Cells kullanılarak içe aktarılır. İkincisi, çalışma zamanında Aspose.Cells API kullanılarak yorum eklemektir. Bu konuda, Aspose.Cells API kullanılarak hücrelere yorum eklenmesi ele alınmaktadır. Yorumların biçimlendirilmesi de açıklanacaktır.

## **Yorum Ekleme**

 öğesini çağırarak bir hücreye yorum ekleyin.[**Yorumlar**](https://reference.aspose.com/cells/net/aspose.cells/commentcollection) koleksiyonun[**Ekle**](https://reference.aspose.com/cells/net/aspose.cells/commentcollection/methods/add/index) yöntem (kapsüllenmiş[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) nesne). Yeni[**Yorum**](https://reference.aspose.com/cells/net/aspose.cells/comment) nesneden erişilebilir.[**Yorumlar**](https://reference.aspose.com/cells/net/aspose.cells/commentcollection) yorum dizinini geçirerek koleksiyon. eriştikten sonra[**Yorum**](https://reference.aspose.com/cells/net/aspose.cells/comment) kullanarak yorum notunu özelleştirin.[**Yorum**](https://reference.aspose.com/cells/net/aspose.cells/comment) nesnenin[**Not**](https://reference.aspose.com/cells/net/aspose.cells/comment/properties/note)Emlak.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Comments-AddingComment-1.cs" >}}

## **Yorum Biçimlendirme**

Yükseklik, genişlik ve yazı tipi ayarlarını yapılandırarak yorumların görünümünü biçimlendirmek de mümkündür.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Comments-CommentFormatting-1.cs" >}}

## **Yoruma Resim Ekleyin**

Microsoft Excel 2007 ile, bir hücre yorumunun arka planı olarak bir görüntüye sahip olmak da mümkündür. Excel 2007'de bu, aşağıdaki adımlar izlenerek gerçekleştirilir. (Zaten bir hücre yorumu eklediğinizi varsayarlar.)

1. Açıklamayı içeren hücreye sağ tıklayın.
1.  Seçme**Yorumları Göster/Gizle**, ve yorumdaki tüm metni temizleyin.
1. Seçmek için yorumun kenarlığına tıklayın.
1.  Seçme**Biçim** , sonra**Yorum**.
1.  Üzerinde**Renkler ve Çizgiler** sekmesini genişletin**Renk** liste.
1.  Tıklamak**Dolgu Efektleri**.
1.  Üzerinde**Resim** sekme, tıklayın**Resim Seç**.
1. Resmi bulun ve seçin.
1.  Tıklamak**TAMAM** tüm diyaloglar kapanana kadar.

Aspose.Cells de bu özelliği sağlıyor. Aşağıda sıfırdan bir XLSX dosyası oluşturan ve "A1" hücresine arka planı resim olarak ayarlanmış bir yorum ekleyen bir kod örneği verilmiştir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Comments-AddImageToComment-1.cs" >}}

## **ileri konular**
- [Yorumun Metin Yönünü Değiştirme](/cells/tr/net/change-text-direction-of-the-comment/)
- [Yorum Yazı Tipi Rengi nasıl değiştirilir?](/cells/tr/net/how-to-change-the-comment-font-color/)
- [Yorum arka planı nasıl ayarlanır?](/cells/tr/net/how-to-set-comment-background/)
- [Zincirleme Yorumlar](/cells/tr/net/threaded-comments/)

