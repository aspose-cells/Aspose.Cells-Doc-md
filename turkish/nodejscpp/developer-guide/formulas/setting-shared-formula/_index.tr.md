---
title: Node.js ile C++ kullanarak Paylaşılan Formül Ayarlama
linktitle: Paylaşılan Formülü Ayarlama
type: docs
weight: 10
url: /tr/nodejs-cpp/setting-shared-formula/
---

{{% alert color="primary" %}}

Bir çalışma sayfasına hesaplamalar yapacak bir fonksiyon eklemek istiyorsanız, bu makale Aspose.Cells for Node.js via C++ kullanarak bu işlemi nasıl gerçekleştireceğinizi açıklar.

{{% /alert %}}

## Aspose.Cells for Node.js via C++ kullanarak Paylaşılan Formül Ayarlama

Aşağıdaki örnek elektronik tabloya benzer biçimde veriyle dolu bir çalışma sayfasını varsayalım.

|**Giriş dosyası ile tek sütun veri**|
| :- |
|![todo:image_alt_text](setting-shared-formula_1.png)|

Bir fonksiyon eklemek istiyorsunuz ve bu fonksiyon, verinin ilk satırı için satış vergisini hesaplayacak. Vergi **%9**. Satış vergisini hesaplayan formül şudur: **"=A2*0.09"**. Bu makale, bu formülü Aspose.Cells ile nasıl uygulayacağınızı açıklar.

Aspose.Cells, [**Cell.getFormula()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getFormula--) özelliğini kullanarak bir formül belirtmenizi sağlar. Sütunun diğer hücrelerine (B3, B4, B5 ve benzeri) formül eklemek için iki seçenek bulunmaktadır.

İlk hücrede yaptığınız gibi, formülü her hücreye etkin şekilde ayarlayın, hücre referansını uygun şekilde güncelleyerek (A3*0.09, A4*0.09, A5*0.09 vb.). Bu, her satırın hücre referanslarının güncellenmesini gerektirir. Ayrıca, Aspose.Cells'un her formülü ayrı ayrı çözümlemesi gerekir, bu büyük tablolar ve karmaşık formüller için zaman alıcı olabilir. Ayrıca, fazla kod satırı eklenir, ancak döngüler bunları biraz azaltabilir.

Başka bir yaklaşım, **paylaşılan bir formül** kullanmaktır. Paylaşılan formülle, formüller her satırın hücre referansları için otomatik olarak güncellenir, böylece vergi uygun şekilde hesaplanır. [**Cell.setSharedFormula(string, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setSharedFormula-string-number-number-) yöntemi, birinci yöntemden daha verimlidir.

Aşağıdaki örnek, bunu nasıl kullanacağınızı göstermektedir.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a Workbook from existing file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "source.xlsx"));

// Get the cells collection in the first worksheet
const cells = workbook.getWorksheets().get(0).getCells();

// Apply the shared formula in the range i.e.., B2:B14
cells.get("B2").setSharedFormula("=A2*0.09", 13, 1);

// Save the excel file
workbook.save(path.join(dataDir, "Output_out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
