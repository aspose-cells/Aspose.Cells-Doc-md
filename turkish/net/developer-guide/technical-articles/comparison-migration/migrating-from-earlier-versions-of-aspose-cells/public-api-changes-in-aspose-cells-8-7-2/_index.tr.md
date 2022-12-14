---
title: Genel API Aspose.Cells 8.7.2'deki değişiklikler
type: docs
weight: 250
url: /tr/net/public-api-changes-in-aspose-cells-8-7-2/
---
{{% alert color="primary" %}} 

Bu belge, Aspose.Cells API sürümünde 8.7.1'den 8.7.2'ye modül/uygulama geliştiricilerin ilgisini çekebilecek değişiklikleri açıklamaktadır. Yalnızca yeni ve güncellenmiş genel yöntemleri, eklenen ve kaldırılan sınıfları vb. değil, aynı zamanda Aspose.Cells'deki perde arkasındaki davranış değişikliklerinin açıklamasını da içerir.

{{% /alert %}} 
## **Eklenen API'ler**
### **Varsayılan Hesaplama Motorunu Genişletti**
Aspose.Cells API'leri, neredeyse tüm Microsoft Excel işlevlerini hesaplayabilen güçlü bir hesaplama motoruna sahiptir. Ayrıca, Aspose.Cells API'leri artık herhangi bir uygulamanın özel hesaplama gereksinimlerini karşılamak için varsayılan hesaplama motorunun genişletilmesine izin veriyor.

Aspose.Cells for .NET 8.7.2 sürümüyle aşağıdaki API'ler eklenmiştir.

1. SoyutHesaplamaMotor Sınıfı
1. CalculationData Sınıfı
1. CalculationOptions.CustomEngine Özellik

{{% alert color="primary" %}} 

Yukarıda belirtilen API'ler, tüm işlevler için (Excel'in yerel işlevleri dahil) daha fazla esneklikle özel hesaplama motorunun uygulanmasına izin verir.

{{% /alert %}} {{% alert color="primary" %}} 

 Bu özellikle ilgili daha fazla ayrıntı için, lütfen adresindeki ayrıntılı makaleyi inceleyin.[Özel Hesaplama Motorunu Uygulama](/cells/tr/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}} 

Basit kullanım senaryosu aşağıdadır.

**C#**

{{< highlight "csharp" >}}

 public class MyEngine : AbstractCalculationEngine

{

    public override void Calculate(CalculationData data)

    {

        string funcName = data.FunctionName.ToUpper();

        if ("MYFUNC".Equals(funcName))

        {

            //do calculation for MYFUNC here

            int count = data.ParamCount;

            object res = null;

            for (int i = 0; i < count; i++)

            {

                object pv = data.GetParamValue(i);

                if (pv is ReferredArea)

                {

                    ReferredArea ra = (ReferredArea)pv;

                    pv = ra.GetValue(0, 0);

                }

                //process the parameter here

                //res = ...;

            }

            data.CalculatedValue = res;

        }

    }

}

{{< /highlight >}}


### **TextBoxCollection için Aşırı Yüklenmiş Dizin Oluşturucu eklendi**
Aspose.Cells for .NET 8.7.2, adını dize olarak kullanarak TextBox örneğine erişmek için TextBoxCollection sınıfı için aşırı yüklenmiş dizini ortaya çıkardı.

{{% alert color="primary" %}} 

 Bu özellikle ilgili daha fazla ayrıntı için, lütfen adresindeki ayrıntılı makaleyi inceleyin.[TextBox'a Adı Üzerinden Erişmek](/cells/tr/net/access-the-text-box-by-the-name/)

{{% /alert %}} 

Basit kullanım senaryosu aşağıdaki gibidir.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

Workbook workbook = new Workbook();

//Access the first Worksheet from the collection

Worksheet sheet = workbook.Worksheets[0];

//Add a TextBox to the collection

int idx = sheet.TextBoxes.Add(10, 10, 10, 10);

//Access the TextBox using its index

TextBox box = sheet.TextBoxes[idx];

//Set the name for the TextBox

box.Name = "MyTextBox";

//Access the same TextBox via its name

box = sheet.TextBoxes["MyTextBox"];

{{< /highlight >}}


### **GridWeb için OnAfterColumnFilter Etkinliği Eklendi**
Aspose.Cells.GridWeb for .NET 8.7.2, Aspose.Cells.GridWeb kullanıcı arabirimi aracılığıyla gerçekleştirilen filtreleme mekanizmasına geri arama işlevi gören OnAfterColumnFilter olayını ortaya çıkardı. Adından da anlaşılacağı gibi olay, sütun filtreleme uygulandıktan sonra tetiklenir ve filtrenin uygulandığı sütun dizini ve seçilen filtre değeri gibi filtreleme bilgilerini almak için kullanılabilir.

Basit kullanım senaryosu aşağıdaki gibidir.

**C#**

{{< highlight "csharp" >}}

 protected void GridWeb1_AfterColumnFilter(object sender, Aspose.Cells.GridWeb.RowColumnEventArgs e)

{

    string msg = "Column index: " + (e.Num) + ", Filtered Value:" + e.Argument;

}

{{< /highlight >}}

{{% alert color="primary" %}} 

Olayı GridWeb kontrolüne kaydetmeyi unutmayın<acw:gridweb OnAfterColumnFilter="GridWeb1_AfterColumnFilter"/>

{{% /alert %}}
