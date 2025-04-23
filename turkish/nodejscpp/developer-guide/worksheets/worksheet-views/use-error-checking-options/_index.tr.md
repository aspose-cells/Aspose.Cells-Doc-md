---  
title: Hata Kontrol Seçeneklerini Node.js ve C++ kullanarak kullanın  
linktitle: Hata Kontrolü Seçeneklerini Kullanma  
type: docs  
weight: 140  
url: /tr/nodejs-cpp/use-error-checking-options/  
description: Aspose.Cells for Node.js via C++ kullanarak Excel çalışma sayfalarında hata kontrol seçeneklerini programlı olarak nasıl kullanacağınızı öğrenin.  
keywords: excelde sayıyı metin olarak saklama, node.js ve C++ ile hata kontrolü excel seçenekleri, node.js ve C++ ile uygulama  
---  

{{% alert color="primary" %}}  
Microsoft Excel, kullanıcıların hata kontrol seçeneklerini ve kurallarını tanımlamalarına izin verir. Kullanıcılar, formüller oluştururken sık ​​sık hata kontrolleri görür, bir hücrenin sağ üst köşesinde küçük bir üçgen, bir hücrede bir sorun olduğunda vurgulanır. Excel, kullanıcılara hücreyle ilgili yaygın problemleri düzeltmelerine yardımcı olacak bilgiler sağlar.  
{{% /alert %}}  

## **Hata türleri**  

Formülü sonucu döndürmeyen hatalar — sıfıra bölmek gibi — acil dikkat gerektirir ve hücrede bir hata değeri görüntülenir. Yeşil üçgen üzerine tıklamak ünlem işareti gösterir; buna tıklandığında seçenekler listesi açılır.  

Hata, seçenekler kullanılarak çözülebilir veya görmezden gelinebilir. Bir hatayı görmezden gelmek, o hatanın sonraki hata kontrollerinde görünmeyeceği anlamına gelir.  

Aspose.Cells, hata kontrolü özellikleri sağlar. [**ErrorCheckOption**](https://reference.aspose.com/cells/nodejs-cpp/errorcheckoption) sınıfı farklı hata kontrolleri yönetir, örneğin, metin olarak saklanan sayılar, formül hesaplama hataları ve doğrulama hataları. İstenen hata kontrolünü ayarlamak için [**ErrorCheckType**](https://reference.aspose.com/cells/nodejs-cpp/errorchecktype) adlı sıralamayı kullanın.  

## **Metin Olarak Saklanan Sayılar**  

Bazen, sayılar hücrelerde metin olarak biçimlendirilmiş ve saklanmış olabilir. Bu, hesaplamalarda sorunlara neden olabilir veya karışık sıralama düzenleri oluşturabilir. Metin olarak biçimlendirilmiş sayılar, hücrede sağa hizalanmış olarak değil, sola hizalanmış olarak bırakılır. Bir hücrelerde matematiksel bir işlem yapması gereken bir formül değeri döndürmezse, formülün başvurduğu hücrelerdeki hizalama kontrol edilmelidir - bu hücrelerin bazıları veya tümü metin olarak biçimlendirilmiş sayılar olabilir.  

Metin olarak saklanan sayıları hızlı bir şekilde gerçek sayılara dönüştürmek için hata kontrol seçeneklerini kullanabilirsiniz. Microsoft Excel 2003'te:  

1. **Araçlar** menüsünde **Seçenekler**'i tıklayın.  
1. Hata Kontrolü sekmesini seçin.  
   **Metin olarak saklanan sayı** seçeneği varsayılan olarak işaretlidir.  
1. Bu seçeneği devre dışı bırakın.  

Aşağıdaki örnek kod, Aspose.Cells API'lerini kullanarak bir çalışma sayfasındaki metin olarak saklanan sayılar hata kontrol seçeneğini devre dışı bırakmanın nasıl yapıldığını göstermektedir.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Create a workbook and opening a template spreadsheet
const workbook = new AsposeCells.Workbook(filePath);

// Get the first worksheet
const sheet = workbook.getWorksheets().get(0);
// Instantiate the error checking options
const opts = sheet.getErrorCheckOptions();

const index = opts.add();
const opt = opts.get(index);
// Disable the numbers stored as text option
opt.setErrorCheck(AsposeCells.ErrorCheckType.NumberStoredAsText, false);
// Set the range
opt.addRange(AsposeCells.CellArea.createCellArea(0, 0, 1000, 50));

const outputFilePath = path.join(dataDir, "out_test.out.xlsx");
// Save the Excel file
workbook.save(outputFilePath);
```  
