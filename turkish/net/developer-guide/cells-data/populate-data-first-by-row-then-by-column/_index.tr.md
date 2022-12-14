---
title: Verileri Önce Satıra, Sonra Sütuna Göre Doldurun
type: docs
weight: 1000
url: /tr/net/populate-data-first-by-row-then-by-column/
---
{{% alert color="primary" %}} 

Bir e-tabloyu verilerle önce satıra, ardından sütuna göre doldurmak, genel performansı artırır.

{{% /alert %}} 

Verileri A1, B1, A2, B2 sıralamasına koymak A1, A2, B1, B2'den daha hızlıdır. Bir çalışma sayfasında çok sayıda hücre varsa ve ikinci sırayı takip ederseniz, yani verileri satır satır dolduruyorsanız, bu ipucu programı çok daha hızlı hale getirebilir.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-PopulateDataEfficiently-PopulateDataFirstByRowThenColumns.cs" >}}
