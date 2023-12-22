---
title: Birden Fazla Konudaki Cell Değerlerini Aynı Anda Okumak
linktitle: Çoklu Konular
type: docs
weight: 1100
url: /tr/java/reading-cell-values-in-multiple-threads-simultaneously/
description: Aspose.Cells for Java API'leri ile Birden Çok Konudaki Cell Değerlerini Aynı Anda Nasıl Okuyacağınızı öğrenin.
keywords: Java Read Cell Values in Multiple Threads Simultaneously, Multiple Threads for Aspose.Cells for Java APIs.
---
{{% alert color="primary" %}}

Aynı anda birden fazla iş parçacığında hücre değerlerinin okunmasının gerekliliği ortak bir gereksinimdir. Bu makalede, bu amaçla Aspose.Cells'in nasıl kullanılacağı açıklanmaktadır.

{{% /alert %}}

##  **Aspose.Cells for Java ile Birden Fazla Konudaki Cell Değerleri Aynı Anda Nasıl Okunur?**

 Birden fazla iş parçacığında hücre değerlerini aynı anda okumak için[**Worksheet.getCells().setMultiThreadReading()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MultiThreadReading)*doğruya**. Bunu yapmazsanız yanlış hücre değerlerini alabilirsiniz. Hücre değerlerini biçimlendirme gibi bazı özelliklerin birden çok iş parçacığı için desteklenmediğini lütfen unutmayın. Yani MultiThreadReading yalnızca hücrenin orijinal verilerine erişmenizi sağlar. Çoklu iş parçacığı ortamında, sayısal değerler için Cell.getStringValue() gibi hücrenin biçimlendirilmiş değerini almaya çalışırsanız, beklenmeyen sonuç veya istisnayla karşılaşabilirsiniz.

Aşağıdaki kod:

1. Bir çalışma kitabı oluşturur.
1. Bir çalışma sayfası ekler.
1. Çalışma sayfasını dize değerleriyle doldurur.
1. Daha sonra rastgele hücrelerden değerleri aynı anda okuyan iki iş parçacığı oluşturur.
 Okunan değerler doğru ise hiçbir şey olmaz. Okunan değerler hatalıysa bir mesaj görüntülenir.

Bu satıra yorum yaparsanız:

{{< highlight "java" >}}

testWorkbook.getWorksheets().get(0).getCells().setMultiThreadReading(true);

{{< /highlight >}}

ardından aşağıdaki mesaj görüntülenir:

{{< highlight "java" >}}

if (s.equals("R" + row + "C" + col)!=true)

{

    System.out.println("This message box will show up when cells read values are incorrect.");

}

{{< /highlight >}}

Aksi takdirde program herhangi bir mesaj vermeden çalışır, bu da hücrelerden okunan tüm değerlerin doğru olduğu anlamına gelir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ThreadProc-ThreadProc.java" >}}
