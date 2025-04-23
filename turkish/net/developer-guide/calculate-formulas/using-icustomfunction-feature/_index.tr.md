---
title: ICustomFunction Özelliği Kullanımı
description: Bu makale, Aspose.Cells kütüphanesinde ICustomFunction özelliğini kullanarak Microsoft Excel de özel bir işlev oluşturmanın nasıl yapılacağını açıklar. Varolan bir Excel dosyasını yükleyerek veya yeni bir Excel dosyası oluşturarak, Aspose.Cells tarafından sağlanan yöntemleri kullanarak özel işlevleri tanımlayabilir ve kaydederiz ve sonunda değiştirilmiş Excel dosyasını diske kaydederiz.
keywords: Aspose.Cells, Excel, ICustomFunction özellikleri, özel fonksiyonlar, özel fonksiyonların nasıl hesaplanacağı.
type: docs
weight: 30
url: /tr/net/how-to-calculate-custom-fuctions/
---

{{% alert color="primary" %}} 

Bu makale, ICustomFunction özelliğini kullanarak özel işlevleri Aspose.Cells API'leri ile nasıl uygulayacağınızı ayrıntılı bir şekilde anlatmaktadır.

ICustomFunction arabirimine, belirli gereksinimleri karşılamak için Aspose.Cells'in temel hesaplama motorunu genişletmek için özel formül hesaplama işlevleri eklemeye olanak tanır. Bu özellik, özel (kullanıcı tanımlı) işlevleri bir şablon dosyasında veya kodda tanımlamak ve değerlendirmek için kullanışlıdır.

Lütfen unutmayın bu arabirim [AbstractCalculationEngine](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine/) ile değiştirilmiş ve gelecekte kaldırılacaktır. Yeni API hakkında bazı teknik makale/örnekler: [burada](/cells/tr/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/) ve [burada](/cells/tr/net/returning-a-range-of-values-using-abstractcalculationengine/)

{{% /alert %}} 
## **Kullanıcı Tanımlı Bir İşlev Oluşturma ve Değerlendirme**
Bu makale, ICustomFunction arabirimini uygulayarak özel bir işlevi yazmayı ve bu işlevi elektronik tabloda kullanmayı ve sonuçları almayı göstermektedir. **MyFunc** adında 2 parametre kabul eden özel bir işlevi tanımlayacağız.

- 1. parametre, bir hücreye atıfta bulunur
- 2. parametre, hücrelerin bir aralığına atıfta bulunur

Özel işlev, 2. parametre olarak belirtilen hücre aralığındaki tüm değerleri ekler ve 1. parametredeki değerle bölerek sonucu verir.

İşte CalculateCustomFunction yöntemini nasıl uyguladığımız.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-UsingICustomFunctionfeature-ICustomFunction.cs" >}}


Yeni tanımlanan işlevi bir elektronik tabloda nasıl kullandığımız.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-UsingICustomFunctionfeature-UsingICustomFunctionFeature.cs" >}}
## **Genel Bakış**
Aspose.Cells API'leri, ilgili parametre bir başvuru olduğunda veya hesaplanan sonucu bir başvuru olduğunda, ReferredArea nesnesini 'paramsList' içine yerleştirir. Başvuruyu kendiniz kullanmak istiyorsanız, ReferredArea'yı doğrudan kullanabilirsiniz. Formülün konumuna karşılık gelen başvurudan tek bir hücre değerini almanız gerekiyorsa, ReferredArea.GetValue(rowOffset, int colOffset) yöntemini kullanabilirsiniz. Alanın tamamı için hücre değerleri dizisi almanız gerekiyorsa, ReferredArea.GetValues yöntemini kullanabilirsiniz.

Aspose.Cells API'leri tarafından 'paramsList' içine ReferredArea verildiğinden, 'contextObjects' içindeki ReferredAreaCollection artık gereksiz olmayacak (eski sürümlerde özel işlev parametrelerine her zaman birbirine tekabül etmeyen bir eşleme yapamazdı) ve bu nedenle 'contextObjects' içinden kaldırılmıştır.

{{< highlight java >}}

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
{{< app/cells/assistant language="csharp" >}}
