---
title: Hücre adı ile satır/sütun dizini arasındaki dönüşüm
linktitle: Cell İsim ve Dizin Dönüşümü
type: docs
weight: 10
url: /tr/net/names-and-indices/
description: Aspose.Cells for .NET API aracılığıyla hücre adı ile satır/sütun dizini arasındaki dönüşümü nasıl alacağınızı öğrenin.
keywords: Get Cell Name from Row and Column Indices, Get Row and Column Indices from Cell Name, Create safe worksheet names, Add safe worksheet names
---
##  **Satır ve Sütun İndekslerinden Cell Adını Alın**
Satır ve sütun indeksine göre bir hücrenin adını bulmak mümkündür. Bu makalede bunun nasıl yapılacağı açıklanmaktadır.
Aspose.Cells, geliştiricilerin satır ve sütun dizinini sağlamaları durumunda hücrenin adını almasına olanak tanıyan CellsHelper.CellIndexToName yöntemini sağlar.

{{% alert color="primary" %}} 

Satır ve sütun dizinlerinin 1'den başladığı Microsoft Excel'in aksine, Aspose.Cells, satır ve sütun dizinlerini 0'dan saymaya başlar.

{{% /alert %}} 

Aşağıdaki örnek kod, bilinen bir satır ve sütun dizini verilen hücrenin adına erişmek için CellsHelper.CellIndexToName öğesinin nasıl kullanılacağını gösterir. Kod aşağıdaki çıktıyı üretir.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelperClass-IndexToName-1.cs" >}}
##  **Cell Adından Satır ve Sütun İndekslerini Alın**
Adından hücrenin satır ve sütun indeksini bulmak mümkündür. Bu makalede bunun nasıl yapılacağı açıklanmaktadır.
Aspose.Cells, geliştiricilerin hücre adından satır ve sütun dizini almasına olanak tanıyan CellsHelper.CellNameToIndex yöntemini sağlar.

{{% alert color="primary" %}} 

Satır ve sütun dizinlerinin 1'den başladığı Microsoft Excel'in aksine, Aspose.Cells, satır ve sütun dizinlerini 0'dan saymaya başlar.

{{% /alert %}} 

Aşağıdaki örnek kod, hücrenin adından satır ve sütun dizinini almak için CellsHelper.CellNameToIndex'in nasıl kullanılacağını gösterir. Kod aşağıdaki çıktıyı üretir.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelperClass-NameToIndex-1.cs" >}}
##  **Güvenli sayfa adları oluşturun**
 Bazen çalışma zamanında sayfa adını atamaya ihtiyaç duyulur. Bu senaryoda, aşağıdaki gibi bazı ek karakterleri içerebilecek sayfa adları olabilir:<>+(?". Sayfa adı olarak kullanılmasına izin verilmeyen herhangi bir karakterin, kullanıcı tarafından sağlanan önceden ayarlanmış bir karakterle değiştirilmesine ihtiyaç vardır. Benzer şekilde uzunluk, kesilmesi gereken 31 karakterden fazla artabilir. Apache POI sağlar Güvenli adlar oluşturmanın belirli özellikleri olduğundan, tüm bu sorunları çözmek için Aspose.Cells tarafından benzer bir özellik sağlanmıştır. Aşağıdaki örnek kod bu özelliği göstermektedir:



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelper-CreateSafeSheetNames.cs" >}}

Çıktı:

bu cre olan ilk isim

` `<> + (adj.Özel _ " Özel"
