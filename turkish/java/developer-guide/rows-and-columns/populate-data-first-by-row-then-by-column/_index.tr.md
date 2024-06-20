---
title: Verileri Önce Satır, Sonra Sütun Olarak Doldur
type: docs
weight: 10
url: /tr/java/populate-data-first-by-row-then-by-column/
---

{{% alert color="primary" %}}

Bir elektronik tabloya verileri önce satır, sonra sütun olarak doldurmak genel performansı iyileştirir.

{{% /alert %}}

## Verileri Önce Satır, Sonra Sütun Olarak Doldur

A1, B1, A2, B2 şeklinde veri yerleştirmek, A1, A2, B1, B2 şeklinde yerleştirmekten daha hızlıdır. Eğer bir çalışma sayfasında çok fazla hücre varsa ve ikinci sırayı takip ediyorsanız, yani verileri satır satır dolduruyorsanız, bu ipucu programı çok daha hızlı hale getirebilir.

## Java koduyla verileri önce satır, sonra sütun olarak doldurma

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-PopulateDatabyRowthenColumn-PopulateDatabyRowthenColumn.java" >}}
