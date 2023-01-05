---
title: ICustomFunction Özelliğini Kullanma
type: docs
weight: 30
url: /tr/net/using-icustomfunction-feature/
---
{{% alert color="primary" %}} 

Bu makale, Aspose.Cells API'leri ile özel işlevleri uygulamak için ICustomFunction özelliğinin nasıl kullanılacağına ilişkin ayrıntılı bir anlayış sağlar.

ICustomFunction arabirimi, belirli gereksinimleri karşılamak amacıyla Aspose.Cells' çekirdek hesaplama motorunu genişletmek için özel formül hesaplama işlevleri eklemeye izin verir. Bu özellik, bir şablon dosyasında veya kodda özel (kullanıcı tanımlı) işlevleri tanımlamak için kullanışlıdır; burada özel işlev, diğer herhangi bir varsayılan Microsoft Excel işlevi gibi Aspose.Cells API'leri kullanılarak uygulanıp değerlendirilebilir.

{{% /alert %}} 
## **Kullanıcı Tanımlı Bir İşlev Oluşturma ve Değerlendirme**
Bu makale, sonuçları almak için özel bir işlev yazmak ve bunu elektronik tabloda kullanmak için ICustomFunction arabiriminin uygulanmasını gösterir. Ada göre özel bir işlev tanımlayacağız**MyFunc** aşağıdaki ayrıntılarla 2 parametreyi kabul edecek.

- 1. parametre tek bir hücreyi ifade eder
- 2. parametre, bir hücre aralığını ifade eder

Özel işlev, 2. parametre olarak belirtilen hücre aralığındaki tüm değerleri toplayacak ve sonucu 1. parametredeki değere bölecektir.

CalculateCustomFunction yöntemini şu şekilde uyguladık.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-UsingICustomFunctionfeature-ICustomFunction.cs" >}}


Yeni tanımlanmış işlevi bir elektronik tabloda nasıl kullanacağınız aşağıda açıklanmıştır



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-UsingICustomFunctionfeature-UsingICustomFunctionFeature.cs" >}}
## **genel bakış**
Aspose.Cells API'leri, karşılık gelen parametre bir referans olduğunda veya hesaplanan sonucu referans olduğunda, ReferredArea nesnesini "paramsList" içine koyar. Referansın kendisine ihtiyacınız varsa, doğrudan ReferredArea'yı kullanabilirsiniz. Formülün konumuna karşılık gelen referanstan tek bir hücrenin değerini almanız gerekiyorsa, ReferredArea.GetValue(rowOffset, int colOffset) yöntemini kullanabilirsiniz. Tüm alan için hücre değerleri dizisine ihtiyacınız varsa o zaman ReferredArea.GetValues yöntemini kullanabilirsiniz.

Aspose.Cells API'leri "paramsList" içindeki ReferredArea'yı verdiğinden, "contextObjects" içindeki ReferredAreaCollection'a artık gerek kalmayacak (eski sürümlerde her zaman özel işlevin parametrelerine bire bir harita veremiyordu), bu nedenle "contextObjects"ten kaldırıldı.

{{< highlight "java" >}}

 public object CalculateCustomFunction(string functionName, ArrayList paramsList, ArrayList contextObjects)

{

    ...

    object o = paramsList[i];

    if(o is ReferredArea) //fetch data from reference

    {

        ReferredArea ra = (ReferredArea)o;

        if(ra.IsArea)

        {

            o = ra.GetValues();

        }

        else

        {

            o = ra.GetValue(0, 0);

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
