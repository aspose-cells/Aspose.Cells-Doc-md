---
title: Aynı Anda Birden Fazla İş Parçacığından Hücre Değerlerini Okuma
linktitle: Çoklu İş Parçacıkları
type: docs
weight: 1100
url: /tr/java/reading-cell-values-in-multiple-threads-simultaneously/
description: Aspose.Cells for Java API leri ile Aynı Anda Çoklu İş Parçacığından Hücre Değerlerini Okumanın Nasıl Yapılacağını Öğrenin.
keywords: Java da Aspose.Cells for Java API leri için Aynı Anda Çoklu İş Parçacığında Hücre Değerlerini Oku, Çoklu İş Parçacıkları.
---

{{% alert color="primary" %}}

Aynı Anda Birden Fazla İş Parçacığında hücre değerlerini okuma ihtiyacı yaygın bir gereksinimdir. Bu makale bu amaçla Aspose.Cells'in nasıl kullanılacağını açıklar.

{{% /alert %}}

## **Aspose.Cells for Java ile Aynı Anda Çoklu İş Parçacığından Hücre Değerlerini Okumanın Yolu**

Aynı anda birden fazla iş parçacığında hücre değerlerini okumak için [**Worksheet.getCells().setMultiThreadReading()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MultiThreadReading)'yi **true** olarak ayarlayın. Eğer yapmazsanız, yanlış hücre değerleri alabilirsiniz. Lütfen dikkat edin, formatlı hücre değerleri gibi bazı özellikler çoklu iplikler için desteklenmez. Bu nedenle, MultiThreadReading sadece hücrenin orijinal verilerine erişmenizi sağlar. Birden fazla iplikler ortamında hücrenin biçimlendirilmiş değerini almayı denerken, örneğin sayısal değerler için Cell.getStringValue() ile beklenmeyen bir sonuç veya istisna alabilirsiniz.

Aşağıdaki kod:

1. Bir çalışma kitabı oluşturur.
1. Bir çalışma sayfası ekler.
1. Çalışma sayfasını dize değerleriyle doldurur.
1. Sonra rastgele hücrelerden aynı anda değer okuyan iki iş parçacığı oluşturur.
   Okunan değerler doğru ise hiçbir şey olmaz. Okunan değerler yanlışsa bir mesaj görüntülenir.

Eğer bu satırı yorumlarsanız:

{{< highlight java >}}

testWorkbook.getWorksheets().get(0).getCells().setMultiThreadReading(true);

{{< /highlight >}}

o zaman aşağıdaki mesaj görüntülenir:

{{< highlight java >}}

if (s.equals("R" + row + "C" + col)!=true)

{

    System.out.println("This message box will show up when cells read values are incorrect.");

}

{{< /highlight >}}

Aksi takdirde, program herhangi bir mesaj göstermeden çalışır, bu da demek olur ki tüm hücrelerden okunan değerler doğrudur.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ThreadProc-ThreadProc.java" >}}
{{< app/cells/assistant language="java" >}}
