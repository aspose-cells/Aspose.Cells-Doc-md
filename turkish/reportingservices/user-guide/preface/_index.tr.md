---
title: Önsöz
type: docs
weight: 20
url: /tr/reportingservices/preface/
---
{{% alert color="primary" %}} 

Aspose.Cells for Reporting Services temel olarak iki bileşen içerir: Aspose.Cells.Report.Designer ve Aspose.Cells.Renderer for Reporting Services. İlki, doğrudan Microsoft Excel'de raporları tasarlamak için kullanılır ve ikincisi, Microsoft Excel'e bir RDL raporu oluşturmaktan sorumludur.

{{% /alert %}} 
### **Rapor Tasarımcısı ile Rapor Tasarlama**
Aspose.Cells.Report.Designer kullanarak bir rapor tasarlamanın ana adımları şunlardır:

1. **Veri kaynakları ve sorgular oluşturma**.
 Microsoft Sorgu, Aspose.Cells.Report.Designer ile entegredir ve veri kaynakları ve sorgular oluşturmak için bir grafik aracı olarak kullanılır. Kullanıcılar, işlemler için veri kaynaklarının ve sorguların mevcut olduğu mevcut bir RDL dosyasını da kullanabilir.
1. **Harita parametreleri**.
 Bir sorgunun SQL ifadeleri parametreler içeriyorsa, kullanıcıların rapor parametreleri oluşturması ve SQL parametrelerini rapor parametreleriyle eşlemesi gerekir. Aspose.Cells.Report.Designer'da bir rapor parametresi için geçerli değerler atayabilirsiniz.
1. **Tasarım Microsoft Excel rapor şablonu içeriği, stilleri ve biçimleri**.
Bir Aspose.Cells rapor şablonu, aşağıdaki rapor öğesi türlerinden herhangi bir sayıda içerebilir:
 1. Tablo
 1. Pivot tablo
 1. Grafik
 1. Metin kutusu
 1. Matris
 Normalde, rapor öğesi için veri kaynağı olarak bir sorgu (yani, DataSet) kullanılır. Bazı rapor öğesi türleri için bir veri kaynağı olarak Raporlama Hizmetleri parametrelerini, formülleri ve genel değişkenleri de kullanabilirsiniz. Rapor öğelerinin stilleri ve biçimleri, yalnızca rapor öğelerini oluşturan hücrelerin stilleri ve biçimleri ayarlanarak belirlenir.
1. **Raporu yayınla**.
 Yukarıdaki adımlardan sonra, rapor yayınlanmaya hazırdır. Kullanıcılar, raporun hangi klasörde yayınlanacağını belirleyebilir. Gerekirse, raporun veri kaynağı olarak Rapor Sunucusunda paylaşılan bir veri kaynağı atayabilirsiniz.
1. **Önizleme raporu**.
Rapor Sunucusunda önizleme için bir rapor seçerken, hangi dosya formatına (örneğin Microsoft Excel 97-2003 ikili XLS formatı, SpreadsheetML veya Microsoft Excel 2007 XLSX formatı) ve oluşturulan herhangi bir girdi raporu parametresini belirtmeniz istenir. rapor tasarımı sırasında. Bundan sonra rapor, Reporting Services tarafından sağlanan verilerle doldurulur.
