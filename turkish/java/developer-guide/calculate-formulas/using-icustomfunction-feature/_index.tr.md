---
title: ICustomFunction Özelliği Kullanımı
type: docs
weight: 890
url: /tr/java/how-to-calculate-custom-fuctions/
description: Bu makale, Aspose.Cells kütüphanesinde ICustomFunction özelliğini kullanarak Microsoft Excel de özel bir işlev oluşturmanın nasıl yapılacağını açıklar. Varolan bir Excel dosyasını yükleyerek veya yeni bir Excel dosyası oluşturarak, Aspose.Cells tarafından sağlanan yöntemleri kullanarak özel işlevleri tanımlayabilir ve kaydederiz ve sonunda değiştirilmiş Excel dosyasını diske kaydederiz.
keywords: Aspose.Cells, Excel, ICustomFunction özellikleri, özel fonksiyonlar, özel fonksiyonların nasıl hesaplanacağı.
---

{{% alert color="primary" %}} 

Bu makale, ICustomFunction özelliğini kullanarak özel işlevleri Aspose.Cells API'leri ile nasıl uygulayacağınızı ayrıntılı bir şekilde anlatmaktadır.

ICustomFunction arabirimine, belirli gereksinimleri karşılamak için Aspose.Cells'in temel hesaplama motorunu genişletmek için özel formül hesaplama işlevleri eklemeye olanak tanır. Bu özellik, özel (kullanıcı tanımlı) işlevleri bir şablon dosyasında veya kodda tanımlamak ve değerlendirmek için kullanışlıdır.

Lütfen dikkat edin, bu arayüz [AbstractCalculationEngine](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine) ile değiştirilmiş ve gelecekte kaldırılacaktır. Yeni API hakkında bazı teknik makaleler/örnekler: [burada](/cells/tr/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/) ve [burada](/cells/tr/java/returning-a-range-of-values-using-abstractcalculationengine/)

{{% /alert %}} {{% alert color="primary" %}} 

Eğer Aspose.Cells for Java API'larına yeni başlıyorsanız, projenizde Aspose.Cells for Java'yi nasıl edinebileceğinizi ve referans verebileceğinizi öğrenmek için lütfen [bu](https://docs.aspose.com/cells/java/installation/) makaleye göz atın.

{{% /alert %}} 
## **Kullanıcı Tanımlı Bir İşlev Oluşturma ve Değerlendirme**
Bu makale, ICustomFunction arabirimini uygulayarak özel bir işlevi yazmayı ve bu işlevi elektronik tabloda kullanmayı ve sonuçları almayı göstermektedir. **MyFunc** adında 2 parametre kabul eden özel bir işlevi tanımlayacağız.

- 1. parametre, bir hücreye atıfta bulunur
- 2. parametre, hücrelerin bir aralığına atıfta bulunur

Özel işlev, 2. parametre olarak belirtilen hücre aralığındaki tüm değerleri ekler ve 1. parametredeki değerle bölerek sonucu verir.

İşte calculateCustomFunction yöntemini nasıl uyguladığımız

**Java**

{{< highlight csharp >}}

 public class CustomFunction implements ICustomFunction

{

    @Override

    public Object calculateCustomFunction(String functionName, java.util.ArrayList paramsList, java.util.ArrayList contextObjects)

    {

        double result = 0f;

        double sum = 0;

        //Get the value of 1st parameter

        Object firstParamB1 = paramsList.get(0);

        if (firstParamB1 instanceof ReferredArea)

        {

            ReferredArea ra = (ReferredArea)firstParamB1;

            firstParamB1 = ra.getValue(0, 0);

        }

        //Get values of 2nd parameter

        Object secondParamC1C5 = paramsList.get(1);

        if (secondParamC1C5 instanceof ReferredArea)

        {

            ReferredArea ra = (ReferredArea)secondParamC1C5;

            for (int i = ra.getStartRow(); i <= ra.getEndRow(); i++)

            {

                //Add all values

                sum += (double)ra.getValue(i, 0);

            }

        }

        result = sum / (double)firstParamB1;

        // Return result of the function

        return result;

    }

}

{{< /highlight >}}

Yeni tanımlanan işlevi bir elektronik tabloda nasıl kullandığımız.

**Java**

{{< highlight csharp >}}

 //Open the workbook

Workbook workbook = new Workbook();

//Obtaining the reference of the first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Adding a sample value to "A1" cell

worksheet.getCells().get("B1").putValue(5);

//Adding a sample value to "A2" cell

worksheet.getCells().get("C1").putValue(100);

//Adding a sample value to "A3" cell

worksheet.getCells().get("C2").putValue(150);

//Adding a sample value to "B1" cell

worksheet.getCells().get("C3").putValue(60);

//Adding a sample value to "B2" cell

worksheet.getCells().get("C4").putValue(32);

//Adding a sample value to "B2" cell

worksheet.getCells().get("C5").putValue(62);

//Adding custom formula to Cell A1

worksheet.getCells().get("A1").setFormula("=MyFunc(B1,C1:C5)");

//Calcualating Formulas

workbook.calculateFormula(false, new CustomFunction());

//Assign resultant value to Cell A1

worksheet.getCells().get("A1").putValue(worksheet.getCells().get("A1").getValue());

//Save the file

workbook.save(dir + "UsingICustomFunction.xls");

{{< /highlight >}}
## **Genel Bakış**
Aspose.Cells API’leri, ilgili parametre bir referans ise veya hesaplanan sonucu referans ise, ReferredArea nesnesini 'paramsList' içine yerleştirir. Eğer referansın kendisine ihtiyacınız varsa, o zaman ReferredArea'yı doğrudan kullanabilirsiniz. Formülün konumuna karşılık gelen referanstan tek bir hücre değerine ihtiyacınız varsa, ReferredArea.getValue(rowOffset, int colOffset) yöntemini kullanabilirsiniz. Eğer sadece alanın tamamı için hücre değerleri dizisine ihtiyacınız varsa, ReferredArea.getValues yöntemini kullanabilirsiniz.

Aspose.Cells API'leri tarafından 'paramsList' içine ReferredArea verildiğinden, 'contextObjects' içindeki ReferredAreaCollection artık gereksiz olmayacak (eski sürümlerde özel işlev parametrelerine her zaman birbirine tekabül etmeyen bir eşleme yapamazdı) ve bu nedenle 'contextObjects' içinden kaldırılmıştır.

{{< highlight java >}}

 public Object calculateCustomFunction(String functionName, ArrayList paramsList, ArrayList contextObjects)

{

    ...

    Object o = paramsList.get(i);

    if(o is ReferredArea) //fetch data from reference

    {

        ReferredArea ra = (ReferredArea)o;

        if(ra.isArea())

        {

            o = ra.getValues();

        }

        else

        {

            o = ra.getValue(0, 0);

        }

    }

    if (o is Array)

    {

        ...

    }

    else if...

    ...

}

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
