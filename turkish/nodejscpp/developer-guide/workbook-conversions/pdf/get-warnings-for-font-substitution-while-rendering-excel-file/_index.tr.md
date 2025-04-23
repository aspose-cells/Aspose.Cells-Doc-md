---  
title: Node.js ile C++ kullanarak Excel Dosyasını Görüntüye Dönüştürürken Yazı Tipi Değişimini Uyarılarını Alın  
linktitle: Excel Dosyasını Rendelerken Yazı Tiplerinin Yerine Kullanılacak Uyarıları Alma  
type: docs  
weight: 230  
url: /tr/nodejs-cpp/get-warnings-for-font-substitution-while-rendering-excel-file/  
description: Excel dosyalarını PDF’ye dönüştürürken yazı tipi değişimini uyarıları almak için Aspose.Cells for Node.js via C++ kullanmayı öğrenin.  
---  

{{% alert color="primary" %}}  

Bazen, bir Microsoft Excel dosyasını PDF'e render ederken, Aspose.Cells fontları değiştirir. Aspose.Cells, geliştiricilerin hangi belirli fontun değiştirildiğini bildiren bir uyarı ile ilgili bir özellik sağlar. Bu, bir Aspose.Cells tarafından render edilmiş PDF'nin orijinal Microsoft Excel dosyasından farklı görünmesinin nedenini belirlemenize ve uygun işlemleri almanıza yardımcı olabilecek faydalı bir özelliktir. Örneğin, eksik fontları yükleyerek render sonuçlarının aynı görünmesini sağlamak gibi.

{{% /alert %}}  

Excel dosyasını PDF’ye dönüştürürken yazı tipi değişimini uyarıları almak için, IWarningCallback arayüzünü uygulayın ve PdfSaveOptions.warningCallback özelliğini sizin uyguladığınız arayüz ile ayarlayın.

Aşağıdaki ekran görüntüsü, aşağıdaki kodda kullanacağımız kaynak Excel dosyasını göstermektedir. A6 ve A7 hücrelerinde, Microsoft Excel tarafından düzgün bir şekilde render edilmeyen fontlarda bazı metinler bulunmaktadır.

|**Tüm fontlar düzgün bir şekilde render edilmiyor**|  
| :- |  
|![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_1.png)|  
Aspose.Cells, A6 ve A7 hücrelerindeki yazı tiplerini aşağıda gösterildiği gibi uygun yazı tipleriyle değiştirecektir.

|**Değiştirilen fontlar**|  
| :- |  
|![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_2.png)|  
## **Kaynak Dosya ve Çıktı PDF'sini İndir**  
Kaynak Excel dosyasını ve çıktı PDF'sini aşağıdaki bağlantılardan indirebilirsiniz

- [source.xlsx](5112611.xlsx)  
- [output.pdf](5112616.pdf)  
## **Kod**  
Aşağıdaki kod, IWarningCallback’i uygular ve PdfSaveOptions.warningCallback özelliğine uygulanan arayüzü atar. Artık bir hücrede herhangi bir font değiştirildiğinde, Aspose.Cells bir uyarı tetikler ve WarningCallback.Warning() metodunu çağırır.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

class GetWarningsForFontSubstitution {
static warning(info) {
if (info.getType() === AsposeCells.WarningType.FontSubstitution) {
console.log("WARNING INFO: " + info.getDescription());
}
}

static run() {
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "source.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

const options = new AsposeCells.PdfSaveOptions();
options.setWarningCallback(GetWarningsForFontSubstitution);
const outputFilePath = path.join(dataDir, "output_out.pdf");
workbook.save(outputFilePath, options);
}
}
```  
## **Çıktı**  
Kaynak Excel dosyasının PDF olarak dönüştürülmesinden sonra uyarılar şu şekilde hata ayıklama konsoluna çıktı verilir:

{{< highlight java >}}  

 WARNING INFO: Font substitution: Font [ Athene Logos; Regular ] has been substituted in Cell [ A6 ] in Sheet [ Sheet1 ].  

WARNING INFO: Font substitution: Font [ B Traffic; Regular ] has been substituted in Cell [ A7 ] in Sheet [ Sheet1 ].  

{{< /highlight >}}  

{{% alert color="primary" %}}  

Eğer elektronik tablonuz formüller içeriyorsa, elektronik tabloyu PDF formatına dönüştürmeden hemen önce Workbook.calculateFormula metodunu çağırmak en iyisidir. Bu sayede formül bağımlı değerler tekrar hesaplanacak ve PDF'de doğru değerler görüntülenecektir.

{{% /alert %}}  

