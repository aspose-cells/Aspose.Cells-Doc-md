---  
title: Node.js kullanarak çalışma kitabına VBA proje referansı ekleyin  
linktitle: VBA projesine kitap başvurusu ekleyin  
type: docs  
weight: 80  
url: /tr/nodejs-cpp/add-a-library-reference-to-vba-project-in-workbook/  
---  

{{% alert color="primary" %}}  

Bazen, kitabın VBA projesine kütüphane başvurusu eklemeniz veya kaydetmeniz gerekebilir. Aspose.Cells [**VbaProjectReferenceCollection.addRegisteredReference(string, string)**](https://reference.aspose.com/cells/nodejs-cpp/vbaprojectreferencecollection/#addRegisteredReference-string-string-) yöntemini kullanarak bunu yapabilirsiniz.  

{{% /alert %}}  

## **Microsoft Excel'de VBA projelerine kütüphane başvurusu ekleyin**  

Microsoft Excel'de, **Araçlar > Başvurular...** seçeneklerine tıklayarak VBA projelerine kütüphane başvurusu ekleyebilirsiniz.  

## **Aspose.Cells for Node.js via C++ kullanarak bir çalışma kitabına VBA proje referansı ekleyin**  

Aşağıdaki örnek kod, [**VbaProjectReferenceCollection.addRegisteredReference(string, string)**](https://reference.aspose.com/cells/nodejs-cpp/vbaprojectreferencecollection/#addRegisteredReference-string-string-) yöntemiyle VBA projesine iki kütüphane referansı ekler veya kaydeder.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const outputPath = path.join(dataDir, "Output_out.xlsm");

const workbook = new AsposeCells.Workbook();

const vbaProj = workbook.getVbaProject();
vbaProj.getReferences().addRegisteredReference("stdole", "*\\G{00020430-0000-0000-C000-000000000046}#2.0#0#C:\\Windows\\system32\\stdole2.tlb#OLE Automation");
vbaProj.getReferences().addRegisteredReference("Office", "*\\G{2DF8D04C-5BFA-101B-BDE5-00AA0044DE52}#2.0#0#C:\\Program Files\\Common Files\\Microsoft Shared\\OFFICE14\\MSO.DLL#Microsoft Office 14.0 Object Library");

workbook.save(outputPath);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
