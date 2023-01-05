---
title: ICustomFunction Özelliğini Kullanma
type: docs
weight: 890
url: /tr/java/using-icustomfunction-feature/
---
{{% alert color="primary" %}} 

Bu makale, Aspose.Cells API'leri ile özel işlevleri uygulamak için ICustomFunction özelliğinin nasıl kullanılacağına ilişkin ayrıntılı bir anlayış sağlar.

ICustomFunction arabirimi, belirli gereksinimleri karşılamak amacıyla Aspose.Cells' çekirdek hesaplama motorunu genişletmek için özel formül hesaplama işlevleri eklemeye izin verir. Bu özellik, bir şablon dosyasında veya kodda özel (kullanıcı tanımlı) işlevleri tanımlamak için kullanışlıdır; burada özel işlev, diğer herhangi bir varsayılan Microsoft Excel işlevi gibi Aspose.Cells API'leri kullanılarak uygulanıp değerlendirilebilir.

 Lütfen dikkat, bu arayüz şu şekilde değiştirildi:[SoyutHesaplamaMotoru](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine) ve gelecekte kaldırılacaktır. Yeni API ile ilgili bazı teknik makaleler/örnekler:[Burada](/cells/tr/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/) ve[Burada](/cells/tr/java/returning-a-range-of-values-using-abstractcalculationengine/)

{{% /alert %}} {{% alert color="primary" %}} 

 Aspose.Cells for Java API'lerinde yeniyseniz, lütfen kontrol edin[Bu](https://docs.aspose.com/cells/java/installation/) Aspose.Cells for Java'i projenizde nasıl edinebileceğinizi ve referans alabileceğinizi öğrenmek için makale.

{{% /alert %}} 
## **Kullanıcı Tanımlı Bir İşlev Oluşturma ve Değerlendirme**
Bu makale, sonuçları almak için özel bir işlev yazmak ve bunu elektronik tabloda kullanmak için ICustomFunction arabiriminin uygulanmasını gösterir. Ada göre özel bir işlev tanımlayacağız**MyFunc** aşağıdaki ayrıntılarla 2 parametreyi kabul edecek.

- 1. parametre tek bir hücreyi ifade eder
- 2. parametre, bir hücre aralığını ifade eder

Özel işlev, 2. parametre olarak belirtilen hücre aralığındaki tüm değerleri toplayacak ve sonucu 1. parametredeki değere bölecektir.

HesaplamaCustomFunction yöntemini şu şekilde uyguladık.

**Java**

{{< highlight "csharp" >}}

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

Yeni tanımlanmış işlevi bir elektronik tabloda nasıl kullanacağınız aşağıda açıklanmıştır

**Java**

{{< highlight "csharp" >}}

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
## **genel bakış**
Aspose.Cells API'leri, karşılık gelen parametre bir referans olduğunda veya hesaplanan sonucu referans olduğunda, ReferredArea nesnesini "paramsList" içine koyar. Referansın kendisine ihtiyacınız varsa, doğrudan ReferredArea'yı kullanabilirsiniz. Formülün konumuna karşılık gelen referanstan tek bir hücrenin değerini almanız gerekiyorsa, ReferredArea.getValue(rowOffset, int colOffset) yöntemini kullanabilirsiniz. Tüm alan için hücre değerleri dizisine ihtiyacınız varsa o zaman ReferredArea.getValues yöntemini kullanabilirsiniz.

Aspose.Cells API'leri "paramsList" içindeki ReferredArea'yı verdiğinden, "contextObjects" içindeki ReferredAreaCollection'a artık gerek kalmayacak (eski sürümlerde her zaman özel işlevin parametrelerine bire bir harita veremiyordu), bu nedenle "contextObjects"ten kaldırıldı.

{{< highlight "java" >}}

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
