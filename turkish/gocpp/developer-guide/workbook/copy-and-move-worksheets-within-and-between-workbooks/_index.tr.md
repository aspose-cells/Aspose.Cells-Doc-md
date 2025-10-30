---
title: Çalışma Kitapları İçinde ve Arasında Sayfaları Kopyala ve Taşı Golang ile C++
linktitle: Sayfaları Kopyalayın ve Taşıyın
type: docs
weight: 80
url: /tr/go-cpp/copy-and-move-worksheets-within-and-between-workbooks/
description: Excel çalışma kitapları içinde ve arasında çalışma sayfalarını nasıl kopyalayacağınızı ve taşıyacağınızı Aspose.Cells for C++ kullanarak öğrenin.
---

{{% alert color="primary" %}}

Bazen, ortak biçimlendirme ve veri girişine sahip birden çok sayfaya ihtiyacınız olur. Örneğin, üç aylık bütçelerle çalışıyorsanız, aynı sütun başlıkları, satır başlıkları ve formülleri içeren çalışma sayfaları olan bir çalışma kitabı oluşturmak isteyebilirsiniz. Bunu yapmanın bir yolu vardır: bir sayfa oluşturmak ve sonra onu birden çok kez kopyalamak.

Aspose.Cells, çalışma kitapları arasında veya içinde çalışma sayfalarını kopyalama veya taşımayı destekler. Veri, biçimlendirme, tablolar, matrisler, grafikler, resimler ve diğer nesnelerin yanı sıra sayfalar en yüksek hassasiyetle kopyalanır.

{{% /alert %}}

## **Çalışma Sayfalarını Kopyalama ve Taşıma**

### **Bir Çalışma Sayfasını Bir Çalışma Kitabı İçinde Kopyalama**

Başlangıç adımları tüm örnekler için aynıdır:

1. Microsoft Excel’de bazı verilerle iki çalışma kitabı oluşturun. Bu örnekte, Microsoft Excel’de iki yeni çalışma kitabı oluşturduk ve çalışma sayfalarına bazı veriler girdik:
   - FirstWorkbook.xlsx (3 çalışma sayfası)
   - SecondWorkbook.xlsx (1 çalışma sayfası)

1. Aspose.Cells'i indirin ve kurun:
   1. [Aspose.Cells for C++ İndirme](https://downloads.aspose.com/cells/go-cpp/)
   1. Geliştirme bilgisayarınıza kurun

1. Bir proje oluşturun:
   1. Tercih ettiğiniz IDE’de yeni bir C++ projesi oluşturun

1. Referanslar ekleyin:
   1. Aspose.Cells for C++ kütüphanesini projenize ekleyin

1. Bir çalışma kitabı içindeki çalışsayfayı kopyalama
   İlk örnek, İlkÇalışmaKitabı.xlsx içindeki ilk çalışsayfayı (Kopya) kopyalar.

Kod çalıştırıldığında, Kopya adlı çalışsayfa, İlkÇalışmaKitabı.xlsx içinde Last Sheet adıyla kopyalanır.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopyAndMoveWorksheetsWithinAndBetweenWorkbooks.go" >}}
### **Bir Çalışma Kitabı içinde bir Çalışsayfayı Taşıma**

Aşağıdaki kod, bir çalışma kitabı içindeki bir çalışsayfayı bir konumdan başka bir konuma taşımanın nasıl yapıldığını gösterir. Kod çalıştırıldığında, İlkÇalışmaKitabı.xlsx içindeki İndex 1'de Move olarak adlandırılan çalışsayfa, İndex 2'ye taşınır.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopyAndMoveWorksheetsWithinAndBetweenWorkbooks-1.go" >}}
### **Çalışma Kitapları Arasında Bir Çalışma Sayfası Kopylama**

Kodu çalıştırmak, Copy adlı çalışma sayfasını SecondWorkbook.xlsx’e kopyalar ve adı Sheet2 olur.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopyAndMoveWorksheetsWithinAndBetweenWorkbooks-2.go" >}}
### **Çalışma Kitapları Arasında Bir Çalışma Sayfası Taşıma**

Kod çalıştırıldığında, İlkÇalışmaKitabı.xlsx içindeki Move adlı çalışsayfa, İkinciÇalışmaKitabı.xlsx içine Sheet3 adıyla taşınır.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopyAndMoveWorksheetsWithinAndBetweenWorkbooks-3.go" >}}
