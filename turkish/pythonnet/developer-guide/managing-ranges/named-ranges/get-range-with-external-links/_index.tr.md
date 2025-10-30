---
title: Harici Bağlantıları İçeren Menzil Al
type: docs
weight: 120
url: /tr/python-net/get-range-with-external-links/
description: Bu makale, Aspose.Cells ile Python via .NET API si tarafından Dış Bağlantılara Sahip Aralığı Almayı göstermektedir.
keywords: Python Excel Kütüphanesi, Python Dış Bağlantılara Sahip Aralığı Almak.
---

## **Harici Bağlantıları Olan Aralığı Al**

Çoğu zaman Excel dosyaları, dış bağlantıları kullanarak diğer Excel dosyalarından veriye erişir. Aspose.Cells for Python via .NET, dış bağlantıları almak için [**Name.get_referred_areas**](https://reference.aspose.com/cells/python-net/aspose.cells/name/get_referred_areas/#bool) yöntemini kullanmayı sağlar. [**Name.get_referred_areas**](https://reference.aspose.com/cells/python-net/aspose.cells/name/get_referred_areas/#bool) yöntemi, bir [**ReferredArea**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea) türünde dizi döndürür. [**ReferredArea**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea) sınıfı, dış dosya adını döndüren bir özellik sağlar. [**external_file_name**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/external_file_name/) özelliğine dış dosyanın adını döndüren [**ReferredArea**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea) sınıfı erişir.

- [**end_column**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/end_column/): Alanın son sütunu
- [**end_row**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/end_row/): Alanın son satırı
- [**external_file_name**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/external_file_name/): Bu harici bir başvuru ise harici dosya adını al
- [**is_area**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/is_area/): Bu bir alan mı belirtir
- [**is_external_link**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/is_external_link/): Bu bir harici bağlantı mı belirtir
- [**sheet_name**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/sheet_name/): Bu başvurunun hangi tabloda olduğunu belirtir
- [**start_column**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/start_column): Alanın başlangıç sütunu
- [**start_row**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/start_row): Alanın başlangıç satırı

Aşağıdaki örnek kod, [**Name.get_referred_areas**](https://reference.aspose.com/cells/python-net/aspose.cells/name/get_referred_areas/#bool) yöntemi kullanarak Dış Bağlantılı Aralıkları almanın kullanımını gösterir.

## **Örnek Kod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-Worksheets-GetRangeWithExternalLinks-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
