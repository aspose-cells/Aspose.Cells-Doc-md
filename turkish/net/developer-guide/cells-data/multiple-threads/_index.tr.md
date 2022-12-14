---
title: Cell Değerlerini Birden Çok Konuda Aynı Anda Okumak
linktitle: Çoklu Konular
type: docs
weight: 1800
url: /tr/net/reading-cell-values-in-multiple-threads-simultaneously/
---
{{% alert color="primary" %}}

Aynı anda birden çok iş parçacığındaki hücre değerlerini okuma ihtiyacı yaygın bir gereksinimdir. Bu makalede, Aspose.Cells'in bu amaçla nasıl kullanılacağı açıklanmaktadır.

{{% /alert %}}

 Aynı anda birden fazla iş parçacığındaki hücre değerlerini okumak için,[**Worksheet.Cells.MultiThreadReading**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/multithreadreading) ile**doğru**. Bunu yapmazsanız, yanlış hücre değerleri alabilirsiniz.

Aşağıdaki kod:

1. Bir çalışma kitabı oluşturur.
1. Bir çalışma sayfası ekler.
1. Çalışma sayfasını dize değerleriyle doldurur.
1. Daha sonra rastgele hücrelerden değerleri aynı anda okuyan iki iş parçacığı oluşturur.
 Okunan değerler doğruysa hiçbir şey olmaz. Okunan değerler yanlışsa bir mesaj görüntülenir.

Bu satırı yorumlarsanız:

{{< highlight "java" >}}

 testWorkbook.Worksheets[0].Cells.MultiThreadReading = true;

{{< /highlight >}}

ardından aşağıdaki mesaj görüntülenir:

{{< highlight "java" >}}

 if (s != "R" + row + "C" + col)

{

    MessageBox.Show("This message box will show up when cells read values are incorrect.");

}

{{< /highlight >}}

Aksi takdirde program herhangi bir mesaj göstermeden çalışır, bu da hücrelerden okunan tüm değerlerin doğru olduğu anlamına gelir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ReadingCellValuesInMultipleThreadsSimultaneously-1.cs" >}}
