---  
title: Şifre Kontrolü ile Dosya Düzenleme Parolası Kontrolü kullanmak için Aspose.Cells for Node.js via C++  
linktitle: Düzenleme parolası kontrolü yapma  
type: docs  
weight: 2400  
url: /tr/nodejs-cpp/check-password-to-modify-using-aspose-cells/  
description: Aspose.Cells for Node.js via C++ kullanarak düzenleme için şifre kontrolü nasıl yapılır öğrenin.  
---  

{{% alert color="primary" %}}  
Bazen, programlı olarak verilen şifrenin “Düzenleme Parolası” ile eşleşip eşleşmediğini kontrol etmeniz gerekebilir. Aspose.Cells, verilen Parola ile doğrulama yapmanızı sağlayan `WorkbookSettings.writeProtection.validatePassword()` metodunu sağlar.  
{{% /alert %}}  

## **Microsoft Excel'de Değiştirme Şifresini Kontrol Etme**  

Microsoft Excel'de çalışma kitapları oluştururken **Açma Şifresi** ve **Değiştirme Şifresi** atayabilirsiniz. Bu şifreleri belirlemek için Microsoft Excel'in sağladığı arayüzü gösteren bu ekran görüntüsüne bakınız.  

|![todo:image_alt_text](check-password-to-modify-using-aspose-cells_1.png)|  
| :- |  

## **Aspose.Cells for Node.js via C++ kullanarak Düzenleme Parolası Kontrolü**  

Aşağıdaki örneklerde, [kaynak Excel dosyası](5112232.xlsx) yüklenir. Dosyanın açma şifresi 1234 ve düzenleme şifresi 5678 olarak belirlenmiştir. Kod ilk olarak, 567'nin doğru düzenleme parolası olup olmadığını kontrol eder ve false döner; ardından 5678 olup olmadığını kontrol eder ve true döner.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Specify password to open inside the load options
const opts = new AsposeCells.LoadOptions();
opts.setPassword("1234");

// Open the source Excel file with load options
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sampleBook.xlsx"), opts);

// Check if 567 is Password to modify
let ret = workbook.getSettings().getWriteProtection().validatePassword("567");
console.log("Is 567 correct Password to modify: " + ret);

// Check if 5678 is Password to modify
ret = workbook.getSettings().getWriteProtection().validatePassword("5678");
console.log("Is 5678 correct Password to modify: " + ret);
```  

### **Konsol Çıktısı**  

Yukarıdaki örnek kodun [kaynak Excel](5112232.xlsx) dosyasını yükledikten sonraki Konsol Çıkışı burada.  

{{< highlight java >}}  
Is 567 correct Password to modify: False  
Is 5678 correct Password to modify: True  
{{< /highlight >}}  
