---
title: Aspose.Cells 8.7.2 de Genel API Değişiklikleri
type: docs
weight: 250
url: /tr/net/public-api-changes-in-aspose-cells-8-7-2/
---

{{% alert color="primary" %}} 

Bu belge, modül/uygulama geliştiricileri için 8.7.1'den 8.7.2'e Aspose.Cells API'sindeki değişiklikleri açıklar. Yeni ve güncellenmiş genel yöntemler, eklenen ve kaldırılan sınıflar vb. dahil olduğu gibi, Aspose.Cells'in arkasındaki davranışlarda da herhangi bir değişikliğin açıklamasını içerir.

{{% /alert %}} 
## **Eklenen API'lar**
### **Varsayılan Hesaplama Motoru Genişletildi**
Aspose.Cells API'ları güçlü bir hesaplama motoruna sahiptir ve neredeyse tüm Microsoft Excel işlevlerini hesaplayabilir. Ayrıca, Aspose.Cells API'ları artık herhangi bir uygulamanın özel hesaplama gereksinimlerini karşılamak için varsayılan hesaplama motorunu genişletmesine izin verir.

Aşağıdaki API'ler Aspose.Cells for .NET 8.7.2 sürümünün yayınlanmasıyla eklendi.

1. AbstractCalculationEngine Sınıfı
1. CalculationData Sınıfı
1. CalculationOptions.CustomEngine Özelliği

{{% alert color="primary" %}} 

Yukarıda bahsedilen API'ler, tüm işlevler (Excel'in orijinal işlevleri de dahil olmak üzere) için özel hesaplama motoru uygulamanıza izin verir ve daha fazla esneklik sağlar.

{{% /alert %}} {{% alert color="primary" %}} 

Bu özellikle ilgili daha fazla ayrıntı için [Varsayılan Hesaplama Motorunu Genişletmek](/cells/tr/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/) ayrıntılı makalesine göz atın

{{% /alert %}} 

Basit kullanım senaryosu aşağıda gösterilmektedir.

**C#**

{{< highlight csharp >}}

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


### **TextBoxCollection için Aşırı Yüklü İndeksleyici eklendi**
Aspose.Cells for .NET 8.7.2, TextBoxCollection sınıfı için adının bir dize olarak kullanılarak TextBox örneğine erişmek için aşırı yüklenmiş indeksi açığa çıkardı.

{{% alert color="primary" %}} 

Bu özellikle ilgili daha fazla ayrıntı için [Adıyla TextBox'a Erişme](/cells/tr/net/access-the-text-box-by-the-name/) ayrıntılı makalesine göz atın

{{% /alert %}} 

Basit kullanım senaryosu aşağıdaki gibi görünüyor.

**C#**

{{< highlight csharp >}}

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


### **GridWeb için OnAfterColumnFilter Olayı Eklendi**
Aspose.Cells.GridWeb için .NET 8.7.2, Aspose.Cells.GridWeb UI üzerinden yapılan filtreleme mekanizması için geri çağrı olarak hizmet eden OnAfterColumnFilter olayını açığa çıkardı. İsminden de anlaşılacağı gibi, olay, sütun filtresi uygulandıktan sonra tetiklenir ve filtreleme bilgilerini almak için kullanılabilir. Bu bilgiler arasında, hangi sütun endeksine ve seçilen filtre değerine filtre uygulandığının yer aldığı gibi.

Basit kullanım senaryosu aşağıdaki gibi görünüyor.

**C#**

{{< highlight csharp >}}

 protected void GridWeb1_AfterColumnFilter(object sender, Aspose.Cells.GridWeb.RowColumnEventArgs e)

{

    string msg = "Column index: " + (e.Num) + ", Filtered Value:" + e.Argument;

}

{{< /highlight >}}

{{% alert color="primary" %}} 

Do not forget to register the event to GridWeb control <acw:gridweb OnAfterColumnFilter="GridWeb1_AfterColumnFilter"/>

{{% /alert %}}
