---
title: Hücre adı ve satır/sütun dizini arasında dönüştürme işlemi
linktitle: Hücre Adı ve Dizin Dönüştürme
type: docs
weight: 10
url: /tr/python-net/names-and-indices/
description: Aspose.Cells for Python via .NET API si aracılığıyla Hücre Adı ve Satır/Sütun Dizini Arasındaki Dönüşümü Nasıl Alacağınızı Öğrenin.
keywords: Python Excel Kütüphanesi, Python Satır ve Sütun Dizilerinden Hücre Adı Alın, Python Satır ve Sütun Dizilerinden Hücre Adı Alın, Python Güvenli Çalışma Sayfası Adları Oluşturun, Python Güvenli Çalışma Sayfası Adları Ekleyin
---

## **Satır ve Sütun Dizilerinden Hücre Adı Alın**
Bir hücrenin adını bulmak mümkündür, verilen satır ve sütun dizini. Bu makale açıklar.
Aspose.Cells for Python via .NET, bir hücrenin adını almak için geliştiricilere bir yöntem sağlar [**CellsHelper.cell_index_to_name**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/cell_index_to_name/#int-int) sağlarlar.

{{% alert color="primary" %}} 

Microsoft Excel'de satır ve sütun dizinleri 1'den başlarken, Aspose.Cells for Python via .NET satır ve sütun dizinlerini 0'dan başlatır.

{{% /alert %}} 

Aşağıdaki örnek kod, bilinen bir satır ve sütun dizin verildiğinde [**CellsHelper.cell_index_to_name**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/cell_index_to_name/#int-int) kullanarak hücrenin adına erişmeyi açıklar. Kod aşağıdaki çıktıyı oluşturur.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-CellsHelper-IndexToName-1.py" >}}

## **Hücre Adından Satır ve Sütun Dizilerini Alın**
Bir hücrenin adından satır ve sütun dizinini bulmak mümkündür. Bu makale açıklar.
Aspose.Cells for Python via .NET, hücrenin adından satır ve sütun dizinini almak için geliştiricilere [**CellsHelper.cell_name_to_index**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/cell_name_to_index/#str-any-any) sağlar.

{{% alert color="primary" %}} 

Microsoft Excel'de satır ve sütun dizinleri 1'den başlarken, Aspose.Cells for Python via .NET satır ve sütun dizinlerini 0'dan başlatır.

{{% /alert %}} 

Aşağıdaki örnek kod, hücrenin adından satır ve sütun dizinini almak için [**CellsHelper.cell_name_to_index**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/cell_name_to_index/#str-any-any) kullanımını açıklar. Kod aşağıdaki çıktıyı oluşturur.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-CellsHelper-NameToIndex-1.py" >}}

## **Güvenli Çalışma Sayfası Adları Oluşturun**
Bazı durumlarda çalışma zamanında sayfa adının atanması gerekebilir. Bu senaryoda, sayfa adları arasında <>+(?” gibi ek karakterler içerebilecek karakterler olabilir. Sayfa adı olarak izin verilmeyen herhangi bir karakterin, kullanıcı tarafından belirtilen önceden ayarlanmış bir karakterle değiştirilmesi gerekmektedir. Benzer şekilde karakter uzunluğu 31 karakterden fazla olabilir ve bu durumda kısaltılması gerekir. Apache POI güvenli adlar oluşturma özellikleri sunar. Bu nedenle, Aspose.Cells for Python via .NET tarafından tüm bu sorunları ele almak için benzer bir özellik sağlanmaktadır. Aşağıdaki örnek kod bu özelliği göstermektedir:



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-CellsHelper-CreateSafeSheetNames.py" >}}

Çıktı:

Bu, oluşturulmuş ilk adın kısaltıldığı ad

` <> + (adj.Private _ "Özel"
