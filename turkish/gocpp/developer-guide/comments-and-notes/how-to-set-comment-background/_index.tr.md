---
title: Excel de Yorum un Arka Planını Golang ve C++ kullanarak nasıl değiştiririm
linktitle: Yorum Arka Planı
type: docs
weight: 190
url: /tr/go-cpp/how-to-set-comment-background/
description: Excel de yoruma renk nasıl değiştirilir. C++ kullanarak Excel de yoruma resim veya görüntü nasıl eklenir.
keywords: Yorum arkaplan rengi ekle, resim ekle, yorum gölgeleme excel
---

{{% alert color="primary" %}}

 Yorumlar, hücrelere eklenen ve yorumları kaydetmek için kullanılan yorumlardır, formülün nasıl çalıştığı, değerlerin nereden geldiği veya inceleyenlerin soruları gibi detayları içerir. Yorumlar, birden fazla kişinin aynı belgeyi farklı zamanlarda tartışması veya gözden geçirmesi sırasında son derece önemli rol oynar. Farklı kişilerin yorumlarını nasıl ayırt edebilirim? Evet, her yorum için farklı bir arkaplan rengi ayarlayabiliriz. Ancak, çok sayıda belge ve yorum işlemeniz gerektiğinde, bu manuel olarak yapmak bir felakettir. Neyse ki, [**Aspose.Cells**](https://products.aspose.com/cells/go-cpp/) bir API sağlar ve bunu koda uygun şekilde yapmanıza imkan tanır.

{{% /alert %}}

## **Excel'de yorumda renk nasıl değiştirilir**

Varsayılan yorum arkaplan rengini kullanmak istemiyorsanız, onu ilgilendiğiniz bir renk ile değiştirmek isteyebilirsiniz. Excel'de Yorum kutusunun arkaplan rengini nasıl değiştiririm?

 Aşağıdaki kod, [**Aspose.Cells**](https://products.aspose.com/cells/go-cpp/) kullanarak kendi seçtiğiniz yorumlara favori arkaplan renginizi eklemenize nasıl yardımcı olacağını gösterecek.

 Size bir [örnek dosya](exmaple.xlsx) hazırladık. Bu dosya, aşağıdaki kodda Workbook nesnesini başlatmak için kullanılır.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-HowToSetCommentBackground.go" >}}
 Yukarıdaki kodu çalıştırın ve bir [sonuç dosyası](result.xlsx) alın.

## **Excel'de yorumlara resim veya görüntü eklemek**

 Microsoft Excel, kullanıcıların elektronik tabloların görünümünü ve hissini büyük ölçüde özelleştirmesine olanak tanır. Yorumlara arkaplan resmi eklemek bile mümkündür. Bir arkaplan resmi eklemek estetik bir tercih olabilir veya markalaşmayı güçlendirmek için kullanılabilir.

 Aşağıdaki örnek kod, [**Aspose.Cells**](https://products.aspose.com/cells/go-cpp/) API kullanarak sıfırdan bir XLSX dosyası oluşturur ve hücre A1'e resimli arkaplan ile bir yorum ekler.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-HowToSetCommentBackground-1.go" >}}
