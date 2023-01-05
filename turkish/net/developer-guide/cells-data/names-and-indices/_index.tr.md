---
title: Hücre adı ile satır/sütun dizini arasında dönüştürme
linktitle: Cell Ad ve Dizin Dönüştürme
type: docs
weight: 10
url: /tr/net/names-and-indices/
---
## **Satır ve Sütun İndekslerinden Cell Adını Alın**
Satır ve sütun dizini verilen bir hücrenin adını bulmak mümkündür. Bu makale nasıl yapılacağını açıklıyor.
Aspose.Cells, geliştiricilerin satır ve sütun dizini sağlamaları halinde bir hücrenin adını almalarına olanak tanıyan CellsHelper.CellIndexToName yöntemini sağlar.

{{% alert color="primary" %}} 

Satır ve sütun indekslerinin 1'den başladığı Microsoft Excel'in aksine, Aspose.Cells, satır ve sütun indekslerini 0'dan saymaya başlar.

{{% /alert %}} 

Aşağıdaki örnek kod, bilinen bir satır ve sütun dizini verilen hücrenin adına erişmek için CellsHelper.CellIndexToName'in nasıl kullanılacağını gösterir. Kod aşağıdaki çıktıyı üretir.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelperClass-IndexToName-1.cs" >}}
## **Cell Adından Satır ve Sütun İndekslerini Alın**
Adından hücrenin satır ve sütun indeksini bulmak mümkündür. Bu makale nasıl yapılacağını açıklıyor.
Aspose.Cells, geliştiricilerin hücrenin adından bir satır ve sütun dizini almasına olanak tanıyan CellsHelper.CellNameToIndex yöntemini sağlar.

{{% alert color="primary" %}} 

Satır ve sütun indekslerinin 1'den başladığı Microsoft Excel'in aksine, Aspose.Cells, satır ve sütun indekslerini 0'dan saymaya başlar.

{{% /alert %}} 

Aşağıdaki örnek kod, hücrenin adından satır ve sütun dizinini almak için CellsHelper.CellNameToIndex'in nasıl kullanılacağını gösterir. Kod aşağıdaki çıktıyı üretir.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelperClass-NameToIndex-1.cs" >}}
## **Güvenli sayfa adları oluşturun**
 Bazen çalışma zamanında sayfa adının atanması gerekebilir. Bu senaryoda, bazı ek karakterler içerebilen sayfa adları olabilir.<>+(?”. Sayfa adı olarak izin verilmeyen bu tür herhangi bir karakterin, kullanıcı tarafından sağlanan önceden ayarlanmış bir karakterle değiştirilmesi gerekir. Benzer şekilde, uzunluk, kesilmesi gereken 31 karakterden fazla artabilir. Apache POI şunları sağlar: güvenli adlar oluşturmanın belirli özellikleri, dolayısıyla benzer özellik, tüm bu sorunların üstesinden gelmek için Aspose.Cells tarafından sağlanmaktadır. Aşağıdaki örnek kod, bu özelliği göstermektedir:



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelper-CreateSafeSheetNames.cs" >}}

Çıktı:

bu ilk isim olan cre

` `<> + (adj.Özel _ " Özel"
