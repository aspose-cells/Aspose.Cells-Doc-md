---
title: Node.js kullanarak VBA Kodunun İmzalanıp İmzalanmadığını kontrol edin
linktitle: VBA Kodunun İmzalı Olup Olmadığını Kontrol Et
type: docs
weight: 100
url: /tr/nodejs-cpp/check-if-vba-code-is-signed/
description: Aspose.Cells for Node.js via C++ kullanarak VBA kod projesinin imzalanıp imzalanmadığını nasıl kontrol edeceğinizi öğrenin. 
---

{{% alert color="primary" %}}

Aspose.Cells, kullanıcının VBA kod projesinin imzalı olup olmadığını kontrol etmesine izin verir. Lütfen VBA kod projesinin imzalı olup olmadığını kontrol etmek için [**VbaProject.isSigned()**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#isSigned--) özelliğini kullanın.

{{% /alert %}}

Aşağıdaki kod, [**VbaProject.isSigned()**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#isSigned--) özelliği kullanılarak VBA kodunun imzalanıp imzalanmadığını nasıl kontrol edeceğinizi gösterir. Bu kodu test etmek için herhangi bir Excel dosyanızı kullanabilirsiniz. Test amacıyla, aşağıdaki kodda kullanılan [bu Excel dosyasını](5115032.xlsm) kullanabilirsiniz.

## **VBA Kodu İmzalandı mı kontrol et Node.js**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleVBAProjectSigned.xlsm");

// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

console.log("Is VBA Code Project Signed: " + workbook.getVbaProject().isSigned());
```

## Konsol Çıkışı

Aşağıda sağlanan bağlantıdaki [örnek excel dosyası](5115032.xlsm) kullanılarak yukarıdaki kodun konsol çıktısı bulunmaktadır.

{{< highlight java >}}

Is VBA Code Project Signed: True

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
