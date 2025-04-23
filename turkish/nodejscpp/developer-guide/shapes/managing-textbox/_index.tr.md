---
title: Node.js ile C++ üzerinden TextBox yönetimi
linktitle: Metin Kutusunu Yönet
type: docs
weight: 50
url: /tr/nodejs-cpp/managing-textbox-of-excel/
description: Excel de TextBox ı nasıl yöneteceğinizi öğrenin Aspose.Cells for Node.js via C++ kullanarak. 
keywords: Excel de TextBox ı Node.js ile C++ üzerinden yönetin 
---


## **Olası Kullanım Senaryoları**
Bir Excel çalışma sayfasında TextBox nesnelerini eklemeniz, güncellemeniz veya manipüle etmeniz gereken durumlar olabilir. Bu, açıklamalar, yönlendirme metinleri veya veri sunumuna yardımcı olacak herhangi bir ek bilgi eklemek için faydalı olabilir. Aspose.Cells for Node.js via C++, Excel belgelerinde TextBox'ı yönetmek için güçlü işlevsellik sağlar. 

## **Aspose.Cells for Node.js via C++ kullanarak TextBox yönetimi**
Bu örnek aşağıdakileri göstermektedir:

1. Yeni bir çalışma kitabı oluşturun.
2. Bir TextBox şekli ekleyin.
3. Gerektiğinde TextBox özelliklerini değiştirin.

```javascript
const Cells = require("aspose.cells"); // Ensure you have linked the Aspose.Cells library correctly

// Create a new workbook
let workbook = new Cells.Workbook();
// Access the first worksheet
let worksheet = workbook.getWorksheets().get(0);

// Adding a TextBox shape
let textBox = worksheet.getShapes().addTextBox(2, 2, 100, 100);

// Set TextBox properties
textBox.setText("This is a TextBox.");
textBox.setFontSize(12);
textBox.setFillColor(Cells.Color.fromArgb(255, 255, 255)); // White background

// Save the workbook
workbook.save("TextBoxExample.xlsx");
```

Bu kod, Excel çalışma sayfasında bir TextBox oluşturma ve yapılandırma yöntemini gösterir, boyutunu, konumunu ayarlamayı ve gereksinimlerinize göre biçimlendirmeyi gösterir.

Metin kutularıyla olan etkileşimlerin belirli kullanım durumlarına göre değişebileceğini unutmayın, bu nedenle ek yöntemler ve özellikler için Aspose.Cells for Node.js via C++ dokümantasyonuna bakın.

---
