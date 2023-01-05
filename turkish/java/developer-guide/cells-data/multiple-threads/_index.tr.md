---
title: Cell Değerlerini Birden Çok Konuda Aynı Anda Okumak
linktitle: Çoklu Konular
type: docs
weight: 1100
url: /tr/java/reading-cell-values-in-multiple-threads-simultaneously/
---
{{% alert color="primary" %}}

Aynı anda birden çok iş parçacığındaki hücre değerlerini okuma ihtiyacı yaygın bir gereksinimdir. Bu makalede, Aspose.Cells'in bu amaçla nasıl kullanılacağı açıklanmaktadır.

{{% /alert %}}

 Aynı anda birden fazla iş parçacığındaki hücre değerlerini okumak için,[**Worksheet.getCells().setMultiThreadReading()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MultiThreadReading) ile**doğru**Bunu yapmazsanız, yanlış hücre değerleri alabilirsiniz. Hücre değerlerini biçimlendirme gibi bazı özelliklerin birden çok iş parçacığı için desteklenmediğini lütfen unutmayın. Yani MultiThreadReading, yalnızca hücrenin yalnızca orijinal verilerine erişmenizi sağlar. Çoklu iş parçacığı ortamında, sayısal değerler için Cell.getStringValue() gibi hücrenin biçimlendirilmiş değerini almaya çalışırsanız, beklenmeyen bir sonuç veya istisna alabilirsiniz.

Aşağıdaki kod:

1. Bir çalışma kitabı oluşturur.
1. Bir çalışma sayfası ekler.
1. Çalışma sayfasını dize değerleriyle doldurur.
1. Daha sonra rastgele hücrelerden değerleri aynı anda okuyan iki iş parçacığı oluşturur.
 Okunan değerler doğruysa hiçbir şey olmaz. Okunan değerler yanlışsa bir mesaj görüntülenir.

Bu satırı yorumlarsanız:

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

Aksi takdirde program herhangi bir mesaj göstermeden çalışır, bu da hücrelerden okunan tüm değerlerin doğru olduğu anlamına gelir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ThreadProc-ThreadProc.java" >}}
