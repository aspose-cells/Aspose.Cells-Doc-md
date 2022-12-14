---
title: Aspose.Cells Şablon ve Akıllı İşaretleyiciler
type: docs
weight: 30
url: /tr/reportingservices/aspose-cells-template-and-smart-markers/
---
{{% alert color="primary" %}} 

Aspose.Cells şablonu, Akıllı İşaretleyiciler içeren bir Microsoft Excel çalışma kitabıdır. Akıllı İşaretleyiciler, rapor öğeleri için veri yer tutucu görevi görür ve işleme zamanında karşılık gelen verilerle değiştirilir. Aşağıda listelenen beş tür akıllı işaretçi vardır. Tüm işaretçiler, Aspose.Cells.Report.Designer tarafından bir şablona eklenebilir. Ayrıca manuel olarak da düzenlenebilir.

{{% /alert %}} 
### **Akıllı İşaretleyiciler**
#### **Veri İşaretleyicileri**
 formatı**veri işaretleri** &=DataSetName.FieldName'dir. Örneğin: &=SalesDetail.sales, burada SalesDetail bir veri kümesinin veya sorgunun adıdır ve sales, alanlarından birinin adıdır. İşleme sırasında, veri işaretçileri, Reporting Services tarafından sağlanan veri kümesinin değerleri ile değiştirilir.
#### **Raporlama Hizmetleri Formüller İşaretleyiciler**
 Raporlama Hizmetlerinin formatı**formül işaretleri**&= ifadedir. Örneğin: &=sum(SalesDetail.sales)/100. İfade, işlev, veri kümesi alanları, operatör vb.'den oluşur. Oluşturma zamanında. Raporlama Hizmetleri formül işaretçileri, hesaplanan değerlerle değiştirilir.
#### **Raporlama Hizmetleri Küresel Değişken Belirteçleri**
 Raporlama Hizmetlerinin formatı**genel değişken işaretleri** &=Globals! Değişken ismi. Örneğin: &=Globals!ExecutionTime burada ExecutionTime global bir değişkenin adıdır. Global değişken işaretçileri, oluşturma zamanında global değişken değerleri ile değiştirilir.
#### **Raporlama Hizmetleri Parametreleri İşaretleyiciler**
 Bir rapor parametresinin iki özelliği vardır: değer ve etiket. Sonuç olarak,**parametre işaretleri** iki formatı vardır: &= Parametreler! ParamName.Value ve &=Parametreler! ParamName.Label. Sırasıyla parametrenin adını ve etiketini gösterirler. Oluşturma sırasında, parametre işaretleri, kullanıcı tarafından girilen parametre değerleri ile değiştirilir.
#### **Dinamik Formüller**
 Eklenen satırlarda hesaplama yapmak için dinamik formüller kullanın.**dinamik formüller** Microsoft Excel'in formüllerini, bir formül dışa aktarma işlemi sırasında eklenecek satırlara başvurduğunda bile hücrelere eklemenize olanak tanır. Eklenen her satır için tekrarlanabilirler veya yalnızca onlar için veri işaretçilerinin yerleştirildiği hücrelerle birlikte kullanılabilirler.

Dinamik formüllerin formatı &=&=RepeatDynamicFormula'dır.

Dinamik Formüller aşağıdaki ek seçeneklere izin verir:

- {r} – Geçerli satır numarası.
- {2}, {-1} – Geçerli satır numarasına kaydır.

**Yinelenen bir dinamik formül ve sonuçta ortaya çıkan Excel çalışma sayfası** 

![yapılacaklar:resim_alternatif_Metin](aspose-cells-template-and-smart-markers_1.png)
