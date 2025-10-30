---
title: Aynı Anda Birden Fazla İş Parçacığından Hücre Değerlerini Okuma
linktitle: Çoklu İş Parçacıkları
type: docs
weight: 1800
url: /tr/nodejs-cpp/reading-cell-values-in-multiple-threads-simultaneously/
description: Aspose.Cells for Node.js via C++ API aracılığıyla birden fazla iş parçacığında hücre değerlerini aynı anda okuma öğrenin.
keywords: Node.js C++ ile Çoklu İş Parçacığında Hücre Değerlerini Oku, Aspose.Cells C++ Çoklu İş Parçacığıyla, Çoklu İş Parçacığında Veri Okuma
---

{{% alert color="primary" %}}

Aynı Anda Birden Fazla İş Parçacığında hücre değerlerini okuma ihtiyacı yaygın bir gereksinimdir. Bu makale bu amaçla Aspose.Cells'in nasıl kullanılacağını açıklar.

{{% /alert %}}

Birden fazla iş parçacığında aynı anda hücre değerleri okumak için, [**Cells.setMultiThreadReading(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#setMultiThreadReading-boolean-) değerini **doğru** olarak ayarlayın. Aksi takdirde yanlış hücre değerleri alabilirsiniz.

Aşağıdaki kod:

1. Bir çalışma kitabı oluşturur.
1. Bir çalışma sayfası ekler.
1. Çalışma sayfasını dize değerleriyle doldurur.
1. Sonra rastgele hücrelerden aynı anda değer okuyan iki iş parçacığı oluşturur.
   Okunan değerler doğru ise hiçbir şey olmaz. Okunan değerler yanlışsa bir mesaj görüntülenir.

Eğer bu satırı yorumlarsanız:

{{< highlight javascript >}}

testWorkbook.getWorksheets().get(0).getCells().setMultiThreadReading(true);

{{< /highlight >}}

o zaman aşağıdaki mesaj görüntülenir:

{{< highlight javascript >}}

if (s !== "R" + row + "C" + col)
{
    console.log("This message box will show up when cells read values are incorrect.");
}

{{< /highlight >}}

Aksi takdirde, program herhangi bir mesaj göstermeden çalışır, bu da demek olur ki tüm hücrelerden okunan değerler doğrudur.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-multiple-threads.js" >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
