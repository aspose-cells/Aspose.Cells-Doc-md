---  
title: Node.js ve C++ kullanarak Çalışma Kitabı nın Otomatik Kurtarma özelliğini nasıl ayarlayabilirsiniz.  
linktitle: Çalışma Kitabının Otomatik Kurtarma Özelliğini Ayarlamak  
type: docs  
weight: 220  
url: /tr/nodejs-cpp/how-to-set-autorecover-property-of-workbook/  
description: Aspose.Cells for Node.js via C++ kullanarak bir çalışma kitabının Otomatik Kurtarma özelliğini ayarlamayı öğrenin.  
---  

{{% alert color="primary" %}}  
Aspose.Cells kullanarak Çalışma Kitabı'nın Otomatik Kurtarma özelliğini ayarlayabilirsiniz. Bu özelliğin varsayılan değeri **true**'dur. Bir çalışma kitabında bunu **false** olarak ayarladığınızda, Microsoft Excel Otomatik Kurtarma (Otomatik Kaydet) devre dışı kalır.  

Aspose.Cells, bu seçeneği etkinleştirmek veya devre dışı bırakmak için [**Workbook.getAutoRecover()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getAutoRecover--) özelliğini sağlar.  
{{% /alert %}}  

Aşağıdaki kod, çalışma kitabının [**Workbook.getAutoRecover()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getAutoRecover--) özelliğinin nasıl kullanılacağını açıklar. Kod önce bu özelliğin varsayılan değeri olan **true**'yu okur, sonra bunu **false** yapar ve çalışma kitabını kaydeder. Ardından tekrar okur ve bu özelliğin değerinin şu anda **false** olduğunu gösterir.  

## Node.js kullanarak Çalışma Kitabının Otomatik Kurtarma özelliğini ayarlayan kod  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object
const workbook = new AsposeCells.Workbook();

// Read AutoRecover property
console.log("AutoRecover: " + workbook.getSettings().getAutoRecover());

// Set AutoRecover property to false
workbook.getSettings().setAutoRecover(false);

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));

// Read the saved workbook again
const workbook2 = new AsposeCells.Workbook(path.join(dataDir, "output_out.xlsx"));

// Read AutoRecover property
console.log("AutoRecover: " + workbook2.getSettings().getAutoRecover());
```  

## **Çıktı**  

Yukarıdaki örnek kodun konsol çıktısı burada gösterilmektedir.  

{{< highlight java >}}  
AutoRecover: True  
AutoRecover: False  
{{< /highlight >}}  

{{< app/cells/assistant language="nodejs-cpp" >}}
