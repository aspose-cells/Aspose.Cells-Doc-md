---
title: Önsöz
type: docs
weight: 20
url: /tr/reportingservices/preface/
---

{{% alert color="primary" %}} 

Aspose.Cells for Reporting Services, Aspose.Cells.Report.Designer ve Raporlama Hizmetleri için Aspose.Cells.Renderer olmak üzere iki bileşeni içermektedir. İlki, raporları doğrudan Microsoft Excel'de tasarlamak için kullanılır ve ikincisi, bir RDL raporunu Microsoft Excel'e dönüştürmekten sorumludur. 

{{% /alert %}} 
### **Rapor Tasarımcısı ile Rapor Tasarlama**
Aspose.Cells.Report.Designer kullanarak bir rapor tasarlamak için temel adımlar:

1. **Veri kaynakları ve sorgular oluşturun**.
   Microsoft Sorgusu, Aspose.Cells.Report.Designer ile entegre edilir ve veri kaynakları ve sorgular oluşturmak için grafiksel bir araç olarak kullanılır. Kullanıcılar, veri kaynakları ve sorguların yapılandırılabilir olduğu mevcut bir RDL dosyasını da kullanabilirler.
1. **Parametreleri eşleştirin**.
   Bir sorgunun SQL ifadeleri parametre içeriyorsa, kullanıcılar rapor parametreleri oluşturup SQL parametrelerini rapor parametrelerine eşlemek zorundadır. Aspose.Cells.Report.Designer'da bir rapor parametresi için geçerli değerleri belirleyebilirsiniz.
1. **Microsoft Excel rapor şablonu içeriğini, stillerini ve formatlarını tasarlayın**.
   Bir Aspose.Cells rapor şablonu, aşağıdaki rapor öğe türlerinden herhangi bir sayıda içerebilir: 
   1. Tablo
   1. Pivot tablo
   1. Grafik
   1. Metin kutusu
   1. Matrix
      Normalde bir sorgu (yani DataSet), rapor öğesinin veri kaynağı olarak kullanılır. Ayrıca, bazı rapor öğe türleri için Reporting Services parametreleri, formülleri ve genel değişkenleri veri kaynağı olarak kullanabilirsiniz. Rapor öğelerinin stilleri ve formatları, rapor öğelerini oluşturan hücrelerin stillerini ve formatlarını ayarlayarak belirlenir.
1. **Raporu yayınla**.
   Yukarıdaki adımlardan sonra, rapor yayına hazır hale gelir. Kullanıcılar raporun yayınlanacağı klasörü belirleyebilirler. Gerekirse, rapor için Rapor Sunucusunda paylaşılan veri kaynağını veri kaynağı olarak atayabilirsiniz.
1. **Raporu önizle**.
   Rapor Sunucusunda önizleme için bir rapor seçerken, dışa aktarılacak dosya biçimini belirtmeniz istenir (örneğin Microsoft Excel 97-2003 ikili XLS biçimi, SpreadsheetML veya Microsoft Excel 2007 XLSX biçimi) ve rapor tasarım sırasında oluşturulan herhangi bir giriş rapor parametresini belirtmeniz istenir. Bundan sonra, rapor, Reporting Services tarafından sağlanan verilerle doldurulur.
