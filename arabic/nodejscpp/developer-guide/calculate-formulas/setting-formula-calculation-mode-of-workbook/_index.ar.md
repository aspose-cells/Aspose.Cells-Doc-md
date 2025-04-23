---  
title: ضبط وضع حساب الصيغة لدفتر العمل باستخدام Node.js عبر C++  
linktitle: ضبط وضع حساب الصيغ لسجل العمل  
description: تقدم هذه المقالة شرحًا لكيفية ضبط وضع حساب الصيغة في دفتر العمل في مايكروسوفت إكسل باستخدام Aspose.Cells for Node.js via C++. عن طريق تحميل ملف إكسل موجود أو إنشاء ملف جديد، يمكننا استخدام الطريقة التي توفرها Aspose.Cells لضبط وضع حساب الصيغة والحصول على النتيجة. وأخيرًا، نحفظ ملف إكسل المعدل على القرص.  
keywords: Aspose.Cells، إكسل، دفتر العمل، وضع حساب الصيغة، الإعدادات، Node.js عبر C++  
type: docs  
weight: 110  
url: /ar/nodejs-cpp/setting-formula-calculation-mode-of-workbook/  
---  

{{% alert color="primary" %}}  
يتيح Microsoft Excel لك تعيين وضع حساب الصيغة، أي الطريقة التي يتم بها حساب الصيغ. هناك ثلاثة قيم ممكنة:  

- تلقائي - إعادة الحساب كلما تم تغيير شيء ما، وفي كل مرة يتم فيها فتح دفتر العمل.  
- تلقائي ما عدا الجداول البيانية - إعادة الحساب كلما تم تغيير شيء ما، ولكن دون الجداول البيانية.  
- يدوي - إعادة الحساب فقط عندما يطلب المستخدم ذلك صراحة عن طريق الضغط على F9 أو CTRL+ALT+F9، أو عند حفظ دفتر العمل.  
{{% /alert %}}  

لتعيين وضع حساب الصيغ في Microsoft Excel:  

1. حدد **الصيغ** ثم **خيارات الحساب**.  
1. حدد أحد الخيارات.  

يتيح لك Aspose.Cells for Node.js via C++ أيضًا تعيين **وضع حساب الصيغة** باستخدام خاصية الوضع [**FormulaSettings.getCalculationMode()**](https://reference.aspose.com/cells/nodejs-cpp/formulasettings/#getCalculationMode--). يمكنك تخصيصها باستخدام التعداد [**CalcModeType**](https://reference.aspose.com/cells/nodejs-cpp/calcmodetype) والذي يتضمن القيم التالية:  

- CalcModeType.Automatic  
- CalcModeType.AutomaticExceptTable  
- CalcModeType.Manual  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create a workbook
const workbook = new AsposeCells.Workbook();

// Set the Formula Calculation Mode to Manual
workbook.getSettings().getFormulaSettings().setCalculationMode(AsposeCells.CalcModeType.Manual);

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```  

