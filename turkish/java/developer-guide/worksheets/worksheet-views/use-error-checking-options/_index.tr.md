---
title: Hata Kontrolü Seçeneklerini Kullanma
type: docs
weight: 60
url: /tr/java/use-error-checking-options/
---

{{% alert color="primary" %}} 

Microsoft Excel, kullanıcılara hata kontrol seçenekleri ve kurallarını tanımlama imkanı sunar. Kullanıcılar genellikle formül oluştururken hata kontrollerini görür, bir hücrenin sağ üst köşesindeki küçük üçgen, bir hücrede bir sorun olduğunda vurgulanır. Excel, kullanıcılara bir hücredeki bir problemle ilgili yardımcı olacak bilgileri sağlar.

{{% /alert %}} 
## **Hata türleri**
Formülün bir sonuç döndüremeyeceği anlamına gelen hatalar - örneğin bir sayıyı sıfıra bölmek gibi - hemen dikkat gerektirir ve hücrede bir hata değeri gösterilir. Yeşil üçgenin üzerine tıklamak bir ünlem işareti gösterir, bu tıklama seçenek listesini açar. 

Hata, seçenekler kullanılarak çözülebilir veya yok sayılabilir. Bir hatayı yok saymak, o hatanın daha sonra yapılan hata kontrollerinde görünmeyeceği anlamına gelir.

Aspose.Cells, hata kontrol seçenek özelliklerini sağlar. ErrorCheckOptions sınıfı, metin olarak saklanan sayılar, formül hesaplama hataları ve doğrulama hataları gibi farklı türlerde hata kontrollerini yönetir. İstenen hata kontrolünü ayarlamak için ErrorCheckType numaralandırmasını kullanın.
## **Metin Olarak Saklanan Sayılar**
Bazen, sayılar hücrelerde metin olarak biçimlendirilmiş ve saklanmış olabilir. Bu, hesaplamalarda sorunlara neden olabilir veya karışık sıralama düzenleri oluşturabilir. Metin olarak biçimlendirilmiş sayılar, hücrede sağa hizalanmış olarak değil, sola hizalanmış olarak bırakılır. Bir hücrelerde matematiksel bir işlem yapması gereken bir formül değeri döndürmezse, formülün başvurduğu hücrelerdeki hizalama kontrol edilmelidir - bu hücrelerin bazıları veya tümü metin olarak biçimlendirilmiş sayılar olabilir.

Metin olarak saklanan sayıları hızlı bir şekilde gerçek sayılara dönüştürmek için hata kontrol seçeneklerini kullanabilirsiniz. Microsoft Excel 2003'te:

1. **Araçlar** menüsünde **Seçenekler**'i tıklayın.
1. Hata Kontrolü sekmesini seçin.
   **Metin olarak saklanan sayı** seçeneği varsayılan olarak işaretlidir. 
1. Bu seçeneği devre dışı bırakın.
   Aşağıdaki resimde MS Excel'deki veriler için yeşil üçgenin nasıl görüntülendiğini görmek için aşağıdaki resme bakın.

![todo:image_alt_text](use-error-checking-options_1.png)

Aşağıdaki örnek kod, Aspose.Cells API'lerini kullanarak bir çalışma sayfasındaki metin olarak saklanan sayılar hata kontrol seçeneğini devre dışı bırakmanın nasıl yapıldığını göstermektedir. 

**Java**

{{< highlight csharp >}}

 //Create a workbook and opening a template spreadsheet

Workbook workbook = new Workbook("d:\\files\\Book1.xls");

//Get the first worksheet

Worksheet sheet = workbook.getWorksheets().get(0);

//Instantiate the error checking options

ErrorCheckOptionCollection opts = sheet.getErrorCheckOptions();

int index = opts.add();

ErrorCheckOption opt = opts.get(index);

//Disable the numbers stored as text option

opt.setErrorCheck(ErrorCheckType.TEXT_NUMBER, false);

//Set the range

opt.addRange(CellArea.createCellArea(0, 0, 65535, 255));

//Save the Excel file

workbook.save("d:\\files\\out_test.xls");



{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
