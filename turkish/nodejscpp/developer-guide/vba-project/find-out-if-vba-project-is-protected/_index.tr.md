---
title: VBA Projesinin Korunup Korunmadığını Node.js ve C++ kullanarak bulun
linktitle: VBA Projesinin Korunup Korunmadığını Bul
type: docs
weight: 20
url: /tr/nodejs-cpp/find-out-if-vba-project-is-protected/
---

## **Node.js kullanarak VBA Projesinin Korunup korunmadığını bulun**

Excel dosyanızdaki VBA (Visual Basic Applications) Projesinin korunan olup olmadığını Aspose.Cells kullanarak [**VbaProject.isProtected()**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#isProtected--) özelliği ile öğrenebilirsiniz.

## **Örnek Kod**

Aşağıdaki örnek kod, bir çalışma kitabı oluşturur ve ardından VBA projesinin korunup korunmadığını kontrol eder. Ardından VBA projesini korur ve tekrar kontrol eder. Lütfen referans olarak konsol çıkışını inceleyin. Koruma öncesinde, [**VbaProject.isProtected()**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#isProtected--) **false** döner, ancak korumadan sonra **true** döner.

```javascript
const AsposeCells = require("aspose.cells.node");

// Create a workbook.
const wb = new AsposeCells.Workbook();

// Access the VBA project of the workbook.
const vbaProj = wb.getVbaProject();

// Find out if VBA Project is Protected using isProtected method.
console.log("IsProtected - Before Protecting VBA Project: " + vbaProj.isProtected());

// Protect the VBA project.
vbaProj.protect(true, "11");

// Find out if VBA Project is Protected using isProtected method.
console.log("IsProtected - After Protecting VBA Project: " + vbaProj.isProtected());
```

## **Konsol Çıktısı**

Yukarıdaki örnek kodun konsol çıktısı referans için görüntülenmiştir.

{{< highlight java >}}

IsProtected - Before Protecting VBA Project: False

IsProtected - After Protecting VBA Project: True

{{< /highlight >}}
