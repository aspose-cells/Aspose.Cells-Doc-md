---
title: Aspose.Cells Şablonu ve Akıllı İşaretçiler
type: docs
weight: 30
url: /tr/reportingservices/aspose-cells-template-and-smart-markers/
---

{{% alert color="primary" %}} 

Bir Aspose.Cells şablonu, Akıllı İşaretçiler içeren bir Microsoft Excel çalışma kitabıdır. Akıllı İşaretçiler, rapor öğeleri için veri yer tutucusu olarak işlev görür ve işlem sırasında karşılık gelen veri ile değiştirilir. Beş tür akıllı işaretçi vardır, aşağıda listelenmiştir. Tüm işaretçiler, Aspose.Cells.Report.Designer tarafından bir şablon içine eklenir. Ayrıca manuel olarak da düzenlenebilirler. 

{{% /alert %}} 
### **Akıllı İşaretçiler**
#### **Veri İşaretçileri**
**Veri işaretçilerinin** biçimi &=DataSetAdı.AlanAdı. Örneğin: &=SalesDetail.sales burada SalesDetail bir veri seti veya sorgunun adı, sales ise alanlardan birinin adıdır. İşlem sırasında, veri işaretçileri, Raporlama Hizmetleri tarafından sağlanan veri kümesi değerleriyle değiştirilir.
#### **Raporlama Hizmetleri Formül İşaretçileri**
Raporlama Hizmetleri'nin **formül işaretçilerinin** formatı &=ifade. Örneğin: &=toplam(SalesDetail.sales)/100. İfade, fonksiyon, veri kümesi alanları, operatör vb. bütünleşir. İşlem sırasında, Raporlama Hizmetleri formül işaretçileri, hesaplanmış değerlerle değiştirilir.
#### **Raporlama Hizmetleri Küresel Değişken İşaretçileri**
Raporlama Hizmetleri'nin **küresel değişken işaretçilerinin** formatı &=Globals! DeğişkenAdı. Örneğin: &=Globals!ExecutionTime burada ExecutionTime bir küresel değişkenin adıdır. Küresel değişken işaretçileri, işlem sırasında küresel değişken değerleriyle değiştirilir.
#### **Raporlama Hizmetleri Parametre İşaretçileri**
Bir rapor parametresinin iki özelliği vardır: değer ve etiket. Dolayısıyla, **parametre işaretçilerinin** iki biçimi vardır: &= Parametreler! ParamAdı.Değer ve &=Parametreler! ParamAdı.Etiket. Bunlar parametrenin adını ve etiketini gösterir. İşlem sırasında, parametre işaretçileri, kullanıcı tarafından girilen parametre değerleriyle değiştirilir.
#### **Dinamik Formüller**
Eklenen satırlarda hesaplama yapmak için dinamik formülleri kullanın. **Dinamik formüller**, ihraç işlemi sırasında eklenecek satırlara referans veren bir formül olsa bile, hücrelere Microsoft Excel'in formüllerini eklemenizi sağlar. Bunlar, her eklenecek satır için tekrarlanabilir veya bunlar için yalnızca veri işaretçilerinin yerleştirildiği hücrelerle kullanılabilir.

Dinamik formüllerin biçimi &=&=TekrarDinamikFormül.

Dinamik Formüller aşağıdaki ek seçeneklere izin verir:

- {r} – Geçerli satır numarası.
- {2}, {-1} – Geçerli satır numarasına olan ofset.

**Tekrarlayan dinamik formül ve sonuçta Excel çalışma sayfası** 

![todo:image_alt_text](aspose-cells-template-and-smart-markers_1.png)
