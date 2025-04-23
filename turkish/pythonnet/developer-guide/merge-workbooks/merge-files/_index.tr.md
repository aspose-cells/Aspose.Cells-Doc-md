---
title: Dosyaları Birleştirme
type: docs
weight: 20
url: /tr/python-net/merge-files/
---

## **Giriş**

Aspose.Cells for Python via .NET farklı dosya birleştirme yolları sağlar. Veri, biçimlendirme ve formülleri olan basit dosyalar için, [**Workbook.combine()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/combine) yöntemi birkaç çalışma kitabını birleştirmek için kullanılabilir, ve [**Worksheet.copy()**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/copy) yöntemi çalışma sayfalarını yeni bir çalışma kitabına kopyalamak için kullanılabilir. Bu yöntemler kullanımı kolay ve etkilidir, fakat çok sayıda dosyayı birleştiriyorsanız, sistem kaynaklarını çok kullanabilirler. Bunu önlemek için, daha verimli bir yol olan [**CellsHelper.merge_files**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/merge_files) statik yöntemini kullanın, birkaç dosyayı birleştirirken daha etkilidir.

## **Aspose.Cells for Python via .NET kullanarak Dosya Birleştirme**

Aşağıdaki örnek kod, [**CellsHelper.merge_files**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/merge_files) yöntemini kullanarak büyük dosyaları birleştirmenin nasıl yapılacağını göstermektedir. Basit ancak büyük verilere ve formüllere sahip Book1.xls ve Book2.xls adlı iki dosya alır.

{{% alert color="primary" %}}

Metod yalnızca veri, stiller, biçimlendirme ve formülleri birleştirmeyi destekler. Grafikler, resimler, yorumlar veya diğer nesneler gibi objeler, bu yöntemi kullanarak birleştirilmeyebilir. Ayrıca, işlem için geçici verileri saklamak için önbellek dosyası kullanılır.

{{% /alert %}}

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Merge-Workbooks-CellsHelperClass-MergeFiles-1.py" >}}

