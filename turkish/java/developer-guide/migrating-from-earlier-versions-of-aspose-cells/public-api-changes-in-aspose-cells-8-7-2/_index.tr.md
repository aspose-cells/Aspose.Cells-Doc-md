---
title: Genel API Aspose.Cells 8.7.2'deki değişiklikler
type: docs
weight: 260
url: /tr/java/public-api-changes-in-aspose-cells-8-7-2/
---
{{% alert color="primary" %}} 

Bu belge, Aspose.Cells API sürümünde 8.7.1'den 8.7.2'ye modül/uygulama geliştiricilerin ilgisini çekebilecek değişiklikleri açıklamaktadır. Yalnızca yeni ve güncellenmiş genel yöntemleri, eklenen ve kaldırılan sınıfları vb. değil, aynı zamanda Aspose.Cells'deki perde arkasındaki davranış değişikliklerinin açıklamasını da içerir.

{{% /alert %}} 
## **Eklenen API'ler**
### **Varsayılan Hesaplama Motorunu Genişletti**
Aspose.Cells API'leri, neredeyse tüm Microsoft Excel işlevlerini hesaplayabilen güçlü bir hesaplama motoruna sahiptir. Ayrıca, Aspose.Cells API'leri artık herhangi bir uygulamanın özel hesaplama gereksinimlerini karşılamak için varsayılan hesaplama motorunun genişletilmesine izin veriyor.

Aspose.Cells for Java 8.7.2 sürümüyle aşağıdaki API'ler eklenmiştir.

1. SoyutHesaplamaMotor Sınıfı
1. CalculationData Sınıfı
1. CalculationOptions.CustomEngine Özellik

{{% alert color="primary" %}} 

Yukarıda belirtilen API'ler, tüm işlevler için (Excel'in yerel işlevleri dahil) daha fazla esneklikle özel hesaplama motorunun uygulanmasına izin verir.

{{% /alert %}} {{% alert color="primary" %}} 

 Bu özellikle ilgili daha fazla ayrıntı için, lütfen adresindeki ayrıntılı makaleyi inceleyin.[Özel Hesaplama Motorunu Uygulama](/cells/tr/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}} 

Basit kullanım senaryosu aşağıdadır.

**Java**

{{< highlight "csharp" >}}

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
### **TextBoxCollection için Aşırı Yüklenmiş Dizin Oluşturucu eklendi**
Aspose.Cells for Java 8.7.2, adını String olarak kullanarak TextBox örneğine erişmek için TextBoxCollection sınıfı için aşırı yüklenmiş dizin oluşturucuyu kullanıma sundu.

{{% alert color="primary" %}} 

 Bu özellikle ilgili daha fazla ayrıntı için, lütfen adresindeki ayrıntılı makaleyi inceleyin.[TextBox'a Adı Üzerinden Erişmek](/cells/tr/java/access-the-text-box-by-the-name/)

{{% /alert %}} 

 Basit kullanım senaryosu aşağıdaki gibidir.

**Java**

{{< highlight "csharp" >}}

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
