---
title: ICustomFunction Özelliğini Kullanma
description: Bu makalede, Aspose.Cells kitaplığındaki ICustomFunction özelliğini kullanarak Microsoft Excel'de özel işlevin nasıl oluşturulacağı açıklanmaktadır. Mevcut bir Excel dosyasını yükleyerek veya yeni bir Excel dosyası oluşturarak, özel işlevleri tanımlayıp kaydetmek ve sonuçları almak için Aspose.Cells tarafından sağlanan yöntemleri kullanabiliriz. Son olarak değiştirdiğimiz Excel dosyasını diske kaydediyoruz.
keywords: Aspose.Cells, Excel, ICustomFunction features, custom functions
type: docs
weight: 30
url: /tr/net/using-icustomfunction-feature/
---
{{% alert color="primary" %}} 

Bu makale, Aspose.Cells API'leriyle özel işlevleri uygulamak için ICustomFunction özelliğinin nasıl kullanılacağına ilişkin ayrıntılı bir anlayış sağlar.

ICustomFunction arayüzü, belirli gereksinimleri karşılamak amacıyla Aspose.Cells' temel hesaplama motorunu genişletmek için özel formül hesaplama fonksiyonlarının eklenmesine olanak tanır. Bu özellik, bir şablon dosyasında veya özel işlevin diğer herhangi bir varsayılan Microsoft Excel işlevi gibi Aspose.Cells API'leri kullanılarak uygulanabileceği ve değerlendirilebileceği kodda özel (kullanıcı tanımlı) işlevler tanımlamak için kullanışlıdır.

 Lütfen bu arayüzün değiştirildiğini unutmayın.[ÖzetHesaplamaMotoru](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine/) ve gelecekte kaldırılacaktır. Yeni API ile ilgili bazı teknik makaleler/örnekler:[Burada](/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/) Ve[Burada](/net/returning-a-range-of-values-using-abstractcalculationengine/)

{{% /alert %}} 
##  **Kullanıcı Tanımlı Fonksiyon Oluşturma ve Değerlendirme**
 Bu makalede, özel bir işlev yazmak ve sonuçları almak için bunu elektronik tabloda kullanmak için ICustomFunction arabiriminin uygulanması gösterilmektedir. Özel bir işlevi ada göre tanımlayacağız**İşlevim** aşağıdaki ayrıntılara sahip 2 parametreyi kabul edecektir.

- 1. parametre tek bir hücreyi ifade eder
- 2. parametre bir hücre aralığını ifade eder

Özel işlev, 2. parametre olarak belirtilen hücre aralığındaki tüm değerleri toplayacak ve sonucu 1. parametredeki değere bölecektir.

CalculateCustomFunction yöntemini şu şekilde uyguladık.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-UsingICustomFunctionfeature-ICustomFunction.cs" >}}


Yeni tanımlanan işlevin bir e-tabloda nasıl kullanılacağı aşağıda açıklanmıştır



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-UsingICustomFunctionfeature-UsingICustomFunctionFeature.cs" >}}
##  **Genel Bakış**
Aspose.Cells API'leri, karşılık gelen parametre bir referans olduğunda veya hesaplanan sonucu referans olduğunda, ReferredArea nesnesini "paramsList"e yerleştirir. Referansın kendisine ihtiyacınız varsa, doğrudan ReferredArea'yı kullanabilirsiniz. Formülün konumuna karşılık gelen referanstan tek bir hücrenin değerini almanız gerekiyorsa ReferredArea.GetValue(rowOffset, int colOffset) yöntemini kullanabilirsiniz. Alanın tamamı için hücre değerleri dizisine ihtiyacınız varsa ReferredArea.GetValues yöntemini kullanabilirsiniz.

Aspose.Cells API'leri "paramsList"te ReferredArea değerini verdiğinden, "contextObjects" içindeki ReferredAreaCollection'a artık ihtiyaç duyulmayacak (eski sürümlerde özel işlevin parametrelerine her zaman bire bir harita veremiyordu), bu nedenle "contextObjects"ten kaldırıldı.

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
