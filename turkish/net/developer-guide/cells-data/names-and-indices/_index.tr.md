---
title: Hücre adı ve satır/sütun dizini arasında dönüştürme işlemi
linktitle: Hücre Adı ve Dizin Dönüştürme
type: docs
weight: 10
url: /tr/net/names-and-indices/
description: Aspose.Cells for .NET API si aracılığıyla Hücre Adı ve Satır/Sütun İndeks Dönüşümünü Nasıl Alın.
keywords: Satır ve Sütun İndekslerinden Hücre Adı Alın, Satır ve Sütun İndekslerini Hücre Adından Alın, Güvenli çalışma sayfası adları oluşturun, Güvenli çalışma sayfası adları ekleyin
---

## **Satır ve Sütun Dizilerinden Hücre Adı Alın**
Bir hücrenin adını bulmak mümkündür, verilen satır ve sütun dizini. Bu makale açıklar.
Aspose.Cells, geliştiricilere, satır ve sütun dizinini sağladıklarında bir hücrenin adını almasını sağlayan CellsHelper.CellIndexToName yöntemini sağlar.

{{% alert color="primary" %}} 

Microsoft Excel satır ve sütun indekslerini 1’den başlatır. Aspose.Cells ise satır ve sütun indekslerini 0’dan başlatır.

{{% /alert %}} 

Aşağıdaki örnek kod, CellsHelper.CellIndexToName'i bir bilinen satır ve sütun endeksine göre hücrenin adına erişmek için nasıl kullandığını gösterir. Kod aşağıdaki çıktıyı üretir.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelperClass-IndexToName-1.cs" >}}
## **Hücre Adından Satır ve Sütun Dizilerini Alın**
Bir hücrenin adından satır ve sütun dizinini bulmak mümkündür. Bu makale açıklar.
Aspose.Cells, geliştiricilere, hücrenin adını verdiklerinde CellsHelper.CellNameToIndex yöntemini kullanarak satır ve sütun indisini almasını sağlar.

{{% alert color="primary" %}} 

Microsoft Excel satır ve sütun indekslerini 1’den başlatır. Aspose.Cells ise satır ve sütun indekslerini 0’dan başlatır.

{{% /alert %}} 

Aşağıdaki örnek kod, CellsHelper.CellNameToIndex'i kullanarak hücre adından satır ve sütun indeksini nasıl alacağını göstermektedir. Kod aşağıdaki çıktıyı oluşturur.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelperClass-NameToIndex-1.cs" >}}
## **Güvenli Çalışma Sayfası Adları Oluşturun**
Bazı durumlarda çalışma zamanında sayfa adının atanması gerekebilir. Bu senaryoda, kullanıcı tarafından belirtilen bazı özel karakterler içerebilecek sayfa adları olabilir, örneğin <>+(?”. Sayfa adı olarak izin verilmeyen herhangi bir karakterin belirlenmiş bir karakterle değiştirilmesi gerekmektedir. Benzer şekilde uzunluk 31 karakterden fazla olabilir ve kısaltılması gerekmektedir. Apache POI, güvenli adlar oluşturmanın belirli özelliklerini sağlar, bu nedenle Aspose.Cells tarafından tüm bu sorunlarla başa çıkmak için benzer bir özellik sağlanmıştır. Aşağıdaki örnek kod bu özelliği göstermektedir:



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelper-CreateSafeSheetNames.cs" >}}

Çıktı:

Bu, oluşturulmuş ilk adın kısaltıldığı ad

` <> + (adj.Private _ "Özel"
{{< app/cells/assistant language="csharp" >}}
