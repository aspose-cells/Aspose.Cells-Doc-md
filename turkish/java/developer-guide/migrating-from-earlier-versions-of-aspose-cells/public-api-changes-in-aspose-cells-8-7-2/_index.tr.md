---
title: Aspose.Cells 8.7.2 de Genel API Değişiklikleri
type: docs
weight: 260
url: /tr/java/public-api-changes-in-aspose-cells-8-7-2/
---

{{% alert color="primary" %}} 

Bu belge, modül/uygulama geliştiricileri için 8.7.1'den 8.7.2'e Aspose.Cells API'sindeki değişiklikleri açıklar. Yeni ve güncellenmiş genel yöntemler, eklenen ve kaldırılan sınıflar vb. dahil olduğu gibi, Aspose.Cells'in arkasındaki davranışlarda da herhangi bir değişikliğin açıklamasını içerir.

{{% /alert %}} 
## **Eklenen API'lar**
### **Varsayılan Hesaplama Motoru Genişletildi**
Aspose.Cells API'ları güçlü bir hesaplama motoruna sahiptir ve neredeyse tüm Microsoft Excel işlevlerini hesaplayabilir. Ayrıca, Aspose.Cells API'ları artık herhangi bir uygulamanın özel hesaplama gereksinimlerini karşılamak için varsayılan hesaplama motorunu genişletmesine izin verir.

Aspose.Cells for Java 8.7.2'nin piyasaya sürülmesiyle aşağıdaki API'ler eklenmiştir.

1. AbstractCalculationEngine Sınıfı
1. CalculationData Sınıfı
1. CalculationOptions.CustomEngine Özelliği

{{% alert color="primary" %}} 

Yukarıda bahsedilen API'ler, tüm işlevler (Excel'in orijinal işlevleri de dahil olmak üzere) için özel hesaplama motoru uygulamanıza izin verir ve daha fazla esneklik sağlar.

{{% /alert %}} {{% alert color="primary" %}} 

Bu özellikle ilgili daha fazla detay için [Varsayılan Hesaplama Motorunu Genişletme](/cells/tr/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/) adlı ayrıntılı makaleyi inceleyin

{{% /alert %}} 

Basit kullanım senaryosu aşağıda gösterilmektedir.

**Java**

{{< highlight csharp >}}

 public class CustomEngine extends AbstractCalculationEngine

{

	public void calculate(CalculationData data)

        {

		if(data.getFunctionName().toUpperCase().equals("SUM")==true)

                {

                    double val = (double)data.getCalculatedValue();

                    val = val + 30;

                    data.setCalculatedValue(val);

                }

        }

}

{{< /highlight >}}
### **TextBoxCollection için Aşırı Yüklü İndeksleyici eklendi**
Aspose.Cells for Java 8.7.2, TextBoxCollection sınıfı için adını String olarak kullanarak TextBox örneğini erişmek için aşırı yüklü indeksleyiciyi ortaya çıkardı.

{{% alert color="primary" %}} 

Bu özellikle ilgili detaylar için lütfen [Adıyla TextBox Erişimi](/cells/tr/java/access-the-text-box-by-the-name/) başlıklı detaylı makaleye göz atın.

{{% /alert %}} 

Basit kullanım senaryosu aşağıdaki gibi görünüyor. 

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook

Workbook workbook = new Workbook();

//Access the first Worksheet from the collection

Worksheet sheet = workbook.getWorksheets().get(0);

//Add a TextBox to the collection

int idx = sheet.getTextBoxes().add(10, 10, 10, 10);

//Access the TextBox using its index

TextBox box = sheet.getTextBoxes().get(idx);

//Set the name for the TextBox

box.setName("MyTextBox");

//Access the same TextBox via its name

box = sheet.getTextBoxes().get("MyTextBox");

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
