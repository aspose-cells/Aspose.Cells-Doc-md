---  
title: Node.js ve C++ kullanarak Excel Çalışma Kitabının VBA Projesine Parola Koyma  
linktitle: Excel Çalışma Kitabının VBA Projesini Parola Koruması  
type: docs  
weight: 10  
url: /tr/nodejs-cpp/password-protect-the-vba-project-of-excel-workbook/  
description: Excel çalışma kitabının VBA projesine parola koymayı Aspose.Cells for Node.js via C++ kullanarak nasıl yapacağınızı öğrenin.  
---  

## **Node.js'de Excel Çalışma Kitabının VBA Projesini Parola Korumalı Yapma**  

Aspose.Cells kullanarak bir çalışma kitabının VBA (Visual Basic for Applications) Projesini [**VbaProject.protect(boolean, string)**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#protect-boolean-string-) yöntemiyle parola koruyabilirsiniz.  

## **Örnek Kod**  

Aşağıdaki örnek kod, [örnek Excel dosyasını](43352067.xlsm) yükler, VBA Projesine erişir ve ona parola ile korur. Son olarak, [çıktı Excel dosyasına](43352068.xlsm) kaydeder.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Load your source Excel file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "samplePasswordProtectVBAProject.xlsm"));

// Access the VBA project of the workbook.
const vbaProject = workbook.getVbaProject();

// Lock the VBA project for viewing with password.
vbaProject.protect(true, "11");

// Save the output Excel file
workbook.save(path.join(dataDir, "outputPasswordProtectVBAProject.xlsm"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
