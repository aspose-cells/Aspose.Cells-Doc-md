---
title: Hücre adı ve satır/sütun dizini arasında dönüştürme işlemi
linktitle: Hücre Adı ve Dizin Dönüştürme
type: docs
weight: 10
url: /tr/nodejs-cpp/names-and-indices/
description: Aspose.Cells for Node.js via C++ API kullanarak hücre adları ile satır/sütun dizini arasındaki dönüşüm nasıl yapılır öğrenin.
keywords: Node.js C++ aracılığıyla Satır ve Sütun İndisinden Hücre Adı Al, Hücre Adından Satır ve Sütun İndisini Al, Güvenli çalışma sayfası isimleri oluştur, Güvenli çalışma sayfası isimleri ekle
---

## **Satır ve Sütun Dizilerinden Hücre Adı Alın**
Bir hücrenin adını bulmak mümkündür, verilen satır ve sütun dizini. Bu makale açıklar.
Aspose.Cells for Node.js via C++, CellsHelper.cellIndexToName metodunu sağlar; bu metod, satır ve sütun indeksleri verildiğinde hücrenin adını almanıza olanak tanır.

{{% alert color="primary" %}} 

Microsoft Excel, satır ve sütun indekslerini 1’den saymaya başlar. Aspose.Cells for Node.js via C++ ise satır ve sütun indekslerini 0’dan saymaya başlar.

{{% /alert %}} 

Aşağıdaki örnek kod, bilinen satır ve sütun indeksi verildiğinde CellsHelper.cellIndexToName metodunu kullanarak hücrenin adını nasıl alacağınızı gösterir. Kod aşağıdaki çıktıyı üretir.



{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-CellsHelper-IndexToName-1.js" >}}
## **Hücre Adından Satır ve Sütun Dizilerini Alın**
Bir hücrenin adından satır ve sütun dizinini bulmak mümkündür. Bu makale açıklar.
Aspose.Cells for Node.js via C++, CellsHelper.cellNameToIndex metodunu sağlar; bu metod, hücrenin adından satır ve sütun indekslerini almanıza olanak tanır.

{{% alert color="primary" %}} 

Microsoft Excel, satır ve sütun indekslerini 1’den saymaya başlar. Aspose.Cells for Node.js via C++ ise satır ve sütun indekslerini 0’dan saymaya başlar.

{{% /alert %}} 

Aşağıdaki örnek kod, CellsHelper.cellNameToIndex metodunu kullanarak hücrenin adından satır ve sütun indekslerini nasıl alacağınızı gösterir. Kod aşağıdaki çıktıyı üretir.



{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-CellsHelper-NameToIndex-1.js" >}}

## **Güvenli Çalışma Sayfası Adları Oluşturun**
Bazen çalışma sayfası adını çalışma zamanında atamak gerekebilir. Bu durumda, <>+(?” gibi ek karakterler içerebilecek sayfa isimleri olabilir. Bu tür karakterlerin herhangi birini, sayfa adı olarak kullanılamayan karakterleri, kullanıcı tarafından belirlenen karakterle değiştirmek gerekebilir. Benzer şekilde, uzunluğu 31 karakterin üzerine çıkabilir ve bu durumda kesmek gerekebilir. Apache POI, güvenli isimler oluşturma özellikleri sağlar ve Aspose.Cells for Node.js via C++ de bu sorunları çözmek için benzer özelliği sunar. İşte bu özelliği gösteren örnek kod.



{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-CellsHelper-CreateSafeSheetNames.js" >}}

Çıktı:

Bu, oluşturulmuş ilk adın kısaltıldığı ad

` <> + (adj.Private _ "Özel"
