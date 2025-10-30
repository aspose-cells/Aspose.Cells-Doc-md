---
title: VBA projesinin İmzalanıp İmzalanmadığını Node.js kullanarak kontrol edin
linktitle: Bir Çalışmada VBA Projesinin İmzalı Olup Olmadığını Kontrol Edin
type: docs
weight: 70
url: /tr/nodejs-cpp/check-if-vba-project-in-a-workbook-is-signed/
description: Aspose.Cells for Node.js via C++ kullanarak bir çalışma kitabında VBA projesinin imzalanıp imzalanmadığını nasıl kontrol edeceğinizi öğrenin.
---

{{% alert color="primary" %}}

Microsoft Excel üzerinden **Araçlar > Dijital İmzalar...** menü komutunu kullanarak VBA projenizin imzalı olup olmadığını kontrol edebilirsiniz. Benzer şekilde, Aspose.Cells [**Workbook.getVbaProject()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getVbaProject--) özelliğini kullanarak programlı olarak da kontrol edebilirsiniz.

{{% /alert %}}

## **Node.js kullanarak bir Çalışma Kitabındaki VBA projesinin imzalanıp imzalanmadığını kontrol edin**

 Aşağıdaki kod çalışma kitabını yükler ve VBA projesinin imzalanıp imzalanmadığını [**Workbook.getVbaProject()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getVbaProject--) özelliği kullanarak kontrol eder. Proje imzalanmışsa **true**, değilse **false** döner.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Sample1.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
console.log("VBA Project is Signed: " + workbook.getVbaProject().isSigned());
```
{{< app/cells/assistant language="nodejs-cpp" >}}
